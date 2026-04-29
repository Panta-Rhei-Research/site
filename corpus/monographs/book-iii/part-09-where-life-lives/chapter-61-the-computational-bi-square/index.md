---
layout: "corpus-monograph-chapter"
title: "Chapter 61: The Computational Bi-Square"
permalink: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-61-the-computational-bi-square/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-where-life-lives"
chapter_number: 61
chapter_slug: "chapter-61-the-computational-bi-square"
page_in_book: 311
prev_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-60-witness-search-as-address-resolution/"
prev_chapter_title: "Chapter 60: Witness Search as Address Resolution"
next_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-62-why-there-is-no-barrier/"
next_chapter_title: "Chapter 62: Why There Is No Barrier"
summary_short: "The Computational Bi-Square (*III.D56*) completes the four-level scaling chain; the Product-Meet Collapse (*III.T32*) proves ∧ = × at E₂, yielding the τ-Admissibility Collapse (*III.T33*): τ-P_adm = τ-NP_adm."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
canonical_part_title: "Where Life Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-09-where-life-lives/chapter-61-the-computational-bi-square/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part IX: Where Life Lives"
      url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part IX"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 40
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The bi-square of Book I has appeared at three enrichment levels: algebraic (E₀, where the meet α_p ∧ α_q = α_{p×q} is a static algebraic identity), topological (E₀ → E₁, where holomorphic extension meets boundary-value decomposition), and enriched (E₁+, where sector-coupled dynamics meet spectral force decomposition). This chapter constructs the fourth and final bi-square — the Computational Bi-Square (*III.D56*) at E₂ — and uses it to prove the two central results of Part IX: the Product-Meet Collapse (*III.T32*) and the τ-Admissibility Collapse (*III.T33*), which together establish τ-P_adm = τ-NP_adm.

## What this chapter contributes

Section 1 exhibits the scaling chain of four bi-squares. Each upgrades the pasting operation: at E₀, tower coherence of presheaf values meets spectral naturality; at E₁ topological level, holomorphic extension meets boundary decomposition; at E₁+, sector dynamics meet spectral force decomposition; at E₂, TTM execution (tower coherence) meets CRT-decomposed witnesses (spectral naturality), with the pasting yielding the Product-Meet Collapse. The chain is complete at E₂ — Saturation (*III.T03*) ensures no fifth bi-square is needed.

Section 2 defines the Computational Bi-Square (*III.D56*). For a τ-admissible NP problem Π with TTM verifier V of interface width k₀ and a "yes" instance x, the bi-square at depth k ≥ k₀ is a 2×3 commutative diagram with two squares. The *execution square* (left): the verifier's computation at depth k+1 restricts to depth k via the tower projection, and the spectral characters χ⁺/χ⁻ decompose both. The *witness square* (right): the verifier computation at depth k maps to the witness space W(x,k), and the CRT decomposition π_CRT maps W(x,k) to the product ∏_{i=1}^{k} W(x, p_i) of per-prime witness spaces. The diagram has the same shape as Book I's bi-square: left = tower coherence, right = spectral naturality. Only the objects grow richer.

Section 3 proves the Product-Meet Collapse (*III.T32*): pasting the execution and witness squares yields the identity w₁ ∧ w₂ ∧ ⋯ ∧ w_k = w₁ × w₂ × ⋯ × w_k, where w_i ∈ W(x, p_i) is a per-prime witness. The meet (∧, satisfying all per-prime constraints simultaneously) equals the product (×, CRT reassembly). The execution square establishes that the verifier's acceptance at depth k is determined at depth k₀ (tower coherence, from *III.T31*). The witness square decomposes this factored constraint via the CRT (*III.P22*): per-prime conditions are independent. Pasting: global search decomposes into local searches solved independently and reassembled. Search IS construction.

Section 4 assembles the three-step proof of the τ-Admissibility Collapse (*III.T33*): Step 1 — constant-width verification (TTM Cook–Levin tableau row width W = 1 + m, from Chapter 58); Step 2 — polynomial CRT refinement (Cost(x,k) = O(k² log k), from Chapter 60); Step 3 — Product-Meet Collapse (global search = CRT product of independent per-prime searches). Conclusion: verification is polynomial, search is polynomial, search equals construction — therefore τ-P_adm = τ-NP_adm.

## Lean coverage

The proof mirrors the bi-square diagram: Step 1 secures the left square (constant-width execution), Step 2 secures the right square (CRT refinement of witness space), and Step 3 is the pasting. The theorem holds because all three fit together as a single commutative diagram. The collapse applies to the τ-admissible fragment — problems whose verifier has finite interface width. It does not assert P = NP in the classical Turing machine model; that relationship is examined in Chapter 62.

## Where this leads

Chapter 62 addresses the 1st Edition's "Representation Barrier" — a conjectured obstruction that no faithful encoding {0,1}* → Addr(τ) could preserve complexity separation. The No Barrier Theorem (*III.T34*) diagnoses this as a category error (an E₂ question posed with E₀ tools) and proves that at E₂ no encoding gap exists: programs ARE τ-addresses, and the admissibility collapse holds without encoding overhead.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part09/ch58-the-computational-bi-square.tex -->
