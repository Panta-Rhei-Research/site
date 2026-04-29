---
layout: "corpus-monograph-chapter"
title: "Chapter 20: The Electron Mass Prediction"
permalink: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-20-the-electron-mass-prediction/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 2
part_display: "Part II"
part_slug: "part-02-quantum-mechanics-as-address-obstruction"
chapter_number: 20
chapter_slug: "chapter-20-the-electron-mass-prediction"
page_in_book: 99
prev_chapter_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-19-energy-entropy-and-the-arrow/"
prev_chapter_title: "Chapter 19: Energy, Entropy, and the Arrow"
next_chapter_url: "/corpus/monographs/book-iv/part-03-the-electroweak-arc/chapter-21-gauge-invariance-and-the-tau-maxwell-equations/"
next_chapter_title: "Chapter 21: Gauge Invariance and the τ-Maxwell Equations"
summary_short: "Part II's first quantitative prediction: the neutron-to-electron mass ratio R₀ = ι_τ^{−7} − √3 ι_τ^{−2} ≈ 1838.7, from breathing modes and lemniscate geometry."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
canonical_part_title: "Quantum Mechanics as Address Obstruction"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-20-the-electron-mass-prediction/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part II: Quantum Mechanics as Address Obstruction"
      url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part II"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 44
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Part II culminates in the first quantitative prediction of the τ³ framework: the neutron-to-electron mass ratio, derived from first principles with no free parameters. Three ingredients combine into the formula R₀ = ι_τ^{−7} − √3 ι_τ^{−2}: the breathing modes on T² (oscillatory exchange between a compact torus configuration and its bulk environment), the Epstein zeta function Z(4; iι_τ) whose Chowla–Selberg leading exponent is −7 at s = 4, and the lemniscate capacity √3 arising from the three-fold crossing structure at the wedge point of 𝕃 = S¹ ∨ S¹. With ι_τ = 2/(π + e) ≈ 0.341304 the leading-order ratio is R₀ ≈ 1838.7, in close agreement with the CODATA value m_n/m_e = 1838.684…; adding the holonomy correction δ_hol = π³α² ≈ 0.00165 shifts the prediction to R₁ ≈ 1838.684, matching to 0.025 ppm. The same lemniscate holonomy also yields the Schwinger term a_e = α/(2π) for the electron anomalous magnetic moment, matching experiment at −3 ppm (NLO).

## What this chapter contributes

- **Definitions / Axioms:** *RES.L3.01 — Mass as Resistance*. A massive particle is a T² configuration that refuses to expand with the background solenoidal flow; the tension required equals rest energy mc².
- **Definitions / Axioms:** *RES.L3.02 — Breathing Dynamics*. Oscillatory energy exchange between a T² configuration and its bulk environment; the torus shape ratio r/R = ι_τ determines the breathing mode spectrum.
- **Definitions / Axioms:** *RES.L3.03 — Epstein Zeta Function*. Z(s; iι_τ) = Σ' 1/|m + iι_τ n|^{2s} over (m,n) ∈ ℤ² \ {0}; encodes spectral properties of the T² lattice with modular parameter τ = iι_τ.
- **Definitions / Axioms:** *RES.L3.04 — Holonomy*. Hol(γ) = P exp(−∮_γ A) ∈ U(1) along a closed curve γ; on T² three independent holonomy contributions (poloidal, toroidal, diagonal).
- **Definitions / Axioms:** *RES.L3.05 — Anomalous Magnetic Moment* (IV.D368). a_ℓ = (g_ℓ − 2)/2; for a structureless Dirac particle g = 2 exactly; the anomaly arises from virtual corrections to the electromagnetic vertex.
- **Key results:** *RES.L3.06 — Leading Exponent* (τ-effective): Z(4; iι_τ) ~ ι_τ^{−7} (leading term); the exponent −7 = 2s − 1 at s = 4 arises from the Chowla–Selberg decomposition. Spectral purity (Book III III.T19) ensures clean eigenvalues at this evaluation point.
- **Key results:** *RES.L3.07 — Lemniscate Capacity* (τ-effective): cap(𝕃) = √3 = |1 − ω| for ω = e^{2πi/3}; encodes the three-fold crossing structure at the lemniscate wedge. Well-defined as a topological invariant by Book III III.D35 (Poincaré/Spatial).
- **Key results:** *RES.L3.08 — Neutron-to-Electron Mass Ratio* (τ-effective): R₀ = ι_τ^{−7} − √3 ι_τ^{−2} ≈ 1838.7; a 10-link derivation chain with no free parameters; Lean 4 verified range bounds R₀ ∈ (1837, 1840).
- **Key results:** *RES.L3.09 — Holonomy Correction* (τ-effective): δ_hol = π³α²; three independent U(1) loops each contributing π after CR-parity filtering, times α² from second-order EM coupling. Corrected prediction R₁ ≈ 1838.684, matching CODATA at 0.025 ppm.
- **Key results:** *RES.L3.10 — Schwinger Term from 𝕃-Holonomy* (τ-effective, IV.T179): a_e^{(2)} = α/(2π) = (121/225) ι_τ^4 / (2π) ≈ 0.0011614; single-winding vertex correction on 𝕃, with NLO prediction at −3 ppm and NNLO at +10 ppm.
- **Dependencies:** Chapters 13–19 (full Part II chain); Book III III.T19 (spectral purity at Epstein zeta evaluation), III.D35 (Poincaré/Spatial, lemniscate capacity well-definedness).

## Lean coverage

Range bounds for the mass ratio formula are verified in Lean 4: ι_τ^{−7} ∈ (1853, 1855) and R₀ ∈ (1837, 1840). The full derivation chain does not yet have a complete corresponding TauLib module.

## Where this leads

Part III deploys the quantum mechanical formalism of Part II as a tool for the electroweak sector, treating the W and Z bosons, neutrinos, and electroweak symmetry breaking; the muon g−2 anomaly becomes a discriminating test once α_τ is refined to sub-ppm precision.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part02/ch20-electron-mass-prediction.tex -->
