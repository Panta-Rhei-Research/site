---
layout: "corpus-monograph-chapter"
title: "Chapter 68: Internal Randomness"
permalink: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-68-internal-randomness/"
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
chapter_number: 68
chapter_slug: "chapter-68-internal-randomness"
page_in_book: 253
prev_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-67-bayesian-inference-at-meso-macro-scale/"
prev_chapter_title: "Chapter 67: Bayesian Inference at Meso/Macro Scale"
next_chapter_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/chapter-69-no-external-randomness/"
next_chapter_title: "Chapter 69: No External Randomness"
summary_short: "Randomness in τ is not imported from outside but arises from the internal structural complexity of the kernel's constructions. A process appears random when its description cannot be compressed below its own length—when it is, in the technical sense, incompressible."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-06-categorical-logic-inference/"
canonical_part_title: "Categorical Logic & Inference"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-06-categorical-logic-inference/chapter-68-internal-randomness/"
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

Randomness, in τ, is not imported from outside. It arises from the internal structural complexity of the kernel's constructions. A process appears random when its description cannot be compressed below its own length—when it is, in the technical sense, incompressible: K(C) ≥ |C| − c for a fixed constant c independent of the construction's size. This chapter formalizes internal randomness as a τ-concept, connects it to Kolmogorov complexity measured against the NF address system, and shows that quantum indeterminacy (Book IV) is a special case. The apparent randomness of quantum measurement outcomes is not external noise injected into a deterministic substrate but the incompressibility of the T² fiber's internal structure as seen from the observer's meso-scale perspective. The distinction between genuine and apparent randomness reduces to structural versus perspectival incompressibility—both features of the kernel, neither originating outside it.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D59 — Internal Randomness* (τ-effective). A construction C ∈ τ is internally random when K(C) ≥ |C| − c, where K(C) is Kolmogorov complexity relative to the NF address system and c is an overhead constant independent of C. The definition makes randomness structural, not provenance-based.
- **Key results:** *VII.P15 — Randomness as Internal Complexity* (τ-effective): any apparent randomness is either (i) genuine incompressibility relative to the full NF address system, or (ii) perspectival incompressibility due to the observer's limited access. In neither case is randomness imported from outside τ. Applied to quantum mechanics: the Born rule probabilities are Bayesian credences arising from the T² fiber's incompressibility, with no hidden variables and no physical wavefunction collapse.
- **Dependencies:** terminality of τ (Book I, Axiom K0); Bayesian meso-logic (Chapter 67, VII.D58); T² fiber structure (Book IV).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A future `Randomness.Internal` module would formalize the Kolmogorov complexity definition over the NF address system and state Proposition VII.P15 as a structural theorem.

## Where this leads

Chapter 69 draws the complementary conclusion: because the kernel is terminal, there is no external source of randomness at all, and the classical determinism–indeterminism debate is thereby dissolved.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part06/ch68.tex -->
