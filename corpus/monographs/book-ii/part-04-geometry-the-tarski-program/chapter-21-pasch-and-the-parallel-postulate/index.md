---
layout: "corpus-monograph-chapter"
title: "Chapter 21: Pasch and the Parallel Postulate"
permalink: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-21-pasch-and-the-parallel-postulate/"
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
chapter_number: 21
chapter_slug: "chapter-21-pasch-and-the-parallel-postulate"
page_in_book: 97
prev_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-20-congruence-from-canonical-distance/"
prev_chapter_title: "Chapter 20: Congruence from Canonical Distance"
next_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-22-wave-type-causal-structure/"
next_chapter_title: "Chapter 22: Wave-Type Causal Structure"
summary_short: "The two hardest Tarski axioms — Pasch and the parallel postulate — are earned here as theorems, completing the full Tarski system for τ³ without importing ℝ, Dedekind completeness, or any continuity axiom."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
canonical_part_title: "Geometry: The Tarski Program"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-04-geometry-the-tarski-program/chapter-21-pasch-and-the-parallel-postulate/"
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

Chapters 19 and 20 earned betweenness (*II.D19*, *II.T15*) and congruence (*II.D20*, *II.T16*) from the ultrametric structure of τ³, accounting for nine of Tarski's thirteen axioms. This chapter tackles the two that make the system specifically Euclidean: the **Pasch axiom** — a line entering a triangle through one side must exit through another — and the **parallel postulate** — through a point not on a line, exactly one parallel exists. Most geometry books either assume these outright or prove them from the real continuum. Here both are *earned* without importing ℝ, Dedekind completeness, or any continuity axiom. A critical structural note: the parallel postulate *survives* τ's native compactification because the algebraic base is split-complex (j² = +1, hyperbolic), not classical complex (i² = −1, elliptic). The contrast matters: elliptic compactification wraps parallel directions into intersecting great circles; profinite compactification preserves cylinder separation at every stage.

## What this chapter contributes

Theorem *II.T17* proves Pasch. The proof reduces to cylinder containment: the isosceles ultrametric triangle property forces all five points (a, b, c, p, q) into a common stage-k₁ cylinder, and a CRT interpolation within that cylinder produces the required intersection point x with B(p,x,b) and B(q,x,a). In Archimedean geometry, Pasch requires the Jordan curve theorem or equivalent topological machinery; in the ultrametric setting the rigid isosceles structure does all the work combinatorially.

Theorem *II.T18* proves the parallel postulate. The argument runs in four steps: (1) Hausdorff separation at some stage k₁ places p outside the cylinder containing the line ℓ; (2) at each stage k ≥ k₁, the CRT decomposition Z/P_k ≅ ∏ Z/p_i gives a unique parallel in each prime-order affine factor; (3) coherence of the reduction maps forces compatibility across stages; (4) the inverse-limit assembly ℓ′ = lim ℓ_k′ is the unique parallel through p. Proposition *II.T18-compactification* isolates the reason the postulate survives compactification: j² = +1 gives profinite inverse-limit closure, which preserves disjointness; i² = −1 gives projective closure, which identifies all parallel directions at infinity and destroys the postulate.

With *II.T17* and *II.T18* in place, (τ³, B, ≅) is a full model of Tarski's complete, decidable first-order theory of Euclidean geometry — a consequence noted by a closing theorem collecting *II.T15–II.T18* into a single Tarski-completeness statement. Every first-order Euclidean theorem is now a theorem in τ.

## Lean coverage

Lean coverage: *TauLib.BookII.Geometry.PaschParallel* (planned). Both proofs are constructive: Pasch exhibits the interpolation point explicitly via CRT, and the parallel postulate builds the parallel by inverse-limit assembly. No excluded middle beyond the finite-stage decidability already present is needed.

## Where this leads

The Tarski program is complete. Chapter 22 shifts register: τ's geometry is static (no preferred direction, no causal order), but the split-complex unit j with j² = +1 forces a hyperbolic PDE — the wave equation, not Laplace — giving τ³ a causal structure. Euclidean geometry will reappear as the static limit. Chapter 23 then builds the denotation map from τ³ to ℝ⁴, showing that ℝ⁴ is the Archimedean shadow of τ's profinite tower rather than the ambient space that contains it.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part04/ch20-pasch-parallel.tex -->
