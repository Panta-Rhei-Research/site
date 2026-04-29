---
layout: "corpus-monograph-chapter"
title: "Chapter 73: Modal Logic in τ"
permalink: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-73-modal-logic-in-tau/"
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
chapter_number: 73
chapter_slug: "chapter-73-modal-logic-in-tau"
page_in_book: 269
prev_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-72-truth-and-truth-makers/"
prev_chapter_title: "Chapter 72: Truth and Truth-Makers"
next_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-74-paraconsistent-logic-at-boundaries/"
next_chapter_title: "Chapter 74: Paraconsistent Logic at Boundaries"
summary_short: "Necessity, possibility, and possible worlds receive a categorical treatment. Kripke frames are reconstructed as presheaves over a category of worlds with accessibility morphisms, and the modal operators □ and ◇ arise as adjoint functors over accessible worlds."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/"
canonical_part_title: "Categorical Logic & Inference"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-06-categorical-logic-inference/chapter-73-modal-logic-in-tau/"
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

Necessity, possibility, and possible worlds receive a categorical treatment. Kripke frames are reconstructed as presheaves over an internal category of worlds W with a distinguished class R of accessibility morphisms; the classical triple (W, R, V) becomes (W-object, R-morphisms, V-presheaf) in τ̂. The modal operators □ (necessity) and ◇ (possibility) arise as adjoint functors: □ = ∀_π is the right adjoint to pullback along the source projection π: R → W, and ◇ = ∃_π is the left adjoint. The duality □P = ¬◇¬P is then a consequence of the adjunction, not an axiom. Different modal systems—K, T, S4, S5—correspond to different structural constraints on R: unconstrained, reflexive, reflexive-transitive, and equivalence, respectively. Because morphisms compose but relations merely hold, transitivity in S4 (□P → □□P) becomes a categorical tautology about composable accessibility morphisms.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D62 — Modal Frame in τ* (τ-effective): the triple (W, R, V) categorified as internal-category object, morphism class, and valuation presheaf over the subobject classifier Ω of τ̂. *VII.D63 — Accessibility Morphism* (τ-effective): a morphism r: w → w' in W belonging to R; different closure conditions on R yield systems K, T, S4, S5.
- **Key results:** *VII.T28 — Kripke Soundness in τ* (τ-effective): formulas valid in every Kripke frame whose accessibility relation satisfies R's constraints are internally valid in τ̂; the result covers K, T, S4, and S5 under the respective constraints. *VII.L09 — Modal Collapse Prevention* (τ-effective): if W contains at least two non-isomorphic worlds and R is a proper subclass of Mor(W), then □P ↔ P fails for some P—modality is non-vacuous. The chapter further shows that alethic, deontic, and epistemic modality are instantiations of the same categorical architecture under different choices of W and R.
- **Dependencies:** presheaf topos τ̂ and subobject classifier Ω; truth-makers (Chapter 72, VII.D60, VII.D61); worlds-topos construction (earlier in Book VII).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The adjunction ◇ ⊣ π* ⊣ □ is a standard construction in the internal logic of presheaf topoi and is in principle formalizable in Lean 4 using Mathlib's category-theoretic adjunction API.

## Where this leads

Chapter 74 addresses the boundary region of the logical landscape: where the two spectral sectors disagree, the four-valued Truth4 logic becomes indispensable, and paraconsistency with the explosion barrier as containment takes over from classical Boolean reasoning.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part06/ch73.tex -->
