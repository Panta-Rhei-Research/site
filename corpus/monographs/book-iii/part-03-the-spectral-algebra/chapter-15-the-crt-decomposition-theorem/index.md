---
layout: "corpus-monograph-chapter"
title: "Chapter 15: The CRT Decomposition Theorem"
permalink: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-15-the-crt-decomposition-theorem/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 3
part_display: "Part III"
part_slug: "part-03-the-spectral-algebra"
chapter_number: 15
chapter_slug: "chapter-15-the-crt-decomposition-theorem"
page_in_book: 87
prev_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-14-the-primorial-ladder/"
prev_chapter_title: "Chapter 14: The Primorial Ladder"
next_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-16-hensel-lifting-and-local-fields/"
next_chapter_title: "Chapter 16: Hensel Lifting and Local Fields"
summary_short: "The CRT Decomposition Theorem III.T10 earns the isomorphism ℤ/Prim(k)ℤ ≅ ∏ ℤ/pᵢℤ constructively from Fermat exponentiation alone, yielding the algebraic Euler product and the Reconstruction Functor III.D20."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/"
canonical_part_title: "The Spectral Algebra"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-15-the-crt-decomposition-theorem/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part III: The Spectral Algebra"
      url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part III"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 34
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The Chinese Remainder Theorem is classical, but the standard proof uses the extended Euclidean algorithm, which performs iterated subtraction — an operation the τ-kernel does not import. This chapter earns the CRT constructively, replacing Bézout coefficients obtained by signed arithmetic with modular inverses computed via Fermat exponentiation: for a non-zero element a in ℤ/pℤ, the unique inverse is a^{p−2} mod p, computed purely by iterated multiplication available from axiom K2. The idempotents eᵢ = sᵢ·(Prim(k)/pᵢ) satisfy the partition-of-unity condition Σeᵢ ≡ 1 (mod Prim(k)) and the orthogonality conditions eᵢ ≡ δᵢⱼ (mod pⱼ), yielding the isomorphism Φₖ : ℤ/Prim(k)ℤ → ∏ᵢ ℤ/pᵢℤ with explicit inverse. This constructive proof is cross-validated against the Lean formalisation of I.D29 in TauLib.BookI.Polarity.ChineseRemainder. The algebraic Euler product reading follows: the endomorphism ring of the primorial presheaf decomposes as End(F) ≅ ∏_p End(ℤ/pℤ), one degree of freedom per prime with no inter-prime interaction at the ring level. The Reconstruction Functor then lifts this to an equivalence of module categories, providing the decompose-solve-reassemble engine used by every prime-by-prime argument in Parts IV–VI.

## What this chapter contributes

- **Definitions / Axioms:** *III.D20 — Reconstruction Functor*. The equivalence ℛₖ : ∏(Rᵢ-Mod) → R-Mod and its quasi-inverse restriction functor 𝒮ₖ; both exact; endomorphism algebra decomposition End(F) ≅ ∏_p End(ℤ/pℤ) as the algebraic Euler product.
- **Key results:** *III.T10 — CRT Decomposition Theorem* (τ-effective): the isomorphism ℤ/Prim(k)ℤ ≅ ∏ᵢ ℤ/pᵢℤ is earned using only multiplication (K2) and divisibility (K3), with explicit idempotents from Fermat exponentiation; the module-level equivalence is exact. *III.P05 — Independence of Prime-Level Actions*: modifying one prime-level action leaves all others unchanged; composition and equality are prime-wise; the τ-incarnation of the local-global principle.
- **Dependencies:** *III.D19* (Primorial Ladder, cofinality); *III.T09* (Cofinality Theorem); *I.D83* (Primorial presheaf); *I.T41* (Bi-square characterisation).

## Lean coverage

This chapter is prose-only at the current release; the constructive Fermat-exponentiation proof and the Reconstruction Functor equivalence do not yet have corresponding TauLib modules, though the idempotent basis is cross-validated against I.D29.

## Where this leads

Chapter 16 climbs the prime-power towers vertically: given a root modulo p, constructive Hensel lifting extends it to a root modulo p², p³, and so on, producing the τ-native p-adic integers ℤₚ^τ as an inverse limit without any metric or topological axiom. Chapter 17 then assembles all the local fields into the τ-adele ring.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part03/ch15-the-crt-decomposition-theorem.tex -->
