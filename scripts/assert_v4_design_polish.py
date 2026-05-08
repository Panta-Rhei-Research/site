#!/usr/bin/env python3
"""Assertions for the v4 design-system polish pass."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path


LANE_LABELS = {
    "discover/index.html": "DISCOVER · LANE ROOT · CANONICAL",
    "program/index.html": "PROGRAM · LANE ROOT · CANONICAL",
    "agenda/index.html": "AGENDA · LANE ROOT · CANONICAL",
    "corpus/index.html": "CORPUS · LANE ROOT · CANONICAL",
    "results/index.html": "RESULTS · LANE ROOT · CANONICAL",
    "verify/index.html": "VERIFY · LANE ROOT · CANONICAL",
    "publications/index.html": "PUBLICATIONS · LANE ROOT · CANONICAL",
    "impact/index.html": "IMPACT · LANE ROOT · CONDITIONAL",
    "engage/index.html": "ENGAGE · LANE ROOT · ACTIVE",
}

REPRESENTATIVE_ROUTES = [
    "index.html",
    *LANE_LABELS.keys(),
    "sitemap/index.html",
    "program/about/standing-in-the-inquiry-of-being/index.html",
    "agenda/core-semantics/index.html",
    "agenda/structural-challenge-ledger/index.html",
    "results/world-readout/index.html",
    "verify/release-manifest/index.html",
    "publications/research-notes/index.html",
    "impact/global-public-good/index.html",
    "engage/corrections/index.html",
]

LANE_ROOTS = [
    "discover/index.html",
    "program/index.html",
    "agenda/index.html",
    "corpus/index.html",
    "results/index.html",
    "verify/index.html",
    "publications/index.html",
    "impact/index.html",
    "engage/index.html",
]

FORBIDDEN_EYEBROW_FRAGMENTS = [
    "summary",
    "description",
    "keywords",
    "github",
    "discussions",
    "open research",
    "released research artifacts",
    "coherent theory of reality",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing expected text: {needle}")


def visible_text(raw_html: str) -> str:
    without_scripts = re.sub(r"<(script|style)\b.*?</\1>", " ", raw_html, flags=re.I | re.S)
    without_tags = re.sub(r"<[^>]+>", " ", without_scripts)
    return " ".join(html.unescape(without_tags).split())


def attr(html_text: str, pattern: str) -> str:
    match = re.search(pattern, html_text, re.S)
    if not match:
        raise AssertionError(f"Missing expected pattern: {pattern}")
    return html.unescape(match.group(1)).strip()


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    root = site.parent
    css = read(site / "assets/css/main.css").lower()
    governed_routes = set(json.loads(read(root / "_data" / "site_atlas" / "route_index.json")).keys())

    for route in REPRESENTATIVE_ROUTES:
        raw = read(site / route)
        if '<nav class="breadcrumb"' in raw:
            raise AssertionError(f"Detached visual breadcrumb nav rendered on standard page: {route}")
        route_url = "/" if route == "index.html" else f"/{route.removesuffix('index.html')}"
        if route_url in governed_routes:
            require(raw, 'name="prrp:atlas_id"', f"Site Atlas metadata for {route}")

    for route, expected_label in LANE_LABELS.items():
        raw = read(site / route)
        require(raw, 'class="hero-eyebrow-pill hero-eyebrow-breadcrumb"', f"hybrid eyebrow for {route}")
        require(raw, 'class="hero-eyebrow-link"', f"linked ancestor crumbs for {route}")
        require(raw, 'aria-label="Breadcrumb"', f"breadcrumb accessibility label for {route}")
        require(raw, '"@type": "BreadcrumbList"', f"structured breadcrumb JSON-LD for {route}")
        current = attr(raw, r'<span class="hero-eyebrow-current">([^<]+)</span>')
        if current != expected_label:
            raise AssertionError(f"{route} eyebrow current label drifted: {current!r}")
        lowered = current.lower()
        for fragment in FORBIDDEN_EYEBROW_FRAGMENTS:
            if fragment in lowered:
                raise AssertionError(f"{route} eyebrow current label leaks uncontrolled prose/tag text: {current!r}")

    for route in LANE_ROOTS:
        raw = read(site / route)
        require(raw, 'property="og:url"', f"OG URL for {route}")
        require(raw, 'property="og:image"', f"OG image for {route}")
        require(raw, 'property="og:image:width" content="1200"', f"OG width for {route}")
        require(raw, 'property="og:image:height" content="630"', f"OG height for {route}")
        require(raw, 'property="og:image:alt"', f"OG image alt for {route}")
        require(raw, 'name="twitter:card" content="summary_large_image"', f"Twitter card for {route}")
        canonical = attr(raw, r'<link rel="canonical" href="([^"]+)"')
        if not canonical.startswith("https://panta-rhei.site/"):
            raise AssertionError(f"{route} canonical URL is not absolute: {canonical}")
        og_image = attr(raw, r'<meta property="og:image" content="([^"]+)"')
        if not og_image.startswith("https://panta-rhei.site/"):
            raise AssertionError(f"{route} OG image URL is not absolute: {og_image}")

    for token in [
        "--font-sans: source sans 3",
        "--font-serif: garamond premier pro",
        "--font-mono: source code pro",
        "--accent-gold: #a8792a",
        "--layer-e0",
        "--layer-e1",
        "--layer-e2",
        "--layer-e3",
    ]:
        require(css, token, "compiled v4 polish tokens")

    for lane in ["discover", "program", "agenda", "corpus", "results", "verify", "publications", "impact", "engage"]:
        require(css, f"--lane-{lane}: var(--panta-blue-700)", f"neutral lane alias for {lane}")
        require(css, f"--lane-{lane}-soft: var(--panta-blue-50)", f"neutral soft lane alias for {lane}")

    require(css, ".hero-eyebrow-link", "hero eyebrow link styling")
    require(css, "text-decoration:none", "unadorned hero eyebrow links")
    if re.search(r"--lane-(discover|program|agenda|corpus|results|verify|publications|impact|engage):\\s*#", css):
        raise AssertionError("Primary lane aliases must not define distinct hex colors")

    icon_data = read(root / "_data" / "icons.yml")
    for key in ["layers:", "mathematics:", "physics:", "life:", "metaphysics:", "lanes:", "artifacts:"]:
        require(icon_data, key, "canonical icon token map")

    home = read(site / "index.html")
    social_links = re.findall(r'<a\b[^>]*class="[^"]*\bsocial-icon\b[^"]*"[^>]*>.*?</a>', home, re.S)
    if len(social_links) < 5:
        raise AssertionError("Expected social icon links in footer")
    for link in social_links:
        require(link, "aria-label=", "social icon accessible name")
        require(link, "title=", "social icon title")
        require(link, 'class="sr-only"', "social icon hidden text")

    for route in [
        "discover/index.html",
        "discover/follow-the-research/index.html",
        "engage/index.html",
        "engage/follow-the-research/index.html",
        "publications/research-notes/index.html",
    ]:
        text = visible_text(read(site / route))
        require(text, "Publication Notifications", f"publication notification wording on {route}")
        for phrase in ["Follow the Research", "Research Notes by email", "email updates"]:
            if phrase in text:
                raise AssertionError(f"{route} still shows stale publication-notification wording: {phrase}")

    media_posters = visible_text(read(site / "media/posters/index.html"))
    require(media_posters, "1536 × 864 JPG", "scientific plate current asset convention")
    require(media_posters, "2048 × 1152 PNG", "scientific plate future regeneration note")

    publications = read(site / "publications/index.html")
    require(publications, '<table class="artifact-classification-matrix">', "Publications matrix table")
    require(publications, "<caption>", "Publications matrix caption")
    require(publications, "<thead>", "Publications matrix header")
    require(publications, 'scope="col"', "Publications matrix column headers")
    require(publications, 'scope="row"', "Publications matrix row headers")

    results_text = visible_text(read(site / "results/index.html"))
    impact_text = visible_text(read(site / "impact/index.html"))
    engage_text = visible_text(read(site / "engage/index.html"))
    require(results_text, "An internally addressed result is not the same as external verification or scientific acceptance.", "Results claim-safety language")
    require(impact_text, "Impact is conditional.", "Impact claim-safety language")
    require(engage_text, "Engagement without endorsement.", "Engage claim-safety language")

    print("v4 design-system polish assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
