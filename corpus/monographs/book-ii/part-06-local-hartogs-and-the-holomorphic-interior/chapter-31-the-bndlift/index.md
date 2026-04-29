---
layout: "corpus-monograph-chapter"
title: "Chapter 31: The BndLift"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-31-the-bndlift/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-local-hartogs-and-the-holomorphic-interior"
chapter_number: 31
chapter_slug: "chapter-31-the-bndlift"
page_in_book: 151
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-30-split-complex-codomain-with-calibration/"
prev_chapter_title: "Chapter 30: Split-Complex Codomain with Calibration"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-32-mutual-determination-5-way-equivalence/"
next_chapter_title: "Chapter 32: Mutual Determination (5-Way Equivalence)"
summary_short: "BndLift_n is the τ-analogue of Hartogs extension: it promotes holomorphic boundary data at stage n to interior data at stage n+1 via CRT decomposition and bipolar channel splitting."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-31-the-bndlift/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VI: Local Hartogs and the Holomorphic Interior"
      url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 25
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Classical several complex variables extends holomorphic functions from the boundary of a Hartogs figure to the interior via the Bochner–Martinelli kernel. Category τ has no smooth boundary, no Cauchy integral, and no complex structure — yet the same phenomenon holds. This chapter constructs its τ-analogue: the boundary lift operator *BndLift_n*, which extends holomorphic data from stage n of the primorial tower to stage n+1, one prime at a time. The mechanism is the Chinese Remainder Theorem: the isomorphism ℤ/P_{n+1}ℤ ≅ ℤ/P_nℤ × ℤ/p_{n+1}ℤ separates the known stage-n component (the boundary datum) from the unknown p_{n+1}-component (the interior extension to be determined). The diagonal discipline K5 then pins down this unknown uniquely, making the lift computable rather than existential.

## What this chapter contributes

- **Definitions:** *II.D36 — BndLift_n*: given a holomorphic datum f_n on ℤ/P_nℤ valued in *H_τ^cal*, the lifted datum f_{n+1} on ℤ/P_{n+1}ℤ is the unique function satisfying (i) compatibility with f_n on the stage-n component, (ii) bipolar splitting along e_±, (iii) CRT extension of each sector via the lift increment Δ_n^(±), and (iv) inter-channel coupling constraint ‖Δ_n^(+)‖ = ι_τ · ‖Δ_n^(-)‖.
- **Key results:** *II.T26 — BndLift Existence*: for every n ≥ 1 and every holomorphic datum f_n, the lift f_{n+1} exists, is unique (forced by CRT and the diagonal discipline K5), factors as an independent product of B-sector and C-sector lifts, and is asymptotically isometric with constant C_τ = 4/(π + e). *II.P07 — Bipolar Channel Independence*: the two sector lifts are informationally independent — the lift increment Δ_n^(+) is determined solely by B-sector data, Δ_n^(-) solely by C-sector data; the only coupling is the norm ratio governed by ι_τ.
- **Structural results:** an explicit CRT interpolation formula for Δ_n^(±) shows the lift is a computable finite sum at every stage; convergence of the iterated lift system to a profinite limit in Hol(τ³, *H_τ^cal*) establishes the Local Hartogs phenomenon; associativity of iterated lifts follows from *I.P02* (program monoid).
- **Dependencies:** *I.D19*, *I.D20*, *I.D21*, *I.D24*, *I.P02*, *I.T10*, *I.T18*, *II.D08*, *II.D09*, *II.D10*, *II.D32*, *II.D33*, *II.D35*, *II.T04*, *II.T24*, *II.T25*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Hartogs.BndLift` is planned.

## Where this leads

The BndLift is the operational core of Part VI. Chapter 32 uses it as description (H) in the five-way Mutual Determination Theorem, showing that a Hartogs continuation is equivalent to a refinement tail, spectral tail, ω-germ, or boundary character. Chapter 33 composes successive lifts into the evolution operator and derives the causal arrow from the B/C asymmetry.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch30-bndlift-construction.tex -->
