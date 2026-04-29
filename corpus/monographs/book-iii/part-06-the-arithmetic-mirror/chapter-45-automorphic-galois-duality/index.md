---
layout: "corpus-monograph-chapter"
title: "Chapter 45: Automorphic–Galois Duality"
permalink: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-45-automorphic-galois-duality/"
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
chapter_number: 45
chapter_slug: "chapter-45-automorphic-galois-duality"
page_in_book: 229
prev_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-44-the-bsd-coherence-theorem/"
prev_chapter_title: "Chapter 44: The BSD Coherence Theorem"
next_chapter_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-46-functoriality-as-diagram-commutativity/"
next_chapter_title: "Chapter 46: Functoriality as Diagram Commutativity"
summary_short: "The m-axis (Galois) and n-axis (automorphic) of ℤ² differentiate at E₁; automorphic–Galois duality (*III.D63*) is Mutual Determination on ℤ² (*III.P28*), with local instances (*III.D64*) prime by prime."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/"
canonical_part_title: "The Arithmetic Mirror"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-06-the-arithmetic-mirror/chapter-45-automorphic-galois-duality/"
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

This chapter opens the Langlands block by identifying the stage on which the Langlands programme plays out in Category τ. The character lattice ℤ² from the 4+1 sector decomposition carries two natural axes: the m-axis (Galois/arithmetic, decomposing prime by prime via the CRT) and the n-axis (automorphic/spectral, decomposing eigenvalue by eigenvalue via the spectral trichotomy). At E₀ both axes carry identical algebraic structure; at E₁ they differentiate — the m-axis acquires arithmetic content and the n-axis acquires spectral content. We define the automorphic–Galois duality (*III.D63*), construct local Langlands instances (*III.D64*) at each prime, build the Euler product as the CRT decomposition of the spectral determinant, and prove that the duality in Category τ is an instance of Mutual Determination on ℤ² (*III.P28*).

## What this chapter contributes

The automorphic–Galois duality (*III.D63*) is defined as the E₁ enrichment of the identity automorphism on ℤ²: at E₀ the swap (m,n) ↦ (n,m) is a self-map of the character ring; at E₁ the swap carries arithmetic content on the m-axis and spectral content on the n-axis, and the two sides of the swap are no longer algebraically equivalent. The duality is not an involution at E₁ — it is a Mutual Determination, with each side reconstructing the other through the spectral trichotomy. This is the τ-internal formulation of the Langlands correspondence: the m-axis data (Galois representations, encoded as primorial CRT components) determines the n-axis data (automorphic forms, encoded as sector eigenvalue sequences), and vice versa.

The local Langlands instance (*III.D64*) at a prime p is the restriction of the duality to the p-component of the CRT decomposition ℤ² ≅ ∏_p (ℤ/pℤ)². At each prime p, the local instance is a Mutual Determination between the Galois module (ℤ/pℤ acting on the m-coordinate via Frobenius-like map) and the automorphic module (ℤ/pℤ acting on the n-coordinate via sector Label_n stabilisation). The local instances are computed explicitly at p = 2, 3, and 5, corresponding to primorial depths Prim(1), Prim(2), and Prim(3). In each case the local duality is verified to be a bijection at the level of isomorphism classes, confirming the local-global compatibility that the Euler product requires.

The Duality as Mutual Determination Proposition (*III.P28*) proves that the global automorphic–Galois duality is the Mutual Determination instance obtained by taking the Euler product of all local instances over the full primorial tower. The proof proceeds by CRT: the global character (m,n) ∈ ℤ² determines all local components (m mod p, n mod p) at each prime p, and the Mutual Determination at each prime assembles into a global Mutual Determination by the primorial cofinality theorem (*III.T09*). The result is τ-effective; the conjectural identification of the local instances with classical local Langlands correspondences for GL_n is deferred to Part X.

## Lean coverage

- *III.D63* — Automorphic–Galois Duality (τ-effective)
- *III.D64* — Local Langlands Instance (τ-effective)
- *III.P28* — Duality as Mutual Determination (τ-effective)

## Where this leads

Chapter 46 proves that the global Langlands functoriality — base change, automorphic induction, and transfer — corresponds exactly to commutativity of diagram squares in the enriched bi-square. The local instances defined here are the building blocks for that commutativity argument.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part06/ch48-automorphic-galois-duality.tex -->
