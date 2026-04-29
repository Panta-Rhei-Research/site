---
layout: "corpus-monograph-chapter"
title: "Chapter 34: Positive Regularity"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-34-positive-regularity/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-the-physics-layer"
chapter_number: 34
chapter_slug: "chapter-34-positive-regularity"
page_in_book: 175
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-33-the-hartogs-flow-operator/"
prev_chapter_title: "Chapter 33: The Hartogs Flow Operator"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-35-the-strong-sector-and-nf-discreteness/"
next_chapter_title: "Chapter 35: The Strong Sector and NF Discreteness"
summary_short: "The Positive Regularity Theorem *III.T25* assembles three conditions — clopen locality, ω-germ determinacy, and defect-horizon contractivity — to guarantee stabilised ω-germs for all τ-admissible data; blow-up is structurally impossible, not merely bounded."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-34-positive-regularity/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part V: The Physics Layer"
      url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part V"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 36
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

We prove the capstone theorem of Part V. For every τ-admissible initial datum, the Hartogs flow operator produces a stabilised ω-germ (*III.D42*) at every point of the clopen cylinder domain. The proof assembles three conditions from the preceding chapters: clopen locality (Chapter 31), ω-germ determinacy (Chapter 33), and defect-horizon contractivity (Chapter 32). Together they guarantee that the defect functional Δ converges to zero along the primorial tower, which is the τ-internal definition of regularity. This chapter then explains in structural — not analytic — terms why blow-up cannot occur, and closes with NS export contracts (*III.R18*) for downstream Parts.

## What this chapter contributes

The stabilised ω-germ (*III.D42*) is defined precisely: the primorial tower of evaluations becomes eventually constant at each point, and the stabilisation depth N_x records where. The germ value is the eventual common value; it is a character in ℤ² with well-defined ABCD sector projections. The stabilisation depth is bounded above by the admissibility cutoff of the initial datum, so the computational cost of verifying regularity is always finite.

The 3-Condition Sufficiency proposition (*III.P15*) isolates the three conditions as an independent logical unit, making the Positive Regularity Theorem (*III.T25*) a direct corollary. Condition (i) — clopen locality — ensures that the Hartogs flow operator acts on each cylinder patch independently, with no long-range interaction. Condition (ii) — ω-germ determinacy — ensures that the primorial tower of germ values is eventually constant, which is exactly the stabilisation condition. Condition (iii) — defect-horizon contractivity — ensures that the defect Δ(x,k) is strictly decreasing in k and converges to zero, which by the tower-coherence lemma forces stabilisation. The three conditions together are not merely sufficient but minimal: removing any one of them yields a class of counterexamples.

The blow-up impossibility argument is structural: bounded ABCD extraction prevents component divergence; K5 sector isolation prevents cascade between sectors; one-prime-at-a-time refinement prevents new defect accumulation at each primorial step. No PDE inequality is needed — the architecture of the primorial tower makes divergence combinatorially impossible. The scope declaration is precise: τ-regularity is proved for τ-admissible data; the representability question (whether every Schwartz-class datum on ℝ³ has a τ-admissible approximation tower) is open and deferred to Part X. The NS export contracts (*III.R18*) list five deliverables — positive regularity mechanism, H_flow, defect framework, operator polarity swap, and K5 sector isolation — each with explicit preconditions and postconditions for downstream consumers.

## Lean coverage

- *III.T25* — Positive Regularity Theorem (τ-effective)
- *III.D42* — Stabilised ω-Germ (τ-effective)
- *III.P15* — 3-Condition Sufficiency (τ-effective)
- *III.R18* — NS Export Contracts

## Where this leads

This chapter closes the NS block (Chapters 31–34). Its five exports are consumed by: Part X (classical bridge to Clay NS), Books IV–V (physical instantiation of H_flow), Parts VI–VII (defect functional reuse for BSD and Yang–Mills), and every subsequent Millennium block (K5 sector isolation as universal cascade prevention).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch37-positive-regularity.tex -->
