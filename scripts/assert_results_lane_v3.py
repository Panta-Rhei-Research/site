#!/usr/bin/env python3
"""Targeted assertions for the current Results lane projection."""

from __future__ import annotations

import html
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


def load_json(path: str) -> list[dict]:
    data = json.loads((ROOT / path).read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("items", [])


def visible_text(markup: str) -> str:
    markup = re.sub(r"<script[\s\S]*?</script>", " ", markup, flags=re.I)
    markup = re.sub(r"<style[\s\S]*?</style>", " ", markup, flags=re.I)
    markup = re.sub(r"<[^>]+>", " ", markup)
    return re.sub(r"\s+", " ", html.unescape(markup)).strip()


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_contains(path: Path, needle: str) -> None:
    if needle not in path.read_text(encoding="utf-8"):
        raise AssertionError(f"{path.relative_to(ROOT)}: missing {needle!r}")


def source_assertions() -> None:
    results = load_json("_data/results/results.json")
    predictions = load_json("_data/predictions/predictions.json")
    falsifications = load_json("_data/falsifications/falsifications.json")
    structural_counts = {
        domain: len(load_json(f"_data/structural_challenges/{domain}.json"))
        for domain in ("mathematics", "physics", "life", "metaphysics")
    }
    challenge_response_items = [
        path
        for path in (ROOT / "results/challenge-responses").glob("*/*/*.md")
        if path.name != "index.md"
    ]

    assert_equal(len(results), 255, "generic Result count")
    assert_equal(len(predictions), 67, "Prediction facet count")
    assert_equal(len(falsifications), 30, "Falsification Path facet count")
    assert_equal(sum(structural_counts.values()), 214, "Structural Challenge count")
    assert_equal(structural_counts, {"mathematics": 38, "physics": 117, "life": 29, "metaphysics": 30}, "Structural Challenge domain counts")
    assert_equal(len(challenge_response_items), 214, "Challenge Response item pages")

    if (ROOT / "_data/problem_answers").exists():
        raise AssertionError("_data/problem_answers should be pruned from the current Results lane")
    if (ROOT / "assets/data/problem-answers").exists():
        raise AssertionError("public problem-answer data payloads should be pruned")
    assert_contains(ROOT / "results/challenge-responses/index.md", "214 canonical Challenge Responses")
    assert_contains(ROOT / "_includes/result-page-crosslinks.html", "Related Challenge Responses")
    assert_contains(ROOT / "predictions/index.md", "redirect_to: /results/predictions/browse/")
    assert_contains(ROOT / "falsifications/index.md", "redirect_to: /results/falsifications/browse/")


def built_assertions() -> None:
    if not SITE.exists():
        return
    routes = [
        "results/index.html",
        "results/browse/index.html",
        "results/challenge-responses/index.html",
        "results/challenge-responses/mathematics/index.html",
        "results/challenge-responses/physics/cosmology-dark-sector/hubble-tension/index.html",
        "results/challenge-responses/mathematics/canonical-benchmarks/riemann-hypothesis/index.html",
        "results/problem/hubble-tension/index.html",
        "results/predictions/browse/index.html",
        "results/falsifications/browse/index.html",
        "predictions/index.html",
        "falsifications/index.html",
    ]
    for route in routes:
        path = SITE / route
        if not path.exists():
            raise AssertionError(f"built route missing: {route}")
        markup = path.read_text(encoding="utf-8")
        h1_count = len(re.findall(r"<h1\b", markup, flags=re.I))
        assert_equal(h1_count, 1, f"{route} H1 count")

    retired_routes = [
        "results/problem-ledger-answers/physics/hubble-tension/index.html",
        "results/problem-ledger-answers/mathematics/riemann-hypothesis/index.html",
    ]
    for route in retired_routes:
        if (SITE / route).exists():
            raise AssertionError(f"retired legacy answer route still builds: {route}")

    root_text = visible_text((SITE / "results/index.html").read_text(encoding="utf-8"))
    if "255 total result pages" not in root_text and "full 255-page catalogue" not in root_text:
        raise AssertionError("Results root does not expose the 255-result catalogue")
    if "234 total result pages" in root_text:
        raise AssertionError("Results root still exposes 234 total result pages")

    browse_text = visible_text((SITE / "results/browse/index.html").read_text(encoding="utf-8"))
    forbidden = [
        "Status: Resolved",
        "Resolved —",
        "Resolved -",
        "Trolley Problem Resolution",
        "Vacuum Catastrophe Resolution",
        "Fourth Quadrant Resolution",
    ]
    for phrase in forbidden:
        if phrase in browse_text:
            raise AssertionError(f"Browse visible text still contains {phrase!r}")

    response_text = visible_text(
        (SITE / "results/challenge-responses/physics/cosmology-dark-sector/hubble-tension/index.html").read_text(
            encoding="utf-8"
        )
    )
    for phrase in ("Hubble tension", "Structural Challenge", "External-review boundary"):
        if phrase not in response_text:
            raise AssertionError(f"Hubble Challenge Response missing {phrase!r}")

    result_text = visible_text((SITE / "results/problem/hubble-tension/index.html").read_text(encoding="utf-8"))
    if "Related Challenge Responses" not in result_text or "Hubble tension" not in result_text:
        raise AssertionError("Mapped generic Result page does not expose Related Challenge Responses")
    if "/results/problem-ledger-answers/" in (SITE / "results/problem/hubble-tension/index.html").read_text(encoding="utf-8"):
        raise AssertionError("Mapped generic Result page still links to retired Problem Ledger Answers")


def main() -> int:
    source_assertions()
    built_assertions()
    print("Results lane current assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
