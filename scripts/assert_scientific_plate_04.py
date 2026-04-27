#!/usr/bin/env python3
"""Assertions for Scientific Plate 04 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-04-construction-spine"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_04_OG = "/assets/images/plates/plate-04-construction-spine-og.jpg"
ALT = (
    "Scientific plate titled The Construction Spine, showing a vertical ten-step "
    "build sequence from Kernel to Ontic Closure, with side projections for "
    "Registry, TauLib, Research Monographs, and Corpus Graph."
)
CANONICAL_CAPTION = (
    "The Construction Spine is the Corpus-side build narrative: ten canonical "
    "steps from kernel definition through mathematics, physics, life, reflective "
    "structure, self-hosting, and ontic closure, with public projections through "
    "the Registry, TauLib, Research Monographs, and Corpus Graph."
)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1_count = 0
        self.imgs: list[dict[str, str]] = []
        self.sources: list[dict[str, str]] = []
        self.metas: list[dict[str, str]] = []
        self.text: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.imgs.append(attr)
        if tag == "source":
            self.sources.append(attr)
        if tag == "meta":
            self.metas.append(attr)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip:
            self.text.append(data)

    @property
    def visible(self) -> str:
        return " ".join(" ".join(self.text).split())


def read_page(site: Path, route: str) -> tuple[str, Parser]:
    path = site / route.strip("/") / "index.html"
    if route == "/":
        path = site / "index.html"
    if not path.exists():
        raise AssertionError(f"Missing page: {route}")
    html = path.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)
    return html, parser


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def meta_content(parser: Parser, key: str, value: str) -> str | None:
    for meta in parser.metas:
        if meta.get(key) == value:
            return meta.get("content")
    return None


def assert_plate_present(route: str, parser: Parser) -> None:
    require(parser.h1_count == 1, f"{route} should have exactly one H1")
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 04 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 04 WebP source")


def assert_before(text: str, first: str, second: str, route: str) -> None:
    left = text.find(first)
    right = text.find(second)
    require(left >= 0, f"{route} missing expected text: {first}")
    require(right >= 0, f"{route} missing expected text: {second}")
    require(left < right, f"{route} expected '{first}' before '{second}'")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-04-construction-spine-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-04-construction-spine-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-04-construction-spine-hero.jpg",
        "og": site / "assets/images/plates/plate-04-construction-spine-og.jpg",
        "thumb": site / "assets/images/plates/plate-04-construction-spine-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 04 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 04 asset too small to be valid: {path}")

    targets = {
        "/corpus/": [
            "The build-order at a glance",
            "The Construction Spine",
            CANONICAL_CAPTION,
            "The Construction Spine is the primary human-readable route into the Corpus.",
            "Open the Construction Spine",
            "Explore the Registry",
            "Inspect TauLib",
            "Verify the Construction Spine",
        ],
        "/corpus/construction-spine/": [
            "From kernel to ontic closure",
            "The Construction Spine gives the human-readable build order of the Corpus",
            "The ten construction steps show how the Corpus is built",
        ],
        "/program/research-agenda/construction-roadmap/": [
            "Agenda roadmap and Corpus spine",
            "The Construction Roadmap states what must be built; the Construction Spine shows the Corpus-side build narrative.",
            "The Construction Roadmap states the build-order obligation.",
        ],
        "/verify/construction-spine-verification/": [
            "What is being verified",
            "Each construction step has its own inspection mode",
            "Construction-step verification asks what each step builds",
        ],
    }

    for route, required_text in targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")

    _, corpus_root = read_page(site, "/corpus/")
    assert_before(corpus_root.visible, "The Construction Spine", "Current state", "/corpus/")

    for route in ["/corpus/", "/corpus/construction-spine/"]:
        _, parser = read_page(site, route)
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_04_OG}",
            f"{route} missing Plate 04 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_04_OG}",
            f"{route} missing Plate 04 twitter:image",
        )
        require(
            "Corpus Construction Spine as a ten-step build sequence" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 04 OG alt text",
        )

    _, discover = read_page(site, "/discover/")
    require(
        meta_content(discover, "property", "og:image") == f"https://panta-rhei.site{PLATE_01_OG}",
        "/discover/ should keep Plate 01 og:image",
    )

    for route in ["/", "/discover/", "/results/", "/verify/", "/program/research-agenda/"]:
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 04")

    forbidden = ["Companion Papers", "deployment portfolios", "Status: Resolved", "Resolved —"]
    for route in [*targets.keys(), "/", "/discover/", "/results/", "/verify/"]:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 04 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
