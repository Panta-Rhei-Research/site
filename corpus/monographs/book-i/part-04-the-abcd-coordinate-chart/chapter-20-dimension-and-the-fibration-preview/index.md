---
layout: "corpus-monograph-chapter"
title: "Chapter 20: Dimension and the Fibration Preview"
permalink: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-20-dimension-and-the-fibration-preview/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-the-abcd-coordinate-chart"
chapter_number: 20
chapter_slug: "chapter-20-dimension-and-the-fibration-preview"
page_in_book: 79
prev_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-19-the-abcd-coordinate-chart/"
prev_chapter_title: "Chapter 19: The ABCD Coordinate Chart"
next_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-21-the-uniqueness-question/"
next_chapter_title: "Chapter 21: The Uniqueness Question"
summary_short: "dim_τ = 4: the four ABCD coordinates are pairwise independent and no three suffice. The 2+2 split (D,A)×_f(B,C) previews τ³ = τ¹ ×_f T²."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
canonical_part_title: "The ABCD Coordinate Chart"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-04-the-abcd-coordinate-chart/chapter-20-dimension-and-the-fibration-preview/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part IV: The ABCD Coordinate Chart"
      url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part IV"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 5
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

Chapter 19 established that the ABCD coordinate chart Φ : Obj(τ) → τ-Idx⁴ is total. Two questions remain open: Are the four coordinates independent? And is the chart injective? This chapter answers the first by proving *I.P08* (Dimension Theorem): dim_τ = 4. The coordinates A, B, C, D are pairwise independent — no pair is functionally determined by the other — and omitting any single coordinate collapses distinct objects together. The dimension is earned, not stipulated: multiplication supplies A and B, tetration supplies C, and the remainder supplies D. The chapter then refines the 1+3 split into a 2+2 decomposition — base τ¹ (coordinates D, A) and fiber T² (coordinates B, C) — foreshadowing τ³ = τ¹ ×_f T². It also introduces the full quadtree, the Address DAG (*I.D24*), three canonical metrics, and the metric inequality *I.P09*.

## What this chapter contributes

- Defines coordinate independence formally: two coordinate functions f, g : Obj(τ) → τ-Idx are independent if every value-pair (v_f, v_g) in their ranges is realized by some object. Proves pairwise independence for all six pairs of (A, B, C, D) by explicit witness construction — for A vs. B: objects p̲^{b̲} realize any (prime, exponent) pair; for B vs. C: (2̲ ↑↑ c̲)^{b̲} realizes any (exponent, height) pair; remaining pairs by analogous constructions.
- Proves *I.P08* (Dimension Theorem, dim_τ = 4) — both directions. Sufficiency follows from NF existence (Chapter 18). Necessity is proved by dropping each coordinate in turn: dropping D conflates p̲ and p̲·q̲ (sharing (A, B, C) but differing in D); dropping A conflates 2̲ and 3̲ (same (B, C, D), different A); dropping B conflates p̲ and p̲² (same (A, C, D)); dropping C conflates p̲ and p̲ ↑↑ 2̲ (same (A, B, D) — the tetration height carries the distinction, invisible without C). Each dropped coordinate causes genuine information loss.
- States the Dimension Earned Remark: dim_τ = 4 is not postulated but emerges structurally — the four orbit rays O_α, O_π, O_γ, O_η of the generative act foreshadowed this count, and the ABCD chart confirms it from first principles.
- Previews the fibration structure as a 2+2 refinement of the 1+3 split: base τ¹ (coordinates D, A — position: D is remainder/radial distance, A is dominant prime/direction) and fiber T² (coordinates B, C — shape: B is the exponent, C the tetration height). Explains that the geometric form T² = S¹ × S¹ will be earned in Book II. The notation τ³ = τ¹ ×_f T² names a structural decomposition of category τ, not a new mathematical object; neither τ¹ nor T² exists independently of all five generators.
- Notes the No Second Linearity proposition (*I.P53*): Φ(X + Y) ≠ Φ(X) + Φ(Y) in general. Taking X = 2̲, Y = 4̲ gives Φ(6̲) = (3̲, 1̲, 1̲, 2̲), which differs from the componentwise sum of Φ(2̲) and Φ(4̲) in three of four coordinates. The structural reason: α-ray addition redistributes mass across the prime factorization nonlinearly.
- Defines the *full quadtree* Q(x): recurse on all four coordinate indices rather than only the D-remainder. Node x has up to four children — the remainder child D̲ and the index children rank(A̲), rank(B̲), rank(C̲) whenever those exceed α₁. Termination follows from the measure μ(x) = x in the well-ordered τ-Idx: remainder children decrease by prime descent; index children decrease because prime values grow faster than their indices (p̲_k ≥ k+1).
- Defines *I.D24* (Address DAG): globally deduplicate the full quadtree by identifying equal indices. The result is a finite DAG with a diamond shape — branching from root x, reconverging where primes repeat, terminating at α₁. Defines four readout functors π_A, π_B, π_C, π_D extracting individual coordinates; base readouts (π_D, π_A) and fiber readouts (π_B, π_C) realize the 2+2 split.
- Defines the three canonical metrics: ℓ_spine (D-path spine length), ℓ_occ (total quadtree node count with multiplicity, naive-evaluation cost), ℓ_DAG (distinct DAG node count, memoized-evaluation cost).
- Proves *I.P09* (Metric Inequality): ℓ_spine(x) ≤ ℓ_DAG(x) ≤ ℓ_occ(x). The spine is a subpath of the DAG; the DAG identifies repeated nodes that the quadtree counts multiply. Both inequalities are strict whenever x has nontrivial index children or repeated indices.
- Lean coverage: `TauLib.BookI.Coordinates.ABCD` (planned: coord_pairwise_independent, dim_tau_eq_four, dim_necessary).

## Lean coverage

`TauLib.BookI.Coordinates.ABCD` (planned)

## Where this leads

Part IV is complete: the ABCD chart is defined, total, and four-dimensional. One question remains: is Φ injective? Part V answers this with the Hyperfactorization Theorem, converting the total map into a genuine coordinate bijection. The fibration τ³ = τ¹ ×_f T² previewed here receives its full geometric treatment in Book II, where the Central Theorem identifies the sheaf of holomorphic functions on τ³ with the spectral algebra of the algebraic lemniscate.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part04/ch20-dimension-fibration.tex -->
