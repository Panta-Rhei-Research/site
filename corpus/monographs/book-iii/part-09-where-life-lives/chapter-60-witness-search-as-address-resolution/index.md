---
layout: "corpus-monograph-chapter"
title: "Chapter 60: Witness Search as Address Resolution"
permalink: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-60-witness-search-as-address-resolution/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-where-life-lives"
chapter_number: 60
chapter_slug: "chapter-60-witness-search-as-address-resolution"
page_in_book: 307
prev_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-59-interface-width-and-tau/"
prev_chapter_title: "Chapter 59: Interface Width and τ"
next_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-61-the-computational-bi-square/"
next_chapter_title: "Chapter 61: The Computational Bi-Square"
summary_short: "NP witnesses are τ-addresses with ABCD coordinates (*III.D55*); the CRT Witness Decomposition (*III.P22*) factorises search into independent per-prime problems, yielding O(k² log k) total cost (*III.P23*)."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
canonical_part_title: "Where Life Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-09-where-life-lives/chapter-60-witness-search-as-address-resolution/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part IX: Where Life Lives"
      url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part IX"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 40
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Chapter 59 established that τ-admissible computations factor through a single finite quotient ℤ/Prim(k₀)ℤ. This chapter applies that collapse to NP witness search. In classical complexity, a witness is an arbitrary bitstring and the search space is {0,1}^{p(n)} — a flat set with no multiplicative structure, making exhaustive enumeration unavoidable in the worst case. In Category τ, a witness is a canonical address (*III.D55*) whose ABCD coordinates structure the search space, and the CRT decomposition (*III.P22*) factorises the search into k independent per-prime problems. The total search cost is O(k² log k) — polynomial in the primorial depth — because the CRT converts a product of per-prime costs into a sum (*III.P23*).

## What this chapter contributes

Section 1 establishes NP in Category τ. An input x is a τ-address in ℤ̂_τ; a witness w is likewise a τ-address; verification is a TTM computation. The witness space at depth k is W(x, k) = {w ∈ ℤ/Prim(k)ℤ | TTM verifier V accepts (x, w)}.

Section 2 introduces the ABCD decomposition of witnesses (*III.D55*). Every τ-address decomposes canonically into four components via the 4+1 sector structure: A (address: the canonical NF identifier in the additive sector), B (body: the multiplicative layer encoding the divisibility structure, exponent profile across primes p₁, …, p_k), C (content: the exponential depth, bounded by W(V) for τ-admissible computations), and D (depth: the primorial stage Prim(k) at which w is resolved). The four coordinates are algebraically independent — a search strategy can fix three and sweep the fourth. In the SAT example at depth k: D = Prim(k) is fixed, C = 0 (no iterated exponentiation), B encodes variable truth values via polarity χ⁺/χ⁻, and A records the canonical NF address. The search reduces to the B-component, which inherits CRT product structure.

Section 3 proves the CRT Witness Decomposition (*III.P22*): for a τ-admissible problem Π with verifier V at depth k, W(x, k) ≅ ∏_{i=1}^{k} W(x, p_i) where W(x, p_i) ⊆ ℤ/p_iℤ is the per-prime witness space. The decomposition has three properties: independence (w_i at prime p_i does not constrain w_j at p_j for j ≠ i), unique reassembly (given (w₁, …, w_k), the CRT produces a unique global witness), and multiplicative cardinality (|W(x,k)| = ∏|W(x,p_i)|). The proof relies on the Interface Width Principle (*III.T31*) and the Earned Admissibility Proposition (*III.P21*): CRT products of admissible functions preserve admissibility, making per-prime verifications self-contained.

Section 4 proves Polynomial Refinement (*III.P23*): the total search cost Cost(x, k) = ∑_{i=1}^{k} |W(x, p_i)| ≤ ∑_{i=1}^{k} p_i = O(k² log k), by the Prime Number Theorem. The contrast with brute force is exponential: Prim(k) ~ e^{k ln k} versus O(k² log k). The CRT replaces the product of per-prime costs with a sum. The polynomial refinement is not an algorithmic trick — it is a structural consequence of the CRT. Exponential cost reflects the *absence* of multiplicative structure in bitstring witness spaces; polynomial cost reflects its *presence* in the primorial tower.

## Lean coverage

The independence of per-prime witness spaces (from *III.P22*) is the central structural fact: each prime p_i contributes an independent search of size at most p_i, proceeding simultaneously with all other primes. The global witness is assembled via CRT reconstruction — the algebraic analog of parallel computation. The admissibility boundary governs applicability: for τ-admissible instances, the tower stabilises and the factorisation applies; for inadmissible instances (verifier width W(V) = ∞), the tower does not stabilise and the CRT structure cannot be invoked.

## Where this leads

Chapter 61 constructs the Computational Bi-Square (*III.D56*) — the fourth and final bi-square in the scaling chain — and proves the Product-Meet Collapse (*III.T32*) and the τ-Admissibility Collapse (*III.T33*): for every τ-admissible NP problem, τ-P_adm = τ-NP_adm. The polynomial search cost of Chapter 60 provides step 2 of the three-step proof; the Product-Meet Collapse provides step 3.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part09/ch57-witness-search-as-address-resolution.tex -->
