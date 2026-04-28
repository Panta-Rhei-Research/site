#!/usr/bin/env python3
"""Assertions for World Readout / Landmark Results consistency."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


EXPECTED_ANCHOR_COUNTS = {
    "mathematics": 4,
    "physics": 7,
    "life": 4,
    "metaphysics": 3,
}

WORLD_READOUT_ROUTE = "/results/world-readout/"
LANDMARK_ROUTE = "/results/landmark-results/"


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.text: list[str] = []
        self.anchors: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "a":
            self.anchors.append({key: value or "" for key, value in attrs})

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip:
            self.text.append(data)

    @property
    def visible(self) -> str:
        return normalize(" ".join(self.text))


def normalize(value: str) -> str:
    return " ".join(value.split())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_built_page(site: Path, route: str) -> str:
    path = site / route.strip("/") / "index.html"
    require(path.exists(), f"Missing built page: {route}")
    return path.read_text(encoding="utf-8")


def parse_visible(html: str) -> VisibleTextParser:
    parser = VisibleTextParser()
    parser.feed(html)
    return parser


def source_result_links(repo: Path) -> set[str]:
    links: set[str] = set()
    pattern = re.compile(r"""['"](/results/problem/[^'"]+/)['"]""")
    for path in (repo / "results/world-readout").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        links.update(match.group(1) for match in pattern.finditer(text))
    return links


def built_world_readout_html(site: Path) -> str:
    parts: list[str] = []
    root = site / "results/world-readout"
    require(root.exists(), "Missing built World Readout subtree")
    for path in root.rglob("index.html"):
        parts.append(path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    repo = Path(__file__).resolve().parents[1]
    data = json.loads((repo / "_data/results/results.json").read_text(encoding="utf-8"))

    by_url = {item.get("url"): item for item in data if item.get("url")}
    landmarks = [item for item in data if item.get("landmark") is True]
    anchors = [item for item in data if item.get("world_readout_prominence") == "anchor"]
    supports = [item for item in data if item.get("world_readout_prominence") == "support"]
    world_readout_items = [item for item in data if item.get("world_readout") is True]

    require(len(landmarks) == 18, f"Expected 18 Landmark Results, found {len(landmarks)}")
    require(len(anchors) == 18, f"Expected 18 World Readout anchors, found {len(anchors)}")
    require({item["slug"] for item in anchors} == {item["slug"] for item in landmarks}, "World Readout anchors must match the Landmark Result set exactly")
    require(len(supports) >= 7, f"Expected at least 7 World Readout support records, found {len(supports)}")

    layer_counts: dict[str, int] = {}
    for item in anchors:
        layer = item.get("world_readout_layer")
        layer_counts[layer] = layer_counts.get(layer, 0) + 1
    require(layer_counts == EXPECTED_ANCHOR_COUNTS, f"Unexpected World Readout anchor counts by layer: {layer_counts}")

    for item in world_readout_items:
        require(item.get("world_readout_layer") in EXPECTED_ANCHOR_COUNTS, f"Invalid world_readout_layer for {item.get('slug')}: {item.get('world_readout_layer')}")
        require(item.get("world_readout_prominence") in {"anchor", "support"}, f"Invalid world_readout_prominence for {item.get('slug')}: {item.get('world_readout_prominence')}")
        require(item.get("world_readout_reason"), f"Missing world_readout_reason for {item.get('slug')}")
        require(item.get("url"), f"Missing URL for World Readout result {item.get('slug')}")
        require((site / item["url"].strip("/") / "index.html").exists(), f"World Readout result URL does not build: {item['url']}")

    for url in sorted(source_result_links(repo)):
        item = by_url.get(url)
        require(item is not None, f"World Readout source link does not map to result data: {url}")
        require(item.get("world_readout") is True, f"World Readout source link lacks metadata: {url}")

    world_readout_html = built_world_readout_html(site)
    for item in landmarks:
        require(item["url"] in world_readout_html, f"Landmark Result is not linked from the built World Readout subtree: {item['slug']} ({item['url']})")

    overview = read_built_page(site, WORLD_READOUT_ROUTE)
    overview_parser = parse_visible(overview)
    require(LANDMARK_ROUTE in overview, "World Readout overview should link to Landmark Results")
    require("Every Landmark Result is assigned to one of these readouts as an anchor" in overview_parser.visible, "World Readout overview should explain the Landmark anchor relationship")

    for layer in EXPECTED_ANCHOR_COUNTS:
        route = f"/results/world-readout/{layer}/"
        html = read_built_page(site, route)
        parser = parse_visible(html)
        require("World Readout anchors" in parser.visible, f"Missing World Readout anchors section on {route}")
        for item in [anchor for anchor in anchors if anchor.get("world_readout_layer") == layer]:
            require(item["url"] in html, f"{route} missing anchor URL {item['url']}")
            require(item["world_readout_reason"] in parser.visible, f"{route} missing anchor reason for {item['slug']}")

    visible_world_readout = parse_visible(world_readout_html).visible
    for forbidden in [
        "Status: Resolved",
        "Status Resolved",
        "Resolved -",
        "Resolved —",
        "Resolved |",
    ]:
        require(forbidden not in visible_world_readout, f"Unqualified resolved status appears in World Readout pages: {forbidden}")

    print("World Readout consistency assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
