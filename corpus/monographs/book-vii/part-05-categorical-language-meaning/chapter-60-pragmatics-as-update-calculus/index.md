---
layout: "corpus-monograph-chapter"
title: "Chapter 60: Pragmatics as Update Calculus"
permalink: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-60-pragmatics-as-update-calculus/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-categorical-language-meaning"
chapter_number: 60
chapter_slug: "chapter-60-pragmatics-as-update-calculus"
page_in_book: 227
prev_chapter_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-59-reference-and-indexicals/"
prev_chapter_title: "Chapter 59: Reference and Indexicals"
next_chapter_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-61-translation-and-universality/"
next_chapter_title: "Chapter 61: Translation and Universality"
summary_short: "Each utterance is an endofunctor on the category of discourse states. Austin's trichotomy, Searle's five illocutionary types, and Grice's maxims are unified in an update calculus where conversation is sequential endofunctor composition. Performatives are the linguistic entry point of the commitment register."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/"
canonical_part_title: "Categorical Language & Meaning"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-05-categorical-language-meaning/chapter-60-pragmatics-as-update-calculus/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part V: Categorical Language & Meaning"
      url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part V"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 73
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Linguistic communication involves more than reference. When a speaker says "Close the door," the utterance transforms the shared context between speaker and hearer by imposing a practical obligation. This chapter formalizes that transformative dimension by treating pragmatics as an update calculus. A discourse state D is the shared informational and normative context between interlocutors—what has been asserted, questioned, and committed to. A pragmatic update operator U_α is an endofunctor U_α : Disc → Disc indexed by illocutionary type α ∈ {assert, direct, commit, express, declare}, satisfying three conditions: content integration (the propositional content p enters the appropriate component of D), force realization (the transition D → U_α(D) realizes the illocutionary force), and compositionality (successive speech acts compose, recording the conversational history as a trajectory D₀ → D₁ → D₂ → …). Austin's locutionary/illocutionary/perlocutionary trichotomy maps cleanly: the locutionary act is readout-functor evaluation; the illocutionary act is the update proper; the perlocutionary act is a consequence in the hearer's internal state. Searle's five illocutionary types become five distinct endofunctor species. Questions are preparatory operators that partition the space of possible updates without selecting a cell. Grice's four maxims are naturality constraints on the update functor: the update must commute with rational expectations (quantity: bounded non-triviality; quality: truth-preservation; relation: active-partition targeting; manner: readout efficiency). Performatives—utterances that constitute the acts they describe—are declarations that simultaneously update propositional and normative components, and they are the linguistic entry point of the commitment register Reg_C.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D54 — Pragmatic Update Operator* (τ-effective). U_α : Disc → Disc, indexed by illocutionary type α, satisfying content integration (U1), force realization (U2), and compositionality (U3).
- **Key results:** none in formal-derivation form; this chapter establishes Grice's maxims as naturality constraints and the Grice flouting/violating distinction as visible versus hidden failure of naturality. Felicity conditions for performatives are naturality constraints on U_declare.
- **Notation introduced:** Disc (category of discourse states); U_α (pragmatic update operator); discourse trajectory D₀ → D₁ → D₂.
- **Dependencies:** reference morphism (Chapter 59); readout functor; four-register architecture Reg_E, Reg_P, Reg_D, Reg_C.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The update-calculus formalism is defined textually; dynamic-semantics connections to existing categorical logic frameworks are noted but not yet formalized in TauLib.

## Where this leads

The discourse-state machinery developed here underpins the treatment of translation in Chapter 61 (illocutionary force is a kernel property preserved across languages) and reappears in the alignment analysis of Chapter 64, where naturality of the update functor is one of the three conditions for an aligned language model.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part05/ch60.tex -->
