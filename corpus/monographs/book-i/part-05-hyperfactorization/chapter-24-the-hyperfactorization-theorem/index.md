---
layout: "corpus-monograph-chapter"
title: "Chapter 24: The Hyperfactorization Theorem"
permalink: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-24-the-hyperfactorization-theorem/"
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
chapter_number: 24
chapter_slug: "chapter-24-the-hyperfactorization-theorem"
page_in_book: 93
prev_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-23-strict-remainder-descent/"
prev_chapter_title: "Chapter 23: Strict Remainder Descent"
next_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-25-consequences-and-the-constructive-substrate/"
next_chapter_title: "Chapter 25: Consequences and the Constructive Substrate"
summary_short: "The Hyperfactorization Theorem (*I.T04*), the first hinge theorem of the Panta Rhei series: every X ≥ 2 in τ-Idx has a unique ABCD encoding. The ABCD chart is injective and shadow equality collapses to ontic identity."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-05-hyperfactorization/"
canonical_part_title: "Hyperfactorization"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-05-hyperfactorization/chapter-24-the-hyperfactorization-theorem/"
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

This chapter proves the Hyperfactorization Theorem (*I.T04*), the first hinge theorem of the Panta Rhei series. It assembles the three preparatory results: the Fundamental Theorem of Arithmetic (which forces the A-coordinate), the No-Tie Lemma (*I.L03*, Chapter 22, which forces the C- and B-coordinates jointly), and Strict Remainder Descent (*I.L04*, Chapter 23, which supplies the inductive base and forces D). The theorem states that for every X in τ-Idx with X ≥ 2, the decomposition X = ((A ↑↑ C)^B) · D satisfying the four structural constraints — A prime, B and C at least 1, D at least 1 with all prime factors of D strictly below A — exists and is unique. The consequences are immediate: the ABCD chart Φ is injective, shadow equality collapses to ontic identity, and every object of Category τ possesses exactly one canonical address.

## What this chapter contributes

The chapter delivers the Hyperfactorization Theorem (*I.T04*) by strong induction on X. The base case X = 2 is handled directly: the only prime dividing 2 is 2 itself, tetration height C = 1 is forced because 2 ↑↑ 2 = 4 does not divide 2, B = 1 is forced by the 2-adic valuation, and D = 1 follows by exact division. The inductive step takes two encodings of the same X and drives them to equality through four sequential steps: Step 1 uses the FTA to show A = A' (both must be the largest prime dividing X); Step 2 applies the No-Tie Lemma to the A-adic valuations to force C = C' and B = B'; Step 4 cancels the common tower atom to force D = D'. Two immediate corollaries follow. The Injectivity Corollary shows that the chart Φ: Obj(τ) → τ-Idx⁴ is injective. The Shadow Collapse Corollary shows that shadow equality implies ontic identity. A further NF Deduplication Invariant establishes that Address DAG construction is confluent: different deduplication orderings produce the same canonical DAG, because each index has a unique ABCD address. Lean formalization targets `TauLib.BookI.Coordinates.Hyperfact` with theorems `hyperfactorization`, `abcd_injective`, and `shadow_collapse`.

## Lean coverage

Planned for `TauLib.BookI.Coordinates.Hyperfact`. The module will formalize the full uniqueness proof (`hyperfactorization`), injectivity of the ABCD chart (`abcd_injective`), and the collapse of shadow equality to ontic identity (`shadow_collapse`).

## Where this leads

Chapter 25 harvests the downstream consequences: constructive pairing, sequence encoding, the Gödel-numbering connection, and the completeness of the four-dimensional coordinate system. The Hyperfactorization Theorem closes the hinge block's first turn: from Part IV's existence result to Part V's uniqueness result, the ABCD chart becomes a faithful bijective coordinate system. Part VI then asks what additional structure the A-coordinates carry — discovering the Prime Polarity Theorem.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part05/ch24-hyperfactorization.tex -->
