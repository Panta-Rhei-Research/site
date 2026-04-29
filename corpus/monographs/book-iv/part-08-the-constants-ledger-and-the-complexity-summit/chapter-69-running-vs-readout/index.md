---
layout: "corpus-monograph-chapter"
title: "Chapter 69: Running vs.\\ Readout"
permalink: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-69-running-vs-readout/"
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
chapter_number: 69
chapter_slug: "chapter-69-running-vs-readout"
page_in_book: 371
prev_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-68-the-ontological-layer-architecture/"
prev_chapter_title: "Chapter 68: The Ontological Layer Architecture"
next_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-70-the-mass-ratio-r-and-the-10-link-chain/"
next_chapter_title: "Chapter 70: The Mass Ratio R and the 10-Link Chain"
summary_short: "In orthodox quantum field theory, coupling constants ``run'' with the energy scale: α ≈ 1/137 at low energy becomes α ≈ 1/128 at the Z-boson mass. In…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/"
canonical_part_title: "The Constants Ledger and the Complexity Summit"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-69-running-vs-readout/"
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

In orthodox quantum field theory, coupling constants "run" with the energy scale: α ≈ 1/137 at low energy becomes α ≈ 1/128 at the Z-boson mass, and α_s flows in the opposite direction, decreasing toward a small value at high energy (asymptotic freedom). In τ³, the coupling ledger established in Chapter 67 is scale-invariant: every entry is a boundary fixed-point invariant determined by ι_τ = 2/(π + e), a ratio of mathematical constants that carries no dependence on any energy scale. This chapter reconciles the two pictures. What looks like running is readout drift — the variation of a projected coupling value as the resolution aperture of the measurement probe widens or narrows. The coupling is the boundary value; the "running" is a property of the projection, not the constant.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D07 — No-Running Principle* (τ-effective, recapped from Chapter 67): all ten couplings are boundary fixed-point invariants, independent of energy scale, probe resolution, or RG parameter. *IV.D07a — Readout* (τ-effective): a projection Read_μ from 𝒜_spec(𝕃) to a finite-dimensional observable subspace retaining only character modes with spectral weight below μ. *IV.D07b — Readout Drift* (τ-effective): the variation κ_eff(μ) = Read_μ[κ(S;d)] ≠ κ(S;d) as μ changes — the effective coupling depends on μ even though the underlying coupling does not.
- **Key results:** *IV.P — Running Is Readout Drift* (τ-effective): α(μ) = Read_μ[κ(B;2)]·f(μ), where f(μ) is a readout correction factor encoding probe distortion; the factor f(μ) plays the role of the RG beta function but describes the probe, not the coupling. *IV.P — No-GUT Principle* (τ-effective): the sectors {D, A, B, C} remain distinct at all scales; their couplings are independent rational functions of ι_τ with no common root; apparent convergence in the UV is a readout artifact, not a signal of sector merger. *IV.P — Beta Function Reinterpreted* (τ-effective): β_read(μ) = μ·d/dμ[Read_μ[κ(S;d)]] — a property of the readout procedure, not of the coupling itself.
- **Dependencies:** Chapter 67 (complete coupling ledger, No-Running Principle); Chapter 68 (L0/L1/L2 architecture — running is a Layer 2 phenomenon, the coupling is a Layer 1 invariant).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The readout framework is specified precisely enough for future formalization, but the readout projection Read_μ has not been encoded in Lean at this stage.

## Where this leads

With the scale-invariance of the coupling ledger secured, Chapter 70 proceeds to the most precise application: the 10-link derivation of the neutron-to-electron mass ratio, where every link is τ-effective and the result matches CODATA to sub-ppm precision.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part08/ch69-running-vs-readout.tex -->
