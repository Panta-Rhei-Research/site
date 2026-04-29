---
layout: "corpus-monograph-chapter"
title: "Chapter 6: The τ³ Fibration Emerges"
permalink: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-06-the-tau-fibration-emerges/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-interior-points-and-the-tau"
chapter_number: 6
chapter_slug: "chapter-06-the-tau-fibration-emerges"
page_in_book: 27
prev_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-05-the-omega-readout-and-the-lemniscate/"
prev_chapter_title: "Chapter 5: The Omega Readout and the Lemniscate"
next_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-07-bipolar-decomposition-of-interior-points/"
next_chapter_title: "Chapter 7: Bipolar Decomposition of Interior Points"
summary_short: "The peel-order asymmetry of the ABCD chart forces a fibered product rather than a Cartesian factorization: the outer coordinate pair (D, A) forms the base τ¹ and the inner pair (B, C) forms the fiber T², coupled by the constraint that prime factors of D are bounded by A."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
canonical_part_title: "Interior Points and the τ³"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-01-interior-points-and-the-tau/chapter-06-the-tau-fibration-emerges/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part I: Interior Points and the τ³"
      url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part I"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 20
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

The ABCD chart assigns four coordinates to each τ-object, but the four coordinates are not symmetric: the peel-order asymmetry of the greedy hyperfactorization (*I.T04*) creates a structural split between the outer pair (D, A) and the inner pair (B, C). This chapter assembles that split into the fibered product τ³ = τ¹ ×_f T². The outer coordinates form the **base** τ¹ — a two-dimensional number-theoretic space where D records radial depth (prime power cofactor) and A records prime direction (the leading prime). The inner coordinates form the **fiber** T² — a two-dimensional parameter space where B records exponent height (γ-orbit) and C records tetration depth (η-orbit). The product is not Cartesian: the constraint "prime factors of D are strictly less than A" couples the base, and the admissible fiber range over each base point varies with A, giving a genuine fibration structure. The chapter closes with an ontological reframe: τ³ is τ viewed through its coordinate chart; neither τ¹ nor T² exists as an independent category.

## What this chapter contributes

- **Definition *II.D05* — Base τ¹:** the two-dimensional number-theoretic space {(D, A) : D ∈ ℕ≥1, A ∈ ℙ_τ, prime factors of D < A}, carrying the peel-order constraint as an internal validity condition, not a dimension reduction.
- **Definition *II.D06* — Fiber T²:** the two-dimensional parameter space {(B, C) : B ∈ ℕ≥0, C ∈ ℕ≥0}, where B records the γ-orbit (exponent) and C records the η-orbit (tetration height). Notation T² anticipates the torus-like structure earned in Part III; at this stage T² is purely a parameter space.
- **Definition *II.D07* — Fibered product τ³ = τ¹ ×_f T²:** the full interior {(D, A, B, C) : (D, A) ∈ τ¹, (B, C) ∈ T²_(D,A)}, with the projection pr : τ³ → τ¹ forgetting fiber coordinates. The subscript notation T²_(D,A) makes explicit that the admissible fiber depends on the base point.
- **Theorem *II.T03* — Fibration structure:** pr is surjective, fibers vary across base points (fiber geometry depends on the prime A), no global trivialization τ³ ≅ τ¹ × T² exists, and the map Φ : Obj(τ) → τ³ is injective by Hyperfactorization (*I.T04*). The fiber degeneration at ω — the two-dimensional T² pinching to one-dimensional 𝕃 — is confirmed as the structural test of the fibration's compatibility with the bipolar boundary.

## Lean coverage

No Lean module is claimed for this chapter. Definitions *II.D05*–*II.D07* and *II.T03* are planned in `TauLib.BookII.Interior.Fibration`. Surjectivity of pr and faithfulness reduce to Hyperfactorization, already in `TauLib.BookI`.

## Where this leads

Chapter 7 (Bipolar Decomposition of Interior Points) asks whether the bipolar idempotents e± = (1 ± j)/2, earned as boundary structure on 𝕃 in Book I, can be extended from the boundary to every point of the interior τ³ — and shows the answer is yes, via the fiber coordinates (B, C).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part01/ch06-tau3-fibration.tex -->
