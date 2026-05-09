#!/usr/bin/env python3
"""Assertions for the v4 human-readable sitemap."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse


PRIMARY_LANES = [
    "discover",
    "program",
    "agenda",
    "corpus",
    "results",
    "verify",
    "impact",
    "engage",
]


# Coverage floors per lane (added 2026-05-04 sitemap L1/L2 sync wave).
# Each lane card must surface at least this many mini-card links — guards against
# regressions that strip canonical L2 hubs from the sitemap.
LANE_COVERAGE_FLOOR = {
    "discover": 11,
    "program": 11,
    "agenda": 18,
    "corpus": 24,
    "results": 34,
    "verify": 27,
    "impact": 20,
    "engage": 14,
}

# Total link count floor across all primary lanes + support card.
TOTAL_LINK_FLOOR = 180

# Pages that MUST be discoverable from /sitemap/ — these are the canonical L1/L2
# anchors the broader IA depends on, and their absence is treated as a release blocker.
REQUIRED_KEY_PAGES = [
    "/results/challenge-responses/",
    "/agenda/structural-challenge-ledger/",
    "/agenda/structural-challenge-ledger/mathematics/",
    "/agenda/structural-challenge-ledger/physics/",
    "/agenda/structural-challenge-ledger/life/",
    "/agenda/structural-challenge-ledger/metaphysics/",
    "/corpus/bi-square/",
    "/corpus/taulib/",
    "/corpus/foundational-hinges/",
    "/results/world-readout/",
    "/verify/predictions-and-falsification/",
    "/verify/domain-verification/",
    "/impact/global-public-good/",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def strip_tags(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def route_exists(site_root: Path, href: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith("mailto:"):
        return True
    path = parsed.path
    if path == "/sitemap.xml":
        return (site_root / "sitemap.xml").is_file()
    if path == "/":
        return (site_root / "index.html").is_file()
    normalized = path.lstrip("/")
    return (
        (site_root / normalized).is_file()
        or (site_root / normalized / "index.html").is_file()
        or (site_root / f"{normalized}.html").is_file()
    )


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: assert_v4_sitemap.py <built-site-root>")
    site_root = Path(sys.argv[1]).resolve()
    sitemap_path = site_root / "sitemap" / "index.html"
    if not sitemap_path.is_file():
        fail(f"missing built sitemap at {sitemap_path}")

    html = sitemap_path.read_text(encoding="utf-8")
    visible = strip_tags(html)

    if visible.count("Sitemap") < 1:
        fail("sitemap title is not visible")
    if len(re.findall(r"<h1\b", html, flags=re.I)) != 1:
        fail("sitemap must render exactly one h1")
    if "Core lanes" in visible:
        fail("stale 'Core lanes' copy remains visible")
    if "Human-readable map of the Panta Rhei public research observatory" not in visible:
        fail("locked v4 sitemap intro is missing")
    if "Where the built Corpus becomes a world" not in visible:
        fail("Results card does not use the v4 built-Corpus-becomes-a-world description")
    if "/sitemap.xml" not in html:
        fail("machine-readable /sitemap.xml link is missing")
    if "sitemap-chip" in html:
        fail("sitemap still renders pill/chip link classes instead of mini-card tiles")
    if "sitemap-link-grid" not in html or "sitemap-mini-card" not in html:
        fail("sitemap mini-card grid classes are missing")

    # ---- UX uplift assertions (added 2026-05-09) ----
    # Search input
    if 'id="sitemap-search-input"' not in html:
        fail("sitemap search input (#sitemap-search-input) is missing")
    if 'role="search"' not in html:
        fail("sitemap search container missing role=\"search\"")
    # Jump-nav
    if 'class="sitemap-jump"' not in html:
        fail("sitemap jump-nav (.sitemap-jump) is missing")
    jump_pills = re.findall(r'class="sitemap-jump-pill[^"]*"[^>]+data-jump-target="([^"]+)"', html)
    if len(jump_pills) < 9:
        fail(f"sitemap jump-nav must have ≥9 pills (8 lanes + support); found {len(jump_pills)}")
    for lane in PRIMARY_LANES + ["support"]:
        if f"lane-{lane}" not in jump_pills:
            fail(f"sitemap jump-nav missing pill for {lane}")
    # Per-lane count attribute
    if not re.search(r'data-sitemap-lane-count="\d+"', html):
        fail("sitemap lane cards missing data-sitemap-lane-count attribute")
    # Per-mini-card title attribute (drives client-side search)
    if 'data-sitemap-link-title="' not in html:
        fail("sitemap mini-cards missing data-sitemap-link-title attribute (search index)")
    # Sitemap-search.js loaded
    if "/assets/js/sitemap-search.js" not in html:
        fail("sitemap-search.js script tag missing from /sitemap/ page")
    # Empty-state element
    if 'id="sitemap-empty"' not in html:
        fail("sitemap empty-state container (#sitemap-empty) is missing")
    # Totals chip
    if 'class="sitemap-totals"' not in html:
        fail("sitemap totals chip is missing from intro")

    card_lanes = re.findall(r'data-sitemap-lane="([^"]+)"', html)
    for lane in PRIMARY_LANES:
        if card_lanes.count(lane) != 1:
            fail(f"expected exactly one primary {lane} card")
    if card_lanes.count("support") != 1:
        fail("expected exactly one support card")
    if "publications" in card_lanes:
        fail("Publications must not render as a primary sitemap lane")

    primary_match = re.search(
        r'<section class="sitemap-section"[^>]*aria-labelledby="sitemap-primary-lanes-heading".*?</section>',
        html,
        flags=re.S,
    )
    if not primary_match:
        fail("primary lanes section is missing")
    primary_html = primary_match.group(0)
    if "Agenda" not in strip_tags(primary_html):
        fail("Agenda is missing from primary lanes")
    if re.search(r"<h3>\s*Publications\s*</h3>", primary_html):
        fail("Publications appears as a primary lane heading")

    for lane in PRIMARY_LANES:
        card_match = re.search(
            rf'<article class="sitemap-card sitemap-card-primary" data-sitemap-lane="{lane}".*?</article>',
            html,
            flags=re.S,
        )
        if not card_match:
            fail(f"{lane} card markup missing")
        card_html = card_match.group(0)
        if 'class="sitemap-card-cta"' not in card_html:
            fail(f"{lane} card has no root CTA")
        if 'class="sitemap-link-grid"' not in card_html:
            fail(f"{lane} card does not use the mini-card link grid")
        mini_card_count = len(re.findall(r'class="sitemap-mini-card"', card_html))
        if mini_card_count < 4:
            fail(f"{lane} card does not expose useful second-level links")
        floor = LANE_COVERAGE_FLOOR.get(lane, 0)
        if mini_card_count < floor:
            fail(
                f"{lane} card has {mini_card_count} mini-card links but coverage "
                f"floor is {floor} (sync wave 2026-05-04). Restore canonical L2/L3 "
                f"entries in _data/sitemap_v4.yml."
            )
        if re.search(r'<li class="sitemap-mini-card">\s*<a href="[^"]+">\s*<span>[^<]+</span>\s*</a>\s*</li>', card_html) is None:
            fail(f"{lane} card mini-card links must render as li > a > span")

    support_match = re.search(
        r'<article class="sitemap-card sitemap-card-support" data-sitemap-lane="support".*?</article>',
        html,
        flags=re.S,
    )
    if not support_match:
        fail("support card markup missing")
    support_text = strip_tags(support_match.group(0))
    if "Support layer" not in support_text:
        fail("support card eyebrow should read 'Support layer'")
    for required in ["Publications", "Release Artifacts", "Errata", "Media Kit", "XML Sitemap"]:
        if required not in support_text:
            fail(f"support card missing {required}")

    hrefs = re.findall(r'href="([^"]+)"', html)
    missing = sorted({
        href
        for href in hrefs
        if href.startswith("/")
        and not href.startswith(("/assets/", "/pagefind/"))
        and not route_exists(site_root, href)
    })
    if missing:
        fail("sitemap links do not resolve in built site: " + ", ".join(missing[:20]))

    # Total mini-card link count across primary lanes + support card
    total_mini_cards = len(re.findall(r'class="sitemap-mini-card"', html))
    if total_mini_cards < TOTAL_LINK_FLOOR:
        fail(
            f"sitemap has {total_mini_cards} mini-card links but the L1/L2 sync "
            f"floor is {TOTAL_LINK_FLOOR} (set 2026-05-04). Sitemap may be missing "
            f"canonical hubs — see _data/sitemap_v4.yml."
        )

    # Required-key-pages must each appear as a sitemap href
    href_set = {h.rstrip("/") + "/" if h.startswith("/") and not h.endswith("/") else h for h in hrefs}
    href_set |= set(hrefs)
    missing_keys = [p for p in REQUIRED_KEY_PAGES if p not in hrefs]
    if missing_keys:
        fail(
            "required L1/L2 anchor pages are not surfaced on the sitemap: "
            + ", ".join(missing_keys)
        )

    print(f"v4 sitemap assertions passed ({total_mini_cards} mini-card links across {len(PRIMARY_LANES)} primary lanes + support)")


if __name__ == "__main__":
    main()
