---
layout: "corpus-monograph-chapter"
title: "Chapter 70: The Mass Ratio R and the 10-Link Chain"
permalink: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-70-the-mass-ratio-r-and-the-10-link-chain/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 8
part_display: "Part VIII"
part_slug: "part-08-the-constants-ledger-and-the-complexity-summit"
chapter_number: 70
chapter_slug: "chapter-70-the-mass-ratio-r-and-the-10-link-chain"
page_in_book: 375
prev_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-69-running-vs-readout/"
prev_chapter_title: "Chapter 69: Running vs.\\ Readout"
next_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-71-the-neutron-lifetime-crown-of-the-cascade/"
next_chapter_title: "Chapter 71: The Neutron Lifetime: Crown of the Cascade"
summary_short: "The neutron-to-electron mass ratio R = m_n / m_e ≈ 1838.684 is derived from ι<sub>τ</sub> through a chain of exactly 10 links—each τ-effective, with zero…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/"
canonical_part_title: "The Constants Ledger and the Complexity Summit"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-70-the-mass-ratio-r-and-the-10-link-chain/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part VIII: The Constants Ledger and the Complexity Summit"
      url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part VIII"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 50
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

The neutron-to-electron mass ratio R = m_n/m_e ≈ 1838.684 is derived from ι_τ through a chain of exactly 10 links — each τ-effective, with zero conjectural ingredients. In the Standard Model, the electron mass is a free parameter: one of roughly 25 fitted constants. In τ³ it is calculated from first principles. The chain runs from the τ³ fibration (Link 1) through the Hodge Laplacian on T² (Link 2), the breathing operator whose eigenvalues encode mass (Link 3), spectral factorization as a lattice sum (Link 4), the Epstein zeta function Z(s; iι_τ) evaluated at s = 4 to extract the dominant exponent ι_τ⁻⁷ ≈ 1853.6 (Link 5), the lemniscate three-fold correction √3 ≈ 14.9 (Link 6), assembly into R₀ = ι_τ⁻⁷ − √3·ι_τ⁻² (Link 7), the triple U(1) holonomy correction π³α² (Link 8), assembly into R₁ (Link 9), and finally m_e = m_n/R₁ (Link 10). The Level 1+ formula R₁ = ι_τ⁻⁷ − (√3 + π³α²)·ι_τ⁻² matches CODATA to 0.025 ppm. No parameter is fitted at any link.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D46 — Epstein Zeta Function* (τ-effective): Z(s; τ) = Σ_{(m,n)≠(0,0)} 1/|m+nτ|^{2s}, evaluated at the shape parameter τ = iι_τ. *IV.D47 — Breathing Operator* (τ-effective): B = Δ⁻¹|_{T²} on the Hodge Laplacian — mass = resistance to solenoidal expansion, identified with eigenvalues of the breathing operator. *IV.D48 — Holonomy Correction* (τ-effective): π³α²·ι_τ⁻² from triple U(1) holonomy around the three circles of τ³; the π³ factor arises from three circular integrations; α² (not α) because the first-order correction vanishes by charge-conjugation symmetry.
- **Key results:** *IV.T10 — Level 0 Mass Ratio* (τ-effective): R₀ = ι_τ⁻⁷ − √3·ι_τ⁻², matching CODATA to 7.7 ppm. *IV.T15 — Level 1+ Mass Ratio* (τ-effective): R₁ = ι_τ⁻⁷ − (√3 + π³α²)·ι_τ⁻², matching CODATA to 0.025 ppm. *IV.P07 — Lemniscate Spectral Capacity* (τ-effective): √3 = |1 − ω| where ω = e^{2πi/3} — the lemniscate three-fold structure contributes a spectral correction coefficient. *IV.T — Electron Mass* (τ-effective): m_e = m_n/R₁, closing the derivation with the calibration anchor.
- **Dependencies:** Book I Axiom K5 (τ³ = τ¹ ×_f T² fibration); Chapter 67 (α as derived coupling, used in holonomy correction); Chapter 68 (calibration anchor m_n as the single empirical input).

## Lean coverage

`MassRatioFormula.lean` contains `chain_all_tau_effective` (verifying all 10 links carry scope label "tau-effective"), `chain_scope_count`, `bulk_in_range` (brackets ι_τ⁻⁷ ∈ (1853, 1855)), `r0_in_range` (brackets R₀ ∈ (1837, 1840)), `bulk_overshoots_codata`, and `r1_precision` — all proved without sorry.

## Where this leads

With the mass ratio chain established to sub-ppm precision, Chapter 71 assembles the neutron lifetime — the most structurally complex derived quantity in Book IV, touching every earlier layer of the cascade.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part08/ch70-mass-ratio-chain.tex -->
