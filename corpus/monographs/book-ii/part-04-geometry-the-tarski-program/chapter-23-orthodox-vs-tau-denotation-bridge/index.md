---
layout: "corpus-monograph-chapter"
title: "Chapter 23: Orthodox vs.\\ τ Denotation Bridge"
permalink: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-23-orthodox-vs-tau-denotation-bridge/"
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
chapter_number: 23
chapter_slug: "chapter-23-orthodox-vs-tau-denotation-bridge"
page_in_book: 107
prev_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-22-wave-type-causal-structure/"
prev_chapter_title: "Chapter 22: Wave-Type Causal Structure"
next_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-24-lines-from-countable-structure/"
next_chapter_title: "Chapter 24: Lines from Countable Structure"
summary_short: "Parts III and IV earned Euclidean geometry entirely within τ. This chapter constructs the denotation map den : τ³ → ℝ⁴ — continuous, injective on finite points, axiom-preserving — showing that ℝ⁴ is the Archimedean *shadow* of τ's profinite tower, not an ambient space that contains it."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
canonical_part_title: "Geometry: The Tarski Program"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-04-geometry-the-tarski-program/chapter-23-orthodox-vs-tau-denotation-bridge/"
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

Parts III and IV have earned Euclidean geometry from purely discrete, profinite foundations: Stone space structure (*II.D14*), four-dimensionality (*II.T11*), betweenness (*II.T15*), congruence (*II.T16*), Pasch (*II.T17*), the parallel postulate (*II.T18*), and wave-type causal structure with the Euclidean static limit (*II.T19*). All of it was internal to τ — no real numbers, no classical continuum, no ambient Euclidean space. But classical mathematics, physics, and engineering work in ℝ⁴. This chapter constructs the **denotation map** den : τ³ → ℝ⁴ that bridges the two worlds. The map sends each τ-admissible point to the Euclidean limit of its stage-k approximation sequence — rational approximants with primorial denominators converging in the standard metric of ℝ⁴. The result is continuous, injective on finite points, and preserves betweenness and congruence. The key philosophical reversal: ℝ⁴ appears as the *limit* of τ-approximations, not as an ambient space that contains τ³. τ does not sit inside ℝ⁴; ℝ⁴ is the classical shadow of τ³.

## What this chapter contributes

Definition *II.D23* registers the approximation sequence: for a τ-admissible point x, the normalized stage-k ABCD coordinates app_k(x) = (D_k(x)/P_k, A_k(x)/P_k, B_k(x)/P_k, C_k(x)/P_k) ∈ [0,1)⁴ form a Cauchy sequence in ℝ⁴, as the tower coherence condition bounds each coordinate step by 1/P_k → 0. The **denotation map** den(x) = lim_{k→∞} app_k(x) is then well-defined by completeness of ℝ⁴.

Remark *II.R07* characterizes the orthodox denotation bridge: the map is *orthodox* in output (producing standard Euclidean geometry) but non-orthodox in derivation (starting from discrete profinite data). Continuity of den is proved directly — d(x,y) ≤ 2^{−K} implies π_K(x) = π_K(y) implies app_K(x) = app_K(y) — so two τ-points that agree to depth K have images within 4/P_K of each other in ℝ⁴. Injectivity on finite points follows from Hyperfactorization uniqueness: if x ≠ y then some finite stage separates them, and the normalized coordinates inherit the gap. For profinite limit points, injectivity may fail — distinct inverse-limit elements can converge to the same classical point, mirroring the p-adic situation — so den is a continuous surjection onto a dense subset of [0,1)⁴, not a homeomorphism. The axiom preservation proposition confirms that τ-betweenness implies classical betweenness and τ-congruence implies classical congruence under den; Tarski's representation theorem then guarantees the abstract isomorphism between the two Euclidean structures.

The chapter closes by addressing the apparent circularity: if den uses ℝ⁴ as its target, doesn't τ depend on ℝ? The answer is no. τ³ is complete in its own ultrametric — every ultrametric Cauchy sequence already converges within τ³ by compactness (*II.T07*). τ³ has its own geometry (*II.T15–II.T18*). ℝ appears as a theorem (the image of den), not as an axiom.

## Lean coverage

Lean coverage: *BookII.Geometry.OrthodoxBridge* (planned). The Cauchy property of approximation sequences and the continuity of den are straightforward from tower coherence. Axiom preservation requires connecting the ultrametric depth ordering to standard Euclidean coordinate ordering.

## Where this leads

The denotation bridge closes Part IV and sets up Part V. The map den is currently structural — it produces well-defined images in ℝ⁴ but cannot yet compute them to arbitrary precision, because the transcendental constants π, e, and ι_τ have not yet been earned. Part V earns those constants: the real line as an inverse limit of α-ray segments, the circle S¹ as a profinite solenoidal limit, and π, e, ι_τ = 2/(π + e) as calibration outputs. Once calibrated, den becomes a concrete coordinate atlas that connects τ-geometry to the numerical values used throughout classical physics and applied mathematics.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part04/ch22-orthodox-bridge.tex -->
