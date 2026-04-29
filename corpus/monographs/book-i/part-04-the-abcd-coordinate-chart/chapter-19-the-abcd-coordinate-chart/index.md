---
layout: "corpus-monograph-chapter"
title: "Chapter 19: The ABCD Coordinate Chart"
permalink: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-19-the-abcd-coordinate-chart/"
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
chapter_number: 19
chapter_slug: "chapter-19-the-abcd-coordinate-chart"
page_in_book: 75
prev_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-18-the-normal-form-address-encoding/"
prev_chapter_title: "Chapter 18: The Normal-Form Address Encoding"
next_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-20-dimension-and-the-fibration-preview/"
next_chapter_title: "Chapter 20: Dimension and the Fibration Preview"
summary_short: "The ABCD chart assigns every object a canonical four-tuple (A,B,C,D). Total chart; A is a prime (pi-channel), B, C, D are integers in their respective channels."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
canonical_part_title: "The ABCD Coordinate Chart"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-04-the-abcd-coordinate-chart/chapter-19-the-abcd-coordinate-chart/"
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

Chapters 16–18 built the ingredients: internal primes, tower atoms, the greedy peel, and the normal-form address encoding. This chapter assembles them into the *ABCD coordinate chart* — a total map Φ : Obj(τ) → τ-Idx⁴ that assigns every object a canonical four-tuple of typed coordinates. The four coordinate functions are: coord_A(x) = largest prime divisor (π-channel), coord_B(x) = maximal exponent at tower level (γ-channel), coord_C(x) = maximal tetration height (η-channel), coord_D(x) = remainder after tower extraction (α-channel). The chart is entirely earned from the kernel axioms and ρ — no background manifold, vector space, or imported number theory was required. Uniqueness of the encoding (injectivity of Φ) is the Hyperfactorization Theorem of Part V; this chapter establishes totality only.

## What this chapter contributes

- Defines *I.D17* (ABCD Coordinate Chart): Φ(x) = (coord_A(x), coord_B(x), coord_C(x), coord_D(x)), lifting the NF encoding on τ-Idx to a map on all of Obj(τ) via the orbit-depth bijection (Chapter 10). Handles degenerate addresses for idx(x) ∈ {0̲, 1̲} by convention.
- Characterizes the typed coordinates: A ranges over ℙ_τ ∪ {1̲} (primes or degenerate), while B, C, D range over τ-Idx_≥0. The typing reflects the different roles of the four orbit channels, not merely notational convention.
- Proves that Φ is total: every x ∈ Obj(τ) has a well-defined ABCD address, following from the orbit-depth bijection of Chapter 10 and peel termination (Chapter 17).
- Articulates the 1+3 split: D is the *radial* coordinate (α-orbit, "bulk" or "mass"), while (A, B, C) are the *solenoidal triple* (π-, γ-, η-orbits, "angular" or "spectral" structure). This structural fact foreshadows the fibration τ³ = τ¹ ×_f T² — with base τ¹ governed by (D, A) and fiber T² by (B, C).
- Explains why the ABCD chart is earned rather than stipulated: the coordinates emerge from prime factorization and the tetration tower, both derived from the single operator ρ and the six kernel axioms. No background geometric space is assumed.
- Notes the token-set vs. tuple encoding duality: the extensional ABCD tuple and the intensional token-set (a multiset of typed prime factors) carry identical information, as the Hyperfactorization Theorem will confirm.
- Lean coverage: `TauLib.BookI.Coordinates.ABCD` (planned: coord_A/B/C/D, abcd_chart, abcd_total, abcd_typed).

## Lean coverage

`TauLib.BookI.Coordinates.ABCD` (planned)

## Where this leads

Chapter 20 proves the Dimension Theorem dim_τ = 4 — the four coordinates are pairwise independent and no three suffice — and introduces the full quadtree and Address DAG, giving three canonical metrics (spine length, occurrence size, DAG size) related by the metric inequality ℓ_spine ≤ ℓ_DAG ≤ ℓ_occ. Part V will then supply the missing uniqueness result: the Hyperfactorization Theorem.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part04/ch19-abcd-chart.tex -->
