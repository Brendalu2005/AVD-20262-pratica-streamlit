import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_loader import load_data


st.set_page_config(
    page_title="Spotify Streaming Performance",
    page_icon="🎧",
    layout="wide",
)

st.title("Spotify Streaming Performance")
st.caption("Explore os artistas, gêneros e padrões de streaming do dataset.")

df = load_data()

# Garante que as métricas usadas nos gráficos sejam numéricas.
COL_STREAMS = "Total Streams (in millions)"
COL_LEAD = "Lead Streams (in millions)"
COL_FEATURE = "Feature Streams (in millions)"
COL_GENRE = "Primary Genre"
COL_TYPE = "Artist Type"
COL_YEAR = "Debut Year"

for col in [COL_STREAMS, COL_LEAD, COL_FEATURE, COL_YEAR, "anos_carreira"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

with st.sidebar:
    st.header("Filtros")

    if COL_GENRE in df.columns:
        opcoes_genero = sorted(df[COL_GENRE].dropna().unique().tolist())
        generos = st.multiselect("Gênero musical", opcoes_genero, default=opcoes_genero)
    else:
        generos = None

    if COL_TYPE in df.columns:
        opcoes_tipo = sorted(df[COL_TYPE].dropna().unique().tolist())
        tipos = st.multiselect("Tipo de artista", opcoes_tipo, default=opcoes_tipo)
    else:
        tipos = None

    if COL_YEAR in df.columns and df[COL_YEAR].notna().any():
        ano_min = int(df[COL_YEAR].min())
        ano_max = int(df[COL_YEAR].max())
        intervalo_estreia = st.slider(
            "Intervalo de estreia",
            min_value=ano_min,
            max_value=ano_max,
            value=(ano_min, ano_max),
            step=1,
        )
    else:
        intervalo_estreia = None

    limite_ranking = st.slider("Artistas no ranking", min_value=5, max_value=20, value=10)

# Aplica os filtros antes de calcular os indicadores e os gráficos.
df_filtrado = df.copy()
if generos is not None:
    df_filtrado = df_filtrado[df_filtrado[COL_GENRE].isin(generos)]
if tipos is not None:
    df_filtrado = df_filtrado[df_filtrado[COL_TYPE].isin(tipos)]
if intervalo_estreia is not None:
    df_filtrado = df_filtrado[df_filtrado[COL_YEAR].between(*intervalo_estreia)]

st.caption(f"{len(df_filtrado)} de {len(df)} artistas após os filtros.")

if df_filtrado.empty:
    st.info("Nenhum artista corresponde aos filtros selecionados. Ajuste os filtros na lateral.")
    st.stop()

# Indicadores gerais para dar contexto às comparações abaixo.
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
with col_kpi1:
    artista_top = df_filtrado.loc[df_filtrado[COL_STREAMS].idxmax(), "Artist Name"]
    st.metric("Artistas no recorte", f"{len(df_filtrado):,}")
with col_kpi2:
    st.metric("Streams totais", f"{df_filtrado[COL_STREAMS].sum():,.1f} milhões")
with col_kpi3:
    st.metric("Maior audiência", artista_top)

st.divider()

# Visão principal: ranking de artistas e comparação entre gêneros.
col_ranking, col_generos = st.columns([1.15, 1], gap="large")

with col_ranking:
    st.subheader(f"Top {limite_ranking} artistas por streams")
    ranking = df_filtrado.nlargest(limite_ranking, COL_STREAMS).sort_values(COL_STREAMS)
    fig_ranking = px.bar(
        ranking,
        x=COL_STREAMS,
        y="Artist Name",
        orientation="h",
        color=COL_STREAMS,
        color_continuous_scale="Oranges",
        hover_data=[c for c in [COL_GENRE, COL_TYPE, COL_YEAR] if c in ranking.columns],
        labels={COL_STREAMS: "Streams (milhões)", "Artist Name": "Artista"},
    )
    fig_ranking.update_layout(
        coloraxis_showscale=False,
        xaxis_title="Streams totais (milhões)",
        yaxis_title="",
        margin=dict(l=10, r=10, t=20, b=10),
    )
    st.plotly_chart(fig_ranking, use_container_width=True)

with col_generos:
    st.subheader("Média de streams por gênero")
    if COL_GENRE in df_filtrado.columns:
        resumo_genero = (
            df_filtrado.groupby(COL_GENRE, as_index=False)
            .agg(
                media_streams=(COL_STREAMS, "mean"),
                artistas=("Artist Name", "count"),
            )
            .sort_values("media_streams")
        )
        fig_generos = px.bar(
            resumo_genero,
            x="media_streams",
            y=COL_GENRE,
            orientation="h",
            color="media_streams",
            color_continuous_scale="Teal",
            hover_data={"artistas": True, "media_streams": ":.1f"},
            labels={
                "media_streams": "Média de streams (milhões)",
                COL_GENRE: "Gênero",
                "artistas": "Artistas no recorte",
            },
        )
        fig_generos.update_layout(
            coloraxis_showscale=False,
            xaxis_title="Média de streams por artista (milhões)",
            yaxis_title="",
            margin=dict(l=10, r=10, t=20, b=10),
        )
        st.plotly_chart(fig_generos, use_container_width=True)
    else:
        st.info("A coluna de gênero não está disponível neste CSV.")

# Relação entre streams como artista principal e como participação em faixas.
st.subheader("Streams como artista principal e como participação")
if COL_LEAD in df_filtrado.columns and COL_FEATURE in df_filtrado.columns:
    fig_relacao = px.scatter(
        df_filtrado,
        x=COL_LEAD,
        y=COL_FEATURE,
        color=COL_GENRE if COL_GENRE in df_filtrado.columns else None,
        hover_name="Artist Name" if "Artist Name" in df_filtrado.columns else None,
        hover_data=[c for c in [COL_TYPE, COL_STREAMS] if c in df_filtrado.columns],
        labels={
            COL_LEAD: "Streams como artista principal (milhões)",
            COL_FEATURE: "Streams como participação (milhões)",
            COL_GENRE: "Gênero",
        },
        opacity=0.75,
    )
    # Escala log torna visíveis artistas com volumes muito diferentes.
    if (df_filtrado[COL_LEAD] > 0).all() and (df_filtrado[COL_FEATURE] > 0).all():
        fig_relacao.update_xaxes(type="log")
        fig_relacao.update_yaxes(type="log")
    fig_relacao.update_layout(height=500, margin=dict(l=10, r=10, t=20, b=10))
    st.plotly_chart(fig_relacao, use_container_width=True)
else:
    st.info("As colunas de streams principais e de participação não estão disponíveis.")
