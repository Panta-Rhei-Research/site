#!/usr/bin/env python3
"""Assertions for the Landmark Results editorial page."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path


LANDMARK_ROUTE = "/results/landmark-results/"
PLATE_ID = "plate-05-results-world-readout"
PLATE_OG = "/assets/images/plates/plate-05-results-world-readout-og.jpg"
EXPECTED_GROUPS = {
    "foundations": 4,
    "physics": 7,
    "life": 4,
    "mind-metaphysics": 3,
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.h1_count = 0
        self.h2: list[str] = []
        self.capture: str | None = None
        self.buffer: list[str] = []
        self.text: list[str] = []
        self.anchors: list[dict[str, str]] = []
        self.imgs: list[dict[str, str]] = []
        self.sources: list[dict[str, str]] = []
        self.metas: list[dict[str, str]] = []
        self.landmark_cards = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: value or "" for key, value in attrs}
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "h1":
            self.h1_count += 1
        if tag == "h2":
            self.capture = "h2"
            self.buffer = []
        if tag == "a":
            self.anchors.append(attr)
        if tag == "img":
            self.imgs.append(attr)
        if tag == "source":
            self.sources.append(attr)
        if tag == "meta":
            self.metas.append(attr)
        if tag == "li" and "landmark-result-card" in attr.get("class", ""):
            self.landmark_cards += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1
            return
        if self.skip:
            return
        if self.capture == tag:
            self.h2.append(normalize("".join(self.buffer)))
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        self.text.append(data)
        if self.capture:
            self.buffer.append(data)

    @property
    def visible(self) -> str:
        return normalize(" ".join(self.text))


def normalize(value: str) -> str:
    return " ".join(value.split())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_page(site: Path, route: str) -> tuple[str, PageParser]:
    path = site / route.strip("/") / "index.html"
    if route == "/":
        path = site / "index.html"
    require(path.exists(), f"Missing built page: {route}")
    html = path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)
    return html, parser


def meta_content(parser: PageParser, key: str, value: str) -> str | None:
    for meta in parser.metas:
        if meta.get(key) == value:
            return meta.get("content")
    return None


def status_label(code: str) -> str:
    return {
        "R": "Internally addressed",
        "P": "Partial",
        "Q": "Qualitative",
        "C": "Contradicted",
        "N": "Not addressed",
    }.get(code, code)


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    repo = Path(__file__).resolve().parents[1]
    data = json.loads((repo / "_data/results/results.json").read_text(encoding="utf-8"))
    landmarks = [item for item in data if item.get("landmark") is True]

    require(len(landmarks) == 18, f"Expected 18 landmark records, found {len(landmarks)}")
    ranks = sorted(item.get("landmark_rank") for item in landmarks)
    require(ranks == list(range(1, 19)), f"Landmark ranks should be exactly 1..18, found {ranks}")
    require(len({item["slug"] for item in landmarks}) == 18, "Landmark slugs should be unique")

    by_group: dict[str, int] = {}
    for item in landmarks:
        group = item.get("landmark_group")
        by_group[group] = by_group.get(group, 0) + 1
        require(group in EXPECTED_GROUPS, f"Unexpected landmark group for {item['slug']}: {group}")
        require(item.get("landmark_reason"), f"Missing landmark_reason for {item['slug']}")
        require(item.get("url"), f"Missing result URL for {item['slug']}")
        route = site / item["url"].strip("/") / "index.html"
        require(route.exists(), f"Landmark result URL does not build: {item['url']}")
    require(by_group == EXPECTED_GROUPS, f"Unexpected group counts: {by_group}")

    html, parser = read_page(site, LANDMARK_ROUTE)
    visible = parser.visible
    require(parser.h1_count == 1, "Landmark Results page should have exactly one H1")
    require(parser.landmark_cards == 18, f"Expected 18 landmark cards, found {parser.landmark_cards}")
    require(any(PLATE_ID in source.get("srcset", "") for source in parser.sources), "Missing Plate 05 WebP source")
    require(any(PLATE_ID in img.get("src", "") for img in parser.imgs), "Missing Plate 05 image fallback")
    require(
        meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_OG}",
        "Landmark Results page should use Plate 05 og:image",
    )
    require(
        meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_OG}",
        "Landmark Results page should use Plate 05 twitter:image",
    )

    for heading in [
        "What makes a result a landmark",
        "A small kernel, many consequences",
        "The physics shock",
        "Life stops being a side case",
        "Mind, meaning, and normativity as result surfaces",
        "Browse the landmark results",
        "How to challenge this page",
    ]:
        require(heading in parser.h2, f"Missing Landmark Results section: {heading}")

    for needle in [
        "not a claim of external settlement",
        "The selection is intentionally editorial",
        "Landmark status marks internal program significance",
        "These are landmarks because they force the program into contact with precision, bridge adequacy, and empirical accountability.",
    ]:
        require(needle in visible, f"Missing claim-safety or narrative text: {needle}")

    for item in landmarks:
        require(item["url"] in html, f"Landmark page missing link to {item['url']}")
        require(item["landmark_reason"] in visible, f"Landmark page missing reason for {item['slug']}")
        require(status_label(item.get("status_code", "")) in visible, f"Missing public-safe status for {item['slug']}")

    forbidden = [
        "Status: Resolved",
        "Resolved —",
        ">Resolved<",
        " resolved ",
        " raw resolved ",
    ]
    lower_visible = f" {visible.lower()} "
    for phrase in forbidden:
        if phrase.startswith(" ") or phrase.islower():
            require(phrase not in lower_visible, f"Forbidden visible status phrase appears: {phrase}")
        else:
            require(phrase not in html, f"Forbidden raw status phrase appears: {phrase}")

    print("Landmark Results assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
