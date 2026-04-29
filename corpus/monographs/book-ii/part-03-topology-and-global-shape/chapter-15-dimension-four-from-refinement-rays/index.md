---
layout: "corpus-monograph-chapter"
title: "Chapter 15: Dimension Four from Refinement Rays"
permalink: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/chapter-15-dimension-four-from-refinement-rays/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 3
part_display: "Part III"
part_slug: "part-03-topology-and-global-shape"
chapter_number: 15
chapter_slug: "chapter-15-dimension-four-from-refinement-rays"
page_in_book: 71
prev_chapter_url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/chapter-14-topology-as-invariant-of-canonical-denotation/"
prev_chapter_title: "Chapter 14: Topology as Invariant of Canonical Denotation"
next_chapter_url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/chapter-16-boundary-minimality-and-angular-sectors/"
next_chapter_title: "Chapter 16: Boundary Minimality and Angular Sectors"
summary_short: "Classical covering dimension returns zero for τ³ because the space is totally disconnected. This chapter introduces τ-dimension — counting independent refinement rays whose joint cylinders separate all points — and proves dim_τ = 4, with a forced 1+3 radial–solenoidal split."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/"
canonical_part_title: "Topology and Global Shape"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-03-topology-and-global-shape/chapter-15-dimension-four-from-refinement-rays/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part III: Topology and Global Shape"
      url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part III"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 22
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Classical covering dimension, inductive dimension, and Hausdorff dimension all return zero for τ³, because every totally disconnected space has covering dimension zero. Yet τ³ requires four coordinates to specify a point, and those coordinates are pairwise independent (*I.P08*, Book I). The resolution is that classical dimensions measure the size of continuous neighborhoods, while τ³'s neighborhoods are clopen atoms (stage-k cylinders, *II.D10*) — the correct invariant counts *independent refinement directions* instead. The four ABCD rays — D (radial depth, α-orbit), A (prime label, π-orbit), B (exponent, γ-orbit), C (tetration height, η-orbit) — provide four one-parameter families of single-coordinate constraints. Each ray is pairwise independent of the other three by the Dimension Theorem (*I.P08*), and the four rays are jointly complete by the Hyperfactorization Theorem (*I.T04*): two points with identical ABCD coordinates at every stage are the same point. No three rays suffice to separate all points: for each of the four possible triples, the missing coordinate is independent of the remaining three, so there exist distinct points that agree on all three selected coordinates at every stage but differ on the fourth. Each triple therefore fails to separate some pair, disqualifying every triple and establishing the lower bound dim_τ ≥ 4.

## What this chapter contributes

Definition *II.D15* (τ-dimension: the minimal number of independent refinement rays whose joint cylinders separate all points), Theorem *II.T11* (dim_τ = 4: upper bound from completeness of ABCD chart, lower bound from pairwise independence), and Definition *II.D16* (radial–solenoidal split: 4 = 1 + 3, where D is radial and A, B, C are solenoidal). The 1+3 split is forced — not conventional — by three asymmetries: D ranges over [0, P_k) (super-exponentially growing) while A, B, C are bounded by p_k; constraint (C3) couples D to A but not B to C; and the D-ray uniquely parametrizes distance from ω while the solenoidal rays parametrize angular position within a depth shell. No automorphism of τ³ maps the radial direction to a solenoidal direction.

## Lean coverage

*TauLib.BookII.Topology.DimensionFour* (planned). The lower bound from pairwise independence is the key target; it inherits directly from Book I's Dimension Theorem (*I.P08*).

## Where this leads

The 1+3 split reappears in Book IV as the 3+1 decomposition of spacetime: three spatial dimensions from the solenoidal coordinates (A, B, C) and one temporal dimension from the radial coordinate (D). The reversal of notation (1+3 here, 3+1 there) reflects perspective — Book II starts from the boundary and moves inward; Book IV starts from the spatial arena and adjoins time — but the underlying structure is identical. The forced asymmetry between D and (A, B, C) is therefore not merely a feature of τ's algebra; it prefigures the structure of physical spacetime as a consequence of the normal-form combinatorics established in Book I.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part03/ch15-dimension-four.tex -->
