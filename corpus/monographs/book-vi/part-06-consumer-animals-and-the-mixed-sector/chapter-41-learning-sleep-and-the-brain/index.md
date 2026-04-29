---
layout: "corpus-monograph-chapter"
title: "Chapter 41: Learning, Sleep, and the Brain"
permalink: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-41-learning-sleep-and-the-brain/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-consumer-animals-and-the-mixed-sector"
chapter_number: 41
chapter_slug: "chapter-41-learning-sleep-and-the-brain"
page_in_book: 243
prev_chapter_url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-40-sensation-perception-and-neural-systems/"
prev_chapter_title: "Chapter 40: Sensation, Perception, and Neural Systems"
next_chapter_url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-42-identity-through-transformation-ship-of-theseus-as-selfdesc/"
next_chapter_title: "Chapter 42: Identity Through Transformation: Ship of Theseus as SelfDesc"
summary_short: "Learning is the PPAS algorithm operating on neural connection weights via synaptic plasticity (Hebbian learning, LTP, LTD), instantiating P vs NP at the…"
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/"
canonical_part_title: "Consumer — Animals and the Mixed Sector"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-41-learning-sleep-and-the-brain/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part VI: Consumer — Animals and the Mixed Sector"
      url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part VI"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 65
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

Evolution runs the PPAS on the space of genotypes across generations. Learning runs the same PPAS within a single organism's lifetime, on the space of synaptic weight configurations. The configuration space is vast — with ~10¹⁴ synapses each having even a modest dynamic range, it dwarfs the evolutionary search space — yet the same structural logic applies: verification (does this weight configuration improve prediction?) is polynomial, and the prover (the brain under Hebbian and reward-modulated plasticity) is locally informed. This chapter develops learning from Hebb's rule through spike-timing-dependent plasticity and the dopamine-gated three-factor rule, in each case identifying the PPAS interpretation: LTP strengthens provers, LTD prunes them, reward prediction error solves the credit assignment problem. Memory consolidation is solution caching: the hippocampus runs fast PPAS search and transfers stable solutions to the neocortex during sleep. Sleep is then given its topological placement: the sleep/wake cycle is the specialization of the temporal lemniscate L_T = S¹_act ∨ S¹_rest to neural carriers, with the wake lobe handling external information acquisition and the sleep lobe handling internal consolidation, synaptic homeostasis, and glymphatic waste clearance. The connection to the neural defect tower of Chapter 40 closes the picture: NREM sleep repairs Level 1 (molecular: glymphatic clearance of amyloid-β and tau) and REM repairs Level 2 (synaptic: Tononi–Cirelli downscaling), while Levels 3–4 accumulate irreversibly. Chronic sleep deprivation skips these repair cycles and accelerates the Hayflick crossing at Level 1.

## What this chapter contributes

- **Defs/Axioms:** *VI.D90* — Sleep Repair Function: maps NREM → Level 1 repair (glymphatic clearance) and REM → Level 2 repair (synaptic homeostasis).
- **Key results:** *VI.P19* — Sleep as Temporal Lemniscate Second Lobe: the sleep/wake lemniscate L_neural = S¹_wake ∨ S¹_sleep with five structural properties (wake lobe, sleep lobe, wedge-point flip-flop, both-lobes necessity, nested NREM–REM ultradian lemniscate); *VI.T53* — Sleep Consolidates Levels 1–2 (Levels 3–4 accumulate irreversibly); *VI.P24* — Sleep Deprivation Accelerates Defect Crossing.
- **Notation:** Hebb rule Δw_ij ∝ x_i x_j; STDP timing window; three-factor rule Δw_ij ∝ x_i · x_j · RPE; L_neural = S¹_wake ∨ S¹_sleep.
- **Dependencies:** Neural architecture *VI.D52* and defect tower *VI.D87–D88* (Ch. 40), temporal lemniscate framework (Ch. circadian rhythms, Part II), PPAS (Ch. 37), repair budget *VI.P16*.

## Lean coverage

Chapter is prose-level; no Lean formalization is planned. *VI.P19*, *VI.T53*, and *VI.P24* are τ-effective structural consequences of the lemniscate and defect frameworks.

## Where this leads

Chapter 42 draws the philosophical consequence of the continuous self-maintenance established in this chapter: if identity survives continuous synaptic rewiring during sleep, it must be lodged in the code, not the carrier — the Ship of Theseus dissolves.

<!-- regenerated 2026-04-29 | source: manuscript-sources/book-06/part06/ch41-learning-sleep.tex -->
