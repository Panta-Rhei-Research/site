#!/usr/bin/env python3
"""Assertions for the v4 Impact validation-language doctrine pilot."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


CHAIN = "Result → Verification & Review → Translation Layer → Domain Uptake → Consequence"

ROUTES = {
    "home": "/",
    "program": "/program/",
    "program_about": "/program/about/",
    "work_matters": "/program/why-this-work-matters/",
    "impact": "/impact/",
    "impact_framework": "/impact/impact-framework/",
    "global_public_good": "/impact/global-public-good/",
    "media": "/media/",
    "open_research": "/media/open-research-brief/",
    "public_good": "/publications/research-briefings/public-good/",
    "public_good_sample": "/publications/research-briefings/public-good/advanced-fission-safety-operations-licensing-fleet-modernization/",
    "portfolio_sample": "/impact/global-public-good/climate/",
    "sitemap": "/sitemap/",
}

DISCOURAGED = [
    "survive scrutiny",
    "survives scrutiny",
    "survival under scrutiny",
    "survive inspection",
    "survives inspection",
    "survive verification",
    "survival under pressure",
    "verification survival",
    "kill the theory",
    "fatal blow",
    "attack surface",
    "take down",
    "takedown",
]

EXEMPT_PREFIXES = (
    "/archive/",
    "/changelog/",
    "/impact/papers/",
    "/corpus/monographs/",
    "/corpus/taulib/",
    "/registry/",
    "/results/metaphysics/glossary/",
    "/verify/taulib/",
)

APPROVED_STATUSES = {"archive", "deprecated", "redirected"}


class PageParser(HTMLParser):
    VOID_TAGS = {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_stack: list[bool] = []
        self.text_parts: list[str] = []
        self.h1: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[str] = []
        self.capture: str | None = None
        self.buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key.lower(): value or "" for key, value in attrs}
        if tag == "meta":
            key = attr.get("name") or attr.get("property")
            if key:
                self.meta[key] = attr.get("content", "")
        if tag == "a" and attr.get("href"):
            self.links.append(attr["href"])
        if tag in self.VOID_TAGS:
            return
        classes = set(attr.get("class", "").split())
        hidden = (
            tag in {"head", "script", "style", "template", "svg", "noscript"}
            or "hidden" in attr
            or attr.get("aria-hidden", "").lower() == "true"
            or "sr-only" in classes
            or "visually-hidden" in classes
        )
        self.hidden_stack.append(hidden)
        if not any(self.hidden_stack) and tag == "h1":
            self.capture = tag
            self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if self.capture == tag:
            self.h1.append(normalize("".join(self.buffer)))
            self.capture = None
            self.buffer = []
        if self.hidden_stack:
            self.hidden_stack.pop()

    def handle_data(self, data: str) -> None:
        if any(self.hidden_stack):
            return
        self.text_parts.append(data)
        if self.capture:
            self.buffer.append(data)

    @property
    def visible_text(self) -> str:
        return normalize(" ".join(self.text_parts))


def normalize(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split())


def fail(message: str) -> None:
    raise AssertionError(message)


def page_path(built_root: Path, route: str) -> Path:
    if route == "/":
        return built_root / "index.html"
    return built_root / route.strip("/") / "index.html"


def route_for_html(path: Path, built_root: Path) -> str:
    rel = path.relative_to(built_root).as_posix()
    if rel == "index.html":
        return "/"
    return "/" + rel.removesuffix("index.html")


def parse_page(built_root: Path, route: str) -> tuple[str, PageParser]:
    path = page_path(built_root, route)
    if not path.exists():
        fail(f"Missing built route: {route}")
    html = path.read_text(encoding="utf-8", errors="ignore")
    parser = PageParser()
    parser.feed(html)
    parser.close()
    return html, parser


def require_text(parser: PageParser, route: str, needle: str) -> None:
    if needle not in parser.visible_text:
        fail(f"{route} missing expected visible text: {needle}")


def require_link(parser: PageParser, route: str, href: str) -> None:
    if href not in parser.links:
        fail(f"{route} missing link to {href}")


def assert_meta(parser: PageParser, route: str, expected: dict[str, str]) -> None:
    for key, value in expected.items():
        if parser.meta.get(key) != value:
            fail(f"{route} {key} expected {value!r}, got {parser.meta.get(key)!r}")


def load_route_statuses(repo_root: Path) -> dict[str, str]:
    payload = json.loads((repo_root / "_data/site_atlas/route_index.json").read_text(encoding="utf-8"))
    return {route: page.get("status", "") for route, page in payload.items()}


def is_exempt_route(route: str, route_status: str) -> bool:
    return route_status in APPROVED_STATUSES or any(route.startswith(prefix) for prefix in EXEMPT_PREFIXES)


def assert_discouraged_terms_absent(built_root: Path, repo_root: Path) -> None:
    route_status = load_route_statuses(repo_root)
    findings: list[str] = []
    for html_path in sorted(built_root.rglob("*.html")):
        route = route_for_html(html_path, built_root)
        if is_exempt_route(route, route_status.get(route, "")):
            continue
        parser = PageParser()
        parser.feed(html_path.read_text(encoding="utf-8", errors="ignore"))
        parser.close()
        text = parser.visible_text.lower()
        for term in DISCOURAGED:
            match = re.search(re.escape(term.lower()), text)
            if not match:
                continue
            start = max(0, match.start() - 90)
            end = min(len(text), match.end() + 90)
            findings.append(f"{route}: {term!r} in ...{text[start:end]}...")
    if findings:
        sample = "\n- ".join(findings[:40])
        fail(f"Discouraged Impact-validation terms found:\n- {sample}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_impact_validation_language.py _site", file=sys.stderr)
        return 2
    built_root = Path(sys.argv[1]).resolve()
    repo_root = Path(__file__).resolve().parents[1]

    html, page = parse_page(built_root, ROUTES["work_matters"])
    if page.h1 != ["Why This Work Matters"]:
        fail(f"{ROUTES['work_matters']} expected one H1, got {page.h1!r}")
    assert_meta(
        page,
        ROUTES["work_matters"],
        {
            "prrp:atlas_id": "0000d2",
            "prrp:page_key": "program.why_this_work_matters",
            "prrp:ia_path": "02-02",
            "prrp:lane": "program",
            "prrp:status": "canonical",
            "prrp:canonical_role": "program_impact_bridge",
        },
    )
    for needle in [
        "Panta Rhei is an independent open research program dedicated to building a coherent theory of reality.",
        "We do not believe public attention is justified by certainty.",
        "The word if is load-bearing.",
        "not a claim that the framework has already changed the world",
        "inspection, correction, verification, translation, and domain uptake",
    ]:
        require_text(page, ROUTES["work_matters"], needle)
    for forbidden in [
        "guarantees impact",
        "has external validation",
        "has peer-review acceptance",
        "is deployment ready",
    ]:
        if forbidden in page.visible_text.lower():
            fail(f"{ROUTES['work_matters']} overclaim leaked visibly: {forbidden}")

    for route in [ROUTES["program"], ROUTES["impact"], ROUTES["media"], ROUTES["open_research"], ROUTES["sitemap"]]:
        _, parser = parse_page(built_root, route)
        require_link(parser, route, ROUTES["work_matters"])

    _, home = parse_page(built_root, ROUTES["home"])
    require_text(home, ROUTES["home"], "remain supported through review, translation, and domain uptake")

    for route in [ROUTES["impact"], ROUTES["impact_framework"], ROUTES["global_public_good"], ROUTES["public_good"]]:
        _, parser = parse_page(built_root, route)
        require_text(parser, route, CHAIN)

    for route in [ROUTES["global_public_good"], ROUTES["public_good"], ROUTES["public_good_sample"], ROUTES["portfolio_sample"]]:
        _, parser = parse_page(built_root, route)
        for needle in ["conditional", "scenario"]:
            require_text(parser, route, needle)

    for route in [ROUTES["media"], ROUTES["open_research"]]:
        _, parser = parse_page(built_root, route)
        require_text(
            parser,
            route,
            "We are not asking for belief first. We are making the work inspectable and inviting structured scrutiny, correction, and review.",
        )

    plates = (repo_root / "_data/plates.yml").read_text(encoding="utf-8")
    if "Verification Survival" in plates:
        fail("_data/plates.yml still contains `Verification Survival`")
    if "Verification & Review" not in plates:
        fail("_data/plates.yml should record the updated Plate 08 chain language")

    assert_discouraged_terms_absent(built_root, repo_root)

    print("v4 Impact validation-language assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
