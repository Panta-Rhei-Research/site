---
layout: "corpus-monograph-chapter"
title: "Chapter 16: TOV Phase Boundary and Forced Topology Relaxation"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-16-tov-phase-boundary-and-forced-topology-relaxation/"
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
chapter_number: 16
chapter_slug: "chapter-16-tov-phase-boundary-and-forced-topology-relaxation"
page_in_book: 109
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-15-tov-existence-and-the-star-builder/"
prev_chapter_title: "Chapter 15: TOV Existence and the Star Builder"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-17-the-calibration-triangle-neutron/"
next_chapter_title: "Chapter 17: The Calibration Triangle: Neutron →"
summary_short: "When the GR tension functional exceeds the structural threshold Λ_τ = (1−ι_τ)/(4ι_τ²), the ball-topology star builder is no longer satisfiable and a forced topology change from ball to torus is required. This transition is structural — a boundary in the space of admissible configurations — not a dynamical collapse event."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-16-tov-phase-boundary-and-forced-topology-relaxation/"
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

Every equilibrium stellar configuration produced by the star builder Star_n(k) exists within a ball topology — the fiber sector carries a contractible boundary character whose GR tension functional is below the stability threshold. As mass accumulates, through accretion or core collapse, the gravitational character G_ω(x) grows monotonically while the matter character T^mat_ω(x) saturates at the neutron-node ceiling. The mismatch in growth rates produces a GR tension that the ball-topology carrier predicate Sph(χ) cannot absorb. This chapter proves three main results. First, the GR tension monotonicity theorem: T_GR(n) is monotonically increasing in the particle count n for any ball-topology stellar configuration. Second, the structural threshold: there exists a finite threshold Λ_τ = (1−ι_τ)/(4ι_τ²) such that no ball-topology boundary character can satisfy the τ-Einstein identity when T_GR exceeds Λ_τ. Third, the forced topology relaxation theorem: when the threshold is crossed, the configuration must change topology from ball to torus — the geometric, deformable ball sector gives way to the topological, stabilized torus sector of the D-sector vacuum. This transition is *structural*, not dynamical: it is a boundary in the space of admissible refinement-coherent configurations, not a physical collapse process occurring in time. The defect cost jumps discontinuously at the phase boundary; the transition is decidable in the sense that Sat_n — the satisfiability predicate for ball-topology configurations — is computable and has a sharp threshold.

## What this chapter contributes

**Definitions and axioms**

- *Coherence horizon* M_n*: the maximum mass (in the neutron-node parameterization) for which a ball-topology zero-defect boundary character exists; the τ-native Chandrasekhar analog at the topology level
- *Structural threshold* Λ_τ = (1−ι_τ)/(4ι_τ²): the GR tension value above which ball-topology satisfaction fails; derived from the master constant ι_τ
- *Forced topology relaxation*: the structural requirement that a configuration exceeding Λ_τ must be represented by a torus-topology boundary character; not a dynamical event but a constraint on admissible configurations
- *Topology crossing event*: the label for the moment (in a refinement sequence) at which the satisfiability predicate Sat_n changes value; conceptually the τ-native analog of gravitational collapse

**Key results**

- GR tension monotonicity theorem: T_GR(n) is strictly increasing in n for ball-topology stars
- The threshold Λ_τ is exact and derived: it follows from ι_τ alone with no free parameters
- Forced topology relaxation theorem: crossing Λ_τ forces a ball→torus topology change; the transition is structural, not dynamical
- Defect cost jump: the cocycle defect is discontinuous at the phase boundary; no smooth interpolation exists between ball and torus configurations
- Decidability of Sat_n: the satisfiability predicate has a computable sharp threshold; the phase boundary is not fuzzy

**Dependencies**

- Star builder and GR tension functional from Chapter 15
- *V.D01*, *V.D02* (Chapter 9): torus vacuum establishing the torus-topology target
- *V.D06* (Chapter 11): τ-Einstein equation whose satisfiability is being analyzed

## Lean coverage

No standalone Lean module is named for this chapter. The forced topology relaxation theorem and the structural threshold are stated as propositions dependent on the `TauLib.BookV.GravityField.TOVStarBuilder` and `TauLib.BookV.Gravity.Schwarzschild` modules. Full formalization of the topology-change argument is in progress.

## Where this leads

The forced topology relaxation theorem completes the structural account of compact objects: neutron stars below Λ_τ, torus-core black holes above. Chapter 17 builds the calibration triangle connecting this macroscopic scale to the neutron-mass anchor of Book IV without invoking SI units.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch18-tov-phase-boundary.tex -->
