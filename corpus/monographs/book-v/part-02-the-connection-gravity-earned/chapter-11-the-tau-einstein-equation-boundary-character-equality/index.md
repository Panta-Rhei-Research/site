---
layout: "corpus-monograph-chapter"
title: "Chapter 11: The τ-Einstein Equation: Boundary-Character Equality"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-11-the-tau-einstein-equation-boundary-character-equality/"
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
chapter_number: 11
chapter_slug: "chapter-11-the-tau-einstein-equation-boundary-character-equality"
page_in_book: 73
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-10-lorentz-without-minkowski-constraint-geometry/"
prev_chapter_title: "Chapter 10: Lorentz Without Minkowski: Constraint Geometry"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-12-linear-tau-einstein-weak-field-regime-and-classical-tests/"
next_chapter_title: "Chapter 12: Linear τ-Einstein: Weak-Field Regime and Classical Tests"
summary_short: "The τ-Einstein equation R^H = κ_τ · T^mat is an algebraic identity in the boundary holonomy algebra H_∂[ω], not a partial differential equation. The curvature character R^H and the matter character T^mat are both ω-germs; their equality is derived, not postulated, and it recovers the orthodox Einstein field equations as a chart shadow."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-11-the-tau-einstein-equation-boundary-character-equality/"
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

The τ-Einstein equation R^H = κ_τ · T^mat is the central gravitational equation of the framework. It is important to be precise about what it is and what it is not. It is *not* a nonlinear partial differential equation on a background manifold. It is an algebraic identity in the boundary holonomy algebra H_∂[ω]: the curvature character R^H (*V.D04*) and the matter character T^mat (*V.D03*) are both ω-germs — elements of the boundary algebra — and their equality, mediated by the gravitational coupling κ_τ ≈ 0.659 (*V.D05*), is a derived consequence of the fiber structure of τ³. The identity is not postulated; it follows from the holonomy transport axioms and the frame holonomy gap established in Chapters 9–10. The orthodox Einstein field equations G_μν = (8πG/c⁴)T_μν are recovered as the chart shadow of this boundary identity under local readout functors; crucially, the factor 8π is itself derived from the τ geometry rather than introduced by convention. Energy-momentum conservation ∇·T = 0 is a corollary of the identity, not an additional axiom. Well-posedness follows from the Hartogs principle applied to H_∂[ω]: boundary data determine interior characters uniquely.

## What this chapter contributes

**Definitions and axioms**

- *V.D03* — Matter character T^mat: the ω-germ encoding the stress-energy content of a boundary configuration
- *V.D04* — Curvature character R^H: the ω-germ encoding the holonomy curvature of the D-sector frame bundle
- *V.D05* — Gravitational coupling character: κ_τ = 1 − ι_τ as an element of the boundary algebra (distinct from the real number κ_τ introduced in Chapter 9; here it is promoted to an algebra element)
- *V.D06* — τ-Einstein equation: R^H = κ_τ · T^mat; the master gravitational identity in H_∂[ω]
- *V.R01* — τ-Bianchi identity: the algebraic identity in H_∂[ω] that implies ∇·T^mat = 0 as a chart-shadow corollary

**Key results**

- The τ-Einstein equation is *derived* from the holonomy axioms; it is not postulated
- Chart shadow recovery: the local readout functor maps R^H = κ_τ · T^mat to G_μν = (8πG/c⁴)T_μν with the 8π factor derived, not inserted
- Backreaction is automatic: the matter character and curvature character are in the same algebra and respond to each other by construction
- Hartogs well-posedness: boundary data on ∂(τ³) determine the interior character uniquely; no Cauchy problem is needed

**Notation introduced**

- R^H: curvature character (ω-germ, not a tensor)
- T^mat: matter character (ω-germ, not a tensor)

**Dependencies**

- *V.D01*, *V.D02* (Chapter 9): torus vacuum and gravitational constant
- Book III, *III.T05*: Hartogs extension theorem applied to ω-germs

## Lean coverage

The τ-Einstein equation and all named definitions in this chapter are formalized in `TauLib.BookV.Gravity.EinsteinEquation`. The module declares *V.D03*, *V.D04*, *V.D05*, *V.D06*, and *V.R01* as verified Lean 4 terms, with the chart-shadow recovery established as a derived proposition.

## Where this leads

The τ-Einstein equation (*V.D06*) is the starting point for all subsequent chapters in Part II. Chapter 12 extracts the linear regime and recovers the classical tests of GR; Chapter 13 handles the nonlinear regime via address resolution; Chapters 14–16 apply the equation to compact objects (Schwarzschild readout, TOV star builder, topology relaxation).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch13-tau-einstein-equation.tex -->
