#!/usr/bin/env python3
"""Targeted checks for Site Atlas release-readiness remediation wave 1."""

from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse


HIDDEN_TAGS = {"head", "script", "style", "template", "svg", "noscript"}

ONE_H1_ROUTES = [
    "/404.html",
    "/discover/ai-assisted-discovery/",
    "/agenda/core-semantics/",
    "/agenda/core-semantics/mathematics/",
    "/agenda/core-semantics/physics/",
    "/agenda/core-semantics/life/",
    "/agenda/core-semantics/metaphysics/",
]

TERMINOLOGY_ROUTES = [
    "/discover/",
    "/program/about/",
    "/agenda/",
    "/agenda/kernel-model-reality/ontic-status-burden/",
    "/media/",
    "/results/progress-against-agenda/",
]

STALE_LINKS_BY_ROUTE = {
    "/agenda/": ["/agenda/work-roadmap/"],
    "/agenda/roadmap/": ["/engage/media-kit/"],
    "/verify/domain-verification/life/": ["/results/challenge-responses/life/origin-of-life/"],
    "/results/progress-against-agenda/": [
        "/program/research-agenda/problem-ledger/",
        "/program/research-agenda/recovery-requirements/",
    ],
}

TITLE_PAIRS = [
    ("/discover/guided-tours/", "/publications/guided-tours/"),
    ("/discover/follow-the-research/", "/engage/follow-the-research/"),
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_stack: list[bool] = []
        self.h1_count = 0
        self.hrefs: list[str] = []
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {key.lower(): value or "" for key, value in attrs}
        classes = set(attr_map.get("class", "").split())
        hidden = (
            tag in HIDDEN_TAGS
            or "hidden" in attr_map
            or attr_map.get("aria-hidden", "").lower() == "true"
            or "sr-only" in classes
            or "visually-hidden" in classes
        )
        self.hidden_stack.append(hidden)
        if tag == "h1":
            self.h1_count += 1
        if tag == "a" and attr_map.get("href"):
            self.hrefs.append(attr_map["href"])
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        if self.hidden_stack:
            self.hidden_stack.pop()

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if not any(self.hidden_stack) and data.strip():
            self.text_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join(" ".join(self.title_parts).split())

    @property
    def visible_text(self) -> str:
        return " ".join(" ".join(self.text_parts).split())


def route_to_file(built_root: Path, route: str) -> Path:
    if route == "/":
        return built_root / "index.html"
    if route == "/404.html":
        return built_root / "404.html"
    if route.endswith(".html"):
        return built_root / route.strip("/")
    return built_root / route.strip("/") / "index.html"


def parse_page(built_root: Path, route: str) -> PageParser:
    path = route_to_file(built_root, route)
    if not path.exists():
        raise AssertionError(f"{route}: built page missing at {path}")
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    parser.close()
    return parser


def local_href_to_route(href: str) -> str | None:
    href, _fragment = urldefrag(href)
    if not href or href.startswith(("mailto:", "tel:", "#")):
        return None
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None
    if not href.startswith("/"):
        return None
    if href.endswith(".pdf") or href.startswith(("/assets/", "/pagefind/")):
        return None
    return href


def route_exists(built_root: Path, route: str) -> bool:
    return route_to_file(built_root, route).exists()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_root", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("."))
    args = parser.parse_args()

    errors: list[str] = []

    for route in ONE_H1_ROUTES:
        page = parse_page(args.built_root, route)
        if page.h1_count != 1:
            errors.append(f"{route}: expected exactly one H1, found {page.h1_count}")

    for route in TERMINOLOGY_ROUTES:
        text = parse_page(args.built_root, route).visible_text.lower()
        if "problem ledger" in text or "problem ledgers" in text:
            errors.append(f"{route}: visible deprecated Problem Ledger terminology remains")

    for route, stale_links in STALE_LINKS_BY_ROUTE.items():
        hrefs = parse_page(args.built_root, route).hrefs
        for stale in stale_links:
            if any(stale in href for href in hrefs):
                errors.append(f"{route}: stale link remains: {stale}")

    progress_page = parse_page(args.built_root, "/results/progress-against-agenda/")
    for href in progress_page.hrefs:
        route = local_href_to_route(href)
        if route and not route_exists(args.built_root, route):
            errors.append(f"/results/progress-against-agenda/: broken local link {href}")

    for left, right in TITLE_PAIRS:
        left_title = parse_page(args.built_root, left).title
        right_title = parse_page(args.built_root, right).title
        if left_title == right_title:
            errors.append(f"{left} and {right}: duplicate built title {left_title!r}")

    progress_data_path = args.site_root / "_data/agenda_progress/agenda-progress.json"
    if progress_data_path.exists():
        progress_data = json.loads(progress_data_path.read_text(encoding="utf-8"))
        labels = {item.get("item_kind_label", "") for item in progress_data}
        if "Problem Ledger item" in labels:
            errors.append("agenda-progress data still emits item_kind_label='Problem Ledger item'")
        old_urls = [
            item.get("canonical_program_url", "")
            for item in progress_data
            if str(item.get("canonical_program_url", "")).startswith(
                ("/program/research-agenda/problem-ledger", "/program/research-agenda/recovery-requirements")
            )
        ]
        if old_urls:
            errors.append(f"agenda-progress data still contains {len(old_urls)} old canonical program URL(s)")

    if errors:
        print("Site Atlas release-readiness remediation assertion failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Site Atlas release-readiness remediation assertion passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
