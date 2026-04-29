---
layout: "corpus-monograph-chapter"
title: "Chapter 15: Circadian Rhythms: Poincaré Orbits on the Temporal Circle"
permalink: "/corpus/monographs/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-15-circadian-rhythms-poincar-e-orbits-on-the-temporal-circle/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 2
part_display: "Part II"
part_slug: "part-02-persistence-archaea-and-the-temporal-axis"
chapter_number: 15
chapter_slug: "chapter-15-circadian-rhythms-poincar-e-orbits-on-the-temporal-circle"
page_in_book: 81
prev_chapter_url: "/corpus/monographs/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-14-thermodynamic-necessity-and-the-origin-of-life/"
prev_chapter_title: "Chapter 14: Thermodynamic Necessity and the Origin of Life"
next_chapter_url: "/corpus/monographs/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-16-homochirality-the-parity-bridge-made-visible/"
next_chapter_title: "Chapter 16: Homochirality: The Parity Bridge Made Visible"
summary_short: "Circadian rhythms are Poincaré orbits on the temporal circle τ¹. The 24-hour cycle is formalized as a temporal lemniscate with activity and rest lobes (VI.D27), and the circadian clock is proved to be a limit cycle (VI.T17). Ultradian and infradian rhythms appear as harmonics and subharmonics of this fundamental orbit."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-02-persistence-archaea-and-the-temporal-axis/"
canonical_part_title: "Persistence — Archaea and the Temporal Axis"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-02-persistence-archaea-and-the-temporal-axis/chapter-15-circadian-rhythms-poincar-e-orbits-on-the-temporal-circle/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part II: Persistence — Archaea and the Temporal Axis"
      url: "/corpus/monographs/book-vi/part-02-persistence-archaea-and-the-temporal-axis/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part II"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 61
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

The persistence sector is governed by the α-generator on the base circle τ¹. Any continuous flow on a compact one-dimensional manifold is periodic — there are no non-periodic trajectories on S¹. Circadian rhythms are the biological realization of this topological requirement: they are not merely a convenient adaptation but a structural consequence of operating in the persistence sector. This chapter develops that consequence from a formal definition through a worked molecular example to the full harmonic spectrum of biological rhythms.

The Temporal Lemniscate (VI.D27) formalizes the two-phase structure of the daily cycle. The lemniscate boundary L = S¹ ∨ S¹ from the τ³ domain correspondence has two lobes: S¹_act (the activity phase, during which transcriptional activators dominate) and S¹_rest (the rest phase, during which repressors dominate). The wedge point where the lobes meet corresponds to the dawn and dusk transitions. Every continuous traversal of a figure-eight alternates between the two lobes; the topology forces the alternation.

The Circadian Rhythm as Poincaré Orbit theorem (VI.T17, τ-effective) proves that for any Life loop (D, γ, h) ∈ Pers_α, the projection of γ onto τ¹ is a Poincaré orbit — a stable periodic trajectory satisfying γ_α(t + T) = γ_α(t) — and that the Poincaré return map P: Σ → Σ has a unique stable fixed point on any transversal section. The orbit is a limit cycle: nearby trajectories converge to it. Three empirically established properties of circadian rhythms follow directly from this structure: endogeneity (the orbit is intrinsic to the carrier's dynamics on τ¹, not driven by external forcing), entrainability (the limit cycle can be phase-locked to a zeitgeber when the frequency mismatch is small), and temperature compensation (the period T is a topological invariant of the orbit, not a kinetic parameter — temperature changes traversal speed but not circuit circumference). The mammalian CLOCK–BMAL1/PER–CRY feedback loop is worked through step by step, mapping each phase of the transcription–translation cycle to the corresponding lemniscate segment.

The 24-Hour Cycle as τ¹ Rotation proposition (VI.P09) identifies the circadian period with one full rotation of the α-flow on τ¹. A table of free-running periods across all three domains — cyanobacterial KaiABC (~24 h), archaeal Halobacterium (~24 h), fungal Neurospora (~22 h), plant Arabidopsis (~24 h), Drosophila (~24 h), human (~24.2 h) — documents the convergence of radically different molecular mechanisms on the same topological period: winding number w_α = 1. Ultradian rhythms (cardiac, respiratory, 90-min BRAC) correspond to w_α > 1; infradian rhythms (menstrual, seasonal) correspond to fractional winding. The full biological frequency hierarchy spanning eight orders of magnitude is a Fourier decomposition of the carrier's temporal dynamics, with the circadian orbit as the fundamental mode.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D27 — Temporal Lemniscate* (τ-effective): L_T = S¹_act ∨ S¹_rest with wedge points at dawn and dusk transitions.
- **Key results:** *VI.T17 — Circadian Rhythm as Poincaré Orbit* (τ-effective): the α-projection of any persistence-sector Life loop is a limit cycle on τ¹ tracing L_T, with a unique stable Poincaré return map. *VI.P09 — 24-Hour Cycle as τ¹ Rotation* (τ-effective): the circadian period corresponds to w_α = 1, documented universally across all three domains of life.
- **Notation introduced:** L_T (temporal lemniscate); P: Σ → Σ (Poincaré return map); w_α (winding number on τ¹).
- **Dependencies:** VI.D24 (persistence sector); VI.D25 (temporal stability predicate); ch. 12 (limit-cycle picture of homeostasis); Book III Part II ch. 21–26 (Poincaré force on τ¹).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. VI.T17 is stated and proved by sketch argument; formal Lean verification of the Poincaré orbit claim is pending under the SectorTemplate module extension.

## Where this leads

Chapter 16 turns from temporal periodicity to spatial asymmetry, showing how the persistence sector preserves the Parity Bridge's chiral polarity across geological time as the phenomenon of homochirality.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part02/ch15-circadian-rhythms.tex -->
