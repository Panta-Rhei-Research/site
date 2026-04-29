---
layout: "corpus-monograph-chapter"
title: "Chapter 18: The Internal Bipolar Classifier"
permalink: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-18-the-internal-bipolar-classifier/"
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
chapter_number: 18
chapter_slug: "chapter-18-the-internal-bipolar-classifier"
page_in_book: 105
prev_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-17-the-adelic-embedding/"
prev_chapter_title: "Chapter 17: The Adelic Embedding"
next_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-19-the-spectral-trichotomy/"
next_chapter_title: "Chapter 19: The Spectral Trichotomy"
summary_short: "The bipolar classifier Label_n assigns each prime a sector label B, C, or X via the Legendre symbol (2/p); Label convergence III.T13 shows the assignment stabilizes immediately, turning informal lobe language into a computable decision procedure."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/"
canonical_part_title: "The Spectral Algebra"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-18-the-internal-bipolar-classifier/"
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

Parts I and II referred to the "B-lobe" and "C-lobe" of the lemniscate boundary as informal sector language. This chapter makes that language internal: the bipolar classifier Label_n is a computable function that assigns each prime a definite sector label, turning lobe intuition into a decision procedure. At each primorial depth n, the function Label_n : {p₁,…,pₙ} → {B, C, X} uses the Legendre symbol (2/p) as its oracle: Label_n(p) = B when 2 is a quadratic residue mod p (equivalently, p ≡ ±1 mod 8 by quadratic reciprocity), Label_n(p) = C when p ≡ ±3 mod 8, and Label_n(2) = X. The assignment requires only modular arithmetic — no analytic input, no asymptotic reasoning. The Label Convergence Theorem proves that Label_n(p) stabilises immediately at depth n = 1 for every odd prime: the sector classification is a fixed property of each prime, not a limit. The Label-Idempotent Compatibility proposition then verifies that the B- and C-sector CRT idempotents from Chapter 15 are exactly the characteristic functions of the B- and C-labelled primes, so the classifier is coherent with all the algebraic structure already in place. The X-label at p = 2 marks the inert prime that acts on both sectors equally and contributes to the split-complex unit structure rather than to either bipolar component.

## What this chapter contributes

- **Definitions / Axioms:** *III.D23 — Internal Bipolar Classifier Label_n*. The function Label_n : {p₁,…,pₙ} → {B, C, X} via the Legendre symbol (2/p); the stable limit Label_∞ with the explicit rule Label_∞(p) = B iff p ≡ ±1 (mod 8), C iff p ≡ ±3 (mod 8), X iff p = 2.
- **Key results:** *III.T13 — Label Convergence* (τ-effective): Label_n(p) stabilises at depth n = 1 for every odd prime p; the sector classification is exact and not a limit construction. *III.P08 — Label-Idempotent Compatibility*: the CRT idempotents from Chapter 15 are exactly the characteristic functions of the Label_∞-labelled primes; the classifier is algebraically coherent with the primorial tower.
- **Dependencies:** *III.D22* (τ-adele ring as domain); *III.T10* (CRT Decomposition idempotents); quadratic reciprocity and Legendre symbol from the earned Part II arithmetic.

## Lean coverage

This chapter is prose-only at the current release; the Label_n decision procedure and the Label Convergence Theorem do not yet have corresponding TauLib modules.

## Where this leads

Chapter 19 applies the classifier to prove the Spectral Trichotomy: every character on the adelic boundary decomposes uniquely as χ = χ_B + χ_C, and the two sectors are provably non-isomorphic as modules over the primorial tower. That non-collapse result is the algebraic backbone of the Part IV Riemann Hypothesis argument.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part03/ch18-the-internal-bipolar-classifier.tex -->
