---
layout: "corpus-monograph-chapter"
title: "Chapter 72: Truth and Truth-Makers"
permalink: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-72-truth-and-truth-makers/"
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
chapter_number: 72
chapter_slug: "chapter-72-truth-and-truth-makers"
page_in_book: 265
prev_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-71-inference-as-categorical-necessity/"
prev_chapter_title: "Chapter 71: Inference as Categorical Necessity"
next_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-73-modal-logic-in-tau/"
next_chapter_title: "Chapter 73: Modal Logic in τ"
summary_short: "What makes a proposition true? This chapter reformulates the question in categorical terms: truth-bearers are sections of presheaves, truth-makers are the structural data that ground section-existence, and correspondence and coherence unify as two faces of the sheaf equalizer condition."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/"
canonical_part_title: "Categorical Logic & Inference"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-06-categorical-logic-inference/chapter-72-truth-and-truth-makers/"
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

What makes a proposition true? The philosophical tradition offers two rival answers: correspondence theory (truth as match between proposition and fact) and coherence theory (truth as consistency within a system of beliefs). This chapter reformulates the question in categorical terms. Truth-bearers are candidate global sections {s_i ∈ F(U_i)} of a presheaf F over τ; a truth-bearer is true when the local data satisfy the gluing condition s_i|_{U_i ∩ U_j} = s_j|_{U_i ∩ U_j} and a unique global section exists. Truth-makers are the structural data in τ—local groundings, overlap compatibility witnesses, and global assembly—that certify section-existence. The Alethic Unification Theorem (VII.T27) shows that correspondence and coherence are not rival theories but the two directions of the sheaf equalizer: a compatible family (coherence) determines a unique global section (correspondence), and conversely.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D60 — Truth-Maker in τ* (τ-effective): a structural witness consisting of (TM1) local grounding morphisms, (TM2) overlap-compatibility commuting diagrams, and (TM3) global assembly via sheafification. *VII.D61 — Truth-Bearer as Section* (τ-effective): a candidate global section; true when it glues, false when the local data fail to cohere on overlaps.
- **Key results:** *VII.T27 — Alethic Unification* (τ-effective): correspondence (section-existence) and coherence (overlap-agreement) are structurally identical—both expressed by the sheaf equalizer condition—so the historical debate dissolves. *VII.P16 — Alethic Pluralism* (τ-effective): each of the four registers (Reg_D, Reg_E, Reg_P, Reg_C) admits truth-making through the same categorical architecture, but with different sites, presheaves, and covering families; truth is register-relative in its mechanisms but architecturally uniform.
- **Dependencies:** presheaf topos τ̂ and subobject classifier Ω (earlier parts); knowledge-as-sections (Chapter on knowledge, Book VII); four registers (Part I).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The sheaf-equalizer proof of VII.T27 is directly available in Mathlib's sheaf machinery and would require minimal additional scaffolding to specialize to the τ setting.

## Where this leads

Chapter 73 extends the logical architecture to modal operators □ and ◇, reconstructing Kripke semantics categorically as adjoint functors over a presheaf of possible worlds with accessibility morphisms.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part06/ch72.tex -->
