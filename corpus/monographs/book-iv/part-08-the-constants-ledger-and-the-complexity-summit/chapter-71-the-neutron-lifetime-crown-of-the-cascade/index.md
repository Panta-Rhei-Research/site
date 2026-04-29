---
layout: "corpus-monograph-chapter"
title: "Chapter 71: The Neutron Lifetime: Crown of the Cascade"
permalink: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-71-the-neutron-lifetime-crown-of-the-cascade/"
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
chapter_number: 71
chapter_slug: "chapter-71-the-neutron-lifetime-crown-of-the-cascade"
page_in_book: 379
prev_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-70-the-mass-ratio-r-and-the-10-link-chain/"
prev_chapter_title: "Chapter 70: The Mass Ratio R and the 10-Link Chain"
next_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-72-laws-as-structure/"
next_chapter_title: "Chapter 72: Laws as Structure"
summary_short: "The free neutron decays with a lifetime τ_n ≈ 879 s—roughly fifteen minutes. This single number encodes the entire calibration cascade of Book IV: it depends…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/"
canonical_part_title: "The Constants Ledger and the Complexity Summit"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-71-the-neutron-lifetime-crown-of-the-cascade/"
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

The free neutron decays with a lifetime τ_n ≈ 879 s — roughly fifteen minutes. This single number encodes the entire calibration cascade of Book IV: it depends on the fine structure constant α, the neutron-to-electron mass ratio R, the weak-sector coupling κ(A;1) through the Fermi constant G_F, the axial coupling g_A, the Cabibbo angle |V_ud|, and the phase space integral f that counts kinematically allowed decay products. In the Standard Model, each of these five inputs is a free parameter. In τ³, every ingredient is a derived quantity from ι_τ. No other derived quantity in the microcosm touches as many layers of the framework — which is why τ_n earns the designation "crown of the cascade."

## What this chapter contributes

- **Definitions / Axioms:** *IV.D383 — Neutron Lifetime Input Table* (τ-effective): all eight ingredients of the Fermi golden rule (R, α, sin²θ_W, |V_ud|, g_A, Δ_A, Δ_r, f·(1+3g_A²)) expressed as ι_τ-derived formulas with ppm error budgets. *IV.D — Phase Space Integral* (τ-effective): f = ∫₁^{w₀} w√(w²−1)(w₀−w)² dw, where w₀ = Δm/m_e ≈ 2.531 is the endpoint — a dimensionless count of kinematically accessible final states.
- **Key results:** *IV.T182 — Axial Coupling from CF Window Algebra* (τ-effective): g_A = κ_D²/ι_τ · (1 + (8/17)α) ≈ 1.27637, at +5.5 ppm from PDG; the numerator 8 = 4+4 (self + cross couplings in count), denominator 17 = W₃(3) from the CF partial-quotient window governing M_W and sin²θ_W. *IV.T203 — Neutron Lifetime Precision Prediction* (τ-effective): τ_n ≈ 878.7 s, at +340 ppm from the bottle average (878.4 ± 0.5 s) and excluding the beam value (887.7 ± 1.2 s) at >7σ. *IV.P224 — Cancelled-Form Error Budget* (τ-effective): the "cancelled form" — rewriting the Fermi formula to trade G_F and M_W for the mass ratio R, producing N = 64π³R⁹ / (14⁴(1−Δ_r)²f(1+3g_A²)|V_ud|²) — reduces the effective RSS uncertainty from ~6030 ppm (naive Fermi) to 77 ppm, a 78× improvement. *IV.T — Cascade Closure* (τ-effective): τ_n is the most complex derived quantity in Book IV; no quantity in the book depends on more intermediate results.
- **Dependencies:** Chapter 65 (coupling ledger, κ(A,D) = ι_τ(1−ι_τ) for G_F); Chapter 68 (mass ratio chain R₁); Chapter 67 (running vs. readout, α derivation); Parts III–V (weak sector, quark structure for |V_ud| and g_A).

## Lean coverage

This chapter is prose-only at the current release for the neutron lifetime assembly; its full derivation does not yet have a corresponding TauLib module. Structural range proofs for subsidiary quantities (R₁, α) exist in `MassRatioFormula.lean` and `CouplingFormulas.lean`.

## Where this leads

With the cascade complete, Chapter 72 steps back to ask what kind of thing a physical law is in the τ³ framework — showing that conservation laws, symmetries, Feynman diagrams, and the S-matrix are all internal categorical structure rather than external impositions on matter.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part08/ch71-neutron-lifetime.tex -->
