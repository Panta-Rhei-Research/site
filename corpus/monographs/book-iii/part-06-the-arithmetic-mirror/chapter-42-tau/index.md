---
layout: "corpus-monograph-chapter"
title: "Chapter 42: τ"
permalink: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-42-tau/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-the-arithmetic-mirror"
chapter_number: 42
chapter_slug: "chapter-42-tau"
page_in_book: 211
prev_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-41-enrichment-from-0/"
prev_chapter_title: "Chapter 41: Enrichment from 0"
next_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-43-proto-codes-and-the-bsd-bridgehead/"
next_chapter_title: "Chapter 43: Proto-Codes and the BSD Bridgehead"
summary_short: "τ-rational interior points (*III.D59*) are finitely-stabilising rational addresses in the profinite tower; rank as tower depth (*III.D60*) and the Mordell–Weil analogue (*III.P25*) anchor the BSD bridgehead."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/"
canonical_part_title: "The Arithmetic Mirror"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-06-the-arithmetic-mirror/chapter-42-tau/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part VI: The Arithmetic Mirror"
      url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part VI"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 37
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

With the enrichment functor Enr₀₁ in place (Chapter 41), this chapter identifies the objects that live at the interface between the discrete E₀ tower and the continuous E₁ landscape: the τ-rational interior points. These are addresses in the profinite completion ℤ_τ that stabilise at finite primorial depth and whose ABCD sector coordinates are all rational. The stabilisation condition makes them finitely describable; the rationality condition makes them arithmetically transparent. Together, the two conditions carve out a countable, discrete subset of the continuous enrichment landscape — the substrate on which the BSD bridgehead and the Langlands programme will be erected. We define rank as tower depth and prove a Mordell–Weil analogue: at each primorial level the group of τ-rational points is finitely generated, the rank function is non-decreasing and bounded, and it stabilises at finite depth.

## What this chapter contributes

A τ-rational point (*III.D59*) is an element of the profinite completion ℤ_τ = lim ℤ/Prim(k)ℤ satisfying two conditions: sector-rationality (each ABCD coordinate lies in ℚ when the profinite limit is viewed through the E₁ tensor structure) and finite-depth stabilisation (there exists k₀ such that the image of the point in ℤ/Prim(k)ℤ is constant for all k ≥ k₀). The definition is τ-internal — it does not reference elliptic curves or abelian varieties. The conjectural identification of τ-rational points with rational points on associated abelian varieties is deferred to Part X.

Rank as tower depth (*III.D60*) defines the τ-rank of a set of τ-rational points as the minimal primorial depth k at which the group structure of those points stabilises — that is, at which no new independent points appear at level k+1. This discrete definition mirrors the Mordell–Weil rank of a finitely generated abelian group without requiring the ambient algebraic geometry. The τ-rank is non-negative, integer-valued, and bounded above by the number of primitive sectors (four for ABCD), so τ-rank ≤ 4 for any single sector.

The Mordell–Weil Analogue (*III.P25*) proves three properties of the τ-rational point group at each primorial level: (a) finite generation — the group of τ-rational points at depth k is a finitely generated abelian group of rank at most 4·log Prim(k); (b) monotonicity — the rank at depth k+1 is at least the rank at depth k; (c) stabilisation — there exists a finite depth k* beyond which no new independent τ-rational points appear. Stabilisation follows from the NF discreteness established in Part V (*III.P16*): only finitely many configurations are inequivalent at each depth, so the rank-growth sequence is eventually constant. The proposition is τ-effective; it does not settle the Birch and Swinnerton-Dyer conjecture for any classical elliptic curve.

## Lean coverage

- *III.D59* — τ-Rational Point (τ-effective)
- *III.D60* — Rank as Tower Depth (τ-effective)
- *III.P25* — Mordell–Weil Analogue (τ-effective)

## Where this leads

Chapter 43 introduces proto-codes — E₁ objects with a discrete carrier and a self-verification property but no decoder — and uses the τ-rational point group as the carrier set for the BSD functional. The rank-stabilisation result (*III.P25*) is the input that Chapter 44 elevates to the BSD Coherence Theorem.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part06/ch45-tau-rational-interior-points.tex -->
