import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pandas as pd
import streamlit as st
from streamlit.testing.v1 import AppTest

from src.analytics import (GENRE, TYPE, YEAR, STREAMS, NUMERIC, calculate_kpis,
                           correlation_table, filter_data, select_genres, top_artists)
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

    def test_shared_artist_limit_updates_both_dashboards(self):
        at = self.app()
        at.toggle(key="limit_artists").set_value(True).run()
        at.number_input(key="artist_limit").set_value(50).run()
        expected = top_artists(load_data(), 50)
        self.assertEqual(at.metric[0].value, "50")
        self.assertEqual(at.metric[1].value, f"{expected[STREAMS].sum():,.1f} mi")
        chart_data = []
        original = st.altair_chart

        def capture_data(*args, **kwargs):
            chart_data.append(args[0].data)
            return original(*args, **kwargs)

        with patch("streamlit.altair_chart", side_effect=capture_data):
            at.run()
        # Heatmap, histograma, gêneros, ranking e dispersão.
        self.assertEqual(len(chart_data), 5)
        pd.testing.assert_frame_equal(chart_data[0], correlation_table(expected, tuple(NUMERIC[:3]), "pearson"))
        for data in chart_data[1:]:
            self.assertEqual(set(data["Artist Name"]), set(expected["Artist Name"]))
        at.number_input(key="artist_limit").set_value(100).run()
        self.assertEqual(at.metric[0].value, "100")
        at.toggle(key="limit_artists").set_value(False).run()
        self.assertEqual(at.metric[0].value, str(len(load_data())))
        self.assertFalse(at.exception)

    def test_artist_limit_with_fewer_available_and_empty_filters(self):
        at = self.app()
        at.toggle(key="limit_artists").set_value(True).run()
        at.number_input(key="artist_limit").set_value(500).run()
        at.multiselect(key="genres").set_value(["Pop"]).run()
        expected = load_data().loc[lambda df: df[GENRE].eq("Pop")]
        self.assertEqual(at.number_input(key="artist_limit").value, 500)
        self.assertEqual(at.metric[0].value, str(len(expected)))
        self.assertTrue(any("disponíveis" in info.value for info in at.info))
        at.multiselect(key="genres").set_value([]).run()
        self.assertEqual(at.metric[0].value, "0")
        at.multiselect(key="genres").set_value(["Pop"]).run()
        at.number_input(key="artist_limit").set_value(1).run()
        self.assertEqual(at.metric[0].value, "1")
        self.assertTrue(any("pelo menos dois registros" in info.value for info in at.info))
        self.assertFalse(at.exception)

    def test_alternative_entrypoint(self):
        at = AppTest.from_file(str(ROOT / "app_spotify.py"), default_timeout=30).run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.tabs), 2)

    # [IA] Codex (OpenAI) – simulação do evento de seleção para validar KPIs e dados dos gráficos vinculados.
    def test_chart_selection_updates_dashboard_metrics(self):
        original = st.altair_chart
        secondary_data = []
        selection_applied = False

        def with_selection(*args, **kwargs):
            nonlocal selection_applied
            result = original(*args, **kwargs)
            if kwargs.get("on_select") == "rerun":
                selection_applied = True
                return SimpleNamespace(selection={"genre_click": [{GENRE: "Pop"}]})
            if selection_applied:
                secondary_data.append(args[0].data)
            return result

        with patch("streamlit.altair_chart", side_effect=with_selection):
            at = self.app()
        expected = calculate_kpis(load_data().loc[lambda df: df[GENRE].eq("Pop")])
        self.assertEqual(at.metric[0].value, str(expected["artists"]))
        self.assertEqual(at.metric[1].value, f"{expected['total']:,.1f} mi")
        self.assertEqual(at.metric[2].value, f"{expected['median']:,.1f} mi")
        self.assertEqual(at.metric[3].value, f"{expected['top5']:,.1f}%")
        self.assertEqual(len(secondary_data), 2)
        for data in secondary_data:
            self.assertTrue(data[GENRE].eq("Pop").all())

    def test_numeric_filters_do_not_change_dashboard2(self):
        at = self.app()
        before = [metric.value for metric in at.metric]
        df = load_data()
        value = float(df[STREAMS].min())
        at.slider(key=f"range_{STREAMS}").set_value((value, value)).run()
        self.assertFalse(at.exception)
        self.assertEqual([metric.value for metric in at.metric], before)

    def test_incompatible_csv_shows_friendly_error(self):
        with patch("src.data_loader.load_data", side_effect=ValueError("Colunas obrigatórias ausentes")):
            at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30).run()
        self.assertFalse(at.exception)
        self.assertTrue(any("Colunas obrigatórias" in error.value for error in at.error))


if __name__ == "__main__":
    unittest.main()
