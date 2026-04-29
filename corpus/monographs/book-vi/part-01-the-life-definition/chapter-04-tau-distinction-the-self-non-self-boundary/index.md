---
layout: "corpus-monograph-chapter"
title: "Chapter 4: τ-Distinction: The Self/Non-Self Boundary"
permalink: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-04-tau-distinction-the-self-non-self-boundary/"
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
chapter_number: 4
chapter_slug: "chapter-04-tau-distinction-the-self-non-self-boundary"
page_in_book: 17
prev_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-03-the-parity-bridge-weak-sector-polarity-seeds-life/"
prev_chapter_title: "Chapter 3: The Parity Bridge: Weak-Sector Polarity Seeds Life"
next_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-05-selfdesc-the-internal-decoding-loop/"
next_chapter_title: "Chapter 5: SelfDesc: The Internal Decoding Loop"
summary_short: "The τ-distinction predicate D: X → 2_τ is defined by five load-bearing conditions — clopen, refinement-coherent, eventually stable, law-stable, H_∂-equivariant — and realised by three carrier families: finite-lineage (biological), macro-torus (black hole), and galactic (basins)."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
canonical_part_title: "The Life Definition"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-01-the-life-definition/chapter-04-tau-distinction-the-self-non-self-boundary/"
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

Every living system draws a line: self on one side, non-self on the other. Chapter 3 identified the polarity seed that makes such a line possible; this chapter formalises the predicate that enacts it. The τ-distinction D: X → 2_τ is defined by exactly five conditions on a τ-finite carrier X equipped with boundary holonomy algebra H_∂ and a refinement tower {X_n}. The five conditions are not a shopping list — each rules out a specific failure mode. Without the clopen condition, the boundary is fuzzy rather than binary. Without refinement-coherence, zooming in could reverse a prior classification. Without eventual stability, the boundary could oscillate forever. Without law-stability, the carrier's own dynamics could erase the boundary. Without H_∂-equivariance, the partition would be incompatible with the carrier's topological structure at the lemniscate boundary ℒ = S¹ ∨ S¹. Three carrier families realise this five-condition structure at radically different scales: finite-lineage (biological) carriers, with cell membranes as the lemniscate boundary and genotype-heritable blueprints; macro-torus (black hole) carriers, whose event horizons provide the sharpest possible clopen partition; and galactic carriers, anchored by a central supermassive black hole whose halo boundary approximates the lemniscate topology at cosmological scale. Two canonical modes show how the predicate arises in practice — boundary-induced distinction from physical geometry, and defect-functional distinction from thermodynamic minimisation — and the Distinction Well-Definedness Theorem guarantees that τ-finiteness bounds the stabilisation level.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D02 — τ-Distinction* (τ-effective): the five-condition predicate D: X → 2_τ. *VI.D03 — Finite-Lineage Carrier*: biological carriers with lemniscate membrane boundary, mortality, and genotype-inheritable distinction. *VI.D04 — Macro-Torus Carrier* (τ-effective): black-hole carriers with T² event-horizon boundary, no-shrink immortality, and blueprint-fusing information absorption. *VI.D05 — Galactic Carrier*: SMBH-anchored halo carriers with basin-compatible distinction.
- **Key results:** *VI.T02 — Distinction Well-Definedness Theorem*: for any τ-finite carrier, the stabilisation level N ≤ dim_τ(X), evaluation terminates in at most dim_τ(X) refinement steps, and the distinction is unique up to the H_∂-character χ.
- **Notation introduced:** D: X → 2_τ (the distinction predicate); {X_n} (refinement tower); V_n (defect functional, introduced in the defect-functional mode section).
- **Dependencies:** Chapter 3 (polarity-typed two-point object 2_τ, Parity Bridge); τ-finiteness from Book III.

## Lean coverage

`TauLib.BookVI.Life.Distinction`

## Where this leads

Distinction is necessary but not sufficient for Life: Chapter 5 introduces SelfDesc, the internal decoding loop, and Chapter 6 proves constructively that a neutron star near the TOV limit satisfies all five conditions here while failing SelfDesc — establishing the E₁–E₂ gap as real.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part01/ch04-tau-distinction.tex -->
