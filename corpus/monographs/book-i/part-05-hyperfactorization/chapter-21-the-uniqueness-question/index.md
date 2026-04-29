---
layout: "corpus-monograph-chapter"
title: "Chapter 21: The Uniqueness Question"
permalink: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-21-the-uniqueness-question/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 5
part_display: "Part V"
part_slug: "part-05-hyperfactorization"
chapter_number: 21
chapter_slug: "chapter-21-the-uniqueness-question"
page_in_book: 83
prev_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-20-dimension-and-the-fibration-preview/"
prev_chapter_title: "Chapter 20: Dimension and the Fibration Preview"
next_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-22-no-tie-determinism/"
next_chapter_title: "Chapter 22: No-Tie Determinism"
summary_short: "Part IV proved existence of the ABCD encoding. Chapter 21 frames the sharpened question: is that encoding unique? It states the Hyperfactorization Theorem and lays out the three-lemma proof strategy."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-05-hyperfactorization/"
canonical_part_title: "Hyperfactorization"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-05-hyperfactorization/chapter-21-the-uniqueness-question/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part V: Hyperfactorization"
      url: "/corpus/monographs/book-i/part-05-hyperfactorization/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part V"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 6
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

Part IV established that every object X in τ-Idx admits an ABCD encoding X = ((A ↑↑ C)^B) · D, where A is the dominant prime, B is the tower exponent, C is the tetration height, and D is the remainder whose prime factors all fall strictly below A. That result is an existence theorem: the greedy peel-off algorithm always terminates and produces a valid tuple. But existence is only half of what a coordinate system requires. A chart that maps multiple addresses to the same object is a labeling scheme, not an injective coordinate system. Part V asks the harder question: is the ABCD encoding unique? Could a different tuple, not produced by the greedy peel, also satisfy all four constraints and reconstruct the same X? This chapter frames that uniqueness question precisely, states the Hyperfactorization Theorem as its answer, and lays out the three-lemma proof strategy that Chapters 22, 23, and 24 will execute.

## What this chapter contributes

The chapter's primary contribution is conceptual scaffolding for the entire hyperfactorization proof. It sharpens the uniqueness question by making explicit what must be shown: not merely that the greedy peel is deterministic — that is already known — but that no alternative decomposition satisfying the four structural constraints can exist. The chapter gives an informal preview of the Hyperfactorization Theorem (*I.T04*) and explains why each of the four tuple components is forced in sequence. The A-coordinate is the largest prime dividing X, uniquely determined by the Fundamental Theorem of Arithmetic. The C-coordinate is the maximal tetration height at base A, whose uniqueness requires that tetration cannot "tie" — the subject of Chapter 22's No-Tie Lemma (*I.L03*). The B-coordinate is the A↑↑C-adic valuation of X, uniquely determined once A and C are fixed. The D-coordinate is the exact quotient, uniquely determined once A, B, and C are fixed. The chapter also underscores why tetration injectivity is the critical ingredient: without it, two different heights c₁ and c₂ could produce the same tower base, and the encoding would be ambiguous at the level of C. Finally, the chapter introduces the Hyperfactorization Theorem as the first of the two hinge theorems of the Panta Rhei series — ZFC-provable number-theoretic results on which the entire downstream structure rests.

## Lean coverage

Lean formalization of the Hyperfactorization Theorem is planned for `TauLib.BookI.Coordinates.Hyperfact`. This chapter introduces no new formal results; it sets up the proof architecture. The key results to be formalized in subsequent chapters include `hyperfactorization` (full existence and uniqueness), `abcd_injective` (injectivity of the chart Φ), and `shadow_collapse` (shadow equality implies ontic identity).

## Where this leads

Chapter 22 proves the No-Tie Lemma, establishing that the maximal tetration height is uniquely determined. Chapter 23 proves Strict Remainder Descent, showing D < X and enabling strong induction. Chapter 24 assembles the full uniqueness proof. Chapter 25 harvests the consequences — constructive pairing, sequence encoding, and the earned completeness of the four-dimensional coordinate system. Part VI then discovers that the A-coordinates of the ABCD chart are not all alike: they carry a canonical polarity, yielding the Prime Polarity Theorem.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part05/ch21-uniqueness-question.tex -->
