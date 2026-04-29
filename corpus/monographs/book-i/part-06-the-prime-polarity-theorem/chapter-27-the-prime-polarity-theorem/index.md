---
layout: "corpus-monograph-chapter"
title: "Chapter 27: The Prime Polarity Theorem"
permalink: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/chapter-27-the-prime-polarity-theorem/"
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
chapter_number: 27
chapter_slug: "chapter-27-the-prime-polarity-theorem"
page_in_book: 103
prev_chapter_url: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/chapter-26-the-spectral-question-what-do-primes-see/"
prev_chapter_title: "Chapter 26: The Spectral Question: What Do Primes See?"
next_chapter_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-28-omega-germs-on-the-ontic-elements/"
next_chapter_title: "Chapter 28: Omega-Germs on the Ontic Elements"
summary_short: "The Prime Polarity Theorem (*I.T05*), Hinge Theorem 2: every prime in ℙ_τ is either B-dominant (γ-polar) or C-dominant (η-polar), both classes are infinite, and the polarity map pol: ℙ_τ → {+, −} partitions the primes canonically."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/"
canonical_part_title: "The Prime Polarity Theorem"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-06-the-prime-polarity-theorem/chapter-27-the-prime-polarity-theorem/"
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

This chapter proves the Prime Polarity Theorem (*I.T05*), the second hinge theorem of the Panta Rhei series. Every prime p in ℙ_τ carries a canonical polarity — it is either B-dominant (γ-polar, exponent-primary) or C-dominant (η-polar, tetration-primary) — and both polarity classes are infinite. The polarity is determined not by convention but by the arithmetic structure of τ-Idx: specifically, by the way p interacts with the tower-atom divisibility structure along the primorial ladder. B-dominant primes are those for which the γ-channel (pure power regime) dominates the spectral signature; C-dominant primes are those for which the η-channel (tetration regime) does. The theorem establishes all three conclusions — dichotomy, B-class infinite, C-class infinite — in a single proof that analyzes the scaled-gap inequality along the primorial ladder.

## What this chapter contributes

The chapter delivers the Prime Polarity Theorem (*I.T05*) and its supporting infrastructure. The polarity criterion defines B-dominance and C-dominance via the tower-atom sensitivity: for a given prime p, the question is whether increasing C from 1 to 2 (which multiplies the tower atom by the factor p^(p·B)/p^B = p^((p-1)B)) or increasing B from 1 to 1 + something produces the larger tower for typical objects. The stabilization mechanism formalized in the scaled-gap inequality — comparing score losses Δ(E/p) · p and Δ(E/p^p) · p^p along the primorial ladder E = M_k — shows that eventual stabilization of the argmax is guaranteed by the well-ordering of τ-Idx. The infinitude of the B-class follows from the existence of infinitely many primes for which the pure-power regime dominates; the infinitude of the C-class follows from the slow growth of the tetration tower for small primes (notably p = 2). A key structural result is the polarity pairing: the B-dominant and C-dominant primes are interleaved throughout ℙ_τ, with infinitely many adjacent pairs of opposite polarity (polarity gap 1). This interleaving is the arithmetic precursor of the two-lobe structure of the algebraic lemniscate ℒ: B-dominant primes feed one lobe, C-dominant primes feed the other, and the crossing-point germ sits where the lobes meet. Lean formalization targets `TauLib.BookI.Polarity.Polarity`.

## Lean coverage

Planned for `TauLib.BookI.Polarity.Polarity`. Key results to formalize: `prime_polarity` (the polarity map pol: ℙ_τ → {+, −}), `polarity_dichotomy` (every prime is B-dominant or C-dominant), `b_class_infinite`, and `c_class_infinite`.

## Where this leads

The bipolar partition of the primes is the arithmetic origin of everything that follows in Part VII. Chapter 28 passes from the finite polarity computation to the infinite limit, constructing omega-germs as compatible towers on the primorial ladder. Chapter 29 assigns polarization to those germs. Chapter 30 shows that the three requirements for a scalar algebra on the lemniscate boundary force split-complex scalars (j² = +1), not elliptic ones, and assembles the algebraic lemniscate ℒ = (H_τ, ω_ℒ, σ).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part06/ch27-prime-polarity.tex -->
