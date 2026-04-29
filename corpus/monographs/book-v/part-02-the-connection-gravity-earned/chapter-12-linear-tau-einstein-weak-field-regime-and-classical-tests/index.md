---
layout: "corpus-monograph-chapter"
title: "Chapter 12: Linear τ-Einstein: Weak-Field Regime and Classical Tests"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-12-linear-tau-einstein-weak-field-regime-and-classical-tests/"
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
chapter_number: 12
chapter_slug: "chapter-12-linear-tau-einstein-weak-field-regime-and-classical-tests"
page_in_book: 79
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-11-the-tau-einstein-equation-boundary-character-equality/"
prev_chapter_title: "Chapter 11: The τ-Einstein Equation: Boundary-Character Equality"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-13-nonlinear-tau-einstein-address-resolution-not-pde-solving/"
next_chapter_title: "Chapter 13: Nonlinear τ-Einstein: Address Resolution, Not PDE Solving"
summary_short: "The linear regime of the τ-Einstein equation recovers all classical tests of general relativity — Newtonian gravity, Mercury precession at 43.0''/century, light deflection at 1.7508'', gravitational redshift, and gravitational waves with exactly two polarizations — as linear chart-shadow readouts, with no approximation beyond linearization."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-12-linear-tau-einstein-weak-field-regime-and-classical-tests/"
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

The τ-Einstein equation R^H = κ_τ · T^mat (*V.D06*) holds at all scales and in all regimes. This chapter extracts its weak-field, slow-motion limit — the linear regime in which the frame holonomy gap is small compared to the identity in H_∂[ω]. In this regime the algebraic identity reduces to a set of linear readout equations, and the chart shadow of those equations is precisely the linearized Einstein equation. Every classical test of general relativity is then a consequence of reading off the linear readout: Newtonian gravitation ∇²Φ = 4πGρ follows directly from the static limit; Mercury's perihelion precession evaluates to 43.0 arcseconds per century; light deflection by the Sun evaluates to 1.7508 arcseconds; gravitational redshift is reproduced exactly; and gravitational waves are present with propagation speed c (exact, from constraint saturation) and exactly two polarizations (from the dimension of T² in the fiber). The LIGO events GW150914 and GW170817 are consistent with the predicted waveform structure. No special-purpose ansätze are introduced: all five results emerge from a single linearization of *V.D06* followed by a chart readout.

## What this chapter contributes

**Definitions and axioms**

- This chapter introduces no new registry-numbered definitions; it operates entirely within *V.D02*, *V.D06*, and the linearization procedure.
- *Linear τ-Einstein regime*: the restriction of *V.D06* to configurations where ‖R^H‖ ≪ 1 in the algebra norm; a structural condition, not a separate axiom

**Key results**

- Newtonian limit: ∇²Φ = 4πGρ recovered as the static, low-velocity chart shadow
- Mercury precession: 43.0''/century derived from the first-order holonomy correction to the Newtonian potential
- Light deflection: 1.7508'' (the full GR value, double the Newtonian prediction) from the null-intertwiner linear readout
- Gravitational redshift: exact agreement with the Pound–Rebka result
- Gravitational waves: speed c exact; two polarizations from dim(T²) = 2; spin-2 from the D-sector generator structure
- GW150914 and GW170817 consistency with the τ-linear polarization structure

**Notation introduced**

- No new notation; the chapter uses the readout conventions established in Chapter 10

**Dependencies**

- *V.D06* (Chapter 11): τ-Einstein equation
- *V.D02* (Chapter 9): gravitational constant G = (c³/ℏ)ι_τ²

## Lean coverage

The linear regime and the classical test derivations are handled by the base `TauLib.BookV.Gravity.EinsteinEquation` module through its linearization lemmas. Full formalization of the five classical tests is ongoing; the Newtonian limit and perihelion precession calculation are the most developed portions of the Lean library at present.

## Where this leads

The classical tests establish empirical adequacy of the τ-framework in the weak-field regime. Chapter 13 moves to the nonlinear regime, where the framework's approach differs most sharply from orthodox GR — not PDE solving but address resolution.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch14-linear-tau-einstein.tex -->
