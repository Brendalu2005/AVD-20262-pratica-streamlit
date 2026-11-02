from pathlib import Path

import pandas as pd
import streamlit as st

from src.analytics import GENRE, TYPE, NUMERIC


@st.cache_data(ttl=3600, max_entries=4)
def load_data(path="data/clean/dataset.csv"):
    """Lê o dataset já tratado (exportado ao final do notebook de EDA)."""
    source = Path(path)
    if not source.is_absolute():
        source = Path(__file__).resolve().parents[1] / source
    df = pd.read_csv(source)
    # [IA] Codex (OpenAI) – validação do esquema e da unicidade de artistas antes do cálculo dos indicadores.
    required = {"Artist Name", GENRE, TYPE, *NUMERIC}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError("Colunas obrigatórias ausentes: " + ", ".join(sorted(missing)))
    if df["Artist Name"].isna().any() or df["Artist Name"].duplicated().any():
        raise ValueError("O CSV deve conter uma linha por artista, com nomes preenchidos e únicos.")
    # [IA] Codex (OpenAI) – conversão numérica e exclusão de valores negativos, inválidos ou infinitos.
    for column in df.columns:
        if "Streams" in column or column == "Debut Year":
            values = pd.to_numeric(df[column], errors="coerce")
            df[column] = values.where(values.ge(0) & values.lt(float("inf")))
    for column in ["Primary Genre", "Artist Type"]:
        df[column] = df[column].fillna("Não informado")
    return df
