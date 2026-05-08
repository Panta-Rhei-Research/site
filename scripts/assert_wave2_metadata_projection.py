#!/usr/bin/env python3
"""Assert the Wave 2 Corpus metadata projection landed in the site worktree."""

from __future__ import annotations

import json
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_COUNTS = {
    "structural_challenges": 214,
    "challenge_responses": 214,
    "generic_results": 255,
    "predictions": 67,
    "falsification_n_tests": 30,
}

REQUIRED_DATA_FILES = [
    "_data/corpus/structural_challenges.yml",
    "_data/corpus/challenge_responses.yml",
    "_data/corpus/results.yml",
    "_data/corpus/predictions.yml",
    "_data/corpus/falsifications.yml",
    "_data/corpus/result_statuses.yml",
    "_data/corpus/response_statuses.yml",
    "_data/corpus/wave2_index.yml",
    "_data/corpus/wave2_progress.yml",
    "assets/data/corpus-wave2/index.json",
    "assets/data/corpus-wave2/progress.json",
    "assets/data/corpus-wave2/prediction-falsification-taxonomy.json",
    "assets/data/structural-challenges/manifest/mathematics.json",
    "assets/data/structural-challenges/manifest/physics.json",
    "assets/data/structural-challenges/manifest/life.json",
    "assets/data/structural-challenges/manifest/metaphysics.json",
]

REQUIRED_ROUTES = [
    "agenda/structural-challenge-ledger/index.md",
    "agenda/structural-challenge-ledger/mathematics/canonical-benchmarks/riemann-hypothesis.md",
    "agenda/structural-challenge-ledger/physics/cosmology-dark-sector/dark-matter.md",
    "agenda/structural-challenge-ledger/life/definition-boundary/what-is-life-structural-class.md",
    "agenda/structural-challenge-ledger/metaphysics/ontology-modality-reality/being-and-something-rather-than-nothing.md",
    "results/challenge-responses/index.md",
    "results/challenge-responses/mathematics.md",
    "results/challenge-responses/physics.md",
    "results/challenge-responses/life.md",
    "results/challenge-responses/metaphysics.md",
    "results/browse.md",
    "results/progress-against-agenda/index.md",
    "results/predictions/index.md",
    "results/predictions/timing.md",
    "results/falsifications/index.md",
    "predictions/a.md",
    "falsifications/n9-tensor-to-scalar-ratio-r-4-00136.md",
]

STALE_TEXT_CHECKS = {
    "agenda/structural-challenge-ledger/index.md": [
        "Wave 1 — Foundation",
        "domain landings below are stubs",
        "subsequent waves",
    ],
    "results/challenge-responses/index.md": [
        "Atlas R5 export pipeline",
    ],
    "results/progress-against-agenda/index.md": [
        "v4 Wave",
        "Wave 3:",
        "Atlas regenerates",
    ],
}


def assert_exists(relative: str) -> None:
    path = SITE_ROOT / relative
    if not path.exists():
        raise AssertionError(f"Missing required file: {relative}")


def main() -> int:
    for relative in REQUIRED_DATA_FILES + REQUIRED_ROUTES:
        assert_exists(relative)

    index = json.loads((SITE_ROOT / "assets/data/corpus-wave2/index.json").read_text(encoding="utf-8"))
    counts = index.get("counts", {})
    for key, expected in EXPECTED_COUNTS.items():
        actual = counts.get(key)
        if actual != expected:
            raise AssertionError(f"{key}: expected {expected}, found {actual}")

    progress = json.loads((SITE_ROOT / "assets/data/corpus-wave2/progress.json").read_text(encoding="utf-8"))
    progress_counts = progress.get("progress", {}).get("counts", {})
    for key, expected in EXPECTED_COUNTS.items():
        actual = progress_counts.get(key)
        if actual != expected:
            raise AssertionError(f"progress.{key}: expected {expected}, found {actual}")

    for relative, stale_strings in STALE_TEXT_CHECKS.items():
        text = (SITE_ROOT / relative).read_text(encoding="utf-8")
        for stale in stale_strings:
            if stale in text:
                raise AssertionError(f"{relative}: stale text still present: {stale!r}")

    print(
        "Wave 2 site projection assertions passed "
        f"({EXPECTED_COUNTS['structural_challenges']} challenges, "
        f"{EXPECTED_COUNTS['challenge_responses']} responses, "
        f"{EXPECTED_COUNTS['generic_results']} results, "
        f"{EXPECTED_COUNTS['predictions']} predictions, "
        f"{EXPECTED_COUNTS['falsification_n_tests']} N-tests)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
