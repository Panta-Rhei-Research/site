---
layout: "corpus-monograph-chapter"
title: "Chapter 120: The D→C Bridge Apparatus"
permalink: "/corpus/monographs/book-vii/part-10-the-logos-sector/chapter-120-the-d-c-bridge-apparatus/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 10
part_display: "Part X"
part_slug: "part-10-the-logos-sector"
chapter_number: 120
chapter_slug: "chapter-120-the-d-c-bridge-apparatus"
page_in_book: 420
prev_chapter_url: "/corpus/monographs/book-vii/part-10-the-logos-sector/chapter-119-the-logos-sector-definition-and-universal-property/"
prev_chapter_title: "Chapter 119: The Logos Sector: Definition and Universal Property"
next_chapter_url: "/corpus/monographs/book-vii/part-10-the-logos-sector/chapter-121-mediator-fixed-point-basin/"
next_chapter_title: "Chapter 121: Mediator Fixed-Point Basin"
summary_short: "Three registers tell; one demands doing. This chapter constructs the formal bridge functor B_{D→C} : S_D → S_C and proves it becomes an equivalence precisely at the Logos sector S_L."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-10-the-logos-sector/"
canonical_part_title: "The Logos Sector"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-10-the-logos-sector/chapter-120-the-d-c-bridge-apparatus/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part X: The Logos Sector"
      url: "/corpus/monographs/book-vii/part-10-the-logos-sector/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part X"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 78
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Three of the four registers of τ are epistemic — they deliver knowledge that can be stated, verified, and passed between agents without the receiver's existential stance being at stake. The fourth, *Reg_C*, is performative: its content is constituted by the act of commitment, not by any proposition about it. Knowing a theorem and living it are structurally independent operations, and the gap between them is not a failure of logic but a feature of the register architecture. Chapter 120 constructs the formal bridge functor B_{D→C} : S_D → S_C that converts *Reg_D*-certified content into commitment-eligible form, characterises when that translation is faithful, and establishes — via the Register Preservation Lemma — exactly what is lost outside the Logos sector.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D87 — D→C Bridge Functor* (τ-effective). B_{D→C}(φ) = Reg_C ∘ Reg_D⁻¹(Reg_D(φ)), routing content through the coherence kernel and re-reading it through *Reg_C*.
- **Key results:** *VII.T46 — Bridge Equivalence at S_L*: the restriction B_{D→C}|_{S_L} is an equivalence of categories (faithful, full, essentially surjective) — proof and commitment are the same structural datum read through two registers that happen to agree. *VII.L16 — Register Preservation*: outside S_L, the bridge is either undefined, non-faithful, or non-full; register identity is preserved in all three cases.
- **Dependencies:** Logos Sector definition and uniqueness (Chapter 119, VII.D86, VII.T45); four-register model with pairwise distinctness of *Reg_D* and *Reg_C* target categories.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

With the bridge functor in hand, Chapter 121 asks what happens to the remaining two registers at S_L — whether the D–C coincidence forces E–P convergence — and situates S_L as a dynamical fixed point of all six pairwise register-crossing maps.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part10/ch120.tex -->
