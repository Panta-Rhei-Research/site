---
layout: "corpus-monograph-chapter"
title: "Chapter 22: No-Tie Determinism"
permalink: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-22-no-tie-determinism/"
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
chapter_number: 22
chapter_slug: "chapter-22-no-tie-determinism"
page_in_book: 89
prev_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-21-the-uniqueness-question/"
prev_chapter_title: "Chapter 21: The Uniqueness Question"
next_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-23-strict-remainder-descent/"
next_chapter_title: "Chapter 23: Strict Remainder Descent"
summary_short: "The No-Tie Lemma (*I.L03*) proves that tetration heights cannot compete for the maximum: the maximal C such that A ↑↑ C divides X is uniquely determined, and tower atoms with the same prime base are injective in (B, C)."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-05-hyperfactorization/"
canonical_part_title: "Hyperfactorization"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-05-hyperfactorization/chapter-22-no-tie-determinism/"
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

The greedy peel extracts the largest prime A dividing X, then seeks the maximal tetration height C such that A ↑↑ C divides X. Since A ↑↑ 1 = A already divides X, at least C = 1 is valid. But could two different heights c₁ < c₂ both appear as candidates for the maximum — creating a "tie" that the greedy peel cannot resolve deterministically? The question is more subtle than it first appears: the issue is not whether multiple heights satisfy the divisibility condition, but whether two different (B, C) pairs could produce equal tower atoms from the same prime base, making the encoding ambiguous. This chapter proves the No-Tie Lemma (*I.L03*): the set of valid tetration heights has a well-defined maximum, and tower atoms T(A, b₁, c₁) = T(A, b₂, c₂) with b₁, b₂ ≥ 1 and c₁, c₂ ≥ 1 force c₁ = c₂ and b₁ = b₂. The proof engine is the super-exponential growth of tetration: the gap between consecutive tower levels is so large that no finite exponent adjustment can compensate for a height mismatch.

## What this chapter contributes

The chapter delivers the No-Tie Lemma (*I.L03*) in two parts. Part 1 shows that the set {c ≥ 1 : A ↑↑ c divides X} is finite and has a well-defined maximum C — a consequence of the strict monotonicity of tetration (each level strictly exceeds the previous) combined with the well-ordering of τ-Idx. Part 2 shows that tower atom equality T(A, b₁, c₁) = T(A, b₂, c₂) forces the heights to match. The proof computes A-adic valuations on both sides: the valuation of A ↑↑ c is exactly A ↑↑ (c − 1), so equality of valuations translates into the equation b₁ · (A ↑↑ (c₁ − 1)) = b₂ · (A ↑↑ (c₂ − 1)). If c₁ ≠ c₂, the difference in the tower terms grows super-exponentially while the exponent multipliers b₁ and b₂ are finite, making equality impossible. The chapter concludes with the Deterministic Extraction Corollary: given A and X, the greedy peel produces the unique pair (B, C) such that T(A, B, C) divides X with C maximal. Lean formalization targets `TauLib.BookI.Coordinates.NoTie` with lemmas `tetration_max_exists`, `tower_atom_injective`, and `no_tie`.

## Lean coverage

Planned for `TauLib.BookI.Coordinates.NoTie`. The module will formalize `tetration_max_exists` (the set of valid heights has a maximum), `tower_atom_injective` (T(A, b₁, c₁) = T(A, b₂, c₂) implies (b₁, c₁) = (b₂, c₂)), and `no_tie` (the full two-part lemma).

## Where this leads

The No-Tie Lemma eliminates the first source of potential non-uniqueness in the ABCD encoding: ambiguity in the tetration height C. Chapter 23 eliminates the second source by proving Strict Remainder Descent, which also supplies the inductive base for the full uniqueness proof in Chapter 24. The combination of no-tie determinism and remainder descent is sufficient to close the uniqueness argument by strong induction on X.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part05/ch22-no-tie.tex -->
