---
layout: "corpus-monograph-chapter"
title: "Chapter 47: Hyperfine Structure and the Role of ι<sub>τ</sub>"
permalink: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-47-hyperfine-structure-and-the-role-of-iota-tau/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-atoms-chemistry-and-molecular-structure"
chapter_number: 47
chapter_slug: "chapter-47-hyperfine-structure-and-the-role-of-iota-tau"
page_in_book: 277
prev_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-46-the-hydrogen-spectrum/"
prev_chapter_title: "Chapter 46: The Hydrogen Spectrum"
next_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-48-multi-electron-atoms-and-shell-structure/"
next_chapter_title: "Chapter 48: Multi-Electron Atoms and Shell Structure"
summary_short: "Proton–electron magnetic coupling splits the hydrogen ground state into a triplet and singlet separated by ≈ 5.9 × 10⁻⁶ eV, producing the 21 cm radio line. This chapter also derives the proton charge radius to +12 ppm (NLO) and clarifies the exact scope of the master constant ι_τ."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
canonical_part_title: "Atoms, Chemistry, and Molecular Structure"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-47-hyperfine-structure-and-the-role-of-iota-tau/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part VI: Atoms, Chemistry, and Molecular Structure"
      url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part VI"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 48
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

The proton is not a scalar source: it carries spin s_p = ½ and an anomalous magnetic moment μ_p ≈ 2.793 μ_N. The coupling between the proton and electron magnetic moments splits the hydrogen ground state into a triplet (F = 1) and a singlet (F = 0), separated by ΔE_HF = (4/3)g_p α⁴(mₑ/m_p)mₑc² ≈ 5.88 × 10⁻⁶ eV — about five orders of magnitude below the fine structure, yet measured to 13 significant figures by the hydrogen maser (fractional stability ~10⁻¹⁵). The resulting 21 cm radio line (ν ≈ 1420.405 MHz) is the principal tracer of neutral hydrogen across the universe, maps spiral structure in the Milky Way, probes the cosmic dark ages before reionisation, and defines the quietest band in the radio spectrum — the "water hole" long proposed for interstellar communication. Beyond the splitting itself, this chapter has a second purpose: to state precisely where the master constant ι_τ = 2/(π + e) ≈ 0.341304 enters the physics and — equally important — where it does not. ι_τ governs mass ratios, generation hierarchies, torus aspect ratio, and the neutron lifetime through the weak sector coupling; but it does not alone determine α (which requires an additional rational prefactor 121/225 encoding EM sector holonomy), absolute mass scales (the neutron mass m_n is the single dimensionful input), or gauge-group structure (which arises from sector decomposition of 𝕃). A significant Sprint-6 addition derives the proton charge radius to NLO accuracy: r_p^(NLO) = 4ƛ_p(1 − ι_τ²α/2) = 0.84088 fm, a +12 ppm agreement with the CREMA muonic-hydrogen measurement, a 36× improvement over the leading-order result r_p = 4ƛ_p = 0.84124 fm (+440 ppm). The correction factor ι_τ²α/2 decomposes as holonomy coupling squared (ι_τ²) times EM coupling (α) distributed across two 𝕃 lobes (factor 1/2). The chapter also derives the proton g-factor g_p = (5 − 2ι_τ)/ι_τ = 5.597 (PDG: 5.5857, deviation +2000 ppm, conjectural scope requiring quark-level NLO corrections) and the proton-size Lamb-shift contribution ~0.0121 meV.

## What this chapter contributes

- **Definitions / Axioms:** *IV.T185 — Proton charge radius LO* (τ-effective): r_p = 4ℏ/(m_pc) = 0.84124 fm. *IV.T202 — Proton charge radius NLO* (τ-effective): r_p^(NLO) = 4ƛ_p(1 − ι_τ²α/2) = 0.84088 fm. *IV.T186 — Proton g-factor* (τ-effective): g_p = (5 − 2ι_τ)/ι_τ = 5.597. *IV.P213 — Lamb shift proton-size contribution* (τ-effective). Four-tier calibration cascade definition (Tier 0 topology through Tier 4 macroscopic scales).
- **Key results:** *IV.R437 — Precision atomic assessment update* (τ-effective): NLO proton radius at +12 ppm is the highest-precision atomic prediction in the τ-framework; ι_τ controls mass ratios, generation hierarchies, and torus shape, but does not alone determine α, absolute mass scales, or gauge-group structure — each requires additional structural input.
- **Notation introduced:** ι_τ = 2/(π + e) named and scoped; four calibration tiers defined; g_p formula via ι_τ.
- **Dependencies:** Registry IDs not yet assigned for ch47 hyperfine theorem; *IV.T86* (electron mass), *IV.T109* (proton mass), *IV.T171*, *IV.T142* (quark winding modes) from earlier parts.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The NLO proton radius formula and g_p derivation are marked τ-effective but formal proofs are deferred.

## Where this leads

Chapter 48 moves from one-electron hydrogen to multi-electron atoms, where Pauli exclusion and shell-filling from T² mode saturation generate the periodic table structure that underlies all of chemistry.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part06/ch47-hyperfine-structure.tex -->
