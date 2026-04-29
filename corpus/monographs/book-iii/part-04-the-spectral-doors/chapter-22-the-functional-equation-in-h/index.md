---
layout: "corpus-monograph-chapter"
title: "Chapter 22: The Functional Equation in H_"
permalink: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-22-the-functional-equation-in-h/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-the-spectral-doors"
chapter_number: 22
chapter_slug: "chapter-22-the-functional-equation-in-h"
page_in_book: 127
prev_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-21-the-coherence-programme/"
prev_chapter_title: "Chapter 21: The Coherence Programme"
next_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-23-the-lemniscate-operator/"
next_chapter_title: "Chapter 23: The Lemniscate Operator"
summary_short: "The split-complex zeta ζ_τ(s) = e₊·ζ_B(s) + e₋·ζ_C(s) encodes the classical functional equation as an involution J swapping e₊ and e₋ components; the fixed locus Fix(J) is algebraically forced to be the critical line Re(s) = ½."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
canonical_part_title: "The Spectral Doors"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-04-the-spectral-doors/chapter-22-the-functional-equation-in-h/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part IV: The Spectral Doors"
      url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part IV"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 35
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The Riemann Hypothesis asks where the non-trivial zeros of the Riemann zeta function lie. The classical functional equation ζ(s) = χ(s)·ζ(1 − s) expresses a symmetry of ζ about the line Re(s) = ½; in orthodox analysis, it is a statement about meromorphic continuation. This chapter encodes the same symmetry algebraically. The split-complex zeta is defined as ζ_τ(s) = e₊·ζ_B(s) + e₋·ζ_C(s), where ζ_B and ζ_C are the B-sector and C-sector partial Euler products obtained from the bipolar classifier of Chapter 18, and e₊, e₋ are the split-complex idempotents. The Functional Equation Involution J acts on H_τ by J(s) = 1 − s̄: in split-complex coordinates this swaps the e₊ and e₋ components, mirroring the classical functional equation exactly. The fixed-point set Fix(J) = {s : J(s) = s} is computed by setting 1 − s̄ = s, which gives Re(s) = ½. The critical line is therefore not a conjecture but the algebraic fixed locus of J, determined by the bipolar structure before any zeros are computed. The Bipolar Euler Product Theorem proves that ζ_τ(s) converges as a split-complex Dirichlet series on Re(s) > 1 and that J is an algebra involution on H_τ with the stated fixed locus. This is the algebraic constraint; the spectral argument that forces zeros onto Fix(J) requires the self-adjoint operator of Chapter 23 and the correspondence of Chapter 24.

## What this chapter contributes

- **Definitions / Axioms:** *III.D26 — Split-Complex Zeta ζ_τ*. The bipolar Euler product ζ_τ(s) = e₊·ζ_B(s) + e₋·ζ_C(s) as a split-complex Dirichlet series; the B- and C-sector partial products indexed by the Label_n classifier. *III.D27 — Functional Equation Involution J*. J : H_τ → H_τ defined by J(s) = 1 − s̄; J swaps the idempotent components; Fix(J) = {Re(s) = ½} is the critical line.
- **Key results:** *III.T16 — Bipolar Euler Product* (τ-effective): ζ_τ(s) converges on Re(s) > 1; J is an algebra involution; the critical line is exactly the algebraic fixed locus Fix(J) — a structural fact, not a conjecture.
- **Dependencies:** *III.D23* (Label_n, B/C/X classification); *III.T14* (Spectral Trichotomy, sector decomposition); *III.D22* (τ-adele ring, convergence domain); *III.D24* (Boundary Normal Form, e₊/e₋ coordinates).

## Lean coverage

This chapter is prose-only at the current release; the split-complex Dirichlet series construction and the Bipolar Euler Product Theorem do not yet have corresponding TauLib modules.

## Where this leads

Chapter 23 constructs the lemniscate operator H_L = −d²/dx² with Kirchhoff boundary conditions on L = S¹∨S¹ and proves it self-adjoint, establishing a real discrete spectrum. Self-adjointness is the key input to Chapter 24's Spectral Correspondence, which — conditional on conjecture O3 — identifies zeros of ζ_τ with eigenvalues of H_L and thereby forces σ = ½.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part04/ch22-the-functional-equation-in-h-tau.tex -->
