#!/usr/bin/env python3
"""Targeted assertions for the v2.2 hotfix 2 Impact strata rendering cleanup."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")

EXPECTED_H2 = {
    "/impact/foundational-science/": [
        "Reading discipline",
        "Core idea",
        "Why this stratum comes first",
        "Mathematics: earned structure rather than unrestricted virtual universe",
        "Godel, induction, and unearned diagonal access",
        "Millennium problems and foundational stress tests",
        "Physics: shared ontological carrier rather than forced unification",
        "Life, mind, and metaphysics: constructive articulation, not reduction",
        "Self-enrichment: how new layers can be real without being separate worlds",
        "What would change for foundational science",
        "What this does not mean",
        "Boundary condition",
    ],
    "/impact/applied-science-and-research/": [
        "Reading discipline",
        "Core idea",
        "Why this stratum comes after Foundational Science",
        "Cosmology: refusing Lambda and CDM without refusing the data",
        "High-energy physics: higher energy is not automatically deeper ontology",
        "Simulation and fluid dynamics: native multiscale geometry",
        "What applied science would require",
        "What this does not mean",
        "Boundary condition",
    ],
    "/impact/global-education/": [
        "Reading discipline",
        "Core idea",
        "Why education is an impact stratum",
        "Coherence before specialization",
        "Accessibility without oversimplification",
        "A relational corpus of knowledge",
        "Epistemic clarity and inspectability",
        "Democratizing research participation",
        "Shared semantics for collaboration",
        "What this does not mean",
        "Boundary condition",
    ],
    "/impact/existential-orientation/": [
        "Reading discipline",
        "Core idea",
        "Why this stratum is delicate",
        "Life is not a freak accident",
        "Dignity as structural, not merely conventional",
        "A universe moving toward structure, not only toward death",
        "Meaning without coercion",
        "Faith, commitment, and science without forced conflict",
        "What becomes existentially thinkable",
        "What this does not mean",
        "Boundary condition",
    ],
    "/impact/societal-coherence/": [
        "Reading discipline",
        "Core idea",
        "Why this stratum is sensitive",
        "Science itself is broader than one image of science",
        "Science realigned from within",
        "From objectification to relational intelligibility",
        "Ethics, dignity, and structural validity",
        "Global norms without cultural ownership",
        "Coherence without ideology",
        "The non-coercive force of better reasons",
        "What this does not mean",
        "Boundary condition",
    ],
}


def norm(text: str) -> str:
    text = text.replace("Λ", "Lambda").replace("ö", "o").replace("Gödel", "Godel")
    return re.sub(r"\s+", " ", text).strip()


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.skip = 0
        self.skip_stack: list[str] = []
        self.h1: list[str] = []
        self.h2: list[str] = []
        self.visible_parts: list[str] = []
        self.pre_count = 0
        self.code_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag)
        attr_map = {key: value or "" for key, value in attrs}
        classes = set(attr_map.get("class", "").split())
        if tag == "pre":
            self.pre_count += 1
        if tag == "code":
            self.code_count += 1
        if tag in {"head", "script", "style", "svg"} or "sr-only" in classes or "data-pagefind-meta" in attr_map:
            self.skip += 1
            self.skip_stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if self.skip_stack and self.skip_stack[-1] == tag and self.skip:
            self.skip_stack.pop()
            self.skip -= 1
        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        current = self.stack[-1] if self.stack else ""
        clean = norm(data)
        if not clean:
            return
        if current == "h1":
            self.h1.append(clean)
        elif current == "h2":
            self.h2.append(clean)
        self.visible_parts.append(clean)


def page(route: str) -> PageParser:
    path = SITE / route.strip("/") / "index.html"
    if not path.exists():
        raise AssertionError(f"{route}: missing built page at {path}")
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser


def main() -> int:
    for route, headings in EXPECTED_H2.items():
        parser = page(route)
        visible = norm(" ".join(parser.visible_parts))
        if len(parser.h1) != 1:
            raise AssertionError(f"{route}: expected one h1, found {parser.h1}")
        if parser.h2[: len(headings)] != headings:
            raise AssertionError(f"{route}: h2 sequence mismatch\nexpected={headings}\nactual={parser.h2}")
        if "Codex may use the following as the full replacement body" in visible:
            raise AssertionError(f"{route}: Codex instruction text is visible")
        if "```markdown" in visible or "full replacement body" in visible:
            raise AssertionError(f"{route}: fenced briefing text is visible")
        if parser.pre_count or parser.code_count:
            raise AssertionError(f"{route}: rendered pre/code block found in stratum body")
        if "Reading discipline" not in parser.h2:
            raise AssertionError(f"{route}: missing Reading discipline heading")

    global_public_good = page("/impact/global-public-good/")
    visible_gpg = norm(" ".join(global_public_good.visible_parts))
    for phrase in ["11 conditional public-good portfolios", "44 Public-Good Briefings"]:
        if phrase not in visible_gpg:
            raise AssertionError(f"/impact/global-public-good/: missing {phrase!r}")

    print("v2.2 hotfix 2 Impact strata rendering assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
