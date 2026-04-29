---
layout: "corpus-monograph-chapter"
title: "Chapter 35: The Compact-Object Ladder"
permalink: "/corpus/monographs/book-v/part-05-global-structure/chapter-36-the-compact-object-ladder/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 5
part_display: "Part V"
part_slug: "part-05-global-structure"
chapter_number: 36
chapter_slug: "chapter-36-the-compact-object-ladder"
page_in_book: 247
prev_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-34-rotation-curves-without-dark-matter/"
prev_chapter_title: "Chapter 34: Rotation Curves Without Dark Matter"
next_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-36-core-collapse-and-supernovae/"
next_chapter_title: "Chapter 36: Core Collapse and Supernovae"
summary_short: "White dwarfs, neutron stars, and black holes are relational thresholds at which the D-sector gravitational coupling progressively overcomes fiber-sector pressure, with the Chandrasekhar and TOV limits derived from τ-framework constants alone."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-05-global-structure/"
canonical_part_title: "Global Structure"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-05-global-structure/chapter-36-the-compact-object-ladder/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part V: Global Structure"
      url: "/corpus/monographs/book-v/part-05-global-structure/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part V"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 56
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

When a star exhausts its nuclear fuel the remnant it leaves behind
depends on one number: the mass of the core at the moment of fuel exhaustion.
This chapter traces the **compact-object ladder** —
the sequence of stellar endpoints ordered by mass —
in the language of Category τ.
Below the **Chandrasekhar mass** M_Ch ≈ 1.4 M_☉,
electron degeneracy pressure (a fiber-sector phenomenon, Book IV)
supports the remnant: the result is a **white dwarf**.
Above M_Ch but below the Tolman–Oppenheimer–Volkoff limit M_TOV ≈ 2.0–2.3 M_☉,
neutron degeneracy pressure and the strong nuclear force (the C-sector) support the remnant:
the result is a **neutron star**.
Above M_TOV, no known force can resist gravitational collapse,
and the result is a **black hole** — a topology change to a BH linking class in T².
Each rung of the ladder is a readout of the competition
between the D-sector gravitational coupling κ(D;1) = 1 − ι_τ
and the fiber-sector pressure encoded in the defect functional of Book IV.
The Chandrasekhar and TOV thresholds are *relational thresholds*:
mass values at which the balance between sectors shifts irreversibly.
The chapter closes with pulsar timing —
the most precise clocks in nature —
and their role as probes of the τ-Einstein equation in the strong-field regime.

## What this chapter contributes

**Definitions**
- *Degeneracy Pressure Character P_deg* (*V.D124*, τ-effective) — the B-sector boundary character encoding Fermi-sea resistance to compression; non-relativistic form P_deg ∝ n_e^{5/3}, relativistic form ∝ n_e^{4/3}.

**Key results**
- *Chandrasekhar Mass from τ-Framework* (*V.T86*, τ-effective) — M_Ch = ω₃⁰(ℏc/G)^{3/2}/(μ_e m_u)²; substituting G = (c³/ℏ)ι_τ² gives M_Ch in terms of the calibration anchor m_n with no free parameter.
- *TOV Limit as Relational Threshold* (*V.T87*, τ-effective) — M_TOV emerges from the competition between C-sector (strong nuclear) pressure and D-sector curvature; predicted value 2.0–2.3 M_☉ consistent with observed neutron star mass distribution.
- *Black Hole as Topology Change* (τ-effective) — above M_TOV the defect functional admits a BH linking class in T²; the event horizon is not a geometric surface but a topological transition in the boundary holonomy.
- *Pulsar Timing as Strong-Field Probe* (τ-effective) — pulse arrival times encode the τ-Schwarzschild metric; observed Hulse-Taylor orbital decay matches the quadrupole radiation formula from Chapter 38.
- *Ladder as Endpoint Sequence of the Density Gradient* (τ-effective) — each compact remnant is a step in the temporal arc of the primordial H/He gas differentiating under the τ-Einstein equation.

**Notation**
ω₃⁰ ≈ 2.018 (Lane–Emden n=3 constant), μ_e ≈ 2 (mean molecular weight per electron), m_u (atomic mass unit).

**Dependencies**
- τ-Einstein equation (ch13), Schwarzschild solution (ch16), TOV star builder (ch17), TOV phase boundary (ch18)
- Classical illusion (ch31), Kepler calibration (ch32)
- Defect functional IV.D09; D-sector coupling IV.D05

## Lean coverage

`TauLib.BookV.GlobalStructure.CompactObjectLadder` — Chandrasekhar mass theorem, TOV limit proposition, degeneracy pressure character definition. Pulsar-timing comparison is quantitative but formal Lean proof deferred.

## Where this leads

The compact objects defined on this ladder are the protagonists of the next four chapters: core-collapse supernovae (Chapter 36) open the topological channel at the Chandrasekhar threshold, accretion disks and jets (Chapter 37) form around these remnants, binary mergers (Chapter 38) radiate boundary-character oscillations, and the EHT images (Chapter 39) reveal their toroidal topology.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part05/ch38-compact-object-ladder.tex -->
