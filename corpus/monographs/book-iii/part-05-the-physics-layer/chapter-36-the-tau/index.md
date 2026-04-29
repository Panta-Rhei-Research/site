---
layout: "corpus-monograph-chapter"
title: "Chapter 36: The τ"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-36-the-tau/"
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
chapter_number: 36
chapter_slug: "chapter-36-the-tau"
page_in_book: 183
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-35-the-strong-sector-and-nf-discreteness/"
prev_chapter_title: "Chapter 35: The Strong Sector and NF Discreteness"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-37-the-yang-mills-mass-gap/"
next_chapter_title: "Chapter 37: The Yang–Mills Mass Gap"
summary_short: "The τ-Gap Meta-Theorem *III.T26* proves that any NF-discrete tower with a contractive defect functional has a strictly positive gap constant *III.D45*; the proof is entirely τ-internal and applies uniformly to Yang–Mills and any other sector satisfying the two hypotheses."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-36-the-tau/"
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

We prove the τ-Gap Meta-Theorem: any NF-discrete tower equipped with a contractive defect functional admits a strictly positive spectral gap. The argument is entirely τ-internal — no quantum field theory, no gauge groups, no Lagrangians. NF discreteness (Chapter 35) provides a minimal separation between distinct configurations at each primorial depth; defect contractivity (Chapter 32) prevents accumulation toward zero. These two properties together force the gap constant Γ* (*III.D45*) to be strictly positive. The theorem is a meta-theorem because it applies to any sector satisfying the two hypotheses — Yang–Mills is one instantiation, but the logic is not specific to gauge theory.

## What this chapter contributes

The gap constant (*III.D45*) is defined as the infimum of the defect functional over all non-trivial configurations at all sufficiently deep primorial levels. Unlike a minimum, the infimum could a priori be zero — the interest of the theorem is that it is not. The τ-Gap Meta-Theorem (*III.T26*) is proved by contradiction in six steps: a vanishing sequence of defect values would require configurations to approach their canonical forms arbitrarily closely in the profinite metric; NF discreteness forces identification of any sufficiently close configuration with a specific canonical form; B/C non-collapse prevents that canonical form from being trivial (i.e., the zero configuration); the uniform bound δ* > 0 on the NF-discreteness gap — proved by primorial cofinality — prevents the contradiction from resolving at any finite primorial level; the argument then extends to the profinite limit by compactness; the six-step argument closes.

Gap Stabilisation (*III.P17*) then shows that the finite-depth gap constants Γ_n are non-decreasing and that Γ* = lim Γ_n = Γ₁ > 0. The non-decreasing property is a corollary of the one-prime-at-a-time refinement: adding one prime to the primorial cannot decrease the gap, because the new prime introduces additional NF constraints that can only force further separation. The gap constant is computed explicitly at the first three primorial levels (Prim(1) = 2, Prim(2) = 6, Prim(3) = 30), yielding Γ₁ = Γ₂ = Γ₃ = 1, confirming that new primes do not lower the existing gap. This is the τ-internal structural reason that gap existence is not an approximate or perturbative result but an exact, stable one.

## Lean coverage

- *III.T26* — τ-Gap Meta-Theorem (τ-effective)
- *III.D45* — Gap Constant Γ* (τ-effective)
- *III.P17* — Gap Stabilisation (τ-effective)

## Where this leads

Chapter 37 verifies the two meta-theorem hypotheses for the strong sector specifically and concludes the Yang–Mills Gap Theorem (*III.T27*) as a direct corollary. The meta-theorem structure means that any future sector or problem satisfying NF discreteness and defect contractivity inherits a gap result without additional proof.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch39-the-tau-gap-meta-theorem.tex -->
