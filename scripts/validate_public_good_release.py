#!/usr/bin/env python3
"""Validate the public release surface for Public-Good Impact Dossiers."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import yaml


SITE_ROOT = Path(__file__).resolve().parents[1]
RELEASE_DATA_PATH = SITE_ROOT / "_data" / "impact" / "public_good_dossier_release.yml"
BRIEFINGS_DATA_PATH = SITE_ROOT / "_data" / "impact" / "public-good-briefings.json"
LANDING_ROOT = SITE_ROOT / "publications" / "research-briefings" / "public-good"
PDF_ROOT = SITE_ROOT / "assets" / "pdfs" / "research-briefings" / "public-good"
PORTFOLIO_ORDER_PATH = SITE_ROOT / "_data" / "impact" / "portfolio_order.yml"
RELEASE_DATE = "2026-05-02"
RELEASE_STATUS = "publication_ready"
SOURCE_VERSION = "v3-enriched"
STALE_PHRASES = [
    "deployment papers",
    "public good papers",
    "companion papers",
]
PRIVATE_LEAK_PATTERNS = [
    r"/Users/",
    r"Panta-Rhei-Research/",
    r"\batlas/",
    r"\bprivate repo\b",
    r"\bpapers repo\b",
    r"\bbooks repo\b",
    r"\./atlas\b",
    r"\./papers\b",
    r"\./books\b",
]
LEGACY_ADVANCED_FISSION = (
    "public-good-briefing-2026-04-26-"
    "advanced-fission-safety-operations-licensing-fleet-modernization.pdf"
)


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def page_count(path: Path) -> int:
    try:
        from pypdf import PdfReader  # type: ignore

        return len(PdfReader(str(path)).pages)
    except Exception:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":", 1)[1].strip())
        raise RuntimeError(f"Could not determine page count for {path}")


def site_path(url_path: str) -> Path:
    return SITE_ROOT / url_path.lstrip("/")


def add_if(errors: list[str], condition: bool, message: str) -> None:
    if condition:
        errors.append(message)


def validate() -> list[str]:
    errors: list[str] = []
    release_data: dict[str, dict[str, Any]] = load_yaml(RELEASE_DATA_PATH)
    briefings = json.loads(BRIEFINGS_DATA_PATH.read_text(encoding="utf-8"))
    briefing_by_slug = {item["slug"]: item for item in briefings}

    add_if(errors, len(release_data) != 44, f"expected 44 release records, found {len(release_data)}")
    add_if(errors, len(briefing_by_slug) != 44, f"expected 44 briefing data rows, found {len(briefing_by_slug)}")

    for slug, release in sorted(release_data.items()):
        add_if(errors, slug not in briefing_by_slug, f"{slug}: missing public-good briefing data row")
        pdf_path = site_path(release.get("pdf_path", ""))
        add_if(errors, not pdf_path.is_file(), f"{slug}: missing PDF asset {pdf_path}")
        if pdf_path.is_file():
            add_if(errors, sha256(pdf_path) != release.get("pdf_sha256"), f"{slug}: PDF checksum mismatch")
            add_if(errors, pdf_path.stat().st_size != release.get("pdf_bytes"), f"{slug}: PDF byte count mismatch")
            add_if(errors, page_count(pdf_path) != release.get("pdf_pages"), f"{slug}: PDF page count mismatch")
        for key, expected in [
            ("pdf_status", "available"),
            ("release_date", RELEASE_DATE),
            ("release_status", RELEASE_STATUS),
            ("source_version", SOURCE_VERSION),
            ("domain_review_status", "pending"),
            ("deployment_claim", False),
            ("product_claim", False),
            ("validation_claim", False),
        ]:
            add_if(errors, release.get(key) != expected, f"{slug}: release {key} must be {expected!r}")

        landing_path = LANDING_ROOT / slug / "index.md"
        add_if(errors, not landing_path.is_file(), f"{slug}: missing landing page")
        if landing_path.is_file():
            fm, body = parse_frontmatter(landing_path.read_text(encoding="utf-8"))
            add_if(errors, fm.get("pdf_status") != "available", f"{slug}: landing pdf_status not available")
            add_if(errors, fm.get("pdf_path") != release.get("pdf_path"), f"{slug}: landing pdf_path mismatch")
            add_if(errors, fm.get("artifact_status") != "html_pdf_available", f"{slug}: landing artifact_status mismatch")
            add_if(errors, fm.get("release_status") != RELEASE_STATUS, f"{slug}: landing release_status mismatch")
            add_if(errors, fm.get("domain_review_status") != "pending", f"{slug}: landing domain_review_status mismatch")
            landing_text = yaml.safe_dump(fm, allow_unicode=True) + "\n" + body
            for phrase in STALE_PHRASES:
                add_if(errors, phrase in landing_text.lower(), f"{slug}: stale landing phrase {phrase!r}")

        item = briefing_by_slug.get(slug, {})
        if item:
            for key in ["pdf_status", "pdf_path", "release_status", "source_version", "domain_review_status"]:
                add_if(errors, item.get(key) != release.get(key), f"{slug}: data {key} mismatch")
            add_if(errors, item.get("artifact_status") != "html_pdf_available", f"{slug}: data artifact_status mismatch")
            add_if(errors, item.get("pdf_sha256") != release.get("pdf_sha256"), f"{slug}: data pdf_sha256 mismatch")
            add_if(errors, item.get("pdf_pages") != release.get("pdf_pages"), f"{slug}: data pdf_pages mismatch")

    advanced_legacy = PDF_ROOT / LEGACY_ADVANCED_FISSION
    add_if(errors, not advanced_legacy.is_file(), f"missing advanced-fission legacy PDF URL {advanced_legacy}")

    data_text = BRIEFINGS_DATA_PATH.read_text(encoding="utf-8")
    release_text = RELEASE_DATA_PATH.read_text(encoding="utf-8")
    landing_texts = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(LANDING_ROOT.glob("*/index.md"))
    )
    release_surface_text = "\n".join([data_text, release_text, landing_texts])
    for phrase in STALE_PHRASES:
        add_if(errors, phrase in release_surface_text.lower(), f"stale phrase remains: {phrase!r}")
    for pattern in PRIVATE_LEAK_PATTERNS:
        add_if(errors, re.search(pattern, release_surface_text, flags=re.IGNORECASE) is not None, f"private leak pattern remains: {pattern}")

    for slug in load_yaml(PORTFOLIO_ORDER_PATH):
        old_route = SITE_ROOT / "impact" / "portfolio" / f"{slug}.md"
        add_if(errors, not old_route.is_file(), f"missing old portfolio route source for {slug}")
        if old_route.is_file():
            fm, _ = parse_frontmatter(old_route.read_text(encoding="utf-8"))
            expected = f"/impact/global-public-good/{slug}/"
            add_if(errors, fm.get("layout") != "redirect", f"{slug}: old portfolio route must use redirect layout")
            add_if(errors, fm.get("redirect_to") != expected, f"{slug}: old portfolio redirect_to must be {expected}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Public-Good Dossier release validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Validated 44 Public-Good Impact Dossier PDF releases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
