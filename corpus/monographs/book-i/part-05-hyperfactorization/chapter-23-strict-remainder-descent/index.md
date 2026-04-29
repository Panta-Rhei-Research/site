---
layout: "corpus-monograph-chapter"
title: "Chapter 23: Strict Remainder Descent"
permalink: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-23-strict-remainder-descent/"
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
chapter_number: 23
chapter_slug: "chapter-23-strict-remainder-descent"
page_in_book: 91
prev_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-22-no-tie-determinism/"
prev_chapter_title: "Chapter 22: No-Tie Determinism"
next_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-24-the-hyperfactorization-theorem/"
next_chapter_title: "Chapter 24: The Hyperfactorization Theorem"
summary_short: "The Strict Remainder Descent Lemma (*I.L04*) proves D < X whenever X ≥ 2 and provides both a termination guarantee for iterated peeling and the inductive base needed for the uniqueness proof."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-05-hyperfactorization/"
canonical_part_title: "Hyperfactorization"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-05-hyperfactorization/chapter-23-strict-remainder-descent/"
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

The greedy peel decomposes X = T(A, B, C) · D, and the uniqueness proof of Chapter 24 proceeds by strong induction on X. For that induction to close, two conditions must hold: the remainder D must be strictly smaller than X (so the inductive hypothesis applies to D), and D must live at a strictly lower level of the prime hierarchy (so the analysis does not loop back to A). This chapter proves both conditions through the Strict Remainder Descent Lemma (*I.L04*). The argument is short and elementary: since A is prime, A ≥ 2, so the tower atom T(A, B, C) = (A ↑↑ C)^B is at least 2. Dividing X = T · D by a factor of at least 2 gives D ≤ X/2 < X. The prime-stratum descent — all prime factors of D are strictly less than A — follows directly from the greedy peel's construction, which absorbs all A-factors into the tower atom and leaves none in the remainder.

## What this chapter contributes

The chapter delivers the Strict Remainder Descent Lemma (*I.L04*) in three parts. Part 1 shows T(A, B, C) ≥ 2 for any prime A and any B, C ≥ 1. Part 2 deduces D ≤ X/2 < X, establishing strict numerical descent. Part 3 establishes prime-stratum descent: all prime factors of D are strictly less than A, the dominant prime of X. The chapter explains the two roles that the descent plays in the overall proof architecture. As a termination guarantee, it ensures that iterating the peel produces a strictly decreasing sequence, which must terminate because the denotational order on τ-Idx is a well-ordering. As an inductive base, it licenses the application of the strong induction hypothesis to the remainder D in the uniqueness proof. A remark notes that the bound D ≤ X/2 is tight — achieved precisely when A = 2 and B = C = 1 — but that for larger tower atoms the descent is exponentially steeper. The Prime-Stratum Descent Proposition strengthens the numerical bound: D does not merely have a smaller index value, it lives in a genuinely lower stratum of the prime hierarchy. Lean formalization targets `TauLib.BookI.Coordinates.Descent`.

## Lean coverage

Planned for `TauLib.BookI.Coordinates.Descent`. Key results to formalize: `tower_atom_ge_two` (T(A, B, C) ≥ 2 for prime A, B, C ≥ 1), `remainder_strict_descent` (D < X whenever X ≥ 2), and `remainder_prime_descent` (all prime factors of D are less than A).

## Where this leads

With the No-Tie Lemma (Chapter 22) and Strict Remainder Descent (this chapter) in hand, Chapter 24 can assemble the full uniqueness proof of the Hyperfactorization Theorem by strong induction on X. The prime-stratum descent is the structural ingredient that makes the induction well-founded not just numerically but hierarchically: at each level, the remainder is confined to a strictly lower prime stratum, and the induction runs down the prime hierarchy rather than merely down the integer ordering.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part05/ch23-remainder-descent.tex -->
