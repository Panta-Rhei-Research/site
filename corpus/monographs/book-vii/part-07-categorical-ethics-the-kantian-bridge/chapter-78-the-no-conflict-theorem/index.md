---
layout: "corpus-monograph-chapter"
title: "Chapter 78: The No-Conflict Theorem"
permalink: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-78-the-no-conflict-theorem/"
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
chapter_number: 78
chapter_slug: "chapter-78-the-no-conflict-theorem"
page_in_book: 287
prev_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-77-the-categorical-imperative-as-sheaf-condition/"
prev_chapter_title: "Chapter 77: The Categorical Imperative as Sheaf Condition"
next_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-79-the-trolley-problem-solved/"
next_chapter_title: "Chapter 79: The Trolley Problem Solved"
summary_short: "Within the dignity-filtered admissible world, properly typed duties cannot normatively conflict: their intersection is a subsheaf with nonempty fibers that glues to a global section respecting both obligations simultaneously."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
canonical_part_title: "Categorical Ethics & the Kantian Bridge"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-78-the-no-conflict-theorem/"
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

Can two genuine duties demand incompatible actions in the same situation? Within the admissible world A_dig, the answer is no — provided both duties are properly typed. The chapter opens by drawing a sharp distinction between two phenomena that ordinary ethical discussion conflates. A normative conflict would require two binding obligations whose simultaneous satisfaction is structurally impossible, implying that the ethical framework itself is inconsistent. A feasibility conflict means that the world, under scarcity, time pressure, or limited capacity, does not permit realizing every desideratum at once — a constraint on what can be done, not a proof that dignity must be violated. These two phenomena require entirely different responses.

The Duty Typing Lemma (VII.L11) is the key technical result. It identifies four conditions under which an alleged obligation D is properly typed — is a genuine subsheaf of the maxim sheaf Max: (i) local realizability, meaning the obligation's fiber D(U) is nonempty for every perspective U in every covering family; (ii) dignity preservation, meaning every enactment in D(U) factors through the dignity reflector L_dig; (iii) overlap compatibility, meaning the restriction maps agree on pairwise intersections; (iv) bounded tension, meaning no enactment forces unbounded tension for any admissible perspective. If any of these conditions fails, the alleged obligation is improperly typed and does not constitute a genuine duty within the admissible world.

The No-Conflict Theorem (VII.T32) proves that two properly typed obligations D₁ and D₂, understood as subsheaves of Max, have a nonempty intersection at every perspective. That intersection inherits all four typing conditions from its components and therefore glues — by the sheaf axiom and τ-holomorphic unique continuation — to a global section satisfying both obligations simultaneously without degrading any agent's identity-invariants. The contrapositive is equally important as the theorem itself: when two alleged duties cannot be jointly enacted, at least one is improperly typed. The chapter works through promise-keeping vs. emergency aid and truth-telling vs. preventing harm as cases where improperly typed formulations generate apparent conflict, while properly typed reformulations dissolve it. Moral tragedy is real — scarcity, timing, and human limitation create genuine suffering — but it is a feasibility gap, not a structural inconsistency in the normative framework.

## What this chapter contributes

- **Definitions / Axioms:** **Definitions / Axioms:** none introduced; this chapter develops consequences of VII.D66 and VII.T31.
- **Key results:** *VII.L11 — Duty Typing Lemma*: an obligation is properly typed iff it is a subsheaf of the maxim sheaf (four explicit conditions). *VII.T32 — No-Conflict Theorem*: properly typed duties admit joint global sections; apparent conflicts signal typing errors, incomplete covers, or feasibility constraints — not normative contradictions.
- **Dependencies:** VII.D65 (dignity), VII.T31 (CI-Sheaf Equivalence); sheaf intersection theory; τ-holomorphic unique continuation.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The subsheaf intersection argument uses standard sheaf theory available in Mathlib.

## Where this leads

The no-conflict result is the normative backbone invoked throughout Part VII: Chapter 79 relies on it when deriving the equal-risk protocol, Chapter 82 cites it for the coherence test, and Chapter 85 extends it to temporal covers for intergenerational obligations.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part07/ch78.tex -->
