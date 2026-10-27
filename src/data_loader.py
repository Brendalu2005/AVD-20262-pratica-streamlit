from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data(ttl=3600, max_entries=4)
def load_data(path="data/clean/dataset.csv"):
    """Lê o dataset já tratado (exportado ao final do notebook de EDA)."""
    source = Path(path)
    if not source.is_absolute():
        source = Path(__file__).resolve().parents[1] / source
    df = pd.read_csv(source)
    for column in df.columns:
        if "Streams" in column or column == "Debut Year":
            values = pd.to_numeric(df[column], errors="coerce")
            df[column] = values.where(values.ge(0) & values.lt(float("inf")))
    for column in ["Primary Genre", "Artist Type"]:
        df[column] = df[column].fillna("Não informado")
    return df
