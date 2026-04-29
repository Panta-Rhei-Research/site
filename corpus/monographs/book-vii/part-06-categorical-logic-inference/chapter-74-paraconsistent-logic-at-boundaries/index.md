---
layout: "corpus-monograph-chapter"
title: "Chapter 74: Paraconsistent Logic at Boundaries"
permalink: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-74-paraconsistent-logic-at-boundaries/"
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
chapter_number: 74
chapter_slug: "chapter-74-paraconsistent-logic-at-boundaries"
page_in_book: 272
prev_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-73-modal-logic-in-tau/"
prev_chapter_title: "Chapter 73: Modal Logic in τ"
next_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-75-the-diagrammatic-sector-synthesis/"
next_chapter_title: "Chapter 75: The Diagrammatic Sector Synthesis"
summary_short: "At the lemniscate boundary 𝕃 = S¹ ∨ S¹, the two spectral sectors of the bipolar algebra can disagree, producing the overdetermined truth value B. This chapter develops the philosophical import of Book I's Truth4 logic and explosion barrier: contradictions at boundaries are genuine structural phenomena, contained by spectral orthogonality rather than ruled out."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/"
canonical_part_title: "Categorical Logic & Inference"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-06-categorical-logic-inference/chapter-74-paraconsistent-logic-at-boundaries/"
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

At the lemniscate boundary 𝕃 = S¹ ∨ S¹, the two spectral sectors of the bipolar algebra can disagree: one sector confirms a predicate while the other denies it. The result is the overdetermined truth value B—a structurally real contradiction. This chapter develops the philosophical import of Book I's four-valued logic (Definition I.D21) and the explosion barrier (Theorem I.T13). The natural logic of τ is not Boolean but four-valued; contradictions at boundaries are genuine phenomena rather than defects; and yet the system does not collapse because the spectral decomposition blocks explosion through the orthogonality e₊ · e₋ = 0 of the idempotent sectors. Classical logic governs the interior (where both sectors agree and the Boolean recovery theorem applies); paraconsistent logic governs the boundary. These are not rival logics but different strata of the same structural landscape, distinguished by topology. Dialetheias—true contradictions in Graham Priest's sense—receive a precise geometric interpretation: they are gluing obstructions, local sections of the truth-value presheaf that cohere on each lobe of 𝕃 but fail to glue at the crossing point.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D64 — Paraconsistent Boundary Logic* (τ-effective). Restricts Truth4 to boundary propositions—those requiring information from the crossing point of 𝕃—and characterizes the regime by four-valuedness, paraconsistency (P ∧ ¬P ⊬ Q), and locality (classical logic recovers in the interior via Proposition I.P13).
- **Key results:** *VII.T29 — No-Explosion at Boundaries* (τ-effective): from val(P) = B it does not follow that val(Q) = T for arbitrary Q; the proof is the philosophical application of Theorem I.T13 (explosion barrier). *VII.L10 — Truth4 Paraconsistency* (τ-effective): Truth4 satisfies the standard definition of paraconsistency—under both the polarity-swap negation σ and the conflation negation ∼, P ∧ ¬P evaluates to F or B, not T, and no inference rule of Truth4 derives val(Q) = T from these values. The chapter also treats the liar paradox: the liar receives val(L) = B by the same spectral mechanism, contained by the explosion barrier—not an ad hoc resolution but a boundary-phenomenon diagnosis.
- **Dependencies:** Truth4 logic (Definition I.D21, Book I); explosion barrier (Theorem I.T13, Book I); Boolean recovery (Proposition I.P13, Book I); spectral decomposition (Book I, Chapter 44); Boolean micro-logic (Chapter 66, VII.T22).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The formal spine—orthogonality e₊ · e₋ = 0 and its consequence VII.T29—is a direct corollary of the bipolar algebra formalization in Book I's TauLib modules once those are released.

## Where this leads

Chapter 75 closes the diagrammatic sector by synthesizing the pattern–symbol–proof arc across Parts IV–VI and identifying the precise boundary at which the diagrammatic register must yield to the practical register.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part06/ch74.tex -->
