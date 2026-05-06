#!/usr/bin/env python3
"""Validate governed collection counts against site source and built output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def count_yaml_list_items(path: Path, marker: str = "- ") -> int:
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(marker):
            count += 1
    return count


def count_built_challenge_responses(built_root: Path) -> int:
    root = built_root / "results/challenge-responses"
    if not root.exists():
        return 0
    return len(list(root.glob("*/*/*/index.html")))


def count_structural(site_root: Path) -> tuple[int, dict[str, int]]:
    counts: dict[str, int] = {}
    for domain in ("mathematics", "physics", "life", "metaphysics"):
        data = load_json(site_root / "_data/structural_challenges" / f"{domain}.json")
        counts[domain] = len(data.get("items", []))
    return sum(counts.values()), counts


def count_publications(site_root: Path) -> tuple[int, dict[str, int]]:
    counts = {
        "research_monographs": len(load_json(site_root / "_data/publications/books.json")),
        "monograph_supplements": len(
            [path for path in (site_root / "publications/monograph-supplements").glob("*.md") if path.name != "index.md"]
        ),
        "research_papers": count_yaml_list_items(site_root / "_data/publications/research_papers.yml", "- slug:"),
        "research_notes": len(list((site_root / "_research_notes").glob("*.md"))),
        "research_briefings_public_good": len(load_json(site_root / "_data/impact/public-good-briefings.json")),
        "white_papers": len(list((site_root / "publications/white-papers").glob("*/index.md"))),
        "release_artifacts": 0,
        "errata": count_yaml_list_items(site_root / "_data/publications/errata.yml", "- id:"),
    }
    return sum(counts.values()), counts


def actual_counts(site_root: Path, built_root: Path) -> dict[str, int]:
    structural_count, _ = count_structural(site_root)
    publications_count, _ = count_publications(site_root)
    monograph_books = len(load_json(site_root / "_data/publications/books.json"))
    monograph_parts = len(load_json(site_root / "_data/monograph_projections/parts.json"))
    monograph_chapters = len(load_json(site_root / "_data/monograph_projections/chapters.json"))
    route_index = load_json(site_root / "_data/site_atlas/route_index.json")
    legacy_statuses = {"archive", "deprecated", "redirected"}
    return {
        "structural_challenges": structural_count,
        "challenge_responses": count_built_challenge_responses(built_root),
        "results_records": len(load_json(site_root / "_data/results/results.json")),
        "predictions": len(load_json(site_root / "_data/predictions/predictions.json")),
        "falsifications": len(load_json(site_root / "_data/falsifications/falsifications.json")),
        "core_semantics_recovery": len(load_json(site_root / "_data/core_semantics/recovery-requirements.json")),
        "construction_spine": len(load_json(site_root / "_data/construction_spine/construction-spine.json")),
        "construction_map": len(load_json(site_root / "_data/construction_map/construction-map.json")),
        "foundational_hinges": len(load_json(site_root / "_data/foundational_hinges/foundational-hinges.json")),
        "registry_projection": len(load_json(site_root / "_data/registry/objects.json")),
        "taulib_docs_projection": len(load_json(site_root / "_data/taulib/module-inventory.json")),
        "monograph_projections": monograph_books + monograph_parts + monograph_chapters,
        "publications_artifacts": publications_count,
        "scientific_plates": count_yaml_list_items(site_root / "_data/plates.yml", "- id:"),
        "guided_tours": len(list((site_root / "assets/media").glob("guided-tour-book-*.pdf"))),
        "design_system_assets": len(list((site_root / "_sass").glob("*.scss"))) + len(list((site_root / "assets/css").glob("*.scss"))),
        "redirects_legacy_routes": sum(1 for page in route_index.values() if page.get("status") in legacy_statuses),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_root", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("."))
    args = parser.parse_args()

    manifest = load_json(args.site_root / "_data/site_atlas/collections.json")
    actual = actual_counts(args.site_root, args.built_root)
    errors: list[str] = []
    for collection in manifest.get("collections", []):
        key = collection.get("collection_key")
        expected = collection.get("expected_item_count")
        observed = actual.get(key)
        if observed is None:
            errors.append(f"{key}: no count rule")
        elif observed != expected:
            errors.append(f"{key}: expected {expected}, observed {observed}")

    if errors:
        print("Site Atlas collection count check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Site Atlas collection count check passed: {len(manifest.get('collections', []))} collections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
