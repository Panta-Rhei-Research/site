---
layout: "corpus-monograph-chapter"
title: "Chapter 26: The Spectral Question: What Do Primes See?"
permalink: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/chapter-26-the-spectral-question-what-do-primes-see/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-the-prime-polarity-theorem"
chapter_number: 26
chapter_slug: "chapter-26-the-spectral-question-what-do-primes-see"
page_in_book: 99
prev_chapter_url: "/corpus/monographs/book-i/part-05-hyperfactorization/chapter-25-consequences-and-the-constructive-substrate/"
prev_chapter_title: "Chapter 25: Consequences and the Constructive Substrate"
next_chapter_url: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/chapter-27-the-prime-polarity-theorem/"
next_chapter_title: "Chapter 27: The Prime Polarity Theorem"
summary_short: "The spectral question: does the B/C interaction across all objects with dominant prime p reveal global structure about p itself? Chapter 26 defines the prime spectral signature (*I.D19e*) and establishes the growth-rate separation between exponentiation and tetration."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/"
canonical_part_title: "The Prime Polarity Theorem"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-06-the-prime-polarity-theorem/chapter-26-the-spectral-question-what-do-primes-see/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part VI: The Prime Polarity Theorem"
      url: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 7
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

The Hyperfactorization Theorem gave every object a unique ABCD address, and the A-coordinate selects the dominant prime. But primes occupy the A-coordinate of infinitely many objects simultaneously, and for each such object, the B- and C-coordinates record how the prime is used: through exponentiation (the γ-channel) or through tetration (the η-channel). The spectral question asks whether this stacking pattern, surveyed across the full population of objects for which a given prime p is dominant, reveals a systematic asymmetry intrinsic to p itself. This chapter frames that question precisely by introducing the prime spectral signature (*I.D19e*): the pair (B_N, C_N) of maximal B- and C-coordinates achieved by objects with dominant prime p and index at most N. The key structural observation is a growth-rate separation between the two channels: the maximum achievable B value up to bound N grows as log N, while the maximum achievable C value grows only as the iterated logarithm log* N.

## What this chapter contributes

The chapter defines the prime spectral signature (*I.D19e*) and the associated dominance predicates: p is B-dominant up to N if its spectral B-maximum exceeds its C-maximum, and C-dominant otherwise. The Growth-Rate Separation Proposition establishes the quantitative gap: for large enough N, B_max = ⌊log_p N⌋ grows logarithmically, while C_max grows only as log* N (the inverse of tetration). Because log N grows far faster than log* N for all sufficiently large N, the B-channel systematically dominates in the asymptotic regime. A remark notes, however, that the raw dominance count does not yet determine polarity: the spectral question requires examining the joint B/C interaction across all objects, not just the extremal cases. The chapter closes with a preview: Chapter 27 will show that the B/C sensitivity of the tower atom — how much the tower grows when B is incremented by 1 versus when C is incremented by 1 — creates a genuine bifurcation in which every prime is assigned a canonical polarity, and both polarity classes are infinite. Lean formalization targets `TauLib.BookI.Polarity.Spectral`.

## Lean coverage

Planned for `TauLib.BookI.Polarity.Spectral`. Definitions to formalize: `spectral_signature` (the pair (B_N, C_N)), `b_dominant` and `c_dominant` (dominance predicates), and `growth_rate_separation` (B-max grows as log N, C-max as log* N).

## Where this leads

Chapter 27 proves the Prime Polarity Theorem (*I.T05*), the second hinge theorem, showing that every prime carries a canonical polarity — B-dominant or C-dominant — and that both classes are infinite. The bipolar partition discovered here is the arithmetic foundation from which the algebraic lemniscate ℒ (Part VII) and ultimately the split-complex spectral algebra emerge.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part06/ch26-spectral-question.tex -->
