---
layout: "corpus-monograph-chapter"
title: "Chapter 17: Tower Atoms and the Greedy Peel"
permalink: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-17-tower-atoms-and-the-greedy-peel/"
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
chapter_number: 17
chapter_slug: "chapter-17-tower-atoms-and-the-greedy-peel"
page_in_book: 69
prev_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-16-internal-primes-and-divisibility/"
prev_chapter_title: "Chapter 16: Internal Primes and Divisibility"
next_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-18-the-normal-form-address-encoding/"
next_chapter_title: "Chapter 18: The Normal-Form Address Encoding"
summary_short: "A tower atom T(a,b,c) = (a^^c)^b is the unique nesting from which all three parameters are recoverable. The greedy peel extracts (A,B,C,D) deterministically."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
canonical_part_title: "The ABCD Coordinate Chart"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-04-the-abcd-coordinate-chart/chapter-17-tower-atoms-and-the-greedy-peel/"
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

Chapter 16 gave the Fundamental Theorem of Arithmetic on τ-Idx: every n̲ ≥ 2̲ is a flat product of prime powers p̲^{e̲}. But the arithmetic of Part III reaches beyond multiplication and exponentiation to include *tetration*. A *tower atom* is a prime raised to a power whose base is a tetration tower: T(a̲, b̲, c̲) = (a̲ ↑↑ c̲)^{b̲}. This nesting — tetration first, then outer exponentiation — is the *only* one compatible with the diagonal discipline: it is the unique binding from which all three parameters (prime a̲, exponent b̲, tetration height c̲) are independently and uniquely recoverable. The *greedy peel-off algorithm* then extracts the ABCD coordinates from any X by sequentially peeling the largest prime, the maximal tetration height, the maximal exponent, and recording the remainder — each step deterministic by maximality.

## What this chapter contributes

- Defines *I.D19c* (Tower Atom): T(a̲, b̲, c̲) = (a̲ ↑↑ c̲)^{b̲} for prime a̲, b̲ ≥ 1̲, c̲ ≥ 1̲. Notes that c̲ = 1̲ recovers ordinary prime powers; c̲ ≥ 2̲ produces rapidly growing tetration towers. Every tower atom is computed entirely within the earned arithmetic of Part III.
- Proves that the nesting (a̲ ↑↑ c̲)^{b̲} is *forced* by the diagonal discipline: among the three candidate nestings, only this one permits unique recovery of (a̲, b̲, c̲). Alternative nesting (2) entangles b̲ and c̲ in the exponent; nesting (3) entangles a̲ and b̲ in the tetration base. Uniqueness relies on tetration injectivity (Chapter 12, *I.P05*).
- Defines *I.D19d* (Greedy Peel-Off Algorithm): four steps — (1) find A = largest prime divisor of X; (2) find C = maximal c̲ such that (A ↑↑ c̲) | X; (3) find B = maximal b̲ such that (A ↑↑ C)^{b̲} | X; (4) set D = X / T(A, B, C). Output: Φ(X) = (A, B, C, D).
- Proves that the greedy peel terminates and produces a well-defined tuple for every X ≥ 2̲: each search terminates because tetration values grow unboundedly.
- Explains the peel order (A first, then C, then B): reflects the orbit hierarchy — the π-channel (prime) has highest priority, the η-channel (tetration height) is structurally deeper than the γ-channel (exponent).
- Works three concrete examples: Φ(2̲) = (2̲, 1̲, 1̲, 1̲), Φ(12̲) = (3̲, 1̲, 1̲, 4̲), and the trivial Φ(1̲) by convention.
- Lean coverage: `TauLib.BookI.Coordinates.TowerAtoms` (planned sprint: tower_atom, greedy_peel, peel_terminates, forced_nesting).

## Lean coverage

`TauLib.BookI.Coordinates.TowerAtoms` (planned)

## Where this leads

Chapter 18 applies the peel once to define the normal-form address encoding X = (A ↑↑ C)^{B} · D, proves NF existence for all X ≥ 2̲, and introduces the genealogical decomposition (spine) and the spine Cayley length as a canonical metric. NF *uniqueness* — the Hyperfactorization Theorem — is deferred to Part V.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part04/ch17-tower-atoms-peel.tex -->
