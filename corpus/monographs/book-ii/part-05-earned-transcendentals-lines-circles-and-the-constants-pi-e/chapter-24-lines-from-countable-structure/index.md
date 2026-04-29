---
layout: "corpus-monograph-chapter"
title: "Chapter 24: Lines from Countable Structure"
permalink: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-24-lines-from-countable-structure/"
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
chapter_number: 24
chapter_slug: "chapter-24-lines-from-countable-structure"
page_in_book: 113
prev_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-23-orthodox-vs-tau-denotation-bridge/"
prev_chapter_title: "Chapter 23: Orthodox vs.\\ τ Denotation Bridge"
next_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-25-circles-from-solenoidal-structure/"
next_chapter_title: "Chapter 25: Circles from Solenoidal Structure"
summary_short: "The α-ray — a countable, ultrametric radial sequence in the D-coordinate — is taken to its inverse limit, recovering ℝ as the Archimedean shadow of the primorial grid system without positing an uncountable continuum."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
canonical_part_title: "Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-24-lines-from-countable-structure/"
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

Part IV built the denotation map den : τ³ → ℝ⁴ and confirmed it preserves all Tarski axioms, but ℝ appeared there as a target — a pre-existing Archimedean completion. This chapter earns ℝ from the inside. The *α-ray* ℓ_α = {α_n : n ≥ 1} ∪ {ω} is the canonical radial sequence in the D-coordinate of the ABCD chart (I.D17, Book I): countable, discrete, and equipped with an ultrametric d(α_m, α_n) = 2^{−min(m,n)}. Level circles Λ_k^X at each NF depth k provide the transverse slices that fold the angular directions. The primorial grids G_k = (1/P_k)ℤ ∩ [0,1) refine super-exponentially — spacing 1/P_k shrinks faster than any geometric sequence — and their inverse limit recovers the real line via nested intervals. *II.T20* (*R as Inverse Limit*) makes this precise: ℝ ≅ lim_← (1/P_k)ℤ, every coherent grid sequence determining a unique real number by intersection. No uncountable continuum is assumed; the Cantor diagonal is inapplicable to the structured CRT refinement sequence, consistent with I.T35 (Book I). The profinite D-line ℓ_D and the Archimedean interval [0,1) are two completions of the same discrete data: ℓ_D retains the ultrametric, [0,1) retains the ordering. Lines emerge from the radial direction; the chapter closes by previewing how level circles form an angular inverse system whose limit — the solenoidal circle — will be the subject of Chapter 25.

## What this chapter contributes

**Definitions / Axioms**
- *II.D24* — α-ray line ℓ_α: the countable radial sequence {α_n} ∪ {ω} in the D-coordinate with its ultrametric
- *II.D25* — Level circle Λ_k^X: the finite cyclic transverse slice at NF depth k in each angular direction X ∈ {A, B, C}

**Key results**
- *II.T20* — *R as Inverse Limit*: ℝ ≅ lim_← (1/P_k)ℤ; coherent primorial grid sequences biject with real numbers via nested intervals; no uncountable continuum required

**Notation**
- G_k := (1/P_k)ℤ ∩ [0,1) for the stage-k primorial grid; ℓ_D for the profinite D-line

**Dependencies**
- *I.T04* (CRT independence), *I.T18* (stage-k reductions), *I.T35* (Cantor refutation), *I.D19* (boundary ring), *II.D13* (ultrametric distance), *II.D14*, *II.D15*, *II.T11* (ABCD four-dimensional chart)

## Lean coverage

`BookII.Transcendentals.Lines` (planned). No Lean proofs present at this writing.

## Where this leads

The level circles Λ_k^X form angular inverse systems whose Archimedean limits are solenoidal circles (Chapter 25), and those circles supply the geometric arena in which π is earned (Chapter 26). The radial/angular split established here — lines from the D-direction, circles from the A/B/C directions — underlies the full calibration dictionary of Part V.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part05/ch23-lines-countable.tex -->
