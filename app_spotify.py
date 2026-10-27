"""Entrada alternativa: mantém o comando streamlit run app_spotify.py funcionando."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("app.py")), run_name="__main__")
