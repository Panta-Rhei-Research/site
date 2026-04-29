---
layout: "corpus-monograph-chapter"
title: "Chapter 31: Gravity Without Dark Matter: The Classical Illusion"
permalink: "/corpus/monographs/book-v/part-05-global-structure/chapter-32-gravity-without-dark-matter-the-classical-illusion/"
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
chapter_number: 32
chapter_slug: "chapter-32-gravity-without-dark-matter-the-classical-illusion"
page_in_book: 219
prev_chapter_url: "/corpus/monographs/book-v/part-04-collective-dynamics/chapter-30-macro-phase-transitions-and-regime-crossings/"
prev_chapter_title: "Chapter 30: Macro Phase Transitions and Regime Crossings"
next_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-32-kepler-and-the-solar-system-as-calibration-laboratory/"
next_chapter_title: "Chapter 32: Kepler and the Solar System as Calibration Laboratory"
summary_short: "Newton's inverse-square law is not a fundamental equation — it is a readout artifact of the τ-Einstein equation that holds only when three conditions are satisfied simultaneously."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-05-global-structure/"
canonical_part_title: "Global Structure"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-05-global-structure/chapter-32-gravity-without-dark-matter-the-classical-illusion/"
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

Why does classical mechanics work?
For three centuries Newtonian gravity governed the heavens
with extraordinary precision:
planetary orbits, tidal forces, projectile motion, the motion of comets.
Its central equation F = −GmM r̂/r² is among the most tested laws in science.
General relativity refined it at the relativistic frontier — perihelion advance,
light deflection, gravitational redshift — but at everyday and solar-system scales Newton reigns.
In Category τ, Newton's inverse-square law is not a fundamental equation.
It is a *readout artifact* — a coarse-grained projection of the τ-Einstein equation
that appears exact when three conditions hold simultaneously:
weak fields (|εh| ≪ 1), slow speeds (v ≪ c), and negligible
boundary-character gradients (|∇𝒞_D|/𝒞_D ≪ r⁻¹).
When any condition fails — at galactic scales, near compact objects,
or at cosmological distances — the classical description breaks down,
and orthodoxy invokes dark matter or dark energy to patch the gap.
The τ-framework offers a different diagnosis:
the breakdown is not a signal of missing matter
but a failure of the coarse-grained projection itself.
The same τ-Einstein equation that reproduces Newton in the solar system
produces modified dynamics at galactic scales not because new physics enters,
but because the readout functor changes regime.
Closed orbits are dictionary entries in the classical readout, not fundamental laws.
Straight lines seem natural only because the constraints that curve them
are invisible to the coarse-grained eye.

## What this chapter contributes

**Definitions**
- *Classical validity scale ℓ_cl* (*V.D117*, τ-effective) — the radius at which condition (iii) saturates; Newtonian projection valid for r ≪ ℓ_cl.
- *Capacity gradient correction g_cap(r)* — the additional gravitational acceleration arising from ∂_r ln 𝒞_D(r) at galactic scales.

**Key results**
- *Newtonian Limit Theorem* (*V.T78*, τ-effective) — the τ-Einstein equation projected through 𝒢_μ under all three conditions recovers the Poisson equation with G = (c³/ℏ)ι_τ².
- *Two-Regime Readout Theorem* (*V.T79*, τ-effective) — the D-sector readout functor exhibits a classical regime (r ≪ ℓ_cl, inverse-square law) and a galactic regime (r ≳ ℓ_cl, capacity-enhanced acceleration); transition is smooth.
- *Photon-Capacity Deflection Theorem* (*V.T210*, τ-effective) — the capacity gradient deflects photons and massive particles identically through the same effective metric; lensing mass equals dynamical mass (*V.P147*).
- *Correspondence Tower Theorem* (*V.T80*, τ-effective) — each level of the approximation hierarchy (full → linearised → post-Newtonian → Newtonian → free) is a systematic truncation of the τ-Einstein equation with controlled residuals.
- *Capacity Gradient as Apparent Dark Matter* (*V.P56*, τ-effective) and *Bertrand as Readout Constraint* (*V.P57*, τ-effective) — closed orbits and the MOND scale are both readout features, not fundamental facts.
- *Newton's First Law as Limit* (*V.P58*, τ-effective) — free-particle straight-line motion holds only when all three conditions hold and 𝒯[χ] = 0.

**Notation**
ℓ_cl (classical validity scale), 𝒞_D (D-sector capacity), 𝒢_μ (readout functor), ι_τ (shape ratio), κ_τ = 1 − ι_τ (gravitational coupling).

**Dependencies**
- τ-Einstein equation (ch13) and linearised form (ch14)
- Readout functor IV.D26
- Sector coupling IV.D05
- Calibration triangle (ch19), closing identity (ch20)
- Macro phase transitions (ch30) for regime-crossing context

## Lean coverage

`TauLib.BookV.GlobalStructure.ClassicalIllusion` — Newtonian limit proof, two-regime readout, correspondence tower. The photon-deflection corollary (*V.P147*) is stated and proof-sketched; full Lean formalisation deferred to the compact-object chapters.

## Where this leads

The capacity gradient identified here is the mechanism invoked in every subsequent chapter of Part V: Chapter 32 calibrates it against solar-system precision tests, Chapter 34 applies it to flat rotation curves, and Chapter 41 proves algebraically that no additional sector can provide an alternative explanation.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part05/ch34-classical-illusion.tex -->
