import unittest
from io import BytesIO

from pptx import Presentation

from reporting.deck import make_deck
from reporting.model import COMPANIES, PERIODS, TOPICS, analyze, finding, load_rows


class ReportingTest(unittest.TestCase):
    def report(self, **changes):
        settings = dict(company=COMPANIES[0], peers=list(COMPANIES[1:]),
                        start=PERIODS[0], end=PERIODS[-1], tier="Full")
        return analyze(**(settings | changes))

    def test_complete_fixture(self):
        rows = load_rows()
        self.assertEqual(len(rows), len(COMPANIES) * len(PERIODS) * len(TOPICS))
        keys = {(r["company"], r["quarter"], r["topic"]) for r in rows}
        self.assertEqual(len(keys), len(rows))
        self.assertTrue(all(0 <= r["favorable"] <= r["responses"] and r["responses"] > 0 for r in rows))

    def test_example_reconciles(self):
        r = self.report()
        topic = next(t for t in r["topics"] if t["topic"] == "Growth opportunities")
        self.assertEqual(topic["focus"], {"favorable": 159, "responses": 288, "pct": 55.2})
        self.assertEqual(topic["peers"], {"favorable": 518, "responses": 756, "pct": 68.5})
        self.assertEqual(topic["gap"], -13.3)
        self.assertEqual(r["focus"]["responses"], 1134)
        self.assertEqual(finding(r), "Growth opportunities are 13.3 points below peers.")

    def test_selected_quarter_and_peer(self):
        r = self.report(peers=[COMPANIES[2]], start=PERIODS[1], end=PERIODS[1])
        self.assertEqual([t["quarter"] for t in r["trend"]], [PERIODS[1]])
        self.assertEqual(r["pool"]["responses"], sum(130 + 3*t for t in range(4)))

    def test_invalid_selections(self):
        for changes in [{"peers": []}, {"peers": [COMPANIES[0]]}, {"peers": [COMPANIES[1]] * 2},
                        {"start": PERIODS[2], "end": PERIODS[0]}, {"tier": "Unknown"}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.report(**changes)

    def test_benchmark_and_full_presentations(self):
        for tier, count in [("Benchmark", 2), ("Full", 3)]:
            with self.subTest(tier=tier):
                r = self.report(tier=tier)
                deck = Presentation(BytesIO(make_deck(r)))
                self.assertEqual(len(deck.slides), count)
                text = "\n".join(shape.text for s in deck.slides for shape in s.shapes if shape.has_text_frame)
                self.assertIn(finding(r), text)
                self.assertIn("55.2%", text)
                self.assertEqual("How the overall result changed" in text, tier == "Full")
