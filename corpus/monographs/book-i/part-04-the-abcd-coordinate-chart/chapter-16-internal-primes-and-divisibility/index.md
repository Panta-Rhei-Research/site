---
layout: "corpus-monograph-chapter"
title: "Chapter 16: Internal Primes and Divisibility"
permalink: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-16-internal-primes-and-divisibility/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-the-abcd-coordinate-chart"
chapter_number: 16
chapter_slug: "chapter-16-internal-primes-and-divisibility"
page_in_book: 63
prev_chapter_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-15-the-denotational-order-and-the-road-ahead/"
prev_chapter_title: "Chapter 15: The Denotational Order and the Road Ahead"
next_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-17-tower-atoms-and-the-greedy-peel/"
next_chapter_title: "Chapter 17: Tower Atoms and the Greedy Peel"
summary_short: "Divisibility and primality are earned from tau-Idx's semiring. The FTA holds internally: every element >= 2 has a unique prime factorization; nothing imported."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
canonical_part_title: "The ABCD Coordinate Chart"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-04-the-abcd-coordinate-chart/chapter-16-internal-primes-and-divisibility/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part IV: The ABCD Coordinate Chart"
      url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part IV"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 5
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

Before the ABCD coordinate chart can be defined, the notion of *prime* must be earned on τ-Idx. In standard mathematics, primes and the Fundamental Theorem of Arithmetic are imported from number theory as background machinery. In τ they are earned: divisibility follows directly from the multiplication of Part III (Chapter 11), and primality is simply irreducibility within τ-Idx. This chapter defines internal divisibility, identifies the set ℙ_τ of internal primes, clarifies the special status of zero as a vacuous non-participant, establishes τ-Idx as an integral domain, and proves the Fundamental Theorem of Arithmetic on τ-Idx: every element n̲ ≥ 2̲ has a unique prime factorization. The prime signature Σ(n̲) derived from the FTA will be the input to the greedy peel-off algorithm of the next chapter.

## What this chapter contributes

- Defines *I.D19a* (Internal Divisibility): a̲ | b̲ iff ∃ k̲ such that b̲ = a̲ × k̲. Proves divisibility is reflexive and transitive, that 1̲ divides everything, that everything divides 0̲, and that a non-zero divisor is bounded by the dividend. Decidability follows from the well-ordering of τ-Idx.
- Defines *I.D19b* (Internal Primes): p̲ ∈ ℙ_τ iff p̲ ≥ 2̲ and p̲ has only trivial divisors. Establishes ℙ_τ is non-empty (2̲ is prime) and infinite by Euclid's argument, earned internally using only τ-Idx's semiring operations.
- Proves *I.P18* (Zero is Vacuous): 0̲ is not prime, not a successor, is divisible by everything, and is the unique multiplicative absorber. Zero is passive (vacuous) rather than active (destructive).
- Proves *I.P19* (Integral Domain): n̲ × m̲ = 0̲ iff n̲ = 0̲ or m̲ = 0̲ — no zero divisors. Follows from positive core closure (Chapter 12).
- Proves *I.T09* (Fundamental Theorem of Arithmetic on τ-Idx): every n̲ ≥ 2̲ has a unique representation as an ordered product of prime powers. Existence by strong induction; uniqueness via an internal Euclid's Lemma, which holds because the Euclidean algorithm terminates under the well-ordering.
- Defines the prime signature Σ(n̲) as the canonical prime-exponent sequence, a complete invariant for τ-Idx.
- Defines the prime enumeration function nthPrime and the prime index function primeIdx, establishing the π-orbit as a faithful enumeration of ℙ_τ. Notes the "earned Sieve of Eratosthenes" — every step is a finite fold of ρ.
- Lean coverage: `TauLib.BookI.Coordinates.Primes` (idx_divides, idx_prime, primes_infinite, prime_product_exists/unique, euclid_lemma) and `TauLib.BookI.Denotation.Structural` (zero vacuity, integral domain). All proofs compile without `sorry`.

## Lean coverage

`TauLib.BookI.Coordinates.Primes`, `TauLib.BookI.Coordinates.PrimeEnumeration`, `TauLib.BookI.Denotation.Structural`

## Where this leads

Chapter 17 lifts the FTA to tower atoms: primes raised to heights that are themselves iterated exponentials. The tower atom structure — and the forced nesting (a̲ ↑↑ c̲)^{b̲} that makes all three parameters uniquely recoverable — is the direct precursor of the greedy peel-off algorithm and the ABCD coordinate chart.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part04/ch16-primes-divisibility.tex -->
