#!/usr/bin/env python3
"""Assertions for the v4 layer color system and clickable hero eyebrow."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PRIMARY_LANES = [
    "discover",
    "program",
    "agenda",
    "corpus",
    "results",
    "verify",
    "publications",
    "impact",
    "engage",
]

OLD_DOMAIN_HEXES = [
    "#1f5d3d",
    "#6b4a14",
    "#4d3a6b",
    "#ddebe2",
    "#f3e8d4",
    "#e8e2ee",
    "#b8d4c2",
    "#d8c5a0",
    "#c2b5d4",
]

REPRESENTATIVE_ROUTES = [
    "index.html",
    "discover/index.html",
    "program/index.html",
    "agenda/index.html",
    "corpus/index.html",
    "results/index.html",
    "verify/index.html",
    "impact/index.html",
    "engage/index.html",
    "sitemap/index.html",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing expected text: {needle}")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    css = read(site / "assets/css/main.css").lower()
    home = read(site / "index.html")
    program = read(site / "program/index.html")

    for lane in PRIMARY_LANES:
        require(css, f"--lane-{lane}: var(--panta-blue-700)", f"neutral lane alias for {lane}")
        require(css, f"--lane-{lane}-soft: var(--panta-blue-50)", f"neutral lane soft alias for {lane}")

    if re.search(r"--lane-(?!support\b)[a-z-]+:\s*#", css):
        raise AssertionError("Primary lane CSS variables must not define distinct hex colors")
    if re.search(r"header-nav-link-(discover|program|agenda|corpus|results|verify|publications|impact|engage)[^{]*\{[^}]*--nav-lane:\s*var\(--lane-", css, re.S):
        raise AssertionError("Header nav keeps lane-specific color overrides instead of the neutral v4 nav color")

    for token in [
        "--layer-e0",
        "--layer-e1",
        "--layer-e2",
        "--layer-e3",
        ".v2-tile-layer",
        ".v2-tile-mathematics",
        ".v2-tile-physics",
        ".v2-tile-life",
        ".v2-tile-metaphysics",
        ".chip-glossary-mathematics",
        ".result-card[data-layer=mathematics]",
        ".result-card[data-world-readout-layer=physics]",
    ]:
        require(css, token, "compiled layer color system")

    for old_hex in OLD_DOMAIN_HEXES:
        if old_hex in css:
            raise AssertionError(f"Old pre-v4 domain color remains in active compiled CSS: {old_hex}")

    for cls in [
        "v2-tile-layer v2-tile-mathematics",
        "v2-tile-layer v2-tile-physics",
        "v2-tile-layer v2-tile-life",
        "v2-tile-layer v2-tile-metaphysics",
    ]:
        require(home, cls, "homepage world-readout layer tiles")

    for layer in ["mathematics", "physics", "life", "metaphysics"]:
        route = site / "results" / "world-readout" / layer / "index.html"
        html = read(route)
        require(html, f'data-world-readout-layer="{layer}"', f"{layer} world-readout anchor layer metadata")

    require(program, 'class="hero-eyebrow-pill hero-eyebrow-breadcrumb"', "clickable hero eyebrow")
    require(program, 'class="hero-eyebrow-link"', "hero eyebrow ancestor links")
    require(program, 'aria-label="Breadcrumb"', "hero eyebrow breadcrumb accessibility")
    require(program, '"@type": "BreadcrumbList"', "structured breadcrumb JSON-LD")
    require(css, ".hero-eyebrow-link", "hero eyebrow link styling")
    require(css, "text-decoration:none", "unstyled hero eyebrow links")

    for route in REPRESENTATIVE_ROUTES:
        html = read(site / route)
        if '<nav class="breadcrumb"' in html:
            raise AssertionError(f"Detached visual breadcrumb nav rendered on {route}")

    nav_match = re.search(r'<nav class="header-nav"[^>]*>(?P<nav>.*?)</nav>', home, re.S)
    if not nav_match:
        raise AssertionError("Header nav not found")
    labels = re.findall(r'class="header-nav-link[^"]*"[^>]*>\s*([^<]+)\s*</a>', nav_match.group("nav"))
    expected = ["Discover", "Program", "Agenda", "Corpus", "Results", "Verify", "Impact", "Engage"]
    if labels != expected:
        raise AssertionError(f"Header nav labels/order drifted: {labels}")

    print("v4 color-system and hero-eyebrow assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
