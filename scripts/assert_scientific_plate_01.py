#!/usr/bin/env python3
"""Assertions for Scientific Plate 01 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-01-public-research-observatory"
ALT = (
    "Scientific plate showing the Panta Rhei Research Program as a public research observatory, "
    "with a central spine from Research Agenda to Corpus to Results to Verify, surrounded by "
    "Discover, Program, Publications, Impact, Engage, inspectability surfaces, and world readouts "
    "for mathematics, physics, life, and metaphysics."
)
HOME_CAPTION = (
    "The Panta Rhei website is structured as a public research observatory: Research Agenda states "
    "the obligations, Corpus carries the construction, Results reports current consequences, Verify "
    "exposes inspection routes, Publications holds stable artifacts, Impact maps conditional "
    "implications, and Engage invites structured scrutiny without endorsement."
)
DISCOVER_CAPTION = (
    "A visual map of the site's research-observatory structure: orientation, obligation, construction, "
    "consequence, inspection, publications, impact, and engagement."
)
OG_IMAGE = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"


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


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-01-public-research-observatory-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-01-public-research-observatory-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-01-public-research-observatory-hero.jpg",
        "og": site / "assets/images/plates/plate-01-public-research-observatory-og.jpg",
        "thumb": site / "assets/images/plates/plate-01-public-research-observatory-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing plate asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate asset too small to be valid: {path}")

    home_html, home = read_page(site, "/")
    discover_html, discover = read_page(site, "/discover/")
    for route, parser in {"/": home, "/discover/": discover}.items():
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 01 alt text")
        require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 01 WebP source")
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{OG_IMAGE}",
            f"{route} missing Plate 01 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{OG_IMAGE}",
            f"{route} missing Plate 01 twitter:image",
        )
        require(
            "Scientific plate mapping the Panta Rhei Research Program" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 01 OG alt text",
        )

    require("homepage-hero" in home_html, "/ missing homepage hero")
    require(home_html.index("homepage-hero") < home_html.index("scientific-plate"), "Homepage plate should sit below the hero")
    require("The public research observatory" in home.visible, "/ missing plate section heading")
    require(HOME_CAPTION in home.visible, "/ missing Plate 01 caption")
    for cta in ["Start with Discover", "Explore the Corpus", "See the Results", "Verify it yourself"]:
        require(cta in home.visible, f"/ missing Plate 01 CTA: {cta}")

    require("How the observatory fits together" in discover.visible, "/discover/ missing plate section heading")
    require(DISCOVER_CAPTION in discover.visible, "/discover/ missing Discover plate caption")
    require("Use this map to orient yourself before entering the deeper lanes." in discover.visible, "/discover/ missing orientation sentence")

    forbidden = ["Companion Papers", "deployment portfolios", "Status: Resolved", "Resolved —"]
    for route, parser in {"/": home, "/discover/": discover}.items():
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 01 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
