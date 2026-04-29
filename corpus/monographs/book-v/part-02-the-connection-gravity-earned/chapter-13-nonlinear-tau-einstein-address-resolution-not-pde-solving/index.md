---
layout: "corpus-monograph-chapter"
title: "Chapter 13: Nonlinear τ-Einstein: Address Resolution, Not PDE Solving"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-13-nonlinear-tau-einstein-address-resolution-not-pde-solving/"
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
chapter_number: 13
chapter_slug: "chapter-13-nonlinear-tau-einstein-address-resolution-not-pde-solving"
page_in_book: 85
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-12-linear-tau-einstein-weak-field-regime-and-classical-tests/"
prev_chapter_title: "Chapter 12: Linear τ-Einstein: Weak-Field Regime and Classical Tests"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-14-the-tau-schwarzschild-readout-torus-vacuum/"
next_chapter_title: "Chapter 14: The τ-Schwarzschild Readout: Torus Vacuum"
summary_short: "In the nonlinear regime the τ-Einstein equation is solved not by integrating a PDE but by address resolution: finding the unique boundary character in H_∂[ω] that minimizes the cocycle defect. Existence, uniqueness, and selection are theorems. The profinite density cap eliminates point masses and curvature singularities structurally."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-13-nonlinear-tau-einstein-address-resolution-not-pde-solving/"
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

Orthodox general relativity in its nonlinear regime is a system of ten coupled nonlinear partial differential equations. Global existence, uniqueness, and regularity of solutions are among the deepest open problems in mathematical physics — cosmic censorship, the Penrose conjecture, the BKL analysis of generic singularities remain unresolved precisely because the PDE approach provides insufficient algebraic control. The τ-framework avoids this class of difficulty entirely. The τ-Einstein equation (*V.D06*) is an algebraic identity in H_∂[ω], not a PDE. In its nonlinear regime, the equation is not integrated from initial data on a Cauchy surface but solved by *address resolution*: given a matter configuration, the algorithm finds the unique boundary character x ∈ H_∂[ω] that satisfies R^H(x) = κ_τ · T^mat(x) by iteratively minimizing the cocycle defect through the τ-NF Einstein iteration. Existence of a solution, uniqueness of the zero-defect character, and selection among multiple approximate solutions are all theorems derived from the profinite structure of Category τ. The profinite density cap — the minimum resolution scale built into the τ³ fibration — prevents any boundary character from concentrating to a point mass, thereby eliminating curvature singularities not by a regularity hypothesis but as a structural consequence of the algebra. Horizons emerge as present-surface contractions of the null structure on τ³, not as coordinate artifacts.

## What this chapter contributes

**Definitions and axioms**

- This chapter introduces no new registry-numbered definitions; its core content is the algorithmic and existential theory of *V.D06* in the nonlinear regime.
- *Address resolution principle*: the procedure of finding the zero-defect boundary character by τ-NF iteration; a structural feature of H_∂[ω], not an external regularization
- *Cocycle defect*: the failure of a trial boundary character to satisfy the τ-Einstein identity; minimized to zero by the iteration
- *Profinite density cap*: the minimum algebraic resolution of H_∂[ω]; structurally prevents point concentrations

**Key results**

- Nonlinear existence theorem: for any admissible matter character T^mat, a boundary character satisfying R^H = κ_τ · T^mat exists
- Uniqueness theorem: the zero-defect character is unique (modulo gauge equivalence in the readout functor)
- Selection theorem: the τ-NF iteration converges to the correct solution from any admissible initial approximation
- Density cap theorem: no solution of *V.D06* contains a point-mass singularity; curvature singularities are structurally absent
- Horizons as present surfaces: event horizons are identified with present-surface contractions rather than coordinate singularities

**Dependencies**

- *V.D06* (Chapter 11): τ-Einstein equation
- Book III, *III.T05*: Hartogs extension for ω-germs

## Lean coverage

The nonlinear existence, uniqueness, and selection theorems are stated in the base `TauLib.BookV.Gravity.EinsteinEquation` module; full Lean proofs of the nonlinear regime are planned for a subsequent formalization pass. The density cap theorem is partially formalized via the profinite structure lemmas in `TauLib.Core`.

## Where this leads

With singularity-free nonlinear solutions established, Chapter 14 applies address resolution to the specific case of a spherically symmetric vacuum to derive the τ-Schwarzschild readout — the torus-vacuum replacement for the classical Schwarzschild solution.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch15-nonlinear-tau-einstein.tex -->
