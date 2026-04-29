---
layout: "corpus-monograph-chapter"
title: "Chapter 3: The Four Registers of Reason"
permalink: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-03-the-four-registers-of-reason/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-metaphysics-definition"
chapter_number: 3
chapter_slug: "chapter-03-the-four-registers-of-reason"
page_in_book: 11
prev_chapter_url: "/corpus/monographs/book-vii/part-00-the-third-self-enrichment/chapter-02-map-of-book-vii/"
prev_chapter_title: "Chapter 2: Map of Book VII"
next_chapter_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-04-selfdesc-of-selfdesc-the-e-structure/"
next_chapter_title: "Chapter 4: SelfDesc-of-SelfDesc: The E₃ Structure"
summary_short: "Every E₃ claim falls into one of four typed registers — empirical, practical, diagrammatic, commitment — each with independent coherence criteria."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/"
canonical_part_title: "The Metaphysics Definition"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-01-the-metaphysics-definition/chapter-03-the-four-registers-of-reason/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part I: The Metaphysics Definition"
      url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part I"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 69
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Every claim a self-modelling observer can make falls into exactly one of four typed registers — empirical (Reg_E), practical (Reg_P), diagrammatic (Reg_D), or commitment (Reg_C) — each of which asks a distinct question, admits independent coherence criteria, and couples to the τ-kernel through a dedicated readout functor. The chapter formalizes these four registers, proves that incoherence in one register does not propagate to any other (the Register Independence Theorem, *VII.T01*), and shows that a wide class of philosophical pseudo-paradoxes dissolves once content is correctly typed. The register model is not a pragmatic classification; it is a structural consequence of the four-sector template that governs every enrichment level, here instantiated at E₃.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D01 — Empirical Register* (Reg_E): the readout functor to observable predictions, with empirical adequacy as its coherence criterion. *VII.D02 — Practical Register* (Reg_P): the readout functor to normative constraints, with normative consistency as its coherence criterion. *VII.D03 — Diagrammatic Register* (Reg_D): the readout functor to structural proofs, with proof-validity as its coherence criterion. *VII.D04 — Commitment Register* (Reg_C): the readout functor to stance-constituted contents, with stance-stability as its coherence criterion.
- **Key results:** *VII.T01 — Register Independence*: for distinct registers X and Y, incoherence of content c in Reg_X entails no conclusion about the coherence of any content in Reg_Y. The proof turns on the fact that the four readout functors have pairwise disjoint codomain categories, with no coherence-propagating natural transformation between them — the sole exception being the Logos sector where Reg_D and Reg_C coincide by construction.
- **Notation introduced:** Reg_E, Reg_P, Reg_D, Reg_C for the four typed readout functors; Coh_E, Coh_P, Coh_D, Coh_C for their respective coherence predicates; the four register questions (observe / do / prove / live-as-true).
- **Dependencies:** E₃ enrichment layer and the MetaDecode operator (Chapter 4 provides the structural grounding, cross-referenced prospectively); the four holonomy sectors at E₁ (Book IV, Part I) whose independence is lifted through E₂ to E₃.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The Lean module `TauLib.BookVII.Meta.Saturation` carries type signatures related to the enrichment ladder that depends on register independence, but the register definitions themselves are not yet formalized.

## Where this leads

The 4+1 sector decomposition (Chapter 5) assigns each register to its corresponding metaphysics sector, grounding the register model in the concrete sector template. The Saturation Theorem (Chapter 8) will then close the door: no fifth register arises because no fifth enrichment layer exists.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part01/ch03.tex -->
