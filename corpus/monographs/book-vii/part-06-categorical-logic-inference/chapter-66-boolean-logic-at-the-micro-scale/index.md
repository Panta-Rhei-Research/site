---
layout: "corpus-monograph-chapter"
title: "Chapter 66: Boolean Logic at the Micro Scale"
permalink: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-66-boolean-logic-at-the-micro-scale/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-categorical-logic-inference"
chapter_number: 66
chapter_slug: "chapter-66-boolean-logic-at-the-micro-scale"
page_in_book: 247
prev_chapter_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-65-prayer-as-logos-dialogue/"
prev_chapter_title: "Chapter 65: Prayer as Logos-Dialogue"
next_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-67-bayesian-inference-at-meso-macro-scale/"
next_chapter_title: "Chapter 67: Bayesian Inference at Meso/Macro Scale"
summary_short: "Logic in τ is scale-dependent. At the micro scale—the level of individual NF addresses, single morphisms, and atomic admissibility checks—logic is classical Boolean: bivalent, decidable, and governed by the excluded middle."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/"
canonical_part_title: "Categorical Logic & Inference"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-06-categorical-logic-inference/chapter-66-boolean-logic-at-the-micro-scale/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part VI: Categorical Logic & Inference"
      url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part VI"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 74
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Logic in τ is scale-dependent. At the micro scale—the level of individual NF addresses, single morphisms, and atomic admissibility checks—logic is classical Boolean: bivalent, decidable, and governed by the excluded middle. This chapter opens Part VI by establishing this micro-scale foundation and previewing how logic changes as the scale increases. The Boolean micro-logic is not axiomatized but *earned*: it is recovered from the four-valued Truth4 logic of Book I (Definition I.D21) via the Boolean recovery theorem (Proposition I.P13), which shows that classical logic emerges as the restriction of Truth4 to the interior of the kernel, away from boundary phenomena. The chapter also lays out the plan for Part VI, mapping the logical strata—Boolean, Bayesian, presheaf, Truth4—against the scales and locations at which they govern.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D57 — Boolean Micro-Logic* (τ-effective). Formalizes micro-propositions—existence, commutativity, admissibility, and identity questions about single NF addresses—as the domain where bivalence and truth-functionality hold without residue.
- **Key results:** *VII.T22 — Single-Address Classical Logic* (τ-effective): for any NF address a and any micro-proposition Φ(a), bivalence, excluded middle, non-contradiction, and truth-functional connectives (∧ ∨ ¬ →) all hold. The proof reduces to Proposition I.P13: at single interior addresses, the two spectral sectors agree, so the forgetful map Truth4 → Bool is an isomorphism on this fragment.
- **Dependencies:** Boolean recovery theorem (Proposition I.P13, Book I); Four Truth Values definition (Definition I.D21, Book I); spectral decomposition (Book I, Chapter 44); explosion barrier (Theorem I.T13, Book I).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The formal spine—Definition VII.D57 and Theorem VII.T22—would map directly to a `MicroLogic.Boolean` module once the Book I spectral machinery is formalized.

## Where this leads

With classical logic secured at the micro scale, Chapter 67 asks what happens when questions involve multiple addresses under partial observation, requiring the Bayesian meso-logic. The stratified picture developed across Chapters 66–74 culminates in Chapter 75's diagrammatic-sector synthesis.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part06/ch66.tex -->
