---
layout: "corpus-monograph-chapter"
title: "Chapter 27: e Earned — The Self-Reproducing Growth Base"
permalink: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-27-e-earned-the-self-reproducing-growth-base/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e"
chapter_number: 27
chapter_slug: "chapter-27-e-earned-the-self-reproducing-growth-base"
page_in_book: 129
prev_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-26-three-perspectives-on-pi/"
prev_chapter_title: "Chapter 26: Three Perspectives on π"
next_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-28-replaces-i-polarity-not-rotation/"
next_chapter_title: "Chapter 28: Replaces i — Polarity, Not Rotation"
summary_short: "The ν-iterator in the generator ladder ρ → μ → ν → θ compounds p_{k+1} refinement steps at each primorial stage, producing e = lim(1 + 1/n)^n as the inevitable Archimedean scaling eigenvalue — the unique self-reproducing growth base."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
canonical_part_title: "Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-27-e-earned-the-self-reproducing-growth-base/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part V: Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
      url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part V"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 24
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapter 26 earned π from three convergent angular perspectives. This chapter earns e from a single, unavoidable radial source: the **ν-iterator** in the generator ladder ρ → μ → ν → θ (I.D04, Book I). Where π is geometric — arising from solenoidal circles in the A/B/C directions — e is arithmetic, arising from stage-to-stage compounding in the D-direction. At each stage k, the ν-iterator applies the refinement map x ↦ x · (1 + 1/p_{k+1}) a total of p_{k+1} times, scaling the coordinate by (1 + 1/p_{k+1})^{p_{k+1}} modulo P_{k+1}. This is an exact integer operation in earned index arithmetic (I.D06, Book I) at every finite stage. As k grows and p_{k+1} → ∞, the scaling factor converges in the Archimedean completion to *e* = 2.71828…, defined as the *ν-eigenvalue* (*II.D30*). The convergence rate along primes is O(1/p_{k+1}) ~ O(1/(k ln k)) — moderate for the compounding formula, but the exponential series partial sums e_k = ∑_{m=0}^{k} 1/m! achieve super-exponential accuracy |e_k − e| ≤ 3/(k+1)!, representable in the CRT tower whenever k! divides P_k. *II.T23* (*e from Index Arithmetic*) establishes: (i) computability at every finite stage, (ii) convergence rate bounds for both formulations, and (iii) Hermite's transcendence result — e is not a finite-stage rational, existing only at the profinite limit. The *growth base* characterization (*II.D31*) pins e uniquely: it is the only b > 0 satisfying lim_{n→∞} n(b^{1/n} − 1) = 1 (equivalently, the unique base whose exponential is its own derivative). This self-reproduction property makes e the structural scaling eigenvalue of the tower, not an imported constant. Unlike π, e does not arise from circles; the B/C angular channels are calibrated by π, the D radial growth rate is calibrated by e. The two constants are structurally independent and will be combined in Chapter 29 as ι_τ = 2/(π + e).

## What this chapter contributes

**Definitions / Axioms**
- *II.D30* — e as ν-eigenvalue: e_ν = lim_{k→∞} (1 + 1/p_{k+1})^{p_{k+1}}, the Archimedean limit of the ν-iterator's scaling factor
- *II.D31* — Growth base: the unique b > 0 satisfying lim_{n→∞} n(b^{1/n} − 1) = 1; e is the unique such base with log b = 1

**Key results**
- *II.T23* — *e from Index Arithmetic*: the compounding sequence and exponential series are both computable in earned index arithmetic; convergence rates O(1/n) and O(1/(k+1)!) respectively; e is transcendental over ℚ (Hermite 1873)

**Notation**
- e_k = ∑_{m=0}^{k} 1/m! for stage-k approximant; ê ∈ ℤ̂ for the profinite avatar; e_p ∈ ℤ_p for the p-adic projection

**Dependencies**
- *I.D04* (generator ladder), *I.D06* (index arithmetic), *I.T05*, *I.T35*, *II.D14*, *II.D15*, *II.T20* (R as inverse limit), *II.T21*, *II.T22* (π)

## Lean coverage

`BookII.Transcendentals.EEarned` (planned). No Lean proofs present at this writing.

## Where this leads

With e earned alongside π, Chapter 28 supplies the algebraic constant j (the split-complex unit j² = +1), and Chapter 29 confirms ι_τ = 2/(π + e) ≈ 0.341304 with both constants now having full τ-internal content. The growth-rate role of e reappears in Part VI when holomorphic extension bounds are controlled by radial e-scaling.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part05/ch26-e-earned.tex -->
