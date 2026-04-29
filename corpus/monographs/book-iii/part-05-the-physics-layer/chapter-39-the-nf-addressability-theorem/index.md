---
layout: "corpus-monograph-chapter"
title: "Chapter 39: The NF-Addressability Theorem"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-39-the-nf-addressability-theorem/"
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
chapter_number: 39
chapter_slug: "chapter-39-the-nf-addressability-theorem"
page_in_book: 195
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-38-sigma/"
prev_chapter_title: "Chapter 38: σ"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-40-the-physics-layer-complete/"
next_chapter_title: "Chapter 40: The Physics Layer Complete"
summary_short: "Every σ-fixed boundary character at finite primorial depth is NF-addressable in every primitive sector *III.T28*; the proof proceeds sector by sector via Label_n stabilisation, with the EM sector as model case and a five-item coherence check against the Mutual Determination schema."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-39-the-nf-addressability-theorem/"
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

Chapter 38 introduced the concepts this chapter brings to proof: σ-fixed boundary characters (*III.D47*) and sector addressability (*III.D48*). We prove the NF-Addressability Theorem (*III.T28*): every σ-fixed boundary character at finite primorial depth is NF-addressable in every primitive sector S ∈ {A, B, C, D}. The proof proceeds sector by sector. The electromagnetic sector (B) serves as the model case using Label_n stabilisation and the CRT decomposition; the strong (C), weak (A), and gravity (D) sectors follow the same schema with sector-specific adjustments. A five-item coherence check against the Mutual Determination checklist closes the chapter.

## What this chapter contributes

The EM Sector Verification (*III.P19*) establishes the model case. For a σ-fixed character χ at primorial depth k, the CRT decomposition of the B-projection π_B(χ) reduces the NF extraction to a prime-by-prime computation: at each prime p_i ≤ Prim(k), the σ-fixed condition forces equal e₊ and e₋ components — the "half-value" condition m_i = n_i — which in turn forces the B-sector Local Label Label_B(p_i) to assign a unique balanced spectral value. Label_n(p_i) stabilises at depth i because all subsequent primes only refine the existing assignment without altering it. Hence the NF of π_B(χ) stabilises at depth k_B = k, which is the definition of sector addressability for the B-sector.

The Sector-by-Sector Protocol (*III.P20*) applies the EM template to the remaining three sectors with sector-specific adjustments. For C: σ-fixedness forces χ_C = χ_B by the σ-conjugacy of B and C projections, so the B-sector argument is verbatim. For A: the π-generator acting on the weak channel selects a different linear combination of e₊ and e₋ components; balanced residues stabilise at each A-sector prime by a separate induction, and the stabilisation depth matches k. For D: the p = 2 degeneracy forces χ mod 2 = 0, fixing the D-sector component at the first primorial level; odd primes then follow the B-sector pattern, giving k_D = k as well. In all four cases the stabilisation depth equals k, confirming that σ-fixed characters are simultaneously sector-addressable in all primitive sectors at depth k.

The five-item coherence check confirms: the theorem operates at E₁, the admissibility predicate is decidable in finite computation, the conjectural bridge to classical Hodge (sector addressability ↔ algebraic representability on smooth projective varieties) is open and explicitly deferred to Part X, and the scope grades are τ-effective for all proved results.

## Lean coverage

- *III.T28* — NF-Addressability Theorem (τ-effective)
- *III.P19* — EM Sector Verification (τ-effective)
- *III.P20* — Sector-by-Sector Protocol (τ-effective)

## Where this leads

This chapter closes the Hodge block and delivers its primary structural input for the enriched bi-square in Part VI: NF-addressability guarantees that every balanced character has a definite sector location, ensuring that the bi-square's sector-level projections are well-defined. The conjectural identification of sector addressability with algebraic representability on smooth projective varieties is addressed in Part X.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch42-the-nf-addressability-theorem.tex -->
