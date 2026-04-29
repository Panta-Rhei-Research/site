---
layout: "corpus-monograph-chapter"
title: "Chapter 37: The Yang–Mills Mass Gap"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-37-the-yang-mills-mass-gap/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-the-physics-layer"
chapter_number: 37
chapter_slug: "chapter-37-the-yang-mills-mass-gap"
page_in_book: 187
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-36-the-tau/"
prev_chapter_title: "Chapter 36: The τ"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-38-sigma/"
next_chapter_title: "Chapter 38: σ"
summary_short: "The τ-Gap Meta-Theorem is instantiated for the strong C-sector, yielding the Yang–Mills Gap Theorem *III.T27*: Γ*_s > 0 for all τ-admissible gauge data. Scope: τ-effective, not Clay-valid; the sector–force identification with SU(3) is explicitly deferred."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-37-the-yang-mills-mass-gap/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part V: The Physics Layer"
      url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part V"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 36
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The τ-Gap Meta-Theorem from Chapter 36 is a machine: feed it an NF-discrete tower with a contractive defect functional and it returns a spectral gap. This chapter turns the machine on. We restrict the defect functional to the strong C-sector, defining the strong defect functional (*III.D46*), verify that τ-admissible gauge data satisfies both meta-theorem hypotheses, and conclude the Yang–Mills Gap Theorem (*III.T27*): the strong-sector gap constant Γ*_s > 0. Every non-trivial τ-admissible gauge configuration carries a strictly positive defect, uniformly bounded below across all primorial depths.

## What this chapter contributes

The strong defect functional (*III.D46*) is the restriction of Δ to C-sector gauge data. Because τ-admissible gauge data has A, B, D, and ω components identically zero, the full defect collapses to the C-sector component alone — a simplification that makes the Yang–Mills instantiation cleaner than the Navier–Stokes one. The strong defect Δ_s(x,k) measures the NF distance between a C-sector configuration at depth k and its nearest canonical C-sector form; contractivity (*III.P14*) then ensures this distance decreases with depth.

The Yang–Mills Gap Theorem (*III.T27*) follows in two steps: verify hypothesis (H1) — NF discreteness — from the NF Discreteness Lemma (*III.P16*), and hypothesis (H2) — defect contractivity — from *III.P14*; then apply the τ-Gap Meta-Theorem (*III.T26*). The two-line proof is entirely τ-internal, with no quantum field theory or gauge group structure required. The structural reason for the gap is made explicit in a separate remark: the profinite configuration space Ẑ_τ is totally disconnected, so there is no continuous family of configurations and no parameter that could tune the strong defect continuously to zero. A gap that cannot be tuned away is not an approximation — it is an exact algebraic constraint.

The scope declaration draws three sharp boundaries: (a) the τ-gap is proved for τ-admissible gauge data on the profinite tower, not for SU(3) connections on ℝ⁴; (b) the sector–force identification (C-sector ≅ SU(3) gauge theory) is conjectural and deferred to Part X; (c) the gap constant Γ*_s is dimensionless in Category τ, and its conversion to physical units requires the sector–force mapping developed in Books IV–V. YM export contracts (*III.R19*) state five deliverables — gap existence, strong defect functional, NF lattice structure, sector isolation, and the K5 cascade bound — each with explicit preconditions and postconditions for Part VI consumers.

## Lean coverage

- *III.T27* — Yang–Mills Gap Theorem (τ-effective)
- *III.D46* — Strong Defect Functional (τ-effective)
- *III.R19* — YM Export Contracts

## Where this leads

Gap existence closes the YM block (Chapters 35–37). The conjectural bridge to the Clay Yang–Mills problem is addressed in Part X. The strong sector structure is consumed by Part VI's enriched bi-square. The strong defect functional is compared with the Yang–Mills action functional in Part X.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch40-the-yang-mills-mass-gap.tex -->
