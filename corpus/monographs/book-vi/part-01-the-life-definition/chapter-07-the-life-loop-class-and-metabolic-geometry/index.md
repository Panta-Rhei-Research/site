---
layout: "corpus-monograph-chapter"
title: "Chapter 7: The Life Loop Class and Metabolic Geometry"
permalink: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-07-the-life-loop-class-and-metabolic-geometry/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-life-definition"
chapter_number: 7
chapter_slug: "chapter-07-the-life-loop-class-and-metabolic-geometry"
page_in_book: 35
prev_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-06-the-layer-separation-lemma-life-is-genuinely-e/"
prev_chapter_title: "Chapter 6: The Layer Separation Lemma: Life Is Genuinely E₂"
next_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-08-the-4/"
next_chapter_title: "Chapter 8: The 4+"
summary_short: "The Life Loop Class Loop_L packages Distinction and SelfDesc into a homotopy-theoretic triple (D, γ, h). DecodeTarget and DecodeHorizon operators extract phenotype and genotype. The Metabolic Fiber Theorem factors every Life loop through source (γ) and closure (η) sub-classes, and Consumer Mixer Uniqueness identifies the unique mixed sector on (γ, η)."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
canonical_part_title: "The Life Definition"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-01-the-life-definition/chapter-07-the-life-loop-class-and-metabolic-geometry/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part I: The Life Definition"
      url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part I"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 60
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

Chapters 4 and 5 defined the two earned predicates separately. This chapter packages them — and the metabolic dynamics they generate — into a single formal object: the Life Loop Class Loop_L. A Life Loop is a triple (D, γ, h): the distinction D: X → 2_τ satisfying SelfDesc, a metabolic cycle γ: [0,1] → End_SD(X) that is a closed path in the monoid of SelfDesc-preserving endomorphisms returning to id_X up to basin equivalence, and h ∈ π₁(End_SD(X), id_X) the homotopy class of γ. The homotopy class captures the topological type of the metabolic cycle — winding number — independent of speed. Two operators extract structure from the blueprint ball B_n. DecodeTarget selects the unique element of B_n with minimal defect V_n(x): the system's phenotype target, the optimal state toward which the metabolic cycle drives the carrier. DecodeHorizon extracts the ω-germ code constant across B_n — the stable genotype. The τ³ fibration τ³ = τ¹ ×_f T² organises the Life loop through the metabolic fiber pair (γ, η): the γ-circle carries source (production) winding and the η-circle carries closure (recycling) winding. The Metabolic Fiber Theorem proves that every Life loop factors through both sub-classes — every living system produces and recycles — because a loop with trivial source cannot maintain the evaluator's own substrate, and one with trivial closure accumulates waste and violates basin stability. The Consumer Mixer Uniqueness theorem then identifies the unique admissible mixed sector on (γ, η): base–base and base–fiber mixings are excluded by the fibration constraint; only the fiber–fiber pair is admissible. This result corrects the first edition's placement of the Life mixer on (α, π).

## What this chapter contributes

- **Definitions / Axioms:** *VI.D08 — Life Loop Class Loop_L*: the triple (D, γ, h) and equivalence under SelfDesc-preserving homotopy. *VI.D09 — DecodeTarget*: argmin of the defect functional on the blueprint ball. *VI.D10 — DecodeHorizon*: the ω-germ code constant across the blueprint ball. *VI.D11 — Source Sub-Class Loop_src*: Life Loops with nontrivial γ-winding. *VI.D12 — Closure Sub-Class Loop_rec*: Life Loops with nontrivial η-winding.
- **Key results:** *VI.T05 — Metabolic Fiber Theorem*: Loop_L ↪ Loop_src × Loop_rec × Loop_base canonically; both source and closure windings are nontrivial for every Life loop. *VI.T06 — Consumer Mixer Uniqueness*: the unique admissible Life mixer sits on the fiber pair (γ, η), not on (α, π). *VI.L03 — Loop Factorization Lemma*: any metabolic cycle decomposes uniquely into source, closure, and base components via π₁(τ³) ≅ π₁(τ¹) × ℤ².
- **Dependencies:** Chapters 4 and 5 (τ-Distinction, SelfDesc); Book III (τ³ = τ¹ ×_f T² fibration; 4+1 template; signature rigidity).

## Lean coverage

`TauLib.BookVI.Life.LoopClass`

## Where this leads

Chapter 8 uses the Metabolic Fiber Theorem and the Consumer Mixer Uniqueness result established here to construct the complete 4+1 Life sector classification at E₂.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part01/ch07-life-loop-class.tex -->
