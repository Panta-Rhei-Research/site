---
layout: "corpus-monograph-chapter"
title: "Chapter 14: The Primorial Ladder"
permalink: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-14-the-primorial-ladder/"
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
chapter_number: 14
chapter_slug: "chapter-14-the-primorial-ladder"
page_in_book: 81
prev_chapter_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-13-the-no-knobs-principle/"
prev_chapter_title: "Chapter 13: The No Knobs Principle"
next_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-15-the-crt-decomposition-theorem/"
next_chapter_title: "Chapter 15: The CRT Decomposition Theorem"
summary_short: "The primorial ladder Mₖ = p₁⋯pₖ is established as the canonical cofinality witness for the full modular tower, replacing ε-δ approximation with algebraic simultaneous verification across all prime moduli."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/"
canonical_part_title: "The Spectral Algebra"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-14-the-primorial-ladder/"
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

Part II closed with the No Knobs Principle, establishing that every sector coupling is a rational function of ι_τ evaluated at a specific primorial depth. The word "primorial" appeared throughout Parts I and II as background infrastructure — the stages of the tower, the levels at which τ-effective statements are verified, the index set of the primorial presheaf (I.D83). This chapter elevates the primorial tower from background assumption to the central organising object of Part III. The primorial numbers Mₖ = p₁⋯pₖ are products of the first k primes; the primorial ladder is the inverse system ℤ/M₁ℤ ← ℤ/M₂ℤ ← ⋯ with canonical reduction maps, and its inverse limit is the τ-profinite completion ℤ̂_τ. Mₖ is the smallest modulus whose CRT decomposition covers exactly k distinct prime directions with no redundancy, which is why the ladder is the canonical cofinal filtration rather than an arbitrary choice. The chapter proves cofinality, introduces the primorial filter that makes infinity computationally tractable via computable stabilisation depths, and closes with a verification table mapping all eight Millennium Problems to their primorial-level check — the structural guarantee that all of Parts IV–VI are accessing the same underlying tower.

## What this chapter contributes

- **Definitions / Axioms:** *III.D19 — Primorial Ladder*. The inverse system ℤ/M₁ℤ ← ℤ/M₂ℤ ← ⋯ with Mₖ = p₁⋯pₖ and canonical reduction maps; the τ-profinite completion ℤ̂_τ = lim← ℤ/Mₖℤ as its inverse limit; the primorial filter and the notion of F_Prim-eventual properties with computable stabilisation depths.
- **Key results:** *III.T09 — Cofinality Theorem* (τ-effective): the primorial ladder is cofinal in the full modular tower; for every squarefree N, there exists a computable k₀ = π(p_max(N)) such that N ∣ Mₖ for all k ≥ k₀; the canonical map ℤ̂_τ → lim← ℤ/Nℤ (squarefree N) is an isomorphism of profinite rings. *III.R08 — Primorial Verification Principle*: every τ-effective reformulation of a millennium problem holds if and only if the corresponding primorial-level check P(Mₖ) holds for all k ≥ k₀, where k₀ is computable.
- **Dependencies:** *I.D83* (Primorial presheaf); *I.T31* (Global Hartogs Extension); *I.T41* (Bi-square characterisation); *III.D18* (Coupling Ledger); *III.T08* (No Knobs Principle).

## Lean coverage

This chapter is prose-only at the current release; the cofinality theorem and primorial filter construction do not yet have corresponding TauLib modules. The primorial presheaf mechanics were formalised in the Book I TauLib under I.D83.

## Where this leads

Chapter 15 proves the Chinese Remainder Theorem constructively within Category τ — without signed arithmetic — decomposing ℤ/Prim(k)ℤ into a product of independent prime fields and reading that decomposition as the algebraic Euler product. The Reconstruction Functor introduced there will assemble local prime-level data back into global primorial data throughout the rest of Book III.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part03/ch14-the-primorial-ladder.tex -->
