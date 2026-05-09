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
    require(index_html, 'class="header-hamburger shell-control"', "shared explore shell control")
    require(css, ".shell-control", "shared shell-control CSS")
    require(css, ".header-page-drawer", "this-page drawer CSS")
    require(css, ".page-tool-row", "page tool row CSS")
    require(css, "body.search-open", "search body scroll lock")
    require(css, "body.page-drawer-open", "page drawer body scroll lock")

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

    for action in [
        "dossier-pdf",
        "markdown",
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


def assert_search_shell(layout_html: str, css: str) -> None:
    require(layout_html, "new PagefindUI", "Pagefind initialization")
    require(layout_html, "syncGoogleSearchLink", "Google fallback search sync")
    require(layout_html, "data-cfasync=\"false\"", "Rocket-Loader-safe search script")
    require(layout_html, "window.closePageDrawer", "page drawer close alias")
    require(layout_html, "navigator.share", "Web Share fallback path")
    require(layout_html, "navigator.clipboard", "clipboard fallback path")
    require(css, ".search-overlay-panel", "search overlay panel CSS")
    require(css, "max-height:calc(100dvh - 56px - 24px)", "mobile search shell-card height constraint")
    if re.search(r"@media \(max-width: 760px\)[\s\S]*?max-height:\s*100dvh", css):
        fail("Mobile search still uses full-screen 100dvh panel sizing")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    source_root = root.parent if root.name == "_site" else Path(".")
    css = read(root / "assets" / "css" / "main.css")
    layout_html = read(source_root / "_layouts" / "default.html")

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

    assert_search_shell(layout_html, css)
    print("v4 mobile shell assertions passed")


if __name__ == "__main__":
    main()
