---
layout: "corpus-monograph-chapter"
title: "Chapter 64: Decidable Regimes and the NFL Theorem"
permalink: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-64-decidable-regimes-and-the-nfl-theorem/"
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
chapter_number: 64
chapter_slug: "chapter-64-decidable-regimes-and-the-nfl-theorem"
page_in_book: 349
prev_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-63-magnetism-on-t/"
prev_chapter_title: "Chapter 63: Magnetism on~T²"
next_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-65-tau-ns-regularity-at-fiber-level/"
next_chapter_title: "Chapter 65: τ-NS Regularity at Fiber Level"
summary_short: "What distinguishes an Euler flow from a Navier–Stokes flow? Physically, the answer is dissipation: Euler flows conserve energy exactly, while NS flows lose…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/"
canonical_part_title: "Condensed Matter and Fluid Dynamics"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-64-decidable-regimes-and-the-nfl-theorem/"
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

What distinguishes an Euler flow from a Navier–Stokes flow? Physically, the answer is dissipation: Euler flows conserve energy exactly while NS flows lose energy to heat. In τ³ this distinction has a precise algebraic formulation. The boundary character algebra H_∂ decomposes via the Chinese Remainder Theorem as ∏_{pᵢ ≤ pₙ} ℤ/pᵢℤ at each refinement stage. An endomorphism Φ: H_∂ → H_∂ preserves all clopen ideals if and only if it is injective on each finite factor — and on a finite ring, injective equals bijective, so preservation of all clopen ideals is equivalent to Φ being an automorphism. Dissipation corresponds to strict endomorphisms that shrink at least one clopen ideal, pushing its encoded information deeper into the primorial filtration — this is the algebraic meaning of energy "lost to heat." From this theorem a universal decidability result follows: every regime predicate is a conjunction of finitely many conditions on the defect tuple, and at finite refinement stage n with bounded budget K the NF code space is finite, making each predicate checkable in finite time.

## What this chapter contributes

- **Definitions / Axioms:** none introduced with new registry IDs; this chapter develops consequences of *IV.D18 — Fluid Regime* and the defect dynamics established in ch58–ch62. Key constructs: non-dissipative endomorphism (preserves all clopen ideals); the NFL-depth corollary (strict endomorphisms push information to finer scales); the ten regime instantiation catalog.
- **Key results:** NFL-Boundary Theorem (τ-effective): NonDiss(Φ) ⟺ Φ ∈ Aut(H_∂). Proved in three steps: CRT reduction to product of finite rings; finite ring injectivity equals bijectivity by pigeonhole; inverse-limit lift to the full profinite algebra. NFL-Depth Corollary (τ-effective): a strict endomorphism maps some clopen ideal into a strictly smaller one at a specific prime level — the algebraic version of "information lost to heat." Decidable Phase Classification Meta-Theorem (τ-effective): at fixed refinement stage n and budget K, every regime predicate (crystal, glass, quasicrystal, Euler, NS, MHD, plasma, superfluid, superconductor, ferromagnet) is decidable by finite recursion on NF codes. Ten Regime Instantiations: each predicate is a horizon-contractivity check with an explicit finite-depth criterion.
- **Notation introduced:** Aut(H_∂) (automorphism group of boundary character algebra); primorial filtration (the tower of CRT factors); horizon-contractivity lemma (term for the regime-specific finite-depth check).
- **Dependencies:** ch56 (defect functional, boundary character algebra H_∂); ch58 (τ-Euler, Kelvin invariant as automorphism action); ch59 (τ-NS dissipation); ch62 (CheckCrystal/CheckGlass procedures).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 65 uses the NFL algebraic framework — particularly the finite-depth cascade property — to instantiate the three conditions of the Positive Regularity Theorem (III.T25) for the fiber-level Navier–Stokes system, resolving the Millennium Problem at fiber level.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part07/ch64-decidable-regimes-nfl.tex -->
