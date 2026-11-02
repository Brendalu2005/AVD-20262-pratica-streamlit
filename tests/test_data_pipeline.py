import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from src.data_loader import load_data

ROOT = Path(__file__).resolve().parents[1]


class DataPipelineTests(unittest.TestCase):
    # [IA] Codex (OpenAI) – execução isolada do notebook para conferir exportação e preservação do CSV bruto.
    def test_export_notebook_preserves_source_and_dashboard_values(self):
        notebook = json.loads((ROOT / "notebooks/eda-com-downloads.ipynb").read_text(encoding="utf-8"))
        # Fixture derivada do CSV versionado: os testes também rodam sem data/raw/.
        expected = pd.read_csv(ROOT / "data/clean/dataset.csv")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            raw = root / "data/raw/Spotify Streaming Performance Dataset.csv"
            raw.parent.mkdir(parents=True)
            expected.rename(columns={"Artist Type": " Artist Type"}).to_csv(raw, index=False)
            original_bytes = raw.read_bytes()
            scope = {}
            with patch("pathlib.Path.cwd", return_value=root):
                for cell in notebook["cells"]:
                    if cell["cell_type"] == "code":
                        exec(compile("".join(cell["source"]), "eda-com-downloads.ipynb", "exec"), scope)
            exported = pd.read_csv(root / "data/clean/dataset.csv")
            pd.testing.assert_frame_equal(exported, expected)
            self.assertEqual(raw.read_bytes(), original_bytes)
            self.assertNotIn("streams_por_ano", exported.columns)

    def test_loader_rejects_wrong_dataset_and_duplicate_artists(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "wrong.csv"
            pd.DataFrame({"age": [30], "chol": [180]}).to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "Colunas obrigatórias"):
                load_data(str(path))
            valid = load_data()
            duplicate = Path(folder) / "duplicate.csv"
            pd.concat([valid.iloc[:1], valid.iloc[:1]]).to_csv(duplicate, index=False)
            with self.assertRaisesRegex(ValueError, "uma linha por artista"):
                load_data(str(duplicate))
