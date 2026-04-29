---
layout: "corpus-monograph-chapter"
title: "Chapter 24: The Spectral Correspondence"
permalink: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-24-the-spectral-correspondence/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-the-spectral-doors"
chapter_number: 24
chapter_slug: "chapter-24-the-spectral-correspondence"
page_in_book: 135
prev_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-23-the-lemniscate-operator/"
prev_chapter_title: "Chapter 23: The Lemniscate Operator"
next_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-25-spectral-purity-and-the-critical-line/"
next_chapter_title: "Chapter 25: Spectral Purity and the Critical Line"
summary_short: "The spectral parameter Λ(s) = ι_τ²(s(1−s) − ¼) maps the critical strip to the non-negative reals; the Spectral Correspondence Theorem III.T18, conditional on the determinant representation conjecture O3, identifies zeros of ζ_τ with eigenvalues of H_L."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
canonical_part_title: "The Spectral Doors"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-04-the-spectral-doors/chapter-24-the-spectral-correspondence/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part IV: The Spectral Doors"
      url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part IV"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 35
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Chapter 22 produced a split-complex zeta ζ_τ whose zeros are the objects of interest; Chapter 23 produced a self-adjoint operator H_L with a known real discrete spectrum. This chapter builds the bridge. The spectral parameter Λ(s) = ι_τ²(s(1 − s) − ¼) is defined so that Λ(s) = 0 exactly when s lies on the critical line Re(s) = ½ or at the trivial zeros; for s in the critical strip with Re(s) = ½, the map s ↦ Λ(s) sends the imaginary part of s to a non-negative real candidate for an eigenvalue of H_L. The Spectral Correspondence Theorem then asserts: if ζ_τ admits a Fredholm determinant representation of the form det(I − (s(1−s)−¼)H_L⁻¹), every non-trivial zero ρ of ζ_τ bijects with an eigenvalue λₙ of H_L via Λ(ρ) = λₙ. The Fredholm representation is conjecture O3 — the single remaining open gap in the proof chain — and all consequences of the Spectral Correspondence are stated as τ-effective conditional on O3. No stronger claim is made. Chapter 26 itemises all six proof obligations O1–O6 in the ledger and establishes which are proved and which are open; this chapter is explicit that the correspondence stands on O3 and that O3 is conjectural.

## What this chapter contributes

- **Definitions / Axioms:** *III.D29 — Spectral Parameter Λ(s)*. The map Λ(s) = ι_τ²(s(1−s)−¼); its zero locus (critical line and trivial zeros); its range on the non-negative reals; the geometric interpretation as a translation from the number-theoretic to the spectral domain.
- **Key results:** *III.T18 — Spectral Correspondence Theorem* (τ-effective, conditional on O3): non-trivial zeros of ζ_τ biject with eigenvalues of H_L via Λ(ρ) = λₙ; scope grade explicitly stated as τ-effective pending the Fredholm determinant representation conjecture O3.
- **Dependencies:** *III.D28* (Lemniscate Operator H_L); *III.T17* (Self-adjointness, providing real eigenvalues); *III.D26* (Split-Complex Zeta, providing the zeros); the six proof obligations O1–O6 previewed here and detailed in Chapter 26.

## Lean coverage

This chapter is prose-only at the current release; the Spectral Correspondence Theorem and the Fredholm determinant construction do not yet have corresponding TauLib modules.

## Where this leads

Chapter 25 harvests the spectral consequence: self-adjointness of H_L forces eigenvalues to be real; real eigenvalues in the Λ parameterisation force Im(Λ(ρ)) = 0, which expands to γ(1 − 2σ) = 0, which — since γ ≠ 0 for non-trivial zeros — forces σ = ½. The Critical Line Theorem is the corollary.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part04/ch24-the-spectral-correspondence.tex -->
