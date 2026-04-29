---
layout: "corpus-monograph-chapter"
title: "Chapter 79: The Trolley Problem Solved"
permalink: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-79-the-trolley-problem-solved/"
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
chapter_number: 79
chapter_slug: "chapter-79-the-trolley-problem-solved"
page_in_book: 290
prev_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-78-the-no-conflict-theorem/"
prev_chapter_title: "Chapter 78: The No-Conflict Theorem"
next_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-80-fairness-as-action-protocols/"
next_chapter_title: "Chapter 80: Fairness-as-Action Protocols"
summary_short: "Trolley variants are resolved by explicit typing: in boundary-symmetric cases the unique dignity-preserving mechanism is an equal-risk lottery (p = 1/2); boundary-asymmetric interventions fail the dignity test before the lottery applies."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
canonical_part_title: "Categorical Ethics & the Kantian Bridge"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-79-the-trolley-problem-solved/"
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

The trolley problem has generated decades of philosophical debate because it conflates structurally distinct situations under a single narrative frame. Narrative proximity obscures the features that matter: who is already within the risk boundary, what type of action the agent's intervention constitutes, and whether the proposed resolution depends on contingent labels. The chapter applies the machinery from Chapters 76–78 — dignity as label-independence, the sheaf condition, and the no-conflict theorem — to decompose the puzzle along exactly these dimensions.

In the switch case a runaway trolley threatens m persons on track A and n persons on track B. All are already within the boundary of risk; the trolley threatens them regardless of the agent's action. The agent's decision distributes an existing harm rather than creating a new one, making this a boundary-symmetric setting. Label-independence, applied to the probability assignment (p, 1−p) over the two groups, requires that the policy commute with all address permutations of the persons involved. Group membership is a contingent label, not an identity-invariant, so any admissible probability assignment must be invariant under permutation of persons. The unique symmetric assignment satisfying 1 − p = p is p = 1/2: a fair lottery at the decision boundary, executed before learning contingent details such as identities or the specific numbers m and n.

In the footbridge case the bystander stands on a bridge above the track and is not within the original risk boundary. Pushing this person creates a new vulnerability rather than redistributing an existing one. Because the intervention introduces a new risk for someone outside the original harm-boundary, it treats that person as a resource to be instrumentalized — failing the respect operator of Chapter 77 and the dignity condition D(π(X)) ≅ D(X) before any lottery analysis begins. The Trolley Resolution (VII.P17) formally establishes this boundary-type distinction: the switch and footbridge variants differ not in moral intuition but in whether the setting is boundary-symmetric or boundary-asymmetric. Most other trolley variants — loop tracks, known versus unknown victims, character judgments, the transplant surgeon — dissolve once these three structural features are made explicit.

## What this chapter contributes

- **Definitions / Axioms:** **Definitions / Axioms:** none introduced; this chapter develops consequences of VII.D65 and VII.T32.
- **Key results:** *VII.P17 — Trolley Resolution* (τ-effective): in boundary-symmetric settings, the equal-risk lottery (p_i = 1/2 for all persons) is the unique dignity-preserving selection mechanism; in boundary-asymmetric settings, creating new risk for persons outside the original boundary is inadmissible.
- **Dependencies:** VII.D65 (label-independence), VII.T30 (Dignity Universality), VII.T32 (No-Conflict Theorem); equal-risk lottery as unique permutation-invariant probability assignment.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

The equal-risk lottery derived here is generalized in Chapter 80, which extends it to a full fairness protocol for resource allocation, triage, and distributive justice whenever dignity-equivalent claims compete under scarcity.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part07/ch79.tex -->
