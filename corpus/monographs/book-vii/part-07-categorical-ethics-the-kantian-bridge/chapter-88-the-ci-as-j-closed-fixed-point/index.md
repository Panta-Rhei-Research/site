---
layout: "corpus-monograph-chapter"
title: "Chapter 88: The CI as j-Closed Fixed Point"
permalink: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-88-the-ci-as-j-closed-fixed-point/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-categorical-ethics-the-kantian-bridge"
chapter_number: 88
chapter_slug: "chapter-88-the-ci-as-j-closed-fixed-point"
page_in_book: 317
prev_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-87-applied-ethics/"
prev_chapter_title: "Chapter 87: Applied Ethics"
next_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-89-the-ci-proof-programme-three-stages/"
next_chapter_title: "Chapter 89: The CI Proof Programme: Three Stages"
summary_short: "The categorical imperative is not postulated but derived: it is the minimal j-closed fixed point of the dignity modality in the presheaf topos, unique up to natural isomorphism by the Minimality Lemma."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
canonical_part_title: "Categorical Ethics & the Kantian Bridge"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-88-the-ci-as-j-closed-fixed-point/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part VII: Categorical Ethics & the Kantian Bridge"
      url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part VII"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 75
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Chapter 77 showed that the categorical imperative is the sheaf condition. This chapter deepens that result: the CI is not merely a useful structure imposed on ethics from outside but the unique minimal fixed point of the dignity modality j_dig within the presheaf topos. The CI Operator Graph (VII.D71) makes the structure explicit as a typed quadruple CI = (M, U, γ, R): the maxim space M (a presheaf over the site of rational perspectives), the universalization endofunctor U : M → M extending any maxim to all perspectives simultaneously, the coherence test γ (the sheaf condition identifying the subsheaf M⁺ of coherent sections), and the respect operator R encoding invariance under Aut(C). Each component corresponds to one Kantian formulation: U to the Formula of Universal Law, γ to the Formula of the Law of Nature, R to the Formula of Humanity, and the site structure of M to the Formula of Autonomy. The CI as j-Closed Fixed Point theorem (VII.T35) proves that j_dig(CI) = CI — each component is individually j-closed, meaning the dignity projection does not alter it, because the CI already encodes dignity in its own structure. The CI Minimality Lemma (VII.L12) establishes that any j-closed operator graph weaker than CI is not j-closed (it fails to enforce the sheaf condition or label-independence, so j_dig would project it further), while any strictly stronger graph contains CI as a retract (the additional constraints are redundant for j-closure). The CI is therefore unique up to natural isomorphism: it is not one ethical theory among many but the structurally forced ethical operator in the presheaf topos.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D71 — CI Operator Graph* (τ-effective). The typed quadruple (M, U, γ, R) with explicit formulas for the universalization extension, the sheaf-condition coherence test, and the automorphism-invariance respect operator; a maxim is CI-admissible iff it passes γ and R simultaneously.
- **Key results:** *VII.T35 — CI as j-Closed Fixed Point* (τ-effective): j_dig(CI) = CI, each component individually j-closed; the CI already lives in A_dig. *VII.L12 — CI Minimality* (τ-effective): CI is the minimum element of the poset of j-closed operator graphs; any weaker graph is not j-closed, any stronger graph contains CI as a retract.
- **Dependencies:** VII.D65, VII.T30 (dignity modality j_dig), VII.T31 (CI as sheaf condition), Knaster–Tarski theorem (lattice completeness for fixed points).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The Knaster–Tarski theorem and Lawvere–Tierney topology machinery are available in Mathlib.

## Where this leads

Chapter 89 asks why this fixed point exists, unfolding the three-stage CI proof programme (Kernel Theorem, Semantic Object Construction, Fixed-Point Uniqueness Conjecture) that grounds the derivation in the self-enrichment structure of τ.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part07/ch88.tex -->
