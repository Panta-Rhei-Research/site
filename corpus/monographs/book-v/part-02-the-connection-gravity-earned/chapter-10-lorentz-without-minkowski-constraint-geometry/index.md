---
layout: "corpus-monograph-chapter"
title: "Chapter 10: Lorentz Without Minkowski: Constraint Geometry"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-10-lorentz-without-minkowski-constraint-geometry/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 2
part_display: "Part II"
part_slug: "part-02-the-connection-gravity-earned"
chapter_number: 10
chapter_slug: "chapter-10-lorentz-without-minkowski-constraint-geometry"
page_in_book: 67
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-09-the-frame-holonomy-sector-gravity-as-canonical-gap/"
prev_chapter_title: "Chapter 9: The Frame Holonomy Sector: Gravity as Canonical Gap"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-11-the-tau-einstein-equation-boundary-character-equality/"
next_chapter_title: "Chapter 11: The τ-Einstein Equation: Boundary-Character Equality"
summary_short: "Lorentz covariance is not a postulate about spacetime geometry in the τ-framework — it is a theorem about the admissible readout functors from H_∂[ω]. The Minkowski metric appears as a chart shadow of the τ³ fibration, and null intertwiners define the light cone without any prior notion of spacetime."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-10-lorentz-without-minkowski-constraint-geometry/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part II: The Connection: Gravity Earned"
      url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part II"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 53
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Orthodox special relativity derives the Lorentz group from two postulates — the principle of relativity and the constancy of the speed of light — and takes Minkowski spacetime as the ontological substrate of physics. This chapter shows that neither postulate is needed. The Lorentz group O(1,3) emerges as a *theorem* about which readout functors from the boundary holonomy algebra H_∂[ω] are admissible: a readout transformation is Lorentz if and only if it preserves the norm structure of ω-germs under the τ³ fibration constraint. The Minkowski metric is not a fundamental object; it is a chart shadow — a convenient coordinate expression of the deeper fibered structure τ³ = τ¹ ×_f T². Null intertwiners, the τ-native objects corresponding to photons, satisfy ‖pr_D‖² = ‖pr_fiber‖², which defines the light cone algebraically. The speed barrier c is not a postulate about propagation in space but the condition of constraint saturation: an intertwiner that exhausts the full D-sector capacity moves at c as a consequence of the algebra.

## What this chapter contributes

**Definitions and axioms**

- This chapter introduces no new registry-numbered definitions; its core result is a structural theorem derived from the fibration constraints established in Book III.
- *Null intertwiner*: an H_∂[ω] element satisfying ‖pr_D‖² = ‖pr_fiber‖²; the τ-native formulation of a massless carrier
- *Chart shadow*: the image of a τ-native ω-germ under a local readout functor; Minkowski metric is the chart shadow of the τ³ null structure

**Key results**

- Lorentz covariance theorem: the group of admissible readout transformations of H_∂[ω] is exactly O(1,3); no spacetime postulate is required
- Minkowski spacetime is recovered as the local chart shadow of τ³ via the MinkowskiExtension functor (cross-ref *III.D76*)
- Null intertwiners define the light cone without prior spacetime geometry
- The speed barrier c emerges as constraint saturation, not as a phenomenological postulate

**Notation introduced**

- pr_D, pr_fiber: projection maps onto the D-sector and fiber-sector components of H_∂[ω] respectively
- MinkowskiExtension: the readout functor that produces Minkowski chart shadows (established in Book III as *III.D76*)

**Dependencies**

- Book III, *III.D76*: MinkowskiExtension functor and its properties
- Chapter 9 (*V.D01*, *V.D02*): torus vacuum geometry that supplies the fiber norm structure

## Lean coverage

No standalone Lean module is named for this chapter. The Lorentz covariance theorem is a structural consequence of the readout functor axioms established in the Book III formalization; the relevant Lean declarations live in the `TauLib.BookIII` hierarchy. The null intertwiner norm condition is used as a definition in `TauLib.BookV.Gravity.EinsteinEquation` (Chapter 11).

## Where this leads

Establishing Lorentz covariance as a theorem — not an axiom — means that the τ-Einstein equation in Chapter 11 is automatically covariant without any additional postulate. The null intertwiner formulation also underpins the gravitational wave analysis in Chapter 12.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch12-lorentz-without-minkowski.tex -->
