"""Transformações compartilhadas pelos dashboards e testes."""
import pandas as pd
import streamlit as st

STREAMS = "Total Streams (in millions)"
GENRE = "Primary Genre"
TYPE = "Artist Type"
YEAR = "Debut Year"
NUMERIC = [STREAMS, "Lead Streams (in millions)", "Feature Streams (in millions)",
           "Solo Streams (in millions)", "Collaborative Streams (in millions)", YEAR]


def filter_data(df, genres, types, years=None):
    mask = df[GENRE].isin(genres) & df[TYPE].isin(types)
    if years is not None:
        mask &= df[YEAR].between(*years)
    return df.loc[mask].copy()


def top_artists(df, count):
    """Limita o recorte pelos maiores volumes, preservando a ordem em empates."""
    return df.sort_values(STREAMS, ascending=False, kind="stable", na_position="last").head(count).copy()


def select_genres(df, items):
    genres = [item[GENRE] for item in items if GENRE in item]
    return df.loc[df[GENRE].isin(genres)] if genres else df


# [IA] Codex (OpenAI) – correlação com cache e conversão da matriz para o formato longo do heatmap.
@st.cache_data(max_entries=64)
def correlation_table(df, variables, method):
    matrix = df[list(variables)].corr(method=method, min_periods=2)
    matrix.index.name = "Variável X"
    return matrix.reset_index().melt(id_vars="Variável X", var_name="Variável Y", value_name="Correlação").dropna()


# [IA] Codex (OpenAI) – implementação dos KPIs, com tratamento de ausentes e denominador zero no Top 5.
def calculate_kpis(df):
    values = df[STREAMS].dropna()
    total = values.sum() if not values.empty else None
    return {
        "artists": df["Artist Name"].nunique(),
        "total": total,
        "median": values.median() if not values.empty else None,
        "top5": 100 * values.nlargest(5).sum() / total if total else None,
    }
