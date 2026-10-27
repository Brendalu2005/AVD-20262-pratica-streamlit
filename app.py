import altair as alt
import pandas as pd
import streamlit as st

from src.analytics import (GENRE, TYPE, YEAR, NUMERIC, STREAMS, calculate_kpis,
                           correlation_table, filter_data, select_genres)
from src.data_loader import load_data

st.set_page_config(page_title="Spotify | Audiência em foco", page_icon=":material/music_note:", layout="wide")
st.title("Spotify — audiência em foco")
st.caption("Explore relações entre variáveis e compare a audiência acumulada dos artistas.")
try:
    df = load_data()
except (FileNotFoundError, KeyError, pd.errors.EmptyDataError) as error:
    st.error(f"Não foi possível carregar o CSV tratado do Spotify: {error}")
    st.stop()

with st.sidebar:
    st.header("Filtros compartilhados")
    genres = sorted(df[GENRE].unique())
    types = sorted(df[TYPE].unique())
    selected_genres = st.multiselect("Gêneros musicais", genres, default=genres, key="genres")
    selected_types = st.multiselect("Tipos de artista", types, default=types, key="types")
    years = None
    valid_years = df[YEAR].dropna()
    if not valid_years.empty:
        low, high = int(valid_years.min()), int(valid_years.max())
        if low < high:
            years = st.slider("Ano de estreia", low, high, (low, high), key="years")
        else:
            st.caption(f"Único ano de estreia: {low}")
    st.caption("Ano de estreia do artista; não é o período das reproduções. Categorias vazias não selecionam artistas.")

filtered = filter_data(df, selected_genres, selected_types, years)
st.caption(f"{len(filtered)} de {len(df)} registros após os filtros compartilhados.")
tab1, tab2 = st.tabs(["Dashboard 1 · Exploração", "Dashboard 2 · Indicadores"])

with tab1:
    variables = st.multiselect("Variáveis quantitativas", NUMERIC, default=NUMERIC[:3], key="variables")
    distinguish = st.toggle("Distinguir por gênero", key="distinguish")
    method_label = st.selectbox("Método de correlação", ["Pearson", "Spearman"], key="method")
    ranges = {}
    with st.expander("Intervalos das variáveis selecionadas"):
        for variable in variables:
            valid = df[variable].dropna()
            if valid.empty or valid.nunique() < 2:
                st.caption(f"{variable}: sem intervalo ajustável.")
                continue
            lo, hi = float(valid.min()), float(valid.max())
            ranges[variable] = st.slider(variable, lo, hi, (lo, hi), key=f"range_{variable}")
    explored = filtered.copy()
    for variable, (lo, hi) in ranges.items():
        explored = explored.loc[explored[variable].between(lo, hi)]
    st.caption(f"{len(explored)} registros no recorte exploratório. Volumes de streams em milhões.")
    if not variables:
        st.info("Selecione pelo menos uma variável para visualizar a distribuição e duas para a correlação.")
    elif explored.empty:
        st.info("Nenhum artista corresponde aos intervalos e filtros. Amplie o recorte.")
    else:
        left, right = st.columns([1, 1.3])
        with left:
            st.subheader("Correlação")
            if len(variables) < 2:
                st.info("Selecione pelo menos duas variáveis para calcular a correlação.")
            elif len(explored) < 2:
                st.info("São necessários pelo menos dois registros para calcular a correlação.")
            else:
                table = correlation_table(explored, tuple(variables), method_label.lower())
                if table.empty:
                    st.info("Correlação indefinida: valores constantes ou pares insuficientes.")
                else:
                    base = alt.Chart(table).encode(x=alt.X("Variável X:N", title=None), y=alt.Y("Variável Y:N", title=None))
                    heat = base.mark_rect().encode(color=alt.Color("Correlação:Q", scale=alt.Scale(domain=[-1, 1], scheme="redblue")), tooltip=["Variável X:N", "Variável Y:N", alt.Tooltip("Correlação:Q", format=".3f")])
                    labels = base.mark_text().encode(text=alt.Text("Correlação:Q", format=".2f"), color=alt.condition("abs(datum['Correlação']) > 0.6", alt.value("white"), alt.value("black")))
                    st.altair_chart((heat + labels).properties(height=360), width="stretch")
                    st.caption("Células indefinidas são omitidas. Correlação não implica causalidade.")
        with right:
            st.subheader("Distribuição")
            variable = st.selectbox("Variável da distribuição", variables, key="distribution")
            bins = st.slider("Número máximo de classes", 5, 60, 20, key="bins")
            data = explored.dropna(subset=[variable])
            if data.empty:
                st.info("Não há valores válidos para esta distribuição.")
            else:
                histogram = alt.Chart(data).mark_bar(opacity=0.75).encode(x=alt.X(f"{variable}:Q", bin=alt.Bin(maxbins=bins)), y=alt.Y("count():Q", title="Artistas"), tooltip=[alt.Tooltip("count():Q", title="Artistas")])
                if distinguish:
                    histogram = histogram.encode(color=alt.Color(f"{GENRE}:N", title="Gênero"))
                else:
                    histogram = histogram.encode(color=alt.value("#C65318"))
                st.altair_chart(histogram.properties(height=360), width="stretch")

with tab2:
    st.subheader("Indicadores de audiência")
    limit = st.slider("Artistas no ranking", 5, 20, 10, key="ranking_limit")
    # O espaço é criado antes do gráfico, mas preenchido após ler o evento.
    metrics_slot = st.container()
    st.caption("Clique em um gênero para filtrar os KPIs e gráficos abaixo. Shift + clique combina gêneros; duplo clique limpa.")
    selected = filtered
    if not filtered.empty:
        click = alt.selection_point(name="genre_click", fields=[GENRE], clear="dblclick")
        bars = alt.Chart(filtered).mark_bar().encode(
            x=alt.X(f"sum({STREAMS}):Q", title="Streams atribuídos (milhões)"),
            y=alt.Y(f"{GENRE}:N", sort="-x", title="Gênero"),
            opacity=alt.condition(click, alt.value(1), alt.value(0.3)),
            color=alt.value("#C65318"),
            tooltip=[GENRE, alt.Tooltip(f"sum({STREAMS}):Q", title="Streams (milhões)", format=",.1f")],
        ).add_params(click).properties(height=300)
        # Uma nova chave ao mudar a população evita seleções antigas invisíveis.
        population = pd.util.hash_pandas_object(filtered, index=True).sum()
        event = st.altair_chart(bars, key=f"genre_chart_{population}", on_select="rerun", width="stretch")
        selected = select_genres(filtered, event.selection.get("genre_click", []))
    kpis = calculate_kpis(selected)
    def display_number(value, suffix=""):
        return "Sem dados" if value is None or pd.isna(value) else f"{value:,.1f}{suffix}"
    with metrics_slot:
        cards = st.columns(4)
        cards[0].metric("Artistas no recorte", str(kpis["artists"]), border=True)
        cards[1].metric("Streams atribuídos", display_number(kpis["total"], " mi"), border=True)
        cards[2].metric("Streams medianos / artista", display_number(kpis["median"], " mi"), border=True)
        cards[3].metric("Participação do Top 5", display_number(kpis["top5"], "%"), border=True)
    if selected.empty:
        st.info("Nenhum artista no recorte. Ajuste os filtros ou limpe a seleção de gêneros.")
    else:
        left, right = st.columns(2)
        with left:
            st.subheader(f"Top {limit} artistas por streams")
            ranking = selected.dropna(subset=[STREAMS]).nlargest(limit, STREAMS)
            if ranking.empty:
                st.info("Sem volumes válidos para o ranking.")
            else:
                chart = alt.Chart(ranking).mark_bar(color="#C65318").encode(x=alt.X(f"{STREAMS}:Q", title="Streams (milhões)"), y=alt.Y("Artist Name:N", sort="-x", title=None), tooltip=["Artist Name", GENRE, alt.Tooltip(f"{STREAMS}:Q", format=",.1f")])
                st.altair_chart(chart.properties(height=400), width="stretch")
        with right:
            st.subheader("Principal × participação")
            lead, feature = NUMERIC[1:3]
            points = selected.dropna(subset=[lead, feature])
            if points.empty:
                st.info("Sem pares válidos para a dispersão.")
            else:
                scatter = alt.Chart(points).mark_circle(size=65, opacity=0.7).encode(x=alt.X(f"{lead}:Q", title="Principal (milhões)"), y=alt.Y(f"{feature}:Q", title="Participação (milhões)"), color=alt.Color(f"{GENRE}:N", title="Gênero"), tooltip=["Artist Name", GENRE, alt.Tooltip(f"{lead}:Q", format=",.1f"), alt.Tooltip(f"{feature}:Q", format=",.1f")]).interactive()
                st.altair_chart(scatter.properties(height=400), width="stretch")
    st.caption("Volumes acumulados atribuídos aos artistas; a soma pode contar participações em duplicidade e não representa streams únicos da plataforma. Top 5 é calculado no recorte completo, independentemente do tamanho do ranking.")
