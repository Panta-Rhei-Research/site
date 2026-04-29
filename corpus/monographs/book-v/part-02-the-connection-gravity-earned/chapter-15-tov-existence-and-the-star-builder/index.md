---
layout: "corpus-monograph-chapter"
title: "Chapter 15: TOV Existence and the Star Builder"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-15-tov-existence-and-the-star-builder/"
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
chapter_number: 15
chapter_slug: "chapter-15-tov-existence-and-the-star-builder"
page_in_book: 101
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-14-the-tau-schwarzschild-readout-torus-vacuum/"
prev_chapter_title: "Chapter 14: The τ-Schwarzschild Readout: Torus Vacuum"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-16-tov-phase-boundary-and-forced-topology-relaxation/"
next_chapter_title: "Chapter 16: TOV Phase Boundary and Forced Topology Relaxation"
summary_short: "The canonical star builder Star_n(k) is a witness construction in H_∂[ω] that produces unique equilibrium stellar configurations from a particle count n and sector index k, replacing the orthodox TOV ODE. The Chandrasekhar limit ≈ 1.4M☉ emerges as a relational threshold from sector coupling ratios, not from a polytropic equation of state."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-15-tov-existence-and-the-star-builder/"
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

The Tolman–Oppenheimer–Volkoff (TOV) equation governs the pressure–density profile of a static, spherically symmetric star in hydrostatic equilibrium. In orthodox GR it is an ordinary differential equation derived from the Einstein equations with a perfect-fluid source, and its solutions trace out the family of equilibrium stellar models — from white dwarfs through neutron stars to the mass threshold beyond which no equilibrium exists. The τ-framework replaces this ODE with a *witness construction* in the boundary holonomy algebra. The canonical star builder Star_n(k) takes two inputs — a particle count n and a sector index k — and produces the unique equilibrium boundary character as a zero-defect element of H_∂[ω]. The construction proceeds in stages: the spherical carrier predicate Sph(χ) defines what spherical symmetry means in the τ-framework (not a symmetry of a manifold but a constraint on the readout functor); the GR tension functional measures departure from flat-torus equilibrium; the neutron node predicate identifies the specific boundary character corresponding to a neutron star; EW stability of the neutron node under electroweak perturbations is proven; and the Chandrasekhar limit ≈ 1.4M☉ is derived as a relational threshold — the particle count at which no spherical carrier predicate can be satisfied within the ball-topology sector. This last result does not depend on a polytropic equation of state but follows from the sector coupling ratios that are themselves fixed by the τ axioms.

## What this chapter contributes

**Definitions and axioms**

- *Spherical carrier predicate* Sph(χ): the τ-native condition on a boundary character χ that corresponds to spherical symmetry; derived from the readout functor constraints, not postulated
- *GR tension functional* T_GR: measures the departure of a boundary character from the flat-torus equilibrium; the algebraic replacement for the TOV pressure-gradient equation
- *Star builder* Star_n(k): the canonical witness construction mapping (n, k) to the unique equilibrium boundary character; an algebraic object in H_∂[ω], not a solution to an ODE
- *Neutron node predicate*: identifies the boundary character corresponding to a neutron-star configuration; derived from the neutron mass m_n fixed in Book IV
- *Chandrasekhar limit as relational threshold*: the value ≈ 1.4M☉ at which the spherical carrier predicate ceases to be satisfiable within ball topology; derived from sector coupling ratios

**Key results**

- Star_n(k) existence and uniqueness: for each admissible (n, k), a unique equilibrium boundary character exists
- TOV balance is algebraic tension equilibrium, not an ODE; no Cauchy data are needed
- EW stability of the neutron node: the equilibrium is stable under electroweak perturbations
- Truncation invariance: the star builder output is independent of the truncation level chosen in the τ-NF iteration
- Chandrasekhar limit ≈ 1.4M☉ from sector couplings, consistent with the observed mass threshold

**Dependencies**

- *V.D06* (Chapter 11): τ-Einstein equation supplying the tension functional
- *V.D01*, *V.D02* (Chapter 9): torus vacuum and G_τ
- Book III, *III.D39*, *III.T25*: carrier predicates and fiber equilibrium

## Lean coverage

The star builder construction, spherical carrier predicate, GR tension functional, and Chandrasekhar threshold are formalized in `TauLib.BookV.GravityField.TOVStarBuilder`.

## Where this leads

The star builder establishes that equilibrium stellar configurations exist within ball topology up to the Chandrasekhar threshold. Chapter 16 determines what happens when that threshold is exceeded: the ball topology cannot absorb the GR tension, and a forced topology relaxation occurs.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch17-tov-star-builder.tex -->
