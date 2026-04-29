---
layout: "corpus-monograph-chapter"
title: "Chapter 58: τ-Euler: Inviscid Flow"
permalink: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-58-tau-euler-inviscid-flow/"
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
chapter_number: 58
chapter_slug: "chapter-58-tau-euler-inviscid-flow"
page_in_book: 325
prev_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-57-the-universal-defect-tuple/"
prev_chapter_title: "Chapter 57: The Universal Defect Tuple"
next_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-59-tau-navier-stokes-viscous-flow/"
next_chapter_title: "Chapter 59: τ-Navier–Stokes: Viscous Flow"
summary_short: "The Euler equations of classical fluid dynamics describe the motion of an inviscid fluid: no friction, no dissipation, no viscosity. In τ³, the Euler…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
canonical_part_title: "Condensed Matter and Fluid Dynamics"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-58-tau-euler-inviscid-flow/"
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

The Euler equations of classical fluid dynamics describe inviscid motion: no friction, no dissipation, no viscosity. In orthodox physics they are postulated. In τ³ they emerge. When the aggregate defect components d̄₂ and d̄₃ are negligible — vorticity dissipation and compression both near zero — the defect ensemble enters the τ-Euler regime and its conservation law directly produces the Euler momentum equation. Pressure arises as the spatial gradient of the defect energy functional 𝓔[𝐝] evaluated at constant comoving volume; the continuity equation follows from defect-number conservation under boundary automorphisms, which neither create nor destroy defect bundles. The compactness of T² adds geometric richness that the classical setting on ℝ³ does not share: there are exactly two independent non-contractible loops, each carrying a conserved circulation by Kelvin's theorem, and the dynamics reduce to pure redistribution of defect density across the compact fiber. The point-vortex Hamiltonian on T² is controlled by the torus Green's function G_T², whose shape is set by the ratio of the two torus radii — the master constant ι_τ. In the incompressible limit, divergence-free flow on T² admits a global stream function ψ satisfying ω = −Δψ, and long-time behavior is far better controlled on the compact domain than on ℝ²: global existence and uniqueness for smooth two-dimensional Euler data follows from the bounded geometry alone.

## What this chapter contributes

- **Definitions / Axioms:** none introduced with new registry IDs; this chapter develops consequences of *IV.D18 — Fluid Regime* (Euler sub-case) and *IV.T04 — Euler Budget Conservation* (τ-effective).
- **Key results:** τ-Euler Equation (τ-effective): the standard continuity and momentum equations ∂_t𝐯 + (𝐯·∇)𝐯 = −(1/ρ)∇p are derived from defect budget conservation rather than postulated. τ-Kelvin Theorem (τ-effective): the circulation Γ_γ around any material loop γ(t) ⊂ T² is conserved; on the compact torus this is a topological statement about H₁(T²). τ-Bernoulli (τ-effective): ½|𝐯|² + h + Φ = const along streamlines, a restatement of defect energy conservation. Point vortex system (τ-effective): N vortices on T² evolve by a Hamiltonian containing the torus Green's function, encoding ι_τ.
- **Notation introduced:** Γ_γ (circulation around loop γ); stream function ψ (incompressible limit); G_T² (torus Green's function).
- **Dependencies:** ch04 (IV.T04, Euler budget conservation); ch56 (defect ensemble principle, Euler regime definition); ch57 (defect phase space 𝒟).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 59 adds viscosity as inter-mode friction on T², extending the τ-Euler system to the τ-Navier–Stokes equation and introducing the Reynolds number as the ratio d̄₃/d̄₁.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part07/ch58-tau-euler.tex -->
