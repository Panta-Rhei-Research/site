---
layout: "corpus-monograph-chapter"
title: "Chapter 44: The BSD Coherence Theorem"
permalink: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-44-the-bsd-coherence-theorem/"
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
chapter_number: 44
chapter_slug: "chapter-44-the-bsd-coherence-theorem"
page_in_book: 223
prev_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-43-proto-codes-and-the-bsd-bridgehead/"
prev_chapter_title: "Chapter 43: Proto-Codes and the BSD Bridgehead"
next_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-45-automorphic-galois-duality/"
next_chapter_title: "Chapter 45: Automorphic–Galois Duality"
summary_short: "The BSD Coherence Theorem (*III.T35*) proves τ-rank r∞ = ord_{s=1} L_τ(s) via three ingredients: rank stabilisation, L-value stabilisation, and E₁ Mutual Determination equality. Scope is τ-effective, not Clay-valid."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/"
canonical_part_title: "The Arithmetic Mirror"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-06-the-arithmetic-mirror/chapter-44-the-bsd-coherence-theorem/"
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

Chapters 42 and 43 assembled the two sides of the BSD equation: the algebraic side (τ-rational points, rank function r(k), Mordell–Weil analogue) and the analytic side (proto-codes, the BSD functional BSD_τ(k), spectral determinant L_τ(s,k)). This chapter proves that the two sides agree. The BSD Coherence Theorem (*III.T35*) states that for every τ-admissible elliptic datum — an E₁ object equipped with proto-code structure — the BSD functional stabilises at finite primorial depth, and its stable value equals the τ-rank of the τ-rational point group. The proof rests on three ingredients isolated in *III.P27*: rank stabilisation from the Mordell–Weil analogue, L-value stabilisation from spectral determinant tower coherence, and equality from the E₁ Mutual Determination instance. The chapter closes with BSD export contracts (*III.R25*) specifying what downstream chapters inherit.

## What this chapter contributes

The BSD Three-Ingredient Proof (*III.P27*) isolates the logical structure of the theorem before the theorem itself is stated. Ingredient (i) is rank stabilisation: by the Mordell–Weil analogue (*III.P25*), the τ-rank r(k) is non-decreasing and eventually constant, converging to a finite limit r∞. Ingredient (ii) is L-value stabilisation: the spectral determinant L_τ(s,k) is defined as the Euler product over the primorial tower, and its order of vanishing at s = 1 stabilises to a finite value n∞ at the same primorial depth as r(k), because both quantities are controlled by the same NF-discreteness bound (*III.P16*). Ingredient (iii) is equality: the E₁ Mutual Determination instance (*III.D58*) — applied to the τ-admissible elliptic datum — forces r∞ = n∞, because the boundary data (proto-code density) determines the spectral structure (L-function zero order) and conversely. Each ingredient is τ-effective and verified by explicit finite primorial computation.

The BSD Coherence Theorem (*III.T35*) assembles the three ingredients: for every τ-admissible elliptic datum, τ-rank r∞ = ord_{s=1} L_τ(s). The proof is τ-internal. Three scope declarations are given immediately after the theorem statement: (a) the τ-L-function L_τ(s) is the spectral determinant of the E₁ enrichment, not the Hasse–Weil L-function of a classical elliptic curve over ℚ; (b) the equality r∞ = ord_{s=1} L_τ(s) is proved for τ-admissible elliptic data, not for all elliptic curves over ℚ; and (c) the conjectural identification of the τ-L-function with the classical L-function, which would allow the theorem to imply the Clay BSD conjecture, is deferred to Part X.

The BSD export contracts (*III.R25*) state five deliverables: the τ-rank as a finite computable integer, the equality result, the proto-code carrier structure, the BSD functional as a tower-coherent measure, and the Mutual Determination framing that Chapters 45–47 consume.

## Lean coverage

- *III.T35* — BSD Coherence Theorem (τ-effective)
- *III.P27* — BSD Three-Ingredient Proof (τ-effective)
- *III.R25* — BSD Export Contracts

## Where this leads

Chapter 45 opens the Langlands block by casting automorphic–Galois duality as Mutual Determination on ℤ²: the m-axis carries Galois data and the n-axis carries automorphic data, and the duality is a single E₁ enrichment step. The BSD export contracts are binding inputs for Chapter 47's enriched bi-square.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part06/ch47-the-bsd-coherence-theorem.tex -->
