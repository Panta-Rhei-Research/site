#!/usr/bin/env python3
"""Focused assertions for Corpus Metadata Wave 4 site projection."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(relative: str):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8")) or {}


def error(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    errata = load_yaml("_data/corpus/governance/errata.yml").get("errata", [])
    changelog = load_yaml("_data/corpus/governance/corpus_changelog.yml").get("entries", [])
    editions = load_yaml("_data/corpus/governance/edition_history.yml").get("editions", [])
    plates = load_yaml("_data/corpus/assets/scientific_plates.yml").get("scientific_plates", [])
    covers = load_yaml("_data/corpus/assets/covers.yml").get("covers", [])

    if len(errata) != 4:
        error(f"expected 4 errata, found {len(errata)}", errors)
    if len(changelog) != 5:
        error(f"expected 5 changelog entries, found {len(changelog)}", errors)
    if len(editions) != 14:
        error(f"expected 14 edition records, found {len(editions)}", errors)
    if len(plates) != 15:
        error(f"expected 15 scientific plates, found {len(plates)}", errors)
    if len(covers) != 35:
        error(f"expected 35 cover assets, found {len(covers)}", errors)
    if any("reporter" in json.dumps(item).lower() for item in changelog + errata):
        error("private reporter metadata leaked into Wave 4 public projection", errors)

    required_routes = [
        "corpus/changelog/index.md",
        "corpus/versioning/index.md",
        "publications/errata/index.md",
        "publications/books/book-i/errata/index.md",
        "publications/books/book-ii/errata/index.md",
        "publications/books/book-iii/errata/index.md",
        "publications/books/book-iv/errata/index.md",
        "publications/books/book-v/errata/index.md",
        "publications/books/book-vi/errata/index.md",
        "publications/books/book-vii/errata/index.md",
        "assets/data/corpus-wave4/index.json",
        "assets/data/corpus-wave4/errata.json",
        "assets/data/corpus-wave4/scientific-plates.json",
    ]
    for route in required_routes:
        if not (ROOT / route).exists():
            error(f"missing Wave 4 route/data file: {route}", errors)

    corpus_changelog = (ROOT / "corpus/changelog/index.md").read_text(encoding="utf-8")
    technical_changelog = (ROOT / "changelog/index.md").read_text(encoding="utf-8")
    if "technical Changelog" not in corpus_changelog and "Technical Changelog" not in corpus_changelog:
        error("/corpus/changelog/ does not route to the technical changelog for separation", errors)
    if "Corpus Changelog" not in corpus_changelog:
        error("/corpus/changelog/ lost Corpus Changelog identity", errors)
    if "technical" not in technical_changelog.lower():
        error("/changelog/ does not retain technical/site changelog framing", errors)

    book_i_errata = (ROOT / "publications/books/book-i/errata/index.md").read_text(encoding="utf-8")
    if "ERRATUM-001" not in book_i_errata or "ERRATUM-003" not in book_i_errata:
        error("Book I errata page missing expected ERRATUM-001/ERRATUM-003 records", errors)
    book_ii_errata = (ROOT / "publications/books/book-ii/errata/index.md").read_text(encoding="utf-8")
    if "No book-specific errata currently issued" not in book_ii_errata:
        error("zero-state book errata page missing for Book II", errors)

    if errors:
        print("Wave 4 site projection assertions failed:")
        for item in errors:
            print(f"- {item}")
        return 1
    print("Wave 4 site projection assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
