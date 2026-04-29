---
layout: "corpus-monograph-chapter"
title: "Chapter 46: The Hydrogen Spectrum"
permalink: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-46-the-hydrogen-spectrum/"
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
chapter_number: 46
chapter_slug: "chapter-46-the-hydrogen-spectrum"
page_in_book: 273
prev_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-45-the-hydrogen-atom-bohr-radius-and-rydberg-constant/"
prev_chapter_title: "Chapter 45: The Hydrogen Atom: Bohr Radius and Rydberg Constant"
next_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-47-hyperfine-structure-and-the-role-of-iota-tau/"
next_chapter_title: "Chapter 47: Hyperfine Structure and the Role of ι<sub>τ</sub>"
summary_short: "The hydrogen atom emits and absorbs light at discrete wavelengths because only integer winding numbers are permitted on T². This chapter derives the Rydberg formula, all five named spectral series, and the fine-structure and Lamb-shift corrections controlled by powers of α."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
canonical_part_title: "Atoms, Chemistry, and Molecular Structure"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-46-the-hydrogen-spectrum/"
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

The hydrogen atom emits and absorbs light at discrete wavelengths, not a continuum. The explanation in Category τ is immediate: the electron mode on T² is labelled by integer winding numbers, so only integer energy differences can be radiated — discrete labels produce discrete differences produce sharp spectral lines. This observation preceded quantum mechanics by decades; Balmer found the visible hydrogen lines empirically in 1885, Rydberg generalised the formula in 1888, and Bohr's atomic model came only in 1913.

Starting from the τ-Bohr energy levels Eₙ = −13.6 eV / n², the chapter derives the Rydberg formula 1/λ = R∞(1/n_f² − 1/n_i²) and organises all transitions into five named series. The Lyman series (n_f = 1) falls in the UV at 91–122 nm; the Balmer series (n_f = 2) spans the visible at 365–656 nm, with Hα (red, 656 nm), Hβ (cyan, 486 nm), Hγ (blue, 434 nm), and Hδ (violet, 410 nm) historically prominent; Paschen (n_f = 3), Brackett (n_f = 4), and Pfund (n_f = 5) fall in the infrared. Each series converges to a limit at n_i → ∞: λ_limit = n_f²/R∞. Degeneracy at level n is gₙ = 2n², and electric dipole transitions are restricted by the selection rules Δℓ = ±1 and Δm_ℓ = 0, ±1 from the angular momentum carried by the emitted photon.

Two correction tiers refine the Rydberg picture. Fine-structure splitting at order α² splits each level n (with ℓ ≥ 1) into sub-levels labelled by total angular momentum j = ℓ ± ½; for n = 2 the 2p₃/₂ and 2p₁/₂ states are separated by ≈ 4.5 × 10⁻⁵ eV. The Lamb shift at order α⁵mₑc² ≈ 4.37 × 10⁻⁶ eV (≈ 1057 MHz) lifts the degeneracy of 2s₁/₂ and 2p₁/₂; in the τ³ framework this arises from electron-mode coupling to the boundary modes on 𝕃, the τ³ analogue of vacuum polarisation. Both corrections are controlled by known powers of α and fit naturally within the calibration hierarchy of Chapter 45. A closing principle makes explicit that "free" electrons are boundary modes on 𝕃, not point particles in empty space, and that the 1/r Coulomb field is the geometric dilution of the 𝕃 boundary coupling over the τ¹ base.

## What this chapter contributes

- **Definitions / Axioms:** Registry IDs not yet assigned (τ-effective). Hydrogen quantum numbers (n, ℓ, m_ℓ, m_s); five named spectral series (Lyman, Balmer, Paschen, Brackett, Pfund) with series limits λ_limit = n_f²/R∞; degeneracy gₙ = 2n² per level.
- **Key results:** Registry IDs not yet assigned (τ-effective): τ-Bohr energy-level theorem Eₙ = −R∞hc/n²; Rydberg spectral formula 1/λ = R∞(1/n_f² − 1/n_i²); fine-structure splitting ΔE_FS ~ α²|Eₙ|; Lamb shift ΔE_Lamb ~ α⁵mₑc² ≈ 4.37 × 10⁻⁶ eV; electric dipole selection rules Δℓ = ±1, Δm_ℓ = 0, ±1.
- **Dependencies:** Chapter 45 (τ-Bohr ground state, R∞, α); Chapter on fine structure (details of fine-structure and Lamb-shift derivations cited back).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The Rydberg formula and degeneracy counting are stated as theorems without formal Lean proof.

## Where this leads

Chapter 47 resolves the next order of structure: the proton's own spin and magnetic moment split the ground state into the hyperfine doublet whose 21 cm transition is the most important single spectral line in observational astronomy.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part06/ch46-hydrogen-spectrum.tex -->
