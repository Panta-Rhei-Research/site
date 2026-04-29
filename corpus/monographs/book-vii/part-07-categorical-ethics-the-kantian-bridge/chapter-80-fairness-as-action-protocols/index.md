---
layout: "corpus-monograph-chapter"
title: "Chapter 80: Fairness-as-Action Protocols"
permalink: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-80-fairness-as-action-protocols/"
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
chapter_number: 80
chapter_slug: "chapter-80-fairness-as-action-protocols"
page_in_book: 293
prev_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-79-the-trolley-problem-solved/"
prev_chapter_title: "Chapter 79: The Trolley Problem Solved"
next_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-81-monodromy-and-moral-ambiguity/"
next_chapter_title: "Chapter 81: Monodromy and Moral Ambiguity"
summary_short: "Fairness is a five-step executable protocol derived from dignity and the sheaf condition; the uniform lottery at the residual tie-breaking step is the unique permutation-invariant probability assignment over structurally indistinguishable candidates."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
canonical_part_title: "Categorical Ethics & the Kantian Bridge"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-80-fairness-as-action-protocols/"
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

Fairness is not an abstract principle but a structured decision procedure, and this chapter makes that structure explicit. Chapter 79 derived the equal-risk lottery for the binary boundary-symmetric case. The present chapter generalises: when multiple dignity-equivalent claims compete under scarcity, what does a label-independent decision procedure look like across its full range of applications?

The Fairness Protocol (VII.D67) answers with a five-step sequence. Step 1 is boundary identification: determine the decision boundary B — the set of persons affected and the set of available actions — and whether the situation is symmetric (all persons already within the risk boundary) or asymmetric (some persons would be newly exposed by the action). Step 2 is structural filtering: apply all available label-independent criteria to reduce the candidate set. Filters such as medical compatibility for organ allocation, academic qualification for scholarships, or urgency classification for triage are admissible precisely because they depend on structural features of the situation, not on names, wealth, or social status. Step 3 is the dignity check: discard any action failing D(π(X)) ≅ D(X) or treating any person as a mere means. Step 4 is residual tie-breaking: if a genuine tie among dignity-equivalent candidates remains after structural filtering — no further label-independent criterion distinguishes them — resolve by a uniform lottery at probability 1/n over the n remaining candidates. Step 5 is unconditional execution: carry out the selected action without conditioning on contingent labels discovered after the lottery. The key design principle is that randomness enters only at step 4, after all structural information has been exhausted.

Fairness from CI (VII.P18) establishes that this protocol is the unique selection mechanism jointly satisfying universalizability (it defines a sheaf from every perspective), no-conflict compatibility (applying the protocol never forces a dignity violation), label-independence (it commutes with address permutations), and structure exhaustion (it uses all available label-independent criteria before randomizing). Uniqueness follows from the fact that the uniform distribution is the only permutation-invariant probability distribution on a finite set. Applications cover organ allocation, emergency triage (urgency and treatability as label-independent filters), and distributive justice more broadly. The chapter also notes a composition property: composing a fresh fair lottery with any prior distribution at a downstream boundary produces a result at least as symmetric as the prior.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D67 — Fairness Protocol* (τ-effective). Five-step executable procedure from boundary identification through label-independent structural filtering, dignity check, uniform-lottery tie-breaking, to unconditional execution.
- **Key results:** *VII.P18 — Fairness from CI* (τ-effective): the protocol is the unique dignity-preserving selection mechanism jointly satisfying universalizability, no-conflict, label-independence, and structure exhaustion; uniqueness follows from the fact that the uniform distribution is the only permutation-invariant distribution on a finite set.
- **Dependencies:** VII.D65 (label-independence), VII.P17 (Trolley Resolution), VII.T31 (CI as sheaf condition), VII.T32 (No-Conflict Theorem).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

The fairness protocol is the operational face of the entire dignity–CI framework. Chapter 85 applies it to intergenerational settings, and Chapter 93 cites it as one of the nine Part VII deliverables forming the dignity–CI–j-closure arc.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part07/ch80.tex -->
