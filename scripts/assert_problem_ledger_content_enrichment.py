#!/usr/bin/env python3
"""Assert that the retired v1 ledger was replaced by the v4 SCL projection."""

from __future__ import annotations

import json
import sys
from pathlib import Path


EXPECTED_COUNTS = {
    "life": 29,
    "mathematics": 38,
    "metaphysics": 30,
    "physics": 117,
}


def page_path(site_dir: Path, url: str) -> Path:
    return site_dir / url.strip("/") / "index.html"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: assert_problem_ledger_content_enrichment.py _site", file=sys.stderr)
        return 2
    site_dir = Path(sys.argv[1])
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    retired_paths = [
        repo_root / "_problem_ledger",
        repo_root / "_data/problem_ledger",
        repo_root / "assets/data/problem-ledger",
        repo_root / "_layouts/problem-ledger-item.html",
    ]
    for path in retired_paths:
        if path.exists():
            errors.append(f"retired v1 Problem Ledger source still exists: {path.relative_to(repo_root)}")

    counts = {}
    for domain, expected in EXPECTED_COUNTS.items():
        data = json.loads((repo_root / "_data/structural_challenges" / f"{domain}.json").read_text(encoding="utf-8"))
        counts[domain] = len(data.get("items", []))
        if counts[domain] != expected:
            errors.append(f"{domain}: expected {expected} Structural Challenges, found {counts[domain]}")

    if sum(counts.values()) != 214:
        errors.append(f"expected 214 Structural Challenges, found {sum(counts.values())}")

    required_routes = [
        "/agenda/structural-challenge-ledger/",
        "/agenda/structural-challenge-ledger/source-policy/",
        "/agenda/structural-challenge-ledger/physics/cosmology-dark-sector/hubble-tension/",
        "/agenda/structural-challenge-ledger/life/origin-substrate-life-as-could-be/abiogenesis-first-persistence/",
    ]
    for route in required_routes:
        if not page_path(site_dir, route).exists():
            errors.append(f"required SCL route missing: {route}")

    retired_item_routes = [
        "/agenda/problem-ledger/physics/hubble-tension/",
        "/agenda/problem-ledger/life/origin-of-life/",
    ]
    for route in retired_item_routes:
        if page_path(site_dir, route).exists():
            errors.append(f"retired generated v1 item route still builds: {route}")

    if errors:
        print("Structural Challenge Ledger replacement assertions failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Structural Challenge Ledger replacement assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
