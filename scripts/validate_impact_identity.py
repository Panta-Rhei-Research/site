#!/usr/bin/env python3
"""Validate the Impact public-good portfolio identity model."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = ROOT / "_data" / "impact"
ICON_ROOT = ROOT / "assets" / "icons" / "lucide"
SPRITE = ROOT / "assets" / "icons" / "lucide-sprite.svg"
BRIEFING_ROOT = ROOT / "publications" / "research-briefings" / "public-good"

REQUIRED_FIELDS = {
    "id",
    "slug",
    "title",
    "family_key",
    "family",
    "summary_short",
    "url",
    "paper_count",
    "briefing_count",
    "accent",
    "accent_dark",
    "accent_pale",
    "gradient_start",
    "gradient_end",
    "icon",
    "icon_alt",
}
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    return yaml.safe_load(text[4:end]) or {}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    portfolios = load_yaml(DATA_ROOT / "portfolios.yml")
    order = load_yaml(DATA_ROOT / "portfolio_order.yml")
    families = load_yaml(DATA_ROOT / "color_families.yml")
    briefings = json.loads((DATA_ROOT / "public-good-briefings.json").read_text(encoding="utf-8"))
    sprite_text = SPRITE.read_text(encoding="utf-8") if SPRITE.is_file() else ""

    if not isinstance(portfolios, dict):
        fail(errors, "portfolios.yml must be a keyed map.")
        portfolios = {}
    if len(portfolios) != 11:
        fail(errors, f"expected 11 portfolios, found {len(portfolios)}.")
    if order != list(portfolios.keys()):
        fail(errors, "portfolio_order.yml must match portfolios.yml key order exactly.")

    ids = set()
    briefing_counts = Counter(item.get("portfolio_id") for item in briefings)
    for slug in order:
        portfolio = portfolios.get(slug)
        if not portfolio:
            fail(errors, f"ordered portfolio {slug} missing from portfolios.yml.")
            continue
        missing = REQUIRED_FIELDS - set(portfolio)
        if missing:
            fail(errors, f"{slug}: missing fields {sorted(missing)}.")
        if portfolio.get("slug") != slug:
            fail(errors, f"{slug}: slug field does not match map key.")
        if portfolio.get("id") in ids:
            fail(errors, f"{slug}: duplicate portfolio id {portfolio.get('id')}.")
        ids.add(portfolio.get("id"))
        if portfolio.get("family_key") not in families:
            fail(errors, f"{slug}: unknown family_key {portfolio.get('family_key')}.")
        for field in ["accent", "accent_dark", "accent_pale", "gradient_start", "gradient_end"]:
            if not HEX.match(str(portfolio.get(field, ""))):
                fail(errors, f"{slug}: {field} must be a #RRGGBB hex color.")
        icon = portfolio.get("icon", "")
        if not (ICON_ROOT / f"{icon}.svg").is_file():
            fail(errors, f"{slug}: missing local icon {icon}.svg.")
        if f'id="{icon}"' not in sprite_text:
            fail(errors, f"{slug}: icon {icon} missing from lucide-sprite.svg.")
        expected = briefing_counts[portfolio.get("id")]
        if int(portfolio.get("briefing_count", -1)) != expected:
            fail(errors, f"{slug}: briefing_count {portfolio.get('briefing_count')} does not match {expected}.")

    for path in sorted(BRIEFING_ROOT.glob("*/index.md")):
        fm = parse_frontmatter(path)
        slug = fm.get("portfolio")
        portfolio_id = fm.get("portfolio_id", "")
        expected_slug = str(portfolio_id).replace("impact-", "")
        if slug not in portfolios:
            fail(errors, f"{path.relative_to(ROOT)}: portfolio must be a canonical slug, got {slug!r}.")
        if expected_slug and slug != expected_slug:
            fail(errors, f"{path.relative_to(ROOT)}: portfolio {slug!r} does not match {portfolio_id!r}.")
        body = path.read_text(encoding="utf-8")
        if re.search(r"#[0-9A-Fa-f]{6}", body):
            fail(errors, f"{path.relative_to(ROOT)}: hardcoded color detected.")

    local_icon_text = "\n".join(path.read_text(encoding="utf-8") for path in ICON_ROOT.glob("*.svg"))
    if "http://www.w3.org/2000/svg" not in local_icon_text:
        fail(errors, "local SVG icons are missing SVG namespace declarations.")
    scan_roots = [ROOT / "_layouts", ROOT / "_includes", ROOT / "_sass", ROOT / "assets" / "css"]
    for root in scan_roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in {".html", ".scss", ".css"}:
                text = path.read_text(encoding="utf-8")
                if "lucide.dev" in text or "unpkg.com/lucide" in text:
                    fail(errors, f"{path.relative_to(ROOT)}: external Lucide reference detected.")

    if errors:
        print("Impact identity validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Impact identity validation passed for 11 portfolios and 44 Public-Good Briefings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
