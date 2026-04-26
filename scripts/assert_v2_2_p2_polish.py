#!/usr/bin/env python3
"""Targeted assertions for the v2.2 Batch 1 P2/backlog polish wave."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")


H1_AUDIT_PATHS = [
    "/engage/media-and-contact/",
    "/impact/by-portfolio/",
    "/publications/physics-ledger/",
    "/verify/custom-axiom-inventory/",
    "/verify/tcb-disclosure/",
    "/publications/books/book-i/part-02-orbit-generation-and-ontic-closure/chapter-08-the-iterator-of-iterator-ladder-and-tetration-saturation/",
    "/publications/books/book-i/part-02-orbit-generation-and-ontic-closure/chapter-09-rigidity-tau/",
    "/publications/books/book-i/part-03-the-denotational-bridge/chapter-10-tau-idx-the-alpha-orbit-as-internal-natural-numbers/",
    "/publications/books/book-i/part-08-the-spectral-ring/chapter-34-the-master-constant-iota-tau-2-pi-e/",
    "/publications/books/book-i/part-11-tau/chapter-45-boolean-recovery-and-the-subobject-classifier-preview/",
    "/publications/books/book-i/part-13-internal-set-theory-the-cantor-mirage/chapter-55-countability-is-not-a-limitation/",
    "/publications/books/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-29-iota-tau-confirmed-the-archimedean-non-archimedean-bridge/",
    "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-35-laurent-series-and-residues/",
    "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-36-the-canonical-holomorphic-basis-b/",
    "/publications/books/book-iii/part-04-the-spectral-doors/chapter-27-the-grand-grh/",
    "/publications/books/book-iii/part-04-the-spectral-doors/chapter-28-poincar-e-s-conjecture/",
    "/publications/books/book-iii/part-04-the-spectral-doors/chapter-29-simply-connected-in-category-tau/",
    "/publications/books/book-iii/part-09-where-life-lives/chapter-57-the-computation-layer/",
    "/publications/books/book-iii/part-09-where-life-lives/chapter-62-why-there-is-no-barrier/",
    "/publications/books/book-iv/part-01-the-joint-core-from-neutron-to-hydrogen/chapter-05-the-photon-as-null-transport/",
    "/publications/books/book-iv/part-03-the-electroweak-arc/chapter-25-electroweak-mixing/",
    "/publications/books/book-iv/part-04-the-strong-sector-and-confinement/chapter-33-the-vacuum-catastrophe-dissolved/",
    "/publications/books/book-iv/part-05-particles-generations-and-nuclear-physics/chapter-38-the-micro-donut-and-ternary-structure/",
    "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-45-the-hydrogen-atom-bohr-radius-and-rydberg-constant/",
    "/publications/books/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-69-running-vs-readout/",
    "/publications/books/book-v/part-01-the-base-itself-time-from-tau/chapter-02-proto-chronos-from-alpha-ticks-to-proper-time/",
    "/publications/books/book-v/part-01-the-base-itself-time-from-tau/chapter-03-the-temporal-ignition-why-a-time-epoch-starts/",
    "/publications/books/book-v/part-01-the-base-itself-time-from-tau/chapter-04-high-energy-and-high-entropy-at-the-beginning/",
    "/publications/books/book-v/part-05-global-structure/chapter-40-the-bullet-cluster-and-large-scale-structure/",
    "/publications/books/book-v/part-06-eternal-dynamics/chapter-49-the-no-shrink-theorem-mature-black-holes-cannot-shrink/",
    "/publications/books/book-v/part-06-eternal-dynamics/chapter-51-global-finiteness-the-four-theorem-chain/",
    "/publications/books/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-14-thermodynamic-necessity-and-the-origin-of-life/",
    "/publications/books/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-15-circadian-rhythms-poincar-e-orbits-on-the-temporal-circle/",
    "/publications/books/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-16-homochirality-the-parity-bridge-made-visible/",
    "/publications/books/book-vii/part-03-categorical-phenomenology/chapter-35-perception-and-experience/",
    "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-77-the-categorical-imperative-as-sheaf-condition/",
    "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-90-the-commitment-register/",
    "/results/problem/axial-coupling-g-a-5pt5-ppm/",
    "/results/problem/baryogenesis-eta-b/",
    "/results/problem/cabibbo-angle/",
    "/results/problem/gravitational-constant-from-iota-tau/",
    "/results/problem/hubble-tension-resolved-h-formula/",
    "/results/problem/tensor-to-scalar-ratio/",
    "/results/world-readout/physics/from-ratio-to-measurement-iota-tau-and-the-calibration-of-physics/",
]


SOFTENED_RESULT_PATHS = [
    "/results/problem/hubble-tension-resolved-h-formula/",
    "/results/problem/s8-tension-resolved-0pt783/",
    "/results/problem/lithium-7-problem-resolved/",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.text_parts: list[str] = []
        self.h1_count = 0
        self._h1_depth = 0
        self._h1_parts: list[str] = []
        self.h1_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "svg"}:
            self.skip += 1
        if tag == "h1" and not self.skip:
            self.h1_count += 1
            self._h1_depth = 1
            self._h1_parts = []
        elif self._h1_depth:
            self._h1_depth += 1
        if not self.skip and tag in {"h1", "h2", "h3", "p", "li", "td", "th", "div", "section", "article", "br"}:
            self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self._h1_depth:
            self._h1_depth -= 1
            if self._h1_depth == 0:
                self.h1_text.append(norm(" ".join(self._h1_parts)))
        if tag in {"script", "style", "svg"} and self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        self.text_parts.append(data)
        if self._h1_depth:
            self._h1_parts.append(data)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def html_path(path: str) -> Path:
    return SITE / path.strip("/") / "index.html"


def page(path: str) -> tuple[str, list[str]]:
    full = html_path(path)
    if not full.exists():
        raise AssertionError(f"{path}: missing built page at {full}")
    parser = PageParser()
    parser.feed(full.read_text(encoding="utf-8", errors="replace"))
    return norm(" ".join(parser.text_parts)), parser.h1_text


def require(path: str, *phrases: str) -> None:
    text, h1 = page(path)
    if len(h1) != 1:
        raise AssertionError(f"{path}: expected exactly one h1, found {h1}")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path}: missing phrase {phrase!r}")


def forbid(path: str, *phrases: str) -> None:
    text, h1 = page(path)
    for phrase in phrases:
        if phrase in text or any(phrase in heading for heading in h1):
            raise AssertionError(f"{path}: forbidden visible phrase still present {phrase!r}")


def main() -> int:
    for audited_path in H1_AUDIT_PATHS:
        _, h1 = page(audited_path)
        if len(h1) != 1:
            raise AssertionError(f"{audited_path}: expected exactly one h1, found {h1}")

    for engage_path in ["/engage/", "/engage/support-the-research/", "/engage/contact/"]:
        require(engage_path, "Participation does not imply endorsement.")
        require(engage_path, "Independence, Scope & Scrutiny")

    for result_path in SOFTENED_RESULT_PATHS:
        if not html_path(result_path).exists():
            raise AssertionError(f"{result_path}: softened legacy route must still build")
        _, h1 = page(result_path)
        if any("Resolved" in heading for heading in h1):
            raise AssertionError(f"{result_path}: h1 still contains unqualified Resolved: {h1}")

    for public_path in [
        "/results/",
        "/results/browse/",
        "/results/by-book/",
        "/results/by-domain/",
        "/results/by-problem/",
        "/results/fields/cosmology-astrophysics/",
        "/results/topic/mathematics/",
        "/results/topic/physics/",
        "/results/predictions/browse/",
        "/results/predictions/timing/",
    ] + SOFTENED_RESULT_PATHS:
        forbid(
            public_path,
            "Hubble Tension Resolved",
            "S₈ Tension Resolved",
            "S8 Tension Resolved",
            "Li-7 Problem Resolved",
            "Lithium-7 Abundance (Resolved)",
            "Status: Resolved",
            "Resolved —",
        )

    require("/publications/physics-ledger/", "Numerical Physics Ledger")
    require("/publications/numerical-physics-ledger/", "Status and scope")

    print("v2.2 Batch 1 P2 polish assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
