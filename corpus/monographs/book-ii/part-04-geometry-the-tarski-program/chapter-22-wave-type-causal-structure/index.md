---
layout: "corpus-monograph-chapter"
title: "Chapter 22: Wave-Type Causal Structure"
permalink: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-22-wave-type-causal-structure/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-geometry-the-tarski-program"
chapter_number: 22
chapter_slug: "chapter-22-wave-type-causal-structure"
page_in_book: 101
prev_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-21-pasch-and-the-parallel-postulate/"
prev_chapter_title: "Chapter 21: Pasch and the Parallel Postulate"
next_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-23-orthodox-vs-tau-denotation-bridge/"
next_chapter_title: "Chapter 23: Orthodox vs.\\ τ Denotation Bridge"
summary_short: "The split-complex unit j with j² = +1 forces the wave equation rather than Laplace, giving τ³ a causal structure — null lines, a forward cone, and a B/C asymmetry that selects a preferred propagation direction. Euclidean geometry is the static limit when wave-type coupling vanishes."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
canonical_part_title: "Geometry: The Tarski Program"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-04-geometry-the-tarski-program/chapter-22-wave-type-causal-structure/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part IV: Geometry: The Tarski Program"
      url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part IV"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 23
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapters 19–21 earned the full Tarski axiom system for Euclidean geometry from the ultrametric structure of τ³ — betweenness, congruence, Pasch, and the parallel postulate, all without importing ℝ. But Euclidean geometry is *static*: it has O(n) symmetry, no preferred direction, and no notion of propagation or causal order. This chapter adds dynamics by attending to an algebraic fact that the Tarski program deliberately set aside. The codomain H_τ carries the split-complex unit j with j² = +1 (*I.T10*, Book I). A split-complex holomorphic function f = u + jv satisfies Cauchy–Riemann equations with a sign flip in the second equation: ∂u/∂y = +∂v/∂x rather than −∂v/∂x. That single sign flip changes the combined PDE from the Laplace equation (elliptic, no real characteristics) to the **wave equation** ∂²u/∂x² − ∂²u/∂y² = 0 (hyperbolic, two families of real characteristics). The wave equation is forced — j² = +1 is not a choice but a consequence of prime polarity (*I.T10*). No input from physics selects it.

## What this chapter contributes

Definition *II.D21* registers the wave-type PDE as the split-complex holomorphic condition on H_τ. The two characteristic families x + y = const and x − y = const are the null lines of the theory; in idempotent coordinates ξ = x + y, ζ = x − y, the equation diagonalizes to ∂²u/∂ξ∂ζ = 0, whose general solution F(ξ) + G(ζ) separates cleanly into two independent propagating channels.

Definition *II.D22* registers the causal structure on τ³. Three ingredients combine: (C1) the null directions from *II.D21*; (C2) the B/C asymmetry from prime polarity (*I.T05*), which places the exponent-coordinate (B) before the tetration-coordinate (C) in the peel-off hierarchy, selecting a preferred forward direction within each time-like sector; (C3) the resulting forward-directed partial order on null-line segments. Classical complex holomorphy (i² = −1) has no causal structure: the elliptic characteristic polynomial ξ² + η² = 0 has no real roots, and SO(2) rotational symmetry prevents any forward direction from being selected even formally.

Theorem *II.T19* establishes Euclidean geometry as the static limit: as the split-complex coupling vanishes (formally, as c → 0), the null cone collapses, the causal structure disappears, and the Tarski axioms *II.T15–II.T18* survive unchanged — they depend only on the ultrametric distance and cylinder structure, neither of which involves j. An additional proposition closes the compact-and-Euclidean puzzle: τ³ is simultaneously compact and satisfies the parallel postulate because j² = +1 gives profinite, flat compactification, while i² = −1 gives projective, positively curved compactification that destroys parallelism.

## Lean coverage

Lean coverage: *BookII.Geometry.CausalStructure* (planned). The wave equation derivation and the static-limit argument are algebraic. The causal ordering in *II.D22* depends on the B/C polarity ordering established in Book I.

## Where this leads

The causal structure earned here is the algebraic seed of spacetime. The forced 1 + 3 split of Chapter 17 (radial D direction plus three solenoidal ABC directions) now acquires dynamical content: D is time-like, ABC are space-like. In Book IV this becomes the 3 + 1 decomposition of Minkowski spacetime; the null cone becomes the physical light cone; the B/C asymmetry becomes the arrow of time. Chapter 23, the final chapter of Part IV, does not yet make those physical identifications — it instead constructs the denotation bridge showing how τ-internal geometry translates into classical ℝ⁴.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part04/ch21-wave-causal.tex -->
