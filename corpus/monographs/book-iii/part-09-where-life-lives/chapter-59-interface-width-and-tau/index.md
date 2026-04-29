---
layout: "corpus-monograph-chapter"
title: "Chapter 59: Interface Width and τ"
permalink: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-59-interface-width-and-tau/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chart"
book_id: "III"
book_slug: "book-iii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-where-life-lives"
chapter_number: 59
chapter_slug: "chapter-59-interface-width-and-tau"
page_in_book: 303
prev_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-58-the-tau/"
prev_chapter_title: "Chapter 58: The τ"
next_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-60-witness-search-as-address-resolution/"
next_chapter_title: "Chapter 60: Witness Search as Address Resolution"
summary_short: "Interface Width (*III.D53*) and τ-Admissibility (*III.D54*) measure computational depth in the primorial tower; the Interface Width Principle (*III.T31*) collapses τ-admissible functions to a single finite quotient."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
canonical_part_title: "Where Life Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-09-where-life-lives/chapter-59-interface-width-and-tau/"
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

The τ-Tower Machine (Chapter 58) computes by inspecting primorial stages of the tower ℤ̂_τ. How many stages does a given computation need? This chapter introduces *interface width* (*III.D53*) — the minimal primorial depth at which a computation stabilises — and defines τ-admissibility (*III.D54*) as the finiteness of this width. The Interface Width Principle (*III.T31*) shows that τ-admissible functions factor through a single finite quotient ℤ/Prim(k₀)ℤ: the entire infinite tower collapses to one level. This collapse is earned: the boundary characters χ⁺, χ⁻ are admissible with width 1, and composition preserves admissibility with sub-additive width bounds (*III.P21*). Interface width is the E₂ analog of the mass gap (E₁): a finite threshold separating tractable structure from infinite regress.

## What this chapter contributes

Section 1 defines Interface Width (*III.D53*). A TTM-computable function f has interface width at size n: w(f, n) = the minimum depth k such that the computation of f(x) on inputs of size n inspects only primorial levels 1, …, k. The overall interface width W(f) = sup_n w(f, n) is the worst-case depth across all input sizes. Stabilisation means that deeper levels of the tower contribute no new information — the output at deeper primorial stages is determined by the data at depth k.

Section 2 defines τ-Admissibility (*III.D54*): a TTM-computable function is τ-admissible if W(f) < ∞. Equivalently, there exists k₀ such that for all input sizes n, the computation stabilises at primorial depth k₀. This is a finiteness condition: no matter how large the input, the computation never needs to look beyond depth k₀. The τ-admissible class is a proper subclass of all TTM-computable functions — functions probing the tower to depth growing with input size are computable but inadmissible. The pattern recurs across enrichment levels: τ-admissible fluid data (NS at E₁), τ-admissible gauge data (YM at E₁), and now τ-admissible computation (P vs NP at E₂) all express the same demand: the infinite primorial tower contributes only finitely many relevant layers.

Section 3 states and proves the Interface Width Principle (*III.T31*): if f is τ-admissible with W(f) = k₀, then f factors through ℤ/Prim(k₀)ℤ — f(x) depends only on x mod Prim(k₀). The proof assembles two steps: tower coherence (the output at depth k₀ determines all deeper levels by definition of interface width) and Global Hartogs at E₂ (by Primorial Cofinality, the stabilised value at depth k₀ extends uniquely to the full profinite tower ℤ̂_τ). Combining them: f is completely determined by the induced map on the finite ring ℤ/Prim(k₀)ℤ. The primorial Prim(k₀) is the computational horizon — the modulus beyond which the computation sees nothing new.

Section 4 proves Earned Admissibility (*III.P21*): the boundary characters χ⁺, χ⁻ are admissible with width 1; the identity has width 0; the successor map has width 1; composition satisfies W(g∘f) ≤ W(f) + W(g) (sub-additive, like circuit depth); and CRT products satisfy W(f₁ × ⋯ × f_k) = max_i w_i. The τ-admissible functions form a compositionally closed class built from earned primitives.

## Lean coverage

The sub-additivity of interface width under composition is the key structural fact: composing two admissible functions costs at most the sum of their individual widths, just as composing two circuits of depths d₁ and d₂ yields depth at most d₁ + d₂. This makes interface width a computable resource. The admissible fragment is provably proper: functions that probe the tower to depth growing with input size exist as TTM computations but are excluded from the τ-effective framework.

## Where this leads

Chapter 60 applies the Interface Width Principle directly to NP witness search. A witness in Category τ is a canonical address whose ABCD coordinates structure the search space. The CRT decomposition factorises the search into independent per-prime problems, converting a product of search costs into a sum and making the total cost O(k² log k) — polynomial in the primorial depth.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part09/ch56-interface-width-and-tau-admissibility.tex -->
