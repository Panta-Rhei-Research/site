---
layout: "corpus-monograph-chapter"
title: "Chapter 38: Binary Mergers and Gravitational-Wave Readout"
permalink: "/corpus/monographs/book-v/part-05-global-structure/chapter-39-binary-mergers-and-gravitational-wave-readout/"
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
chapter_number: 39
chapter_slug: "chapter-39-binary-mergers-and-gravitational-wave-readout"
page_in_book: 273
prev_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-37-accretion-jets-and-active-galactic-nuclei/"
prev_chapter_title: "Chapter 37: Accretion, Jets, and Active Galactic Nuclei"
next_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-39-the-eht-re-read-the-ring-is-the-donut/"
next_chapter_title: "Chapter 39: The EHT Re-Read: The Ring Is the Donut"
summary_short: "Gravitational waves are boundary-character oscillations in H_∂[ω], a binary merger is the coalescence of two coherent instances, and the Chirp Mass Theorem connects the waveform directly to boundary holonomy invariants without free parameters."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-05-global-structure/"
canonical_part_title: "Global Structure"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-05-global-structure/chapter-39-binary-mergers-and-gravitational-wave-readout/"
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

On 14 September 2015, LIGO detected the gravitational-wave signal GW150914:
the merger of two black holes with masses 36 M_☉ and 29 M_☉
at a distance of ~410 Mpc,
releasing ~3 M_☉ c² of energy in gravitational radiation over a fraction of a second.
This detection confirmed a century-old prediction of general relativity
and opened an entirely new observational window onto the universe.
In Category τ, gravitational waves are not ripples in a background spacetime manifold.
They are **boundary-character oscillations** —
periodic perturbations of the holonomy algebra H_∂[ω]
propagating along the base τ¹ at speed c.
A binary merger is the coalescence of two coherent instances —
two localized concentrations of boundary holonomy —
into a single more massive coherent instance.
The gravitational-wave signal is the readout of this coalescence in the D-sector.
This chapter derives the binary inspiral waveform from the τ-Einstein equation,
proves the **Chirp Mass Theorem** (*V.T38*) relating the waveform parameters
to boundary holonomy invariants,
defines the **ringdown readout** (*V.D56*) as the quasi-normal mode spectrum
of the merged coherent instance,
and establishes the **standard siren** (*V.D57*) as a τ-native distance measure.
The LIGO event catalogue is re-read as a table of boundary-holonomy coalescence events,
with GW150914 and GW170817 worked through in detail.
The chapter also addresses post-merger echoes (*V.T225*):
the T²-topology of the remnant predicts a discrete echo spectrum
absent from S²-topology Kerr black holes.

## What this chapter contributes

**Definitions**
- *Binary Coherent-Instance System* (*V.D54*, τ-effective) — pair (ℐ₁, ℐ₂) sharing the same τ¹ progression, with mutual boundary holonomy H₁₂ = H_∂[ω]|_{ℐ₁} ⊗ H_∂[ω]|_{ℐ₂}.
- *GW Boundary-Character Wave* (*V.D55*, τ-effective) — a D-sector perturbation h propagating at c; the two polarisations h₊, h× are readouts of the two independent quadrupole modes of H₁₂.
- *Ringdown Readout* (*V.D56*, τ-effective) — quasi-normal mode spectrum of the merged coherent instance; eigenfrequencies determined by the T² shape ratio ι_τ and the total mass M_f.
- *Standard Siren* (*V.D57*, τ-effective) — luminosity distance from GW amplitude without an electromagnetic distance ladder.
- *GW Event Catalog* (*V.D281*) — τ-native re-read of the LIGO/Virgo/KAGRA catalog.
- *Echo Amplitude Model* (*V.D283*, τ-effective) — predicted echo amplitude from T²-topology boundary reflections.

**Key results**
- *Chirp Mass from Boundary Holonomy* (*V.T38*, τ-effective) — ℳ_c = (M₁M₂)^{3/5}/(M₁+M₂)^{1/5} is a holonomy invariant of the binary; controls the inspiral phase evolution with no free parameter.
- *Ringdown Uniqueness Theorem* (*V.T39*, τ-effective) — the post-merger quasi-normal spectrum uniquely encodes the T² shape ratio ι_τ; distinguishable from Kerr QNM spectrum at SNR ≳ 50.
- *Chirp Mass Consistency* (*V.T222*, τ-effective) and *T² Ringdown Formula* (*V.T223*, τ-effective) — second-generation derivations confirming consistency with GW event data.
- *Echo Detection Threshold* (*V.T225*, τ-effective) — stacked echo search becomes detectable at SNR ~ 8 for O4-class sensitivity.
- *GW Energy Flux* (*V.P22*) and *Merger Graviton Count* (*V.P23*) — energy carried per unit frequency and total graviton number per event, both in τ-native units.

**Notation**
ℳ_c (chirp mass), h₊/h× (GW polarisations), ι_τ (shape ratio), M_f (final merger mass), Q (quality factor of ringdown).

**Dependencies**
- τ-Einstein equation (ch13), Schwarzschild solution (ch16)
- Jet Collimation Theorem (ch37), Accretion Funnel (ch37)
- Boundary holonomy IV.D05; kernel axioms I.K1–K5

## Lean coverage

`TauLib.BookV.Astrophysics.BinaryMergersGW` — binary coherent-instance definition, chirp mass theorem, GW energy flux. Ringdown uniqueness and echo detection theorems stated and proof-sketched; full Lean proofs planned.

## Where this leads

The ringdown spectrum and echo predictions of this chapter are the clearest discriminators between the T² topology of Category τ and the S² topology of GR; Chapter 39 provides the complementary EHT-based discrimination using the shadow shape, and together they define the observational programme that can decide between the two frameworks.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part05/ch41-binary-mergers-gw.tex -->
