---
layout: "corpus-monograph-chapter"
title: "Chapter 10: Predictions by Absence: Virus, Neutron, NS-to-BH"
permalink: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-10-predictions-by-absence-virus-neutron-ns-to-bh/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-life-definition"
chapter_number: 10
chapter_slug: "chapter-10-predictions-by-absence-virus-neutron-ns-to-bh"
page_in_book: 55
prev_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-09-the-seven-hallmarks-derived/"
prev_chapter_title: "Chapter 9: The Seven Hallmarks Derived"
next_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-11-the-seven-forces-and-the-tau-domain/"
next_chapter_title: "Chapter 11: The Seven Forces and the τ³ Domain"
summary_short: "Three canonical non-Life systems — virus (NoDist, host-dependent), free neutron (NoDist, finite-horizon beta decay), neutron star near the TOV limit (NoSelfDesc, boundary instability) — probe structurally distinct failure modes and constitute a falsifiability program for the Life definition."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
canonical_part_title: "The Life Definition"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-01-the-life-definition/chapter-10-predictions-by-absence-virus-neutron-ns-to-bh/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part I: The Life Definition"
      url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part I"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 60
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

A definition gains its force from what it excludes as much as from what it includes. This chapter identifies three canonical systems that fail the Life predicate — each for a structurally distinct reason — and organises these failures into a falsifiability program. The two failure modes are formalised first. NoDist: a system with no map D: X → 2_τ satisfying all five τ-Distinction conditions. NoSelfDesc: a system with a valid τ-Distinction that nonetheless admits no converging internal evaluator. The three test cases then probe different parts of the definition. A virus (NoDist): its capsid provides a clopen boundary, but three of the five τ-Distinction conditions fail outside a host — refinement-coherence beyond the single structural level is absent, eventual stability fails as the capsid degrades, law-stability fails since the virus has no autonomous dynamics, and H_∂-equivariance fails for lack of an autonomous holonomy structure. The verdict is categorical: a virus is a forgetful functor from the host's Life category — information without autonomous boundary maintenance. A free neutron (NoDist): beta decay with mean lifetime ≈ 880 s dissolves the self/non-self boundary within finite time, failing eventual stability and law-stability (the weak sector endomorphisms are admissible and they destroy the distinction). A bound neutron merely transfers the host-dependence from the cell to the nucleus. A neutron star near the TOV limit (NoSelfDesc): this is the canonical counterexample from Chapter 6, revisited here from the classification perspective. The star passes all five τ-Distinction conditions; it fails SelfDesc because boundary instability prevents code closure. These three cases organise into a structural hierarchy — NoDist (no boundary), NoDist (finite-horizon boundary), NoSelfDesc (boundary without decoding loop), Life (boundary with decoding loop) — and the NS-to-BH transition is the canonical Life phase boundary: a sharp bifurcation, not a gradient. The Falsifiability Program (VI.R03) names four structural predictions that would refute specific classifications if empirically violated.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D19 — NoDist*: formal failure mode at the Distinction gate. *VI.D20 — NoSelfDesc*: formal failure mode at the SelfDesc gate.
- **Key results:** *VI.T15 — Virus NoDist Theorem*: three of the five τ-Distinction conditions fail for a virus outside a host; the distinction is host-dependent. *VI.L05 — Neutron NoDist Lemma*: beta decay violates eventual stability and law-stability; the free neutron is NoDist. *VI.L06 — NS-NoSelfDesc Lemma*: the near-TOV neutron star passes all five τ-Distinction conditions but boundary instability prevents code closure. *VI.P05 — Canonical Life Phase Boundary*: the NS-to-BH transition is sharp; below M_TOV: NoSelfDesc; above: Life. *VI.R03 — Falsifiability Program*: four structural predictions that would refute the NoDist or NoSelfDesc classifications.
- **Dependencies:** Chapters 4–6 (τ-Distinction, SelfDesc, Layer Separation Lemma); Book V (TOV equation, beta decay timescale).

## Lean coverage

`TauLib.BookVI.Life.FailureModes`

## Where this leads

Chapter 11 completes Part I by providing the cross-sectoral physical foundations — the seven categorical forces at E₂ and the τ³ domain correspondence — that ground the formal machinery in physical biology.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part01/ch10-predictions-absence.tex -->
