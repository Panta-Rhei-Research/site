#!/usr/bin/env python3
"""Assertions for the v4 mobile shell unification sprint."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise AssertionError(message)


def require(haystack: str, needle: str, label: str) -> None:
    if needle not in haystack:
        fail(f"Missing {label}: {needle}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def built_path(root: Path, route: str) -> Path:
    if route == "/":
        return root / "index.html"
    return root / route.strip("/") / "index.html"


def assert_header_shell(index_html: str, css: str) -> None:
    require(index_html, 'class="header-search shell-control"', "shared search shell control")
    require(index_html, 'onclick="toggleSearch()"', "header search toggle binding")
    require(index_html, 'class="header-hamburger shell-control"', "shared explore shell control")
    require(css, ".shell-control", "shared shell-control CSS")
    require(css, ".header-page-drawer", "this-page drawer CSS")
    require(css, ".page-tool-row", "page tool row CSS")
    require(css, "body.search-open", "search body scroll lock")
    require(css, "body.page-drawer-open", "page drawer body scroll lock")
    if "header-toc-chevron" in index_html or "header-toc-chevron" in css:
        fail("This Page button still renders or styles the old chevron")

    nav_labels = re.findall(r'class="header-nav-link [^"]*">([^<]+)</a>', index_html)
    expected = ["Discover", "Program", "Agenda", "Corpus", "Results", "Verify", "Impact", "Engage"]
    if nav_labels[: len(expected)] != expected:
        fail(f"Header nav order drifted: {nav_labels[:len(expected)]}")


def assert_standard_page(html: str, route: str) -> None:
    require(html, 'class="header-page-wrapper header-toc-wrapper"', f"this-page wrapper on {route}")
    require(html, 'id="header-toc-toggle"', f"legacy-compatible this-page toggle ID on {route}")
    require(html, 'aria-label="This page tools and contents"', f"this-page accessible label on {route}")
    require(html, 'class="header-page-icon"', f"article icon class on {route}")
    require(html, 'viewBox="0 -960 960 960"', f"Material Symbols article icon viewBox on {route}")
    require(html, "M280-280h280v-80H280v80", f"Material Symbols article icon path on {route}")

    old_list_fragments = [
        'x1="6" y1="4" x2="15" y2="4"',
        'cx="3" cy="4" r="1"',
    ]
    for fragment in old_list_fragments:
        if fragment in html:
            fail(f"Old TOC/list icon markup still rendered on {route}: {fragment}")

    tools = html.find("Page tools")
    toc = html.find("On this page")
    if tools < 0 or toc < 0 or tools > toc:
        fail(f"Page drawer sections missing or out of order on {route}")

    # Per atlas/website/briefings/v4/27_v4_share_component_desktop.md §9, the
    # page-tools include no longer renders disabled `pending` placeholder rows
    # for Dossier PDF / Markdown when the page lacks the corresponding
    # frontmatter (page.dossier_pdf_path | page.pdf | page.pdf_url | … and the
    # markdown_export_path equivalents). These rows are now strictly
    # conditional, so the gate cannot require them on every spot-checked
    # route — most lane roots intentionally omit those exports. The four
    # always-on actions remain required.
    for action in [
        "share",
        "copy-link",
        "reviewer-note",
        "copy-citation",
    ]:
        require(html, f'data-page-action="{action}"', f"{action} page action on {route}")

    require(html, 'data-share-url="https://panta-rhei.site', f"share URL fallback on {route}")
    require(html, 'data-copy-value="https://panta-rhei.site', f"copy-link fallback on {route}")
    require(html, "github.com/Panta-Rhei-Research/site/issues/new", f"reviewer note link on {route}")
    require(html, 'id="page-drawer-toc-list"', f"page drawer TOC container on {route}")
    require(html, 'class="page-drawer-empty"', f"page drawer empty-state fallback on {route}")
    require(html, 'name="prrp:atlas_id"', f"Site Atlas metadata preserved on {route}")
    require(html, '"@type": "BreadcrumbList"', f"breadcrumb JSON-LD preserved on {route}")


def assert_search_shell(layout_html: str, css: str, page_actions_js: str = "") -> None:
    require(layout_html, "new PagefindUI", "Pagefind initialization")
    require(layout_html, "syncGoogleSearchLink", "Google fallback search sync")
    require(layout_html, 'aria-label="Search the site"', "search dialog accessible label")
    require(layout_html, "function toggleSearch(force)", "toggle-capable search helper")
    require(layout_html, "toggleSearch();", "header search toggle invocation")
    require(layout_html, "data-cfasync=\"false\"", "Rocket-Loader-safe search script")
    require(layout_html, "window.closePageDrawer", "page drawer close alias")
    # navigator.share / navigator.clipboard moved from inline layout JS to the
    # deferred /assets/js/page-actions.js module per PR #155 (briefing 27).
    # Allow either source (layout fallback for tests that don't supply the JS,
    # canonical home is page-actions.js).
    share_haystack = layout_html + "\n" + page_actions_js
    require(share_haystack, "navigator.share", "Web Share fallback path")
    require(share_haystack, "navigator.clipboard", "clipboard fallback path")
    require(css, ".search-overlay-panel", "search overlay panel CSS")
    require(css, "max-height:calc(100dvh - 56px - 24px)", "mobile search shell-card height constraint")
    require(css, ".pagefind-ui__filter-panel", "defensive Pagefind filter CSS")
    if not re.search(r"display:\s*none\s*!important", css):
        fail("Missing hidden Pagefind filter CSS")
    forbidden = [
        "search-overlay-title",
        "search-overlay-close",
        "search-overlay-hint",
        "showEmptyFilters",
        "openFilters",
        "Search the Site",
        "Try Hubble",
    ]
    for needle in forbidden:
        if needle in layout_html or needle in css:
            fail(f"Search shell still contains removed chrome/filter setting: {needle}")
    if re.search(r"@media \(max-width: 760px\)[\s\S]*?max-height:\s*100dvh", css):
        fail("Mobile search still uses full-screen 100dvh panel sizing")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    source_root = root.parent if root.name == "_site" else Path(".")
    css = read(root / "assets" / "css" / "main.css")
    layout_html = read(source_root / "_layouts" / "default.html")
    # PR #155 moved share / clipboard handlers from inline layout JS to a
    # deferred module at /assets/js/page-actions.js. Read it here so the
    # navigator.share / navigator.clipboard substring checks see the
    # canonical source. Source-tree path is preferred (always present);
    # fall back to the built _site path if running against a built site
    # without a source mirror.
    page_actions_path = source_root / "assets" / "js" / "page-actions.js"
    if not page_actions_path.is_file():
        page_actions_path = root / "assets" / "js" / "page-actions.js"
    page_actions_js = read(page_actions_path) if page_actions_path.is_file() else ""

    index_html = read(built_path(root, "/"))
    assert_header_shell(index_html, css)
    if "header-page-wrapper" in index_html:
        fail("Home shell should not render the this-page utility drawer")

    for route in [
        "/program/",
        "/agenda/",
        "/impact/",
        "/verify/release-manifest/",
        "/results/world-readout/physics/",
    ]:
        assert_standard_page(read(built_path(root, route)), route)

    assert_search_shell(layout_html, css, page_actions_js)
    print("v4 mobile shell assertions passed")


if __name__ == "__main__":
    main()
