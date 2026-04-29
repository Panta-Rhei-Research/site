---
layout: "corpus-monograph-chapter"
title: "Chapter 17: The Adelic Embedding"
permalink: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-17-the-adelic-embedding/"
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
chapter_number: 17
chapter_slug: "chapter-17-the-adelic-embedding"
page_in_book: 99
prev_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-16-hensel-lifting-and-local-fields/"
prev_chapter_title: "Chapter 16: Hensel Lifting and Local Fields"
next_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-18-the-internal-bipolar-classifier/"
next_chapter_title: "Chapter 18: The Internal Bipolar Classifier"
summary_short: "The τ-adele ring A_τ = ∏'_p ℤₚ^τ is defined as a restricted product with no archimedean factor; the Adelic Embedding Theorem III.T12 diagonally embeds τ into A_τ and proves the adelic Euler product formula."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/"
canonical_part_title: "The Spectral Algebra"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-17-the-adelic-embedding/"
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

Chapters 14–16 produced the local infrastructure: the primorial ladder, CRT decomposition, and τ-native p-adic integers ℤₚ^τ. This chapter assembles the global object. The τ-adele ring is the restricted product A_τ = ∏′_p ℤₚ^τ: an adele is a family (aₚ)_p with aₚ ∈ ℤₚ^τ and aₚ ∈ ℤₚ^τ° (the unit ball) for all but finitely many p. The crucial difference from the classical adeles of ℚ is the absence of any archimedean factor: the τ-framework has no ℝ component, because the five generators produce only non-archimedean arithmetic. This is a structural signature, not a deficiency — all analytic content is derived from spectral algebra rather than real-valued analysis. The Adelic Embedding Theorem proves that there is a diagonal ring map τ → A_τ sending each element to the constant sequence at every prime, that this diagonal image is discrete in the restricted-product topology, and that the adelic Euler product formula ∏_p |a|_p · ‖a‖_NF = 1 holds without an archimedean correction factor. The adele ring A_τ is the domain in which the boundary characters χ_B and χ_C of Chapter 18 will be defined and decomposed — it is the global arithmetic arena for the entire Part IV programme.

## What this chapter contributes

- **Definitions / Axioms:** *III.D22 — τ-Adele Ring A_τ*. The restricted product ∏′_p ℤₚ^τ with no archimedean factor; the restricted-product topology; the adele ring as the global non-archimedean arithmetic domain for the τ-framework.
- **Key results:** *III.T12 — Adelic Embedding Theorem* (τ-effective): the diagonal map τ → A_τ is a ring embedding with discrete image; the adele ring is the correct global object for τ-arithmetic. *III.P07 — Adelic Euler Product Formula*: the product formula ∏_p |a|_p · ‖a‖_NF = 1 holds without archimedean factor, as a direct consequence of the local-global bridge of Chapter 16.
- **Dependencies:** *III.D21* (τ-native local field ℤₚ^τ); *III.T11* (Constructive Hensel Lifting, local completeness); *III.T09* (Cofinality Theorem, global assembly); *I.T04* (Hyperfactorization, NF norms).

## Lean coverage

This chapter is prose-only at the current release; the restricted-product construction and the Adelic Embedding Theorem do not yet have corresponding TauLib modules.

## Where this leads

Chapter 18 installs the internal bipolar classifier on the adelic boundary: each prime is labelled B, C, or X via the Legendre symbol (2/p), the labelling lifts to the full adele ring, and the result is a computable partition of the primes that will drive the spectral decomposition of Chapter 19.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part03/ch17-the-adelic-embedding.tex -->
