---
layout: "corpus-monograph-chapter"
title: "Chapter 10: The Ultrametric and First Disagreement Depth"
permalink: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-10-the-ultrametric-and-first-disagreement-depth/"
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
chapter_number: 10
chapter_slug: "chapter-10-the-ultrametric-and-first-disagreement-depth"
page_in_book: 47
prev_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-09-cylinder-domains-from-abcd-refinement/"
prev_chapter_title: "Chapter 9: Cylinder Domains from ABCD Refinement"
next_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-11-holomorphic-implies-continuous-the-inverted-dependency/"
next_chapter_title: "Chapter 11: Holomorphic Implies Continuous (The Inverted Dependency)"
summary_short: "The cylinder topology of Chapter 9 is metrized by recording the first CRT stage at which two points disagree. The resulting distance d(x,y) = 2^{−δ(x,y)} satisfies the strong ultrametric triangle inequality and identifies cylinders with ultrametric balls exactly."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/"
canonical_part_title: "Local Domains: Cylinders as Prefix Predicates"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-10-the-ultrametric-and-first-disagreement-depth/"
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

Chapter 9 built the clopen cylinder basis for τ³ from CRT prefix predicates — a combinatorial structure that specifies which sets are open without assigning numerical distances. This chapter metrizes that structure. The strategy is to compare two points stage by stage: record the last stage k at which their CRT reductions agree, then set d(x, y) = 2^{−δ(x,y)} where δ(x, y) is the **first disagreement depth**. The result is a canonical distance function, forced by the primorial tower without any free parameter — the base 2 is arbitrary and any λ > 1 gives an equivalent metric, but δ itself is canonical. The geometry that emerges is non-Archimedean in a strong sense: every triangle is isosceles with the two longest sides equal, the value set of d is the discrete set {0, 1, 1/2, 1/4, …}, and closeness between two points means depth of agreement through the CRT tower, not magnitude of a difference. Two key payoffs follow immediately. First, every stage-k cylinder C_k(x) is simultaneously the closed ball of radius 2^{−k} and the open ball of radius 2^{−(k−1)}: cylinders are exactly ultrametric balls, and every ball is clopen. Second, the metric space (τ³, d) is complete: any Cauchy sequence has stage reductions that stabilize, defining a coherent limit point in the inverse limit.

## What this chapter contributes

Definitions *II.D12* (first disagreement depth δ) and *II.D13* (ultrametric distance d = 2^{−δ}), Theorem *II.T05* (ultrametric triangle inequality: d(x,z) ≤ max(d(x,y), d(y,z))), and Proposition *II.P04* (cylinders are balls: C_k(x) = B̄(x, 2^{−k}) = B(x, 2^{−(k−1)})). The chapter also establishes completeness and previews compactness via the finite-branching of the cylinder tower. The non-Archimedean character is made explicit: closeness means depth of agreement, not magnitude of difference; all triangles in (τ³, d) are isosceles; the value set is discrete.

## Lean coverage

*TauLib.BookII.Domains.Ultrametric* (planned). The ultrametric triangle inequality is a short algebraic argument from monotonicity of agreement and should formalize readily. Completeness requires the inverse-limit universal property from Book I.

## Where this leads

The ultrametric formulation of Chapter 10 feeds Chapter 11's proof that ω-germ transformers are 1-Lipschitz — since tower coherence implies δ(f(x), f(y)) ≥ δ(x, y), so the distance can only decrease — hence uniformly continuous. The Hausdorff property (Chapter 13) and the constructive compactness argument (Chapter 13) both rely on the explicit metric structure. The canonical character of d — forced by the CRT tower, with δ uniquely determined and base choice immaterial — is the technical substrate for the Topology Uniqueness Theorem in Chapter 14, which proves that any topology satisfying CRT continuity, Hausdorff separation, and compactness must be exactly the cylinder topology.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part02/ch10-ultrametric-depth.tex -->
