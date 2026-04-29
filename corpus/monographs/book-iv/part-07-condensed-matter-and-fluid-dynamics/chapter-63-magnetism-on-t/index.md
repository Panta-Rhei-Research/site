---
layout: "corpus-monograph-chapter"
title: "Chapter 63: Magnetism on~T²"
permalink: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-63-magnetism-on-t/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-condensed-matter-and-fluid-dynamics"
chapter_number: 63
chapter_slug: "chapter-63-magnetism-on-t"
page_in_book: 345
prev_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-62-crystals-glass-and-phase-transitions/"
prev_chapter_title: "Chapter 62: Crystals, Glass, and Phase Transitions"
next_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-64-decidable-regimes-and-the-nfl-theorem/"
next_chapter_title: "Chapter 64: Decidable Regimes and the NFL Theorem"
summary_short: "Magnetism is one of the oldest known physical phenomena, yet its fundamental origin is quantum mechanical: unpaired electron spins generate magnetic moments,…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
canonical_part_title: "Condensed Matter and Fluid Dynamics"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-63-magnetism-on-t/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part VII: Condensed Matter and Fluid Dynamics"
      url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part VII"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 49
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Magnetism is ancient as a phenomenon and quantum mechanical at its core: unpaired defect-bundle spins generate magnetic moments, and their collective alignment or misalignment produces the rich variety of magnetic orders observed in nature. In τ³ magnetism acquires a topological character that changes the explanation of several standard results. The Euler characteristic χ(T²) = 0 means — via the Gauss–Bonnet theorem — that the integral of any curvature 2-form over T² vanishes identically. A magnetic monopole of charge g at a point would require a non-trivial second cohomology class with total flux g, but χ(T²) = 0 forces this to zero. Monopole absence is not an empirical observation; it is a topological necessity of the fiber. The chapter then shows how the Ising model on T² (with periodic boundary conditions that eliminate edge effects) yields spontaneous magnetization below the Curie temperature via Onsager's exact solution, and classifies all five magnetic orders — diamagnetic, paramagnetic, ferromagnetic, antiferromagnetic, ferrimagnetic — as distinct patterns of the d₄ topological component.

## What this chapter contributes

- **Definitions / Axioms:** none introduced with new registry IDs; this chapter develops the ferromagnet sub-case of *IV.D18 — Fluid Regime* (τ-effective). Key constructs: τ-Ising Hamiltonian on T² plaquettes; magnetic domain wall as a codimension-1 defect in the d₄ winding field; five magnetic orders classified by d₄ pattern.
- **Key results:** No Magnetic Monopoles on T² (τ-effective): a short proof from the Gauss–Bonnet theorem — (1/2π)∫_T² F = χ(T²) = 0 — establishes that the total magnetic charge on T² vanishes identically. The asymmetry between electric charge (a boundary obstruction on 𝕃) and magnetic charge (an Euler obstruction on T²) is structural, not contingent. Spontaneous Magnetization from τ-Ising (τ-effective): Kramers–Wannier duality on T² locates the self-dual critical point, below which ⟨|M|⟩ > 0. Curie Transition as T² Symmetry Breaking (τ-effective): a second-order transition with Landau free energy F(ϕ, T) = F₀ + a(T)ϕ² + bϕ⁴, order parameter ϕ measuring global d₄ phase coherence. Domain Wall Energy from T² Winding (τ-effective): σ_wall = 4√(AK) with wall width δ = π√(A/K). Magnetic Orders as Defect-Tuple Signatures (τ-effective): the five orders classified by d₄ alignment patterns, with proofs for each type.
- **Notation introduced:** J (exchange coupling); h (applied field); T_C (Curie temperature); T_N (Néel temperature); domain wall energy σ_wall; wall width δ.
- **Dependencies:** Part II (spin and quantum addresses); Part III ch on gauge invariance and Maxwell; ch62 (Landau theory and phase transition classification).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 64 returns to the algebraic foundations to prove the NFL-boundary theorem — non-dissipative dynamics are precisely the automorphisms of the boundary character algebra H_∂ — and establishes a universal decidability meta-theorem covering all ten regimes.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part07/ch63-magnetism.tex -->
