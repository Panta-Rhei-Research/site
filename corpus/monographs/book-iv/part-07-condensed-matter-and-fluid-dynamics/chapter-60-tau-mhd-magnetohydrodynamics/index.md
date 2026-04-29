---
layout: "corpus-monograph-chapter"
title: "Chapter 60: τ-MHD: Magnetohydrodynamics"
permalink: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-60-tau-mhd-magnetohydrodynamics/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-condensed-matter-and-fluid-dynamics"
chapter_number: 60
chapter_slug: "chapter-60-tau-mhd-magnetohydrodynamics"
page_in_book: 333
prev_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-59-tau-navier-stokes-viscous-flow/"
prev_chapter_title: "Chapter 59: τ-Navier–Stokes: Viscous Flow"
next_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-61-superfluids-and-superconductors/"
next_chapter_title: "Chapter 61: Superfluids and Superconductors"
summary_short: "When a conducting fluid moves through a magnetic field, the fluid and the field evolve together: currents generate fields, fields exert forces, and at large…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
canonical_part_title: "Condensed Matter and Fluid Dynamics"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-60-tau-mhd-magnetohydrodynamics/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part VII: Condensed Matter and Fluid Dynamics"
      url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part VII"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 49
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

When a conducting fluid moves through a magnetic field, the two evolve as a coupled system: currents generate fields, fields exert Lorentz forces, and at the large scales relevant to stellar interiors and laboratory plasmas the fluid and field become inseparable. In τ³ this coupling has a precise origin. The B-sector holonomy — the electromagnetic U(1) connection on T² established in Part III — couples dynamically to the fluid velocity field whenever the defect ensemble carries charge (active EM coupling). The electrical conductivity σ_e is determined by the B-sector coupling constant κ(B; 2) = ι_τ² and the mobility d̄₁. Adding the Lorentz force 𝐉 × 𝐁 to the τ-NS momentum equation and the Faraday–Ohm induction equation for 𝐁 yields the τ-MHD system, while the topological constraint ∇·𝐁 = 0 follows from the absence of sources in the B-sector connection.

## What this chapter contributes

- **Definitions / Axioms:** none introduced with new registry IDs; this chapter develops the MHD and Plasma sub-cases of *IV.D18 — Fluid Regime* (τ-effective). Key constructs: τ-MHD coupling via Ohm's law 𝐉 = σ_e(𝐄 + 𝐯 × 𝐁); magnetic Reynolds number R_m = μ₀σ_e UL; plasma regime (d̄₁ ≫ 0, deconfined charges).
- **Key results:** τ-MHD System (τ-effective): the four-equation MHD system — mass continuity, momentum with Lorentz force, induction equation, no-monopole constraint — is derived from defect transport coupled to B-sector holonomy, not postulated. Alfvén Waves on T² (τ-effective): small perturbations in a uniform background field 𝐁₀ propagate as transverse waves at the Alfvén velocity v_A = |𝐁₀|/√(μ₀ρ); on the compact torus these exist only at discrete wavenumbers in the spectrum ℤ². Frozen-In vs. Diffusive Regimes (τ-effective): R_m ≫ 1 gives the frozen-in condition (field lines advect with the fluid) relevant to stellar and galactic scales; R_m ≪ 1 gives diffusive behavior characteristic of laboratory liquid metals. Magnetic Reconnection (τ-effective): local regime transitions where R_m drops below unity allow field-line topology changes and energy release as kinetic energy and heat.
- **Notation introduced:** σ_e (electrical conductivity); η_m = 1/(μ₀σ_e) (magnetic diffusivity); R_m (magnetic Reynolds number); v_A (Alfvén velocity).
- **Dependencies:** ch56 (MHD regime definition); ch59 (τ-NS equations, mode friction); Part V B-sector coupling (κ(B;2) = ι_τ²).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 61 descends to the quantum fluid regimes — superfluids and superconductors — where the vorticity component d₂ quantizes rather than taking continuous values, and the Meissner effect and Cooper pairing are derived from the topology of T².

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part07/ch60-tau-mhd.tex -->
