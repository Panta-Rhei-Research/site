#!/usr/bin/env python3
"""Assertions for the v4 Program charter pilot."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROUTES = {
    "charter": "/program/about/standing-in-the-inquiry-of-being/",
    "ontology": "/program/about/categorical-ontology/",
    "program": "/program/",
    "about": "/program/about/",
    "coherent": "/program/about/coherent-theory-of-reality/",
    "inspection": "/program/about/inspection-observatory/",
    "related": "/program/about/related-approaches/",
    "red_team": "/program/about/red-team-faq/",
}

CANONICAL_SENTENCE = (
    "The Panta Rhei Research Program is an independent open research program dedicated to building a coherent theory of reality."
)

FORBIDDEN = [
    r"\bmanifesto\b",
    r"\bfinal theory\b",
    r"\bproves the theory\b",
    r"\bnew school of thought\b",
    r"\bsolves ontology\b",
    r"\bultimate theory of reality\b",
    r"\bhistorical culmination\b",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.hidden = 0
        self.text: list[str] = []
        self.h1: list[str] = []
        self.h2: list[str] = []
        self.meta: dict[str, str] = {}
        self.capture: str | None = None
        self.buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k.lower(): v or "" for k, v in attrs}
        if tag == "meta":
            key = attr.get("name") or attr.get("property")
            if key:
                self.meta[key] = attr.get("content", "")
        classes = set(attr.get("class", "").split())
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if "sr-only" in classes or attr.get("hidden") == "hidden" or attr.get("aria-hidden") == "true":
            self.hidden += 1
            return
        if self.skip or self.hidden:
            return
        if tag in {"h1", "h2"}:
            self.capture = tag
            self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1
            return
        if self.hidden:
            self.hidden -= 1
            return
        if self.skip:
            return
        if self.capture == tag:
            value = normalize("".join(self.buffer))
            if tag == "h1":
                self.h1.append(value)
            elif tag == "h2":
                self.h2.append(value)
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.skip or self.hidden:
            return
        self.text.append(data)
        if self.capture:
            self.buffer.append(data)


def normalize(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split())


def fail(message: str) -> None:
    raise AssertionError(message)


def page_path(site: Path, route: str) -> Path:
    return site / route.strip("/") / "index.html"


def read_page(site: Path, route: str) -> tuple[str, str, PageParser]:
    path = page_path(site, route)
    if not path.exists():
        fail(f"Missing built route: {route}")
    html = path.read_text(encoding="utf-8", errors="ignore")
    parser = PageParser()
    parser.feed(html)
    parser.close()
    visible = normalize(" ".join(parser.text))
    return html, visible, parser


def require(text: str, needle: str, route: str) -> None:
    if needle not in text:
        fail(f"{route} missing expected text: {needle}")


def forbid(text: str, route: str) -> None:
    for pattern in FORBIDDEN:
        if re.search(pattern, text, flags=re.IGNORECASE):
            fail(f"{route} contains forbidden wording matching {pattern!r}")


def assert_one_h1(site: Path, route: str, expected: str) -> tuple[str, str, PageParser]:
    html, visible, parser = read_page(site, route)
    if parser.h1 != [expected]:
        fail(f"{route} expected one h1 {expected!r}, got {parser.h1!r}")
    return html, visible, parser


def assert_meta(parser: PageParser, route: str, page_key: str, lane: str = "program") -> None:
    expected = {
        "prrp:page_key": page_key,
        "prrp:lane": lane,
        "prrp:status": "canonical",
    }
    for key, value in expected.items():
        if parser.meta.get(key) != value:
            fail(f"{route} {key} expected {value!r}, got {parser.meta.get(key)!r}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_program_charter.py _site", file=sys.stderr)
        return 2
    site = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    charter_html, charter_visible, charter = assert_one_h1(site, ROUTES["charter"], "Standing in the Inquiry of Being")
    assert_meta(charter, ROUTES["charter"], "program.standing_inquiry_of_being")
    require(charter_visible, "Lineages of Categorical Ontology", ROUTES["charter"])
    require(charter_visible, CANONICAL_SENTENCE, ROUTES["charter"])
    require(charter_visible, "Historical resonance is not evidence of truth.", ROUTES["charter"])
    require(charter_visible, "The lineage helps clarify the ambition, but it does not validate the construction.", ROUTES["charter"])
    if "For contemporary neighboring research programs and comparison surfaces, see" not in charter_html:
        fail(f"{ROUTES['charter']} missing contemporary approaches bridge")
    if f'href="{ROUTES["related"]}"' not in charter_html:
        fail(f"{ROUTES['charter']} bridge must link to Related Approaches")
    for heading in [
        "I. Inquiry Before Doctrine",
        "II. Pythagoras — Formal Intelligibility",
        "III. Heraclitus — Flow and Becoming",
        "IV. Plato — Stable Form and Ontic Structure",
        "V. Aristotle — Categories and Articulation",
        "VI. Leibniz — Relational Rationalism",
        "VII. Kant — Conditions of Intelligibility",
        "VIII. Einstein — Geometry and Physical Intelligibility",
        "IX. Grothendieck — Relation Before Object",
        "X. Toward Categorical Ontology",
        "XI. τ-Theory as Participation, Not Culmination",
        "XII. Conclusion — Standing in the Inquiry of Being",
    ]:
        if heading not in charter.h2:
            fail(f"{ROUTES['charter']} missing h2: {heading}")
    if "00_outline" in charter_visible or "Proposed Essay Architecture" in charter_visible:
        fail("Charter page must not render the source outline")
    forbid(charter_visible, ROUTES["charter"])

    ontology_html, ontology_visible, ontology = assert_one_h1(site, ROUTES["ontology"], "Categorical Ontology")
    assert_meta(ontology, ROUTES["ontology"], "program.categorical_ontology")
    require(ontology_visible, "Categorical ontology is the field of inquiry in which the Panta Rhei Research Program situates τ-Theory.", ROUTES["ontology"])
    require(ontology_visible, "Categorical ontology does not say that ontology is simply category theory.", ROUTES["ontology"])
    require(ontology_visible, "ΙΣΤΟΡΙΑ ΤΟΥ ΟΝΤΟΣ", ROUTES["ontology"])
    forbid(ontology_visible, ROUTES["ontology"])

    program_html, program_visible, _ = assert_one_h1(site, ROUTES["program"], "Program")
    require(program_visible, CANONICAL_SENTENCE, ROUTES["program"])
    require(program_visible, "ΙΣΤΟΡΙΑ ΤΟΥ ΟΝΤΟΣ", ROUTES["program"])
    require(program_visible, "the inquiry it stands in", ROUTES["program"])
    for route in (ROUTES["charter"], ROUTES["ontology"]):
        if f'href="{route}"' not in program_html:
            fail(f"Program root missing link to {route}")
    forbid(program_visible, ROUTES["program"])

    nav_source = (repo / "_data/nav.yml").read_text(encoding="utf-8")
    for title, route in [
        ("Standing in the Inquiry of Being", ROUTES["charter"]),
        ("Categorical Ontology", ROUTES["ontology"]),
    ]:
        if f'title: "{title}"' not in nav_source or f'url: "{route}"' not in nav_source:
            fail(f"Program nav missing {title}")

    bridge_checks = {
        ROUTES["about"]: "The program is also an inquiry of being",
        ROUTES["coherent"]: "For the historical and philosophical orientation behind this phrase",
        ROUTES["inspection"]: "The charter explains why the program remains inquiry rather than doctrine",
        ROUTES["related"]: "Historical lineage vs. related approaches",
        ROUTES["red_team"]: "the charter is not a substitute for verification",
    }
    for route, needle in bridge_checks.items():
        html, visible, parser = read_page(site, route)
        if len(parser.h1) != 1:
            fail(f"{route} should contain exactly one h1, found {len(parser.h1)}")
        require(visible, needle, route)
        if f'href="{ROUTES["charter"]}"' not in html:
            fail(f"{route} must link to the charter page")
        forbid(visible, route)

    print("v4 Program charter assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
