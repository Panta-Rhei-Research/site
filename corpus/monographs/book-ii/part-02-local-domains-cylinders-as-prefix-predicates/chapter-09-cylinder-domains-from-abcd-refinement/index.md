---
layout: "corpus-monograph-chapter"
title: "Chapter 9: Cylinder Domains from ABCD Refinement"
permalink: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-09-cylinder-domains-from-abcd-refinement/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 2
part_display: "Part II"
part_slug: "part-02-local-domains-cylinders-as-prefix-predicates"
chapter_number: 9
chapter_slug: "chapter-09-cylinder-domains-from-abcd-refinement"
page_in_book: 41
prev_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-08-abcd-structure-replaces-quaternions/"
prev_chapter_title: "Chapter 8: ABCD Structure Replaces Quaternions"
next_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-10-the-ultrametric-and-first-disagreement-depth/"
next_chapter_title: "Chapter 10: The Ultrametric and First Disagreement Depth"
summary_short: "Using the CRT reduction maps inherited from Book I, this chapter builds local domains on τ³ by defining stage-k cylinders as prefix predicates — clopen sets of points sharing the same primorial residue — and proves the Cylinder Basis Theorem."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/"
canonical_part_title: "Local Domains: Cylinders as Prefix Predicates"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-09-cylinder-domains-from-abcd-refinement/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part II: Local Domains: Cylinders as Prefix Predicates"
      url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part II"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 21
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

The point set τ³ was established in Part I as the collection of τ-admissible ABCD quadruples completed by the profinite inverse limit. This chapter builds *local domains* on τ³ using the CRT reduction maps π_k : τ³ → ℤ/P_k that Book I's Chinese Remainder Theorem provides. The key construction: a **stage-k cylinder** is the preimage of a single residue class under π_k — the set of all points agreeing with a given point modulo the k-th primorial P_k. This is the *prefix predicate* interpretation: two points share a stage-k cylinder if and only if their first k prime reductions coincide. Every point is a center of any cylinder it belongs to, a fact that follows from symmetry of the equivalence relation π_k(y) = π_k(x) and foreshadows the ultrametric geometry of Chapter 10. Cylinders decompose along the four ABCD coordinates, are simultaneously open and closed, and form a basis for a topology on τ³. Crucially, this topology is not chosen — it is the unique topology making all reduction maps continuous. No metric is used; no holomorphy is invoked. The construction uses only the CRT structure and the normal-form coordinates inherited from Book I.

## What this chapter contributes

Definitions *II.D09* (cylinder domain), *II.D10* (stage-k cylinder), and *II.D11* (clopen basis), together with Theorem *II.T04* (Cylinder Basis Theorem). The theorem proves five properties of the collection 𝒷 = {C_k(x)}: it covers τ³, is closed under intersection refinement, consists entirely of clopen sets, is second countable, and coincides with the profinite inverse-limit topology. A key structural result is the fibered cylinder decomposition: the fiber coordinates (B, C) vary independently (Cartesian), while the base coordinates (D, A) are coupled by constraint (C3), making cylinders fibered products rather than simple Cartesian products. The chapter also establishes Hausdorff separation by showing that the intersection ∩_k C_k(x) = {x} for every point, finite or limit.

## Lean coverage

*TauLib.BookII.Domains.Cylinders* (planned). The clopen property and the basis axioms are expected to be the first formal targets. The fibered decomposition likely requires prior formalization of the ABCD constraint lattice from Book I.

## Where this leads

The cylinder basis established here is the input to Chapter 10, which metrizes it via the first disagreement depth, yielding an ultrametric in which cylinders are precisely ultrametric balls and every ball is simultaneously open and closed. Chapter 11 uses cylinder compatibility — the lemma that ω-germ transformers map C_k(x) into C_k(f(x)) — to prove holomorphic implies continuous. Chapter 12 then pauses to record that the split-complex algebra H_τ, despite being available from Book I, plays no role in Parts I–II; this deliberate restraint is the inverted dependency chain at work. Part III lifts these local domain results to the global topology of τ³ as a compact, Hausdorff, totally disconnected Stone space, with uniqueness of the topology established in Chapter 14.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part02/ch09-cylinder-domains.tex -->
