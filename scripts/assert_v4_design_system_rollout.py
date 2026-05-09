#!/usr/bin/env python3
"""Assertions for the v4 design-system rollout."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPRESENTATIVE_ROUTES = [
    "index.html",
    "discover/index.html",
    "program/index.html",
    "agenda/index.html",
    "corpus/index.html",
    "results/index.html",
    "verify/index.html",
    "publications/index.html",
    "impact/index.html",
    "engage/index.html",
    "sitemap/index.html",
]

STRUCTURED_BREADCRUMB_ROUTES = [
    "program/index.html",
    "agenda/index.html",
    "corpus/index.html",
    "results/index.html",
    "verify/index.html",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing expected text: {needle}")


def normalize(value: str) -> str:
    return " ".join(value.split())


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    css = read(site / "assets/css/main.css")
    home = read(site / "index.html")

    for token in [
        "--panta-blue-800",
        "--paper-50",
        "--ink-900",
        "--layer-e0",
        "--font-serif",
        ".hero-eyebrow-pill",
    ]:
        require(css, token, "compiled v4 design tokens")

    require(home, ".hero-eyebrow-pill", "critical CSS")
    require(home, "--panta-blue-800", "critical CSS")
    top_nav_match = re.search(r'<nav class="header-nav"[^>]*>(?P<nav>.*?)</nav>', home, re.S)
    if not top_nav_match:
        raise AssertionError("Header nav not found")
    labels = re.findall(r'class="header-nav-link[^"]*"[^>]*>\s*([^<]+)\s*</a>', top_nav_match.group("nav"))
    expected_labels = ["Discover", "Program", "Agenda", "Corpus", "Results", "Verify", "Impact", "Engage"]
    if labels != expected_labels:
        raise AssertionError(f"Header nav labels/order drifted: {labels}")

    for route in REPRESENTATIVE_ROUTES:
        html = read(site / route)
        if '<nav class="breadcrumb"' in html:
            raise AssertionError(f"Detached visual breadcrumb nav rendered on {route}")
        if route != "index.html" and "hero-eyebrow-pill" not in html:
            raise AssertionError(f"Hero eyebrow identity missing on {route}")
        require(html, 'name="prrp:atlas_id"', f"Site Atlas metadata for {route}")

    for route in STRUCTURED_BREADCRUMB_ROUTES:
        html = read(site / route)
        require(html, '"@type": "BreadcrumbList"', f"structured breadcrumb data for {route}")

    compact_css = normalize(css)
    for selector in [".hero-card", ".content-card", ".lane-card", ".chip", ".scientific-plate"]:
        if selector not in compact_css:
            raise AssertionError(f"Expected shared component selector missing from compiled CSS: {selector}")
    if "assets/og-cards/index.png" in home or "assets/og-cards/index.svg" in home:
        raise AssertionError("Normal build should not point homepage OG metadata at retired legacy social-preview cards")

    print("v4 design-system rollout assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
