---
layout: "corpus-monograph-chapter"
title: "Chapter 38: σ"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-38-sigma/"
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
chapter_number: 38
chapter_slug: "chapter-38-sigma"
page_in_book: 191
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-37-the-yang-mills-mass-gap/"
prev_chapter_title: "Chapter 37: The Yang–Mills Mass Gap"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-39-the-nf-addressability-theorem/"
next_chapter_title: "Chapter 39: The NF-Addressability Theorem"
summary_short: "The σ-involution on H_τ selects the diagonal sublattice of balanced boundary characters *III.D47*; sector addressability *III.D48* poses the τ-Hodge question, and *III.P18* shows why it is trivial at E₀ and substantive only at E₁."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-38-sigma/"
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

This chapter opens the Hodge block (Chapters 38–39) by posing the Hodge question in the language of Category τ. The classical Hodge Conjecture asks which cohomology classes are algebraic; in τ, the question becomes: which boundary characters on the lemniscate L are NF-addressable within each sector of the 4+1 decomposition? The σ-involution on the split-complex algebra H_τ = ℤ[j]/(j² − 1) swaps the idempotents e₊ and e₋; the σ-fixed characters — those invariant under this swap — are precisely the balanced characters of the spectral trichotomy. The chapter defines the two key concepts, proves why the question is non-trivial only at E₁, and states the τ-Hodge conjecture.

## What this chapter contributes

σ-Fixed characters (*III.D47*) are boundary characters (m, n) ∈ ℤ² with m = n — the diagonal sublattice, which at each primorial depth k contains exactly Prim(k) elements. These are precisely the balanced characters (|m| = |n|) of the spectral trichotomy, the equator between the B-sector (χ₊-dominant) and C-sector (χ₋-dominant). Their B- and C-sector projections are σ-conjugate: depth_B(χ) = depth_C(χ) by the commutativity of σ with the tower maps. This σ-conjugacy is what makes them "self-dual" in the spectral sense — the balanced character sees the same NF structure from both sides of the split-complex decomposition.

Sector addressability (*III.D48*) requires that the S-projection of χ stabilise at finite NF depth k_S ≤ k for each primitive sector S ∈ {A, B, C, D}. The four stabilisation depths are in general distinct: a σ-fixed character is simultaneously addressed in all four sectors if and only if all four NF depths are finite. The definition is τ-effective because each k_S is computed by a finite primorial algorithm.

The proposition "Hodge Requires E₁" (*III.P18*) establishes the non-triviality of the question. At E₀ the Central Theorem of Book II (*II.T49*) already addresses every character globally, so the "which" question has a trivially affirmative answer — the predicate "σ-fixed" carries no extra information. At E₁, the sector admissibility predicates introduce sector-by-sector NF depth bounds that are genuinely non-trivial constraints: a character that is globally addressable at E₀ may fail to be sector-addressable at E₁ if its NF stabilisation depth exceeds the sector's admissibility cutoff. The τ-Hodge conjecture is therefore a substantive E₁ question: every σ-fixed character is sector-addressable in every primitive sector.

## Lean coverage

- *III.D47* — σ-Fixed Character (τ-effective)
- *III.D48* — Sector Addressability (τ-effective)
- *III.P18* — Hodge Requires E₁ (τ-effective)

## Where this leads

Chapter 39 proves the τ-Hodge conjecture — the NF-Addressability Theorem (*III.T28*) — sector by sector, using the model case of the EM (B) sector established here. The conjectural bridge from sector addressability to algebraic representability on smooth projective varieties is deferred to Part X.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch41-sigma-fixed-characters-and-sector-addressability.tex -->
