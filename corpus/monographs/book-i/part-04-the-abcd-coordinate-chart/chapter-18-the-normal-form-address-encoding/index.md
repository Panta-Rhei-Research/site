---
layout: "corpus-monograph-chapter"
title: "Chapter 18: The Normal-Form Address Encoding"
permalink: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-18-the-normal-form-address-encoding/"
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
chapter_number: 18
chapter_slug: "chapter-18-the-normal-form-address-encoding"
page_in_book: 73
prev_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-17-tower-atoms-and-the-greedy-peel/"
prev_chapter_title: "Chapter 17: Tower Atoms and the Greedy Peel"
next_chapter_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/chapter-19-the-abcd-coordinate-chart/"
next_chapter_title: "Chapter 19: The ABCD Coordinate Chart"
summary_short: "NF encoding X = ((A^^C)^B)*D exists for every X >= 2. The remainder satisfies prime descent; iterating the peel yields the genealogical decomposition and spine."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-04-the-abcd-coordinate-chart/"
canonical_part_title: "The ABCD Coordinate Chart"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-04-the-abcd-coordinate-chart/chapter-18-the-normal-form-address-encoding/"
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

Chapter 17 defined tower atoms and the greedy peel-off algorithm, which produces a single tuple (A, B, C, D) from any X ≥ 2̲. But the remainder D is itself an element of τ-Idx — it may be non-trivial and admit further structure. This chapter defines the *normal-form address encoding*: the one-step decomposition X = ((A ↑↑ C)^{B}) · D, and proves its *existence* for all X ≥ 2̲. The key structural property is the prime descent of D: if D > 1̲, its largest prime factor is strictly less than A — so the remainder lives in a lower stratum of the prime hierarchy. Iterating the peel along D's remainder chain produces the *genealogical decomposition* (spine): a finite sequence of ABC-triplets from which X is completely recoverable. The spine Cayley length is a canonical, monoidal metric on τ-Idx. NF *uniqueness* — whether Φ(X) = Φ(Y) implies X = Y — is the Hyperfactorization Theorem of Part V.

## What this chapter contributes

- Defines *I.D16* (NF Address Encoding): X = ((A ↑↑ C)^{B}) · D, the output of one application of the greedy peel. Notes the refinement relationship with the flat prime factorization of Chapter 16: the NF imposes additional hierarchical structure.
- Proves NF Existence: every X ≥ 2̲ has an NF encoding. Follows from peel termination (Chapter 17) and the construction ensuring A is prime, B ≥ 1̲, C ≥ 1̲, and D is well-defined as the exact quotient.
- Proves the five NF properties: A is prime; B, C ≥ 1̲; D ≥ 1̲; if D > 1̲ then the largest prime of D is strictly less than A (prime descent); and T(A, B, C) · D = X.
- The prime descent property is the structural key: it guarantees that the remainder lives in a strictly lower prime stratum, enabling the termination of the full genealogical recursion.
- Defines *I.D23* (Genealogical Decomposition / Spine): iterate the peel along D to obtain the sequence G(X) = ((A₁, B₁, C₁), (A₂, B₂, C₂), …, (Aₖ, Bₖ, Cₖ)) with strictly decreasing primes A₁ > A₂ > … > Aₖ. Proves termination.
- Defines the spine Cayley length ℓ_spine(X) = k, and notes it is a canonical monoidal Cayley metric — the canonical word length over tower atoms.
- Notes the ultrametric prefix structure: the spine of D₁ is the suffix of the spine of X, aligning with ultrametric topology developed in Parts VIII–IX.
- Documents the terminological evolution from CGANF (1st Edition) to ABCD encoding (2nd Edition), and explains how cluster collapse is subsumed automatically by the greedy peel.
- Lean coverage: `TauLib.BookI.Coordinates.ABCD` (planned sprint: nf_encoding, nf_existence, nf_remainder_descent).

## Lean coverage

`TauLib.BookI.Coordinates.NormalForm`, `TauLib.BookI.Coordinates.ABCD` (planned)

## Where this leads

Chapter 19 assembles all ingredients into the ABCD coordinate chart Φ : Obj(τ) → τ-Idx⁴, proves totality, and explains the 1+3 split (D is radial, (A, B, C) are solenoidal) and its preview of the fibration τ³ = τ¹ ×_f T². Chapter 20 then proves dim_τ = 4 via pairwise coordinate independence and deduces the necessity of exactly four orbit channels.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part04/ch18-nf-encoding.tex -->
