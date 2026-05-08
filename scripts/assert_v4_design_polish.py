#!/usr/bin/env python3
"""Assertions for the v4 design-system polish pass."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path


LANE_EYEBROWS = {
    "discover/index.html": ("Discover", "Lane Root", "Canonical"),
    "program/index.html": ("Program", "Lane Root", "Canonical"),
    "agenda/index.html": ("Agenda", "Lane Root", "Canonical"),
    "corpus/index.html": ("Corpus", "Lane Root", "Canonical"),
    "results/index.html": ("Results", "Lane Root", "Canonical"),
    "verify/index.html": ("Verify", "Lane Root", "Canonical"),
    "publications/index.html": ("Publications", "Lane Root", "Canonical"),
    "impact/index.html": ("Impact", "Lane Root", "Conditional"),
    "engage/index.html": ("Engage", "Lane Root", "Active"),
}

REPRESENTATIVE_ROUTES = [
    "index.html",
    *LANE_EYEBROWS.keys(),
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


def require_hero_meta(raw: str, route: str, type_label: str, status_label: str) -> None:
    type_pattern = rf'<span class="[^"]*\bhero-meta-pill--type\b[^"]*"[^>]*>\s*{re.escape(type_label)}\s*</span>'
    status_pattern = rf'<span class="[^"]*\bhero-meta-pill--status\b[^"]*"[^>]*>\s*{re.escape(status_label)}\s*</span>'
    if not re.search(type_pattern, raw):
        raise AssertionError(f"{route} missing hero type metadata pill: {type_label}")
    if not re.search(status_pattern, raw):
        raise AssertionError(f"{route} missing hero status metadata pill: {status_label}")


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

    for route, (current_label, type_label, status_label) in LANE_EYEBROWS.items():
        raw = read(site / route)
        require(raw, 'class="hero-eyebrow-row"', f"split eyebrow row for {route}")
        require(raw, 'hero-breadcrumb-pill hero-eyebrow-breadcrumb', f"breadcrumb pill for {route}")
        require(raw, 'class="hero-eyebrow-link hero-breadcrumb-link"', f"linked ancestor crumbs for {route}")
        require(raw, 'aria-label="Breadcrumb"', f"breadcrumb accessibility label for {route}")
        require(raw, '"@type": "BreadcrumbList"', f"structured breadcrumb JSON-LD for {route}")
        breadcrumb_html = attr(raw, r'<nav class="[^"]*\bhero-breadcrumb-pill\b[^"]*"[^>]*>(.*?)</nav>')
        require(breadcrumb_html, "hero-breadcrumb-separator", f"slash breadcrumb separator for {route}")
        require(breadcrumb_html, "/", f"slash breadcrumb separator for {route}")
        require(breadcrumb_html, current_label, f"current breadcrumb label for {route}")
        if type_label.upper() in breadcrumb_html.upper() or status_label.upper() in breadcrumb_html.upper():
            raise AssertionError(f"{route} breadcrumb pill leaks metadata: {breadcrumb_html!r}")
        require_hero_meta(raw, route, type_label, status_label)
        metadata_text = " ".join(
            re.findall(r'<span class="[^"]*\bhero-meta-pill\b[^"]*"[^>]*>([^<]+)</span>', raw)
        )
        lowered = metadata_text.lower()
        for fragment in FORBIDDEN_EYEBROW_FRAGMENTS:
            if fragment in lowered:
                raise AssertionError(f"{route} eyebrow metadata leaks uncontrolled prose/tag text: {metadata_text!r}")

    deep_expectations = {
        "impact/existential-orientation/index.html": ("Impact", "Existential Orientation", "Impact Stratum", "Conditional"),
        "program/about/standing-in-the-inquiry-of-being/index.html": (
            "About the Program",
            "Standing in the Inquiry of Being",
            "Program Charter",
            "Canonical",
        ),
    }
    for route, (expected_parent, suppressed_title, type_label, status_label) in deep_expectations.items():
        raw = read(site / route)
        breadcrumb_html = attr(raw, r'<nav class="[^"]*\bhero-breadcrumb-pill\b[^"]*"[^>]*>(.*?)</nav>')
        require(breadcrumb_html, expected_parent, f"deep breadcrumb parent for {route}")
        if suppressed_title in breadcrumb_html:
            raise AssertionError(f"{route} repeats current page title in breadcrumb pill: {suppressed_title}")
        require_hero_meta(raw, route, type_label, status_label)

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
