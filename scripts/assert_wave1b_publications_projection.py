#!/usr/bin/env python3
"""Assert the Corpus-backed publication projection is present in the built site."""

from __future__ import annotations

import argparse
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]


def require_path(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"Missing {label}: {path.relative_to(SITE_ROOT)}")


def require_text(path: Path, needles: list[str], label: str) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    missing = [needle for needle in needles if needle not in text]
    if missing:
        joined = ", ".join(repr(needle) for needle in missing)
        raise SystemExit(f"{label} missing expected text in {path.relative_to(SITE_ROOT)}: {joined}")


def forbid_text(root: Path, needles: list[str]) -> None:
    hits: list[str] = []
    for path in sorted(root.rglob("*.html")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle in text:
                hits.append(f"{path.relative_to(root)}: {needle}")
    if hits:
        raise SystemExit("Old Research Notes notification wording remains:\n" + "\n".join(hits[:20]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="_site", help="Built Jekyll site directory.")
    args = parser.parse_args()

    built_site = (SITE_ROOT / args.site).resolve()
    require_path(built_site, "built site")

    for relative in (
        "_data/corpus/publications.yml",
        "_data/corpus/latest_publications.yml",
        "_data/corpus/publication_types.yml",
        "_data/corpus/people.yml",
        "_data/corpus/external_surfaces.yml",
        "_data/corpus/bibliography_summary.yml",
        "assets/data/publications/publications.json",
        "assets/data/publications/latest-publications.json",
    ):
        require_path(SITE_ROOT / relative, "synced Corpus publication data")

    require_path(built_site / "publications" / "latest" / "index.html", "Latest Publications page")
    require_text(
        built_site / "publications" / "latest" / "index.html",
        [
            "Artifact stream, not news",
            "GitHub mirror",
            "Corpus-backed stream",
        ],
        "Latest Publications page",
    )

    require_text(
        built_site / "publications" / "research-papers" / "hyperfactorization-theorem" / "index.html",
        [
            'name="citation_title"',
            'name="citation_author"',
            'name="citation_publication_date"',
            'name="citation_pdf_url"',
            'name="citation_doi"',
            '"@type": "ScholarlyArticle"',
        ],
        "Research Paper metadata",
    )

    require_text(
        built_site / "publications" / "research-notes" / "semantic-space-has-a-shape" / "index.html",
        [
            'name="citation_title"',
            'name="citation_author"',
            'name="citation_publication_date"',
            'name="citation_pdf_url"',
            '"@type": "ScholarlyArticle"',
        ],
        "Research Note metadata",
    )

    forbid_text(
        built_site,
        [
            "How to receive Research Notes",
            "Receive Research Notes",
            "Get new Panta Rhei Research Notes by email",
        ],
    )

    print("Wave 1B publication projection assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
