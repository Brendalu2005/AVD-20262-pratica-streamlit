import unittest
from pathlib import Path

import pandas as pd
from streamlit.testing.v1 import AppTest

from src.analytics import (GENRE, TYPE, YEAR, STREAMS, NUMERIC, calculate_kpis,
                           correlation_table, filter_data, select_genres)
from src.data_loader import load_data

ROOT = Path(__file__).resolve().parents[1]


class AnalyticsTests(unittest.TestCase):
    def test_known_metrics_and_selection(self):
        df = pd.DataFrame({"Artist Name": list("abcdef"), STREAMS: [10, 20, 30, 40, 50, 50], GENRE: ["Pop"] * 3 + ["Rock"] * 3})
        result = calculate_kpis(df)
        self.assertEqual(result["artists"], 6)
        self.assertEqual(result["total"], 200)
        self.assertEqual(result["median"], 35)
        self.assertEqual(result["top5"], 95)
        selected = select_genres(df, [{GENRE: "Pop"}])
        self.assertEqual(calculate_kpis(selected)["total"], 60)
        self.assertEqual(len(select_genres(df, [])), 6)
        self.assertEqual(len(select_genres(df, [{GENRE: "Pop"}, {GENRE: "Rock"}])), 6)
        self.assertIsNone(calculate_kpis(df.iloc[:0])["median"])
        self.assertIsNone(calculate_kpis(df.assign(**{STREAMS: 0}))["top5"])

    def test_filters_recompute_correlation(self):
        df = load_data()
        filtered = filter_data(df, ["Pop"], list(df[TYPE].unique()), (2000, 2010))
        self.assertTrue(filtered[GENRE].eq("Pop").all())
        self.assertTrue(filtered[YEAR].between(2000, 2010).all())
        table = correlation_table(filtered, tuple(NUMERIC[:3]), "pearson")
        expected = filtered[NUMERIC[:3]].corr().iloc[0, 1]
        actual = table.loc[(table["Variável X"] == NUMERIC[0]) & (table["Variável Y"] == NUMERIC[1]), "Correlação"].iloc[0]
        self.assertAlmostEqual(actual, expected)
        self.assertFalse(table.equals(correlation_table(df, tuple(NUMERIC[:3]), "pearson")))
        constant = pd.DataFrame({"x": [1, 1], "y": [2, 2]})
        self.assertTrue(correlation_table(constant, ("x", "y"), "pearson").empty)


class DashboardTests(unittest.TestCase):
    def app(self):
        at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30).run()
        self.assertFalse(at.exception)
        return at

    def test_zero_one_two_and_multiple_variables(self):
        at = self.app()
        self.assertEqual(len(at.tabs), 2)
        for variables in [[], NUMERIC[:1], NUMERIC[:2], NUMERIC[:4]]:
            at.multiselect(key="variables").set_value(variables).run()
            self.assertFalse(at.exception)
            self.assertEqual(len(at.metric), 4)
            if not variables:
                self.assertTrue(any("pelo menos uma" in item.value for item in at.info))
        at.toggle(key="distinguish").set_value(True).run()
        at.selectbox(key="method").set_value("Spearman").run()
        at.selectbox(key="distribution").set_value(NUMERIC[1]).run()
        at.slider(key="bins").set_value(40).run()
        self.assertFalse(at.exception)

    def test_empty_categories_and_single_record(self):
        at = self.app()
        at.multiselect(key="genres").set_value([]).run()
        self.assertFalse(at.exception)
        self.assertEqual(at.metric[0].value, "0")
        self.assertEqual(at.metric[1].value, "Sem dados")
        at.multiselect(key="genres").set_value(["Pop"]).run()
        at.multiselect(key="types").set_value([]).run()
        self.assertFalse(at.exception)
        self.assertEqual(at.metric[0].value, "0")
        at.multiselect(key="types").set_value(["Solo"]).run()
        df = load_data()
        value = float(df.loc[df[GENRE].eq("Pop") & df[TYPE].eq("Solo"), STREAMS].iloc[0])
        at.slider(key=f"range_{STREAMS}").set_value((value, value)).run()
        self.assertFalse(at.exception)
        self.assertTrue(any("pelo menos dois registros" in item.value for item in at.info))

    def test_filter_and_ranking_metrics(self):
        at = self.app()
        at.multiselect(key="genres").set_value(["Pop"]).run()
        expected = load_data().loc[lambda df: df[GENRE].eq("Pop")]
        self.assertEqual(at.metric[0].value, str(expected["Artist Name"].nunique()))
        before = [metric.value for metric in at.metric]
        at.slider(key="ranking_limit").set_value(5).run()
        self.assertEqual([metric.value for metric in at.metric], before)
        self.assertFalse(at.exception)

    def test_alternative_entrypoint(self):
        at = AppTest.from_file(str(ROOT / "app_spotify.py"), default_timeout=30).run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.tabs), 2)


if __name__ == "__main__":
    unittest.main()
