---
layout: "corpus-monograph-chapter"
title: "Chapter 5: The 4+1 Sector Decomposition at E₃"
permalink: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-05-the-4-1-sector-decomposition-at-e/"
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
chapter_number: 5
chapter_slug: "chapter-05-the-4-1-sector-decomposition-at-e"
page_in_book: 18
prev_chapter_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-04-selfdesc-of-selfdesc-the-e-structure/"
prev_chapter_title: "Chapter 4: SelfDesc-of-SelfDesc: The E₃ Structure"
next_chapter_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-06-sector-witness-bundles-vacua-and-normalizers/"
next_chapter_title: "Chapter 6: Sector Witness Bundles, Vacua, and Normalizers"
summary_short: "The 4+1 template is instantiated at E₃: four pure sectors correspond to the four registers; Logos sector S_L is where proof-validity equals stance-stability."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/"
canonical_part_title: "The Metaphysics Definition"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-01-the-metaphysics-definition/chapter-05-the-4-1-sector-decomposition-at-e/"
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

The abstract 4+1 sector template — discovered in Book III, Part II and already instantiated at E₁ (physics) and E₂ (life) — is here concretely instantiated at E₃, the metaphysics layer. The four pure sectors S_E, S_P, S_D, and S_C collect all E₃-admissible contents whose coherence is governed by the empirical, practical, diagrammatic, and commitment registers respectively. The mixed Logos sector S_L is the unique sector where the diagrammatic and commitment registers coincide: content is in S_L when its proof-validity and its stance-stability are mutually witnessing. The Sector Decomposition Theorem proves that every E₃-admissible content belongs to exactly one of the five sectors, and the Sector Independence Proposition restates Register Independence at the sector level.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D07 — Metaphysics Sector S_E* (τ-effective): all E₃-admissible contents whose coherence equals Coh_E; sector question "What do I observe?" *VII.D08 — Metaphysics Sector S_P* (τ-effective): coherence governed by Coh_P; sector question "What should I do?" *VII.D09 — Metaphysics Sector S_D* (τ-effective): coherence governed by Coh_D; sector question "What can I prove?" *VII.D10 — Metaphysics Sector S_C* (τ-effective): coherence governed by Coh_C; sector question "What am I willing to live as true?" *VII.D11 — Logos Sector S_L* (τ-effective): the unique mixed sector defined by Coh_D(c) = Coh_C(c); named by its universal property, not by theological intent.
- **Key results:** *VII.T03 — Sector Decomposition at E₃* (τ-effective): every E₃-admissible content belongs to exactly one of S_E ⊔ S_P ⊔ (S_D \ S_L) ⊔ (S_C \ S_L) ⊔ S_L; proof turns on codomain-distinctness of the four readout functors and the fact that only Proof and Stance admit a natural transformation. *VII.P01 — Sector Independence at E₃*: the four pure sectors are pairwise independent, a direct corollary of VII.T01.
- **Notation introduced:** S_E, S_P, S_D, S_C, S_L for the five metaphysics sectors; Adm_{E₃} for the set of E₃-admissible contents; the sector periodic table mapping each sector to its Book VII parts and chapter range.
- **Dependencies:** Register Independence Theorem (Chapter 3, VII.T01); E₃ Non-Emptiness (Chapter 4, VII.T02); abstract 4+1 template (Book III, Part II).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The sector type signatures are anticipated in future development of `TauLib.BookVII.Meta`.

## Where this leads

Chapter 6 equips each sector with its operational machinery — witness bundles, defect functionals, vacua, and normalisers — converting the static classification into a working diagnostic apparatus. The Logos sector S_L receives its full treatment in Part X.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part01/ch05.tex -->
