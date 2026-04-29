---
layout: "corpus-monograph-chapter"
title: "Chapter 46: Functoriality as Diagram Commutativity"
permalink: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-46-functoriality-as-diagram-commutativity/"
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
chapter_number: 46
chapter_slug: "chapter-46-functoriality-as-diagram-commutativity"
page_in_book: 235
prev_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-45-automorphic-galois-duality/"
prev_chapter_title: "Chapter 45: Automorphic–Galois Duality"
next_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-47-the-enriched-bi-square/"
next_chapter_title: "Chapter 47: The Enriched Bi-Square"
summary_short: "The Functoriality Theorem (*III.T36*) is full enriched bi-square commutativity; RH = one column, GRH = all columns, Langlands = columns plus horizontal maps; base change and transfer are naturality (*III.T37*)."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/"
canonical_part_title: "The Arithmetic Mirror"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-06-the-arithmetic-mirror/chapter-46-functoriality-as-diagram-commutativity/"
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

Chapter 45 established the automorphic–Galois duality (*III.D63*) and the local Langlands instances (*III.D64*), providing the vertical maps in the enriched bi-square. This chapter establishes the horizontal maps: the sector morphisms between primitive sectors. The central result is the Functoriality Theorem (*III.T36*), which asserts that every sector morphism commutes with the automorphic–Galois duality. The argument proceeds through a three-stage scaling: the Riemann Hypothesis corresponds to commutativity of a single column (the B-sector column); the Grand Riemann Hypothesis corresponds to commutativity of all four columns; and Langlands functoriality is commutativity of the entire pasted diagram — columns plus horizontal maps. Two key instances, base change and transfer, are shown to be naturality conditions on the enriched bi-square (*III.T37*).

## What this chapter contributes

The Functoriality Theorem (*III.T36*) proves that every sector morphism f: S → S' in the enriched bi-square commutes with the automorphic–Galois duality — that is, the diagram (Galois data on S) → (automorphic data on S) → (automorphic data on S') commutes with (Galois data on S) → (Galois data on S') → (automorphic data on S'). The proof applies Mutual Determination (*III.D25*) sector by sector, transported through the enrichment functor Enr₀₁ (*III.D57*): each sector morphism is a morphism of Mutual Determination instances, and Mutual Determination instances compose by the bi-square pasting lemma proved in Book I (*I.T41*). The commutativity of each sector column is verified by explicit NF-computation at the first three primorial depths.

The three-stage scaling argument makes the relationship between the Langlands programme and classical conjectures precise within τ. The Riemann Hypothesis at E₁ is the statement that the B-sector (EM) column of the enriched bi-square commutes — equivalently, that the spectral determinant of the B-sector has all its zeros on the critical line of the τ-L-function. The Grand Riemann Hypothesis is the statement that all four primitive sector columns commute simultaneously. Full Langlands functoriality is the statement that the horizontal sector morphisms are also natural — that the entire pasted diagram commutes. Each level is a strictly stronger statement, and each is τ-effective; the conjectural identification with the classical RH, GRH, and Langlands functoriality for GL_n over a number field is deferred to Part X.

The Base Change–Transfer Naturality Theorem (*III.T37*) shows that the two most important sector morphisms in the classical Langlands programme — base change (extending the ground field) and transfer (changing the reductive group) — correspond exactly to horizontal natural transformations in the enriched bi-square. Base change is the tensor product with a primorial extension; transfer is the composition of two sector projections. Both are verified to satisfy the naturality square at each primorial depth, confirming that the τ-internal Langlands functoriality is structurally complete: the bi-square pasting lemma, Mutual Determination, and the enrichment functor together suffice, with no additional structure required.

## Lean coverage

- *III.T36* — Functoriality Theorem (τ-effective)
- *III.T37* — Base Change–Transfer Naturality (τ-effective)

## Where this leads

Chapter 47 assembles the enriched bi-square as the third object in the scaling chain (algebraic *I.T41* → topological *II.T49* → enriched *III.D65*) and proves the Finite Factorization Pasting Lemma (*III.T38*) and the Enriched Bi-Square Comparison Theorem (*III.T39*), crowning Part VI.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part06/ch49-functoriality-as-diagram-commutativity.tex -->
