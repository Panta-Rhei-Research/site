#!/usr/bin/env python3
"""Assertions for Scientific Plate 06 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-06-verification-matrix"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_05_OG = "/assets/images/plates/plate-05-results-world-readout-og.jpg"
PLATE_06_OG = "/assets/images/plates/plate-06-verification-matrix-og.jpg"
ALT = (
    "Scientific plate titled The Verification Matrix, showing obligations, "
    "construction steps, and results flowing into Verify, with six verification "
    "layers, operational surfaces such as TauLib and Release Manifest, a verification "
    "status legend, and the caveat that formal checking is not empirical truth."
)
CANONICAL_CAPTION = (
    "Verification is not a single operation. The Verify lane makes obligations, "
    "construction steps, and results inspectable through research-form checks, "
    "construction-step verification, formal proof checking, bridge adequacy, "
    "predictions and falsification, and external assessment."
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
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 06 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 06 WebP source")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-06-verification-matrix-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-06-verification-matrix-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-06-verification-matrix-hero.jpg",
        "og": site / "assets/images/plates/plate-06-verification-matrix-og.jpg",
        "thumb": site / "assets/images/plates/plate-06-verification-matrix-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 06 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 06 asset too small to be valid: {path}")

    targets = {
        "/verify/": [
            "The inspection layer at a glance",
            "The Verification Matrix",
            CANONICAL_CAPTION,
            "Formal checking is essential, but it is not empirical truth.",
            "Verify the Construction Spine",
            "Inspect TauLib",
            "Read the Release Manifest",
            "Open Predictions & Falsification",
        ],
        "/verify/construction-spine-verification/": [
            "Construction steps inside the verification matrix",
            "Construction-step verification is one part of the broader verification matrix",
            "Construction-step verification asks what each step builds",
        ],
        "/verify/taulib/": [
            "TauLib inside the verification matrix",
            "TauLib is one formalization surface inside the broader verification matrix.",
            "Lean compilation checks formalized obligations; it does not by itself establish empirical truth.",
        ],
        "/verify/release-manifest/": [
            "Release state and trusted base",
            "The Release Manifest anchors the formalization surface inside the broader verification matrix",
            "trusted base, custom axioms, filters, and formalization boundaries",
        ],
        "/verify/predictions-and-falsification/": [
            "Falsification inside the verification matrix",
            "Predictions and falsification are one layer of verification.",
            "They complement formal proof checking and bridge adequacy",
        ],
        "/verify/how-to-verify/": [
            "How the verification matrix becomes a route",
            "How to Verify turns the verification matrix into reviewer entry routes",
            "The matrix is not a single checklist.",
        ],
        "/verify/assessment-protocols/": [
            "Assessment inside the verification matrix",
            "Assessment Protocols are external-review routes inside the broader verification matrix.",
            "they do not replace proof, empirical testing, or peer review",
        ],
    }

    for route, required_text in targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")
        require("Formal checking proves empirical truth" not in parser.visible, f"{route} implies formal checking proves empirical truth")

    for route in targets:
        _, parser = read_page(site, route)
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_06_OG}",
            f"{route} missing Plate 06 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_06_OG}",
            f"{route} missing Plate 06 twitter:image",
        )
        require(
            "Verify lane as a verification matrix" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 06 OG alt text",
        )

    _, discover = read_page(site, "/discover/")
    require(
        meta_content(discover, "property", "og:image") == f"https://panta-rhei.site{PLATE_01_OG}",
        "/discover/ should keep Plate 01 og:image",
    )
    _, results = read_page(site, "/results/")
    require(
        meta_content(results, "property", "og:image") == f"https://panta-rhei.site{PLATE_05_OG}",
        "/results/ should keep Plate 05 og:image",
    )

    for route in ["/", "/discover/", "/program/research-agenda/", "/corpus/", "/results/"]:
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 06")

    forbidden = ["Companion Papers", "deployment portfolios", "Status: Resolved", "Resolved —"]
    for route in [*targets.keys(), "/", "/discover/", "/results/"]:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 06 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
