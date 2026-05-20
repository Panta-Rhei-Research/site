#!/usr/bin/env python3
"""Assertions for the v4 mobile shell unification sprint.

Design philosophy
-----------------
This gate guards two distinct surfaces with different stability profiles:

1.  **Source-level invariants** (CSS rules, JS function names, layout
    handlers). Substring search is the right tool — these are source files
    where literal identifiers are the contract.

2.  **Generated UI invariants** (the rendered drawer, page-tools rows, TOC
    list). Substring search is the wrong tool here, because the brand of the
    contract is *behavioral*, not lexical: "if the page has H2s, the drawer
    TOC should list them; otherwise it should show the empty state." Past
    hotfixes (#160, #161, #162, #165) all bled from rigid substring asserts
    that locked us to placeholder HTML which legitimate UI improvements then
    invalidated.

For (2) we parse the built HTML with BeautifulSoup and assert *functional*
invariants: structural existence of containers, validity of action elements
when they appear, and conditional placeholder behavior driven by page state.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

try:
    from bs4 import BeautifulSoup, Tag
except ImportError as exc:  # pragma: no cover - import-time guard
    raise SystemExit(
        "beautifulsoup4 is required: pip install beautifulsoup4"
    ) from exc


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fail(message: str) -> None:
    raise AssertionError(message)


def require_substring(haystack: str, needle: str, label: str) -> None:
    """Source-level substring check. Use only against CSS / JS / layout source."""
    if needle not in haystack:
        fail(f"Missing {label}: {needle}")


def forbid_substring(haystack: str, needle: str, label: str) -> None:
    if needle in haystack:
        fail(f"{label} still contains forbidden token: {needle}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def soup_of(path: Path) -> BeautifulSoup:
    return BeautifulSoup(read(path), "html.parser")


def built_path(root: Path, route: str) -> Path:
    if route == "/":
        return root / "index.html"
    return root / route.strip("/") / "index.html"


# ---------------------------------------------------------------------------
# HTML invariants — parsed structurally, not by substring
# ---------------------------------------------------------------------------

# Always-on page actions in the mobile drawer. Conditional rows
# (dossier-pdf, markdown) are validated separately when present.
ALWAYS_ON_ACTIONS = ("share", "copy-link", "reviewer-note", "copy-citation")

# Conditional rows: action -> (allowed tag, must-have-attrs).
# When a page renders one of these, we validate it is structurally sound; we
# never require its presence (presence is driven by frontmatter — see
# _includes/page-tools.html for the auto-detect chain).
CONDITIONAL_DOWNLOAD_ACTIONS = ("dossier-pdf", "markdown")


def find_drawer(soup: BeautifulSoup) -> Tag:
    drawer = soup.select_one("#header-toc-dropdown")
    if drawer is None:
        fail("Page drawer container #header-toc-dropdown is missing")
    return drawer


def article_h2_count(soup: BeautifulSoup) -> int:
    """Count H2s the drawer TOC would render — i.e. content H2s.

    The Liquid TOC is built from `content | split: '<h2'`, where `content`
    is the rendered Markdown body — *before* the layout adds the
    above-footer page-tools panel (which itself contains an H2). H2s inside
    any `.page-tools` panel and inside `<header>` must be excluded.
    """
    main = soup.select_one(".main-content") or soup.select_one("main")
    if main is None:
        return 0
    n = 0
    for h2 in main.find_all("h2"):
        if h2.find_parent(class_="page-tools"):
            continue
        if h2.find_parent("header"):
            continue
        n += 1
    return n


def assert_drawer_action_invariants(drawer: Tag, route: str) -> None:
    actions = drawer.select("[data-page-action]")
    by_action: dict[str, list[Tag]] = {}
    for el in actions:
        by_action.setdefault(el.get("data-page-action", ""), []).append(el)

    for action in ALWAYS_ON_ACTIONS:
        if action not in by_action:
            fail(f"Drawer missing always-on page action data-page-action={action!r} on {route}")

    # share button must carry a non-empty https share URL pointing at the
    # canonical site host. We don't pin the path — that legitimately changes
    # per page — only that the attribute is shaped like a real URL.
    share_btn = by_action["share"][0]
    share_url = share_btn.get("data-share-url", "")
    if not share_url.startswith("https://"):
        fail(f"share action data-share-url is not an https URL on {route}: {share_url!r}")

    # copy-link button must carry a non-empty URL in data-copy-value.
    copy_btn = by_action["copy-link"][0]
    copy_value = copy_btn.get("data-copy-value", "")
    if not copy_value.startswith("https://"):
        fail(f"copy-link action data-copy-value is not an https URL on {route}: {copy_value!r}")

    # reviewer-note must be an anchor pointing at the GitHub Issues form
    # (right-click / middle-click fallback for the JS dispatch).
    rev = by_action["reviewer-note"][0]
    if rev.name != "a":
        fail(f"reviewer-note action must be an <a> on {route}, got <{rev.name}>")
    href = rev.get("href", "")
    if not (href.startswith("https://github.com/") and "/issues/new" in href):
        fail(f"reviewer-note href is not a GitHub Issues new-issue URL on {route}: {href!r}")

    # copy-citation must carry a non-empty plain-text citation string.
    cite = by_action["copy-citation"][0]
    if not (cite.get("data-copy-value") or "").strip():
        fail(f"copy-citation action has empty data-copy-value on {route}")

    # Conditional download rows: when present, must be valid <a download> with
    # a non-empty href. Their *absence* is allowed (the Liquid include only
    # renders them when frontmatter declares the export — see briefing 27 §9
    # and briefing 29 §2).
    for action in CONDITIONAL_DOWNLOAD_ACTIONS:
        for el in by_action.get(action, []):
            if el.name != "a":
                fail(f"{action!r} action must be an <a download> on {route}, got <{el.name}>")
            if not el.has_attr("download"):
                fail(f"{action!r} action <a> is missing download attribute on {route}")
            href = el.get("href", "")
            if not href:
                fail(f"{action!r} action <a> has empty href on {route}")


def assert_drawer_toc_invariants(drawer: Tag, soup: BeautifulSoup, route: str) -> None:
    toc_list = drawer.select_one("#page-drawer-toc-list")
    if toc_list is None:
        fail(f"Drawer TOC container #page-drawer-toc-list is missing on {route}")

    h2_count = article_h2_count(soup)
    anchors = toc_list.select("a")
    empty_placeholder = toc_list.select_one(".page-drawer-empty")

    if h2_count == 0:
        # Truly empty: drawer must show the empty-state placeholder.
        if empty_placeholder is None:
            fail(
                f"Drawer TOC has no .page-drawer-empty placeholder on {route} "
                f"despite the article having no H2 headings (briefing 29 §3)"
            )
        if anchors:
            fail(
                f"Drawer TOC unexpectedly contains anchor links on {route} "
                f"despite the article having no H2 headings"
            )
    else:
        # Has headings: TOC must list them, with no empty placeholder.
        if empty_placeholder is not None:
            fail(
                f"Drawer TOC shows empty-state placeholder on {route} "
                f"despite the article having {h2_count} H2 heading(s) "
                f"(briefing 29 §3 — placeholder is conditional)"
            )
        if not anchors:
            fail(
                f"Drawer TOC has no anchor links on {route} despite the "
                f"article having {h2_count} H2 heading(s)"
            )
        # Every anchor should point at an in-page fragment.
        for a in anchors:
            href = a.get("href", "")
            if not href.startswith("#"):
                fail(f"Drawer TOC anchor on {route} is not a fragment link: {href!r}")


def assert_drawer_section_order(drawer: Tag, route: str) -> None:
    """Page tools section must come before the On-this-page section."""
    sections = drawer.select(".page-drawer-section")
    if len(sections) < 2:
        fail(f"Drawer is missing one or more page-drawer-section blocks on {route}")
    classes_in_order = [" ".join(s.get("class") or []) for s in sections]
    tools_idx = next((i for i, c in enumerate(classes_in_order) if "page-drawer-tools" in c), -1)
    toc_idx = next((i for i, c in enumerate(classes_in_order) if "page-drawer-toc" in c and "page-drawer-tools" not in c), -1)
    if tools_idx < 0 or toc_idx < 0 or tools_idx > toc_idx:
        fail(
            f"Drawer section order broken on {route}: "
            f"expected page-drawer-tools before page-drawer-toc, got {classes_in_order}"
        )


# ---------------------------------------------------------------------------
# Header shell (parsed)
# ---------------------------------------------------------------------------

EXPECTED_NAV = ("Discover", "Program", "Agenda", "Corpus", "Results", "Verify", "Impact", "Engage")


def assert_header_shell(soup: BeautifulSoup, css: str) -> None:
    # Shared shell controls — these are stable identifiers shared across desktop
    # and mobile, defined in CSS by class. Asserting their existence is
    # functional, not stylistic.
    if soup.select_one("button.header-search.shell-control") is None:
        fail("Shared header-search shell control is missing")
    if soup.select_one("button.header-hamburger.shell-control") is None:
        fail("Shared header-hamburger shell control is missing")

    # Search button must wire up to the toggleSearch() handler.
    search_btn = soup.select_one("button.header-search.shell-control")
    onclick = (search_btn.get("onclick") or "") if search_btn else ""
    if "toggleSearch(" not in onclick:
        fail(f"Header search button is not bound to toggleSearch(): onclick={onclick!r}")

    # Source-level CSS contracts (stable selectors that JS / layout depend on).
    for needle, label in [
        (".shell-control", "shared shell-control CSS"),
        (".header-page-drawer", "this-page drawer CSS"),
        (".page-tool-row", "page tool row CSS"),
        ("body.search-open", "search body scroll lock"),
        ("body.page-drawer-open", "page drawer body scroll lock"),
    ]:
        require_substring(css, needle, label)

    # The legacy chevron must not have come back.
    if soup.select_one(".header-toc-chevron") is not None:
        fail("This Page button still renders the old chevron element")
    if "header-toc-chevron" in css:
        fail("CSS still styles the removed header-toc-chevron")

    # Nav order — pulled from header-nav-link anchors.
    nav_labels = [a.get_text(strip=True) for a in soup.select("a.header-nav-link")]
    if tuple(nav_labels[: len(EXPECTED_NAV)]) != EXPECTED_NAV:
        fail(f"Header nav order drifted: {nav_labels[: len(EXPECTED_NAV)]}")


# ---------------------------------------------------------------------------
# Standard-page drawer surface
# ---------------------------------------------------------------------------

# Fragments of the legacy TOC/list icon SVG. Their continued absence is the
# functional invariant ("we're not rendering the old icon"); no positive
# substring lock-in.
LEGACY_ICON_FRAGMENTS = (
    'x1="6" y1="4" x2="15" y2="4"',
    'cx="3" cy="4" r="1"',
)


def assert_standard_page(soup: BeautifulSoup, route: str) -> None:
    # 1. Drawer wrapper + toggle button — IDs/classes are stable hooks JS
    #    depends on, so structural existence is the right contract.
    wrapper = soup.select_one(".header-page-wrapper.header-toc-wrapper")
    if wrapper is None:
        fail(f"This-page wrapper is missing on {route}")
    toggle = soup.select_one("#header-toc-toggle")
    if toggle is None:
        fail(f"This-page toggle button #header-toc-toggle is missing on {route}")
    if toggle.get("aria-label") != "This page tools and contents":
        fail(f"This-page toggle accessible label changed on {route}: {toggle.get('aria-label')!r}")

    # 2. Article icon — Material Symbols rendering. We assert *shape* (a
    #    Material Symbols viewBox plus a path), not the exact path-d string,
    #    because the icon glyph may change without the contract changing.
    icon = soup.select_one(".header-page-icon")
    if icon is None:
        fail(f"Header page icon SVG missing on {route}")
    if icon.get("viewbox") != "0 -960 960 960":
        fail(
            f"Header page icon is not the Material Symbols viewBox on {route}: "
            f"{icon.get('viewbox')!r}"
        )
    if icon.find("path") is None:
        fail(f"Header page icon has no <path> element on {route}")

    # 3. Legacy icon markup must stay gone.
    html_text = str(soup)
    for fragment in LEGACY_ICON_FRAGMENTS:
        if fragment in html_text:
            fail(f"Old TOC/list icon markup still rendered on {route}: {fragment}")

    # 4. Drawer structural invariants (sections, ordering, actions, TOC).
    drawer = find_drawer(soup)
    assert_drawer_section_order(drawer, route)
    assert_drawer_action_invariants(drawer, route)
    assert_drawer_toc_invariants(drawer, soup, route)

    # 5. SEO / atlas metadata that the layout must preserve. These are
    #    stable contracts with downstream consumers (Search, Atlas, schema.org).
    if soup.select_one('meta[name="prrp:atlas_id"]') is None:
        fail(f"Site Atlas meta tag (prrp:atlas_id) is missing on {route}")
    breadcrumb_present = any(
        '"@type": "BreadcrumbList"' in (script.string or "")
        for script in soup.select('script[type="application/ld+json"]')
    )
    if not breadcrumb_present:
        fail(f"Breadcrumb JSON-LD is missing on {route}")


# ---------------------------------------------------------------------------
# Search shell (source-level — JS / CSS, not generated UI)
# ---------------------------------------------------------------------------

# v4 anti-regression list for search-modal chrome.
#
# v5 audit Item #10 (May 2026) brings back ONE of these — the explicit X
# close button (`search-overlay-close`) — because mobile users can't rely
# on Esc alone and outside-click can feel accidental. The other tokens
# (modal title, hint, filter-API openers, removed marketing copy) remain
# forbidden: v5 keeps the search overlay sparse, with the count band and
# input as the primary chrome.
FORBIDDEN_SEARCH_CHROME = (
    "search-overlay-title",
    "search-overlay-hint",
    "showEmptyFilters",
    "openFilters",
    "Search the Site",
    "Try Hubble",
)


def assert_search_shell(layout_html: str, css: str, page_actions_js: str) -> None:
    # JS source contracts — these are function names / handler hooks the rest
    # of the layout depends on. Substring search is appropriate against source.
    for needle, label in [
        ("new PagefindUI", "Pagefind initialization"),
        ("syncGoogleSearchLink", "Google fallback search sync"),
        ('aria-label="Search the site"', "search dialog accessible label"),
        ("function toggleSearch(force)", "toggle-capable search helper"),
        ("toggleSearch();", "header search toggle invocation"),
        ('data-cfasync="false"', "Rocket-Loader-safe search script"),
        ("window.closePageDrawer", "page drawer close alias"),
    ]:
        require_substring(layout_html, needle, label)

    # Web Share + Clipboard fallback paths moved to the deferred page-actions
    # module in PR #155 (briefing 27). Either source is acceptable: the canonical
    # home is page-actions.js but the layout is allowed to keep an inline path
    # for environments that don't ship the JS module.
    share_haystack = layout_html + "\n" + page_actions_js
    require_substring(share_haystack, "navigator.share", "Web Share fallback path")
    require_substring(share_haystack, "navigator.clipboard", "clipboard fallback path")

    # CSS contracts the search overlay depends on.
    require_substring(css, ".search-overlay-panel", "search overlay panel CSS")
    require_substring(
        css,
        "max-height:calc(100dvh - 56px - 24px)",
        "mobile search shell-card height constraint",
    )
    require_substring(css, ".pagefind-ui__filter-panel", "defensive Pagefind filter CSS")
    if not re.search(r"display:\s*none\s*!important", css):
        fail("Missing hidden Pagefind filter CSS")

    # Removed chrome must not have come back.
    for needle in FORBIDDEN_SEARCH_CHROME:
        forbid_substring(layout_html, needle, "Search shell layout")
        forbid_substring(css, needle, "Search shell CSS")
    if re.search(r"@media \(max-width: 760px\)[\s\S]*?max-height:\s*100dvh", css):
        fail("Mobile search still uses full-screen 100dvh panel sizing")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

STANDARD_ROUTES: tuple[str, ...] = (
    "/program/",
    "/agenda/",
    "/impact/",
    "/verify/release-manifest/",
    "/results/world-readout/physics/",
)


def find_main_css(root: Path) -> Path:
    """Resolve _site/assets/css/main(.<hash>)?.css.

    PR #176 introduced asset fingerprinting (_plugins/asset_fingerprint.rb)
    which renames main.css → main.<hash>.css after Jekyll writes the
    destination tree. The asserter previously hardcoded main.css and broke
    on every post-#176 deploy. Now we glob and pick the unique non-source-map
    match, falling back to the hardcoded name for fingerprint-disabled builds.
    """
    css_dir = root / "assets" / "css"
    plain = css_dir / "main.css"
    if plain.is_file():
        return plain
    candidates = sorted(p for p in css_dir.glob("main.*.css") if not p.name.endswith(".map"))
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        names = ", ".join(p.name for p in candidates)
        fail(f"Multiple main.*.css candidates in {css_dir}: {names}")
    fail(f"Could not resolve compiled main CSS under {css_dir}; expected main.css or main.<hash>.css")
    raise SystemExit(1)  # unreachable; satisfies type checker


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    source_root = root.parent if root.name == "_site" else Path(".")

    css = read(find_main_css(root))
    layout_html = read(source_root / "_layouts" / "default.html")

    # PR #155 moved share / clipboard handlers from inline layout JS to a
    # deferred module at /assets/js/page-actions.js. Read it so the
    # navigator.share / navigator.clipboard checks see the canonical source.
    page_actions_path = source_root / "assets" / "js" / "page-actions.js"
    if not page_actions_path.is_file():
        page_actions_path = root / "assets" / "js" / "page-actions.js"
    page_actions_js = read(page_actions_path) if page_actions_path.is_file() else ""

    home_soup = soup_of(built_path(root, "/"))
    assert_header_shell(home_soup, css)
    if home_soup.select_one(".header-page-wrapper") is not None:
        fail("Home shell should not render the this-page utility drawer")

    for route in STANDARD_ROUTES:
        assert_standard_page(soup_of(built_path(root, route)), route)

    assert_search_shell(layout_html, css, page_actions_js)
    print("v4 mobile shell assertions passed")


if __name__ == "__main__":
    main()
