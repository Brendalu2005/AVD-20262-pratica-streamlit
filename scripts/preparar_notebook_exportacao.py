"""Cria o notebook de preparação do CSV sem modificar a EDA original."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(kind, source):
    result = {"cell_type": kind, "metadata": {}, "source": source.splitlines(keepends=True)}
    if kind == "code":
        result.update(execution_count=None, outputs=[])
    return result


cells = [
    cell("markdown", """# Preparação e exportação — Spotify

Este notebook prepara os dados para o app. A análise original permanece em
`eda.ipynb` e o exemplo do professor em `arquivo-eda-original.ipynb`.
Usa o **carregamento manual de data/raw/** previsto no roteiro.
Coloque o CSV original `Spotify Streaming Performance Dataset.csv` nessa pasta.
O bruto não é alterado nem sobrescrito.

A EDA identificou um espaço no nome de `Artist Type`, ausência de duplicatas e
de valores ausentes, além de outliers legítimos. Mantemos os volumes originais:
os KPIs não usam log nem capping. Exportamos somente as colunas da fonte,
sem `anos_carreira` e `streams_por_ano`: a referência 2010 usada na EDA não é
uma data de coleta comprovada e essas variáveis não são usadas no dashboard.
"""),
    cell("code", """from pathlib import Path
import pandas as pd

ROOT = Path.cwd()
if not (ROOT / "data" / "raw").is_dir():
    ROOT = ROOT.parent
source = ROOT / "data" / "raw" / "Spotify Streaming Performance Dataset.csv"
if not source.is_file():
    raise FileNotFoundError(f"Coloque o CSV original do Spotify em {source}")
df_raw = pd.read_csv(source)
print(f"Fonte: {source.name}; dimensão: {df_raw.shape}")
"""),
    cell("code", """df = df_raw.copy()
df.columns = df.columns.str.strip()
numeric = ["Debut Year", "Total Streams (in millions)",
           "Lead Streams (in millions)", "Feature Streams (in millions)",
           "Solo Streams (in millions)", "% of Solo Streams",
           "Collaborative Streams (in millions)", "% of Collaborative Streams"]
required = {"Artist Name", "Primary Genre", "Artist Type", *numeric}
missing = required.difference(df.columns)
if missing:
    raise ValueError(f"CSV incompatível com o Spotify. Colunas ausentes: {sorted(missing)}")
for column in numeric:
    values = pd.to_numeric(df[column], errors="coerce")
    valid = values.ge(0) & values.lt(float("inf"))
    if column.startswith("%"):
        valid &= values.le(100)
    df[column] = values.where(valid)
for column in ["Primary Genre", "Artist Type"]:
    df[column] = df[column].fillna("Não informado")
if df["Artist Name"].isna().any() or df["Artist Name"].duplicated().any():
    raise ValueError("A fonte deve conter nomes preenchidos e uma linha por artista.")
print(f"Tratado: {df.shape}; valores numéricos ausentes: {df[numeric].isna().sum().sum()}")
"""),
    cell("code", """destination = ROOT / "data" / "clean" / "dataset.csv"
destination.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(destination, index=False, lineterminator="\\n")
print(f"CSV tratado exportado: {destination}")
print(f"Artistas: {df['Artist Name'].nunique()}")
print(f"Streams atribuídos (milhões): {df['Total Streams (in millions)'].sum():,.1f}")
"""),
]

if __name__ == "__main__":
    notebook = {"cells": cells, "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.14.5"},
    }, "nbformat": 4, "nbformat_minor": 4}
    path = ROOT / "notebooks" / "eda-com-downloads.ipynb"
    path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
