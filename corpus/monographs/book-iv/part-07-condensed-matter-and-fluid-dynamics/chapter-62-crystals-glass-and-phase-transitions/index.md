---
layout: "corpus-monograph-chapter"
title: "Chapter 62: Crystals, Glass, and Phase Transitions"
permalink: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-62-crystals-glass-and-phase-transitions/"
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
chapter_number: 62
chapter_slug: "chapter-62-crystals-glass-and-phase-transitions"
page_in_book: 341
prev_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-61-superfluids-and-superconductors/"
prev_chapter_title: "Chapter 61: Superfluids and Superconductors"
next_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-63-magnetism-on-t/"
next_chapter_title: "Chapter 63: Magnetism on~T²"
summary_short: "The frozen regimes—crystal and glass—are the two faces of immobility. In a crystal, immobility coexists with maximal topological order: atoms lock into a…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
canonical_part_title: "Condensed Matter and Fluid Dynamics"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-62-crystals-glass-and-phase-transitions/"
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

The frozen regimes — crystal and glass — share zero mobility (d̄₁ = 0) but differ in topological order. A crystal has d̄₄ ≫ 0: the defect ensemble locks into a periodic mode pattern and the eigenmodes φ_{k₁,k₂} of the Laplacian on T² inherit the periodicity of a sublattice Λ ⊂ ℤ². A glass has d̄₄ ≈ 0: mobility is kinetically arrested before long-range order develops, producing a mechanically rigid but topologically disordered state. This chapter shows that the five two-dimensional Bravais lattice types correspond to the five structurally distinct sublattices of ℤ² under GL(2, ℤ), that band theory is Bloch's theorem on T² (the crystal momentum k taking values in T²/Λ*), and that phase transitions between regimes are classified by whether the free-energy components are discontinuous (first-order) or continuously vanishing (second-order). Crucially, both crystal and glass detection are algorithmically decidable on finite NF codes.

## What this chapter contributes

- **Definitions / Axioms:** none introduced with new registry IDs; this chapter develops the crystal, glass, and quasicrystal sub-cases of *IV.D18 — Fluid Regime* (τ-effective). Key constructs introduced: glass threshold K_glass (minimal NF budget for mobility arrest); EM-glass (glass with active EM holonomy, covering metallic glasses and spin glasses); CheckCrystal(c, K) and CheckGlass(c, K) as total decidable procedures on finite NF codes; the two-channel framework (geometric channel d₁, d₂, d₃ for ordinary transitions; topological channel d₄ for quantum transitions).
- **Key results:** Bravais Lattices from T² (τ-effective): the 5 two-dimensional Bravais types are the 5 GL(2, ℤ)-orbits of sublattices in ℤ²; ι_τ being irrational makes the natural T² lattice oblique. Bloch's Theorem on T² (τ-effective): single-particle eigenstates in the crystal regime have the form ψ_𝐤(𝐱) = e^{i𝐤·𝐱} u_𝐤(𝐱), leading to the metal/semiconductor/insulator classification by Fermi-level position relative to band gaps. Ehrenfest Classification from 𝒟 (τ-effective): first-order transitions have a discontinuous d̄ᵢ; second-order transitions have divergent susceptibility χᵢ = ∂d̄ᵢ/∂T. Decidability of Crystal and Glass Classification (τ-effective): both CheckCrystal and CheckGlass are total and decidable on finite NF codes, making phase identification algorithmic within τ³.
- **Notation introduced:** Λ (crystal sublattice in ℤ²); K_glass (glass threshold budget); CheckCrystal, CheckGlass (decision procedures).
- **Dependencies:** ch50 (molecular orbitals from Part VI); ch56 (regime definitions); ch57 (defect phase space 𝒟, transition surfaces).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 63 shifts to a purely topological result: χ(T²) = 0 forbids magnetic monopoles, making their absence a theorem rather than an empirical observation, and derives ferromagnetic order from the Ising model on T².

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part07/ch62-crystals-glass-phases.tex -->
