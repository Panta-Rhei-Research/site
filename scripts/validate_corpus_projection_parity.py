#!/usr/bin/env python3
"""Validate that current site projection files match expected public counts.

The retired v1 Problem Ledger export is intentionally no longer part of the
public site parity contract. Current Agenda/Results projection checks are owned
by Structural Challenges, Challenge Responses, Results, and Corpus Monographs.
"""

from __future__ import annotations

import json
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]


def count_json(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    return len(data) if isinstance(data, list) else len(data.get("items", []))


def count_structural_challenges() -> int:
    total = 0
    for domain in ("mathematics", "physics", "life", "metaphysics"):
        total += count_json(SITE_ROOT / "_data" / "structural_challenges" / f"{domain}.json")
    return total


def count_challenge_response_items() -> int:
    return len([path for path in (SITE_ROOT / "results/challenge-responses").glob("*/*/*.md") if path.name != "index.md"])


def main() -> int:
    result_count = count_json(SITE_ROOT / "_data" / "results" / "results.json")
    recovery_count = count_json(SITE_ROOT / "_data" / "core_semantics" / "recovery-requirements.json")
    construction_count = count_json(SITE_ROOT / "_data" / "construction_spine" / "construction-spine.json")
    agenda_progress_count = count_json(SITE_ROOT / "_data" / "agenda_progress" / "agenda-progress.json")
    monograph_count = (
        count_json(SITE_ROOT / "_data" / "publications" / "books.json")
        + count_json(SITE_ROOT / "_data" / "publications" / "parts.json")
        + count_json(SITE_ROOT / "_data" / "publications" / "chapters.json")
    )

    if count_structural_challenges() != 214:
        raise AssertionError(f"expected 214 Structural Challenges, found {count_structural_challenges()}")
    if count_challenge_response_items() != 214:
        raise AssertionError(f"expected 214 Challenge Response items, found {count_challenge_response_items()}")
    if result_count != 255:
        raise AssertionError(f"expected 255 result pages, found {result_count}")
    if recovery_count != 45:
        raise AssertionError(f"expected 45 Core Semantics recovery items, found {recovery_count}")
    if construction_count != 10:
        raise AssertionError(f"expected 10 Construction Spine items, found {construction_count}")
    if agenda_progress_count != 284:
        raise AssertionError(f"expected 284 Agenda Progress items, found {agenda_progress_count}")
    if monograph_count != 621:
        raise AssertionError(f"expected 621 monograph projection objects, found {monograph_count}")

    for retired in (
        SITE_ROOT / "_data" / "problem_ledger",
        SITE_ROOT / "_data" / "problem_answers",
        SITE_ROOT / "_problem_ledger",
        SITE_ROOT / "assets" / "data" / "problem-ledger",
        SITE_ROOT / "assets" / "data" / "problem-answers",
    ):
        if retired.exists():
            raise AssertionError(f"retired v1 projection path still exists: {retired.relative_to(SITE_ROOT)}")

    print("Corpus projection parity passed.")
    print("Structural Challenges: 214")
    print("Challenge Responses: 214")
    print(f"Result pages: {result_count}")
    print(f"Monograph projection objects: {monograph_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
