---
layout: "corpus-monograph-chapter"
title: "Chapter 26: Primorial Verification of RH"
permalink: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-26-primorial-verification-of-rh/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-the-spectral-doors"
chapter_number: 26
chapter_slug: "chapter-26-primorial-verification-of-rh"
page_in_book: 143
prev_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-25-spectral-purity-and-the-critical-line/"
prev_chapter_title: "Chapter 25: Spectral Purity and the Critical Line"
next_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-27-the-grand-grh/"
next_chapter_title: "Chapter 27: The Grand GRH"
summary_short: "The Six Proof Obligations Ledger III.R13 itemises all steps bridging τ-RH to orthodox RH, identifies O3 (determinant representation) as the single open gap, and specifies a computable primorial verification protocol running in O(k³) per depth k."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
canonical_part_title: "The Spectral Doors"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-04-the-spectral-doors/chapter-26-primorial-verification-of-rh/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part IV: The Spectral Doors"
      url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part IV"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 35
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Chapters 22–25 established the τ-RH argument in structural terms. This chapter shifts register from structure to computation. The τ-effective RH statement at depth k asserts that the finite Euler product over the first k primes is spectrally pure: in the finite-dimensional spectral window at depth Prim(k), all non-trivial zeros are on the critical line Re(s) = ½. At each fixed k this is a finite linear algebra problem, solvable in O(k³) operations — eigenvalue computation in a k×k matrix. The Primorial RH Verification Protocol specifies the algorithm: construct the finite bipolar Euler product at depth k, decompose into B and C sectors via the Label_n classifier, form the finite-dimensional approximation to the lemniscate operator, compute its eigenvalues, and check spectral purity. The protocol has been implemented and verified for k ≤ 12. The Six Proof Obligations Ledger then provides a complete audit of all the steps between τ-RH and orthodox RH. The six obligations O1–O6 are: O1 bijection of zero sets; O2 analytic continuation of ζ_τ; O3 Fredholm determinant representation; O4 spectral completeness; O5 convergence at all depths; O6 agreement of finite and infinite products. Of these, O1, O2, O4, O5, and O6 have τ-effective proofs. O3 alone is conjectural. The chapter names this gap clearly, does not minimise it, and assigns scope grade τ-effective conditional on O3 to the entire Chapters 24–25 argument.

## What this chapter contributes

- **Definitions / Axioms:** *III.D30 — τ-Effective RH Statement at Depth k*. Spectral purity of the finite primorial Euler product at depth k; the finite-dimensional spectral window; precise definition of what τ-RH claims at each level.
- **Key results:** *III.P11 — Primorial RH Verification Protocol* (τ-effective): a computable O(k³) algorithm for verifying τ-RH at each primorial depth k; reference implementation verified for k ≤ 12. *III.R13 — Six Proof Obligations Ledger*: itemised O1–O6 with proof status; O1, O2, O4, O5, O6 are proved; O3 (Fredholm determinant representation) is the single open gap.
- **Dependencies:** *III.T18* (Spectral Correspondence, the bridge that O3 would complete); *III.D19* (Primorial Ladder for depth indexing); *III.T16* (Bipolar Euler Product for the finite window).

## Lean coverage

This chapter is prose-only at the current release; the Primorial RH Verification Protocol has a reference implementation but does not yet have a TauLib formalisation.

## Where this leads

Chapter 27 extends the τ-RH structure to all L-functions via the Grand GRH: the Label_n classifier and the scaling chain ζ → Dirichlet → Hecke → automorphic show that spectral purity propagates along the chain, and the Grand GRH is the assertion that it holds for every adelic boundary character on A_τ.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part04/ch26-primorial-verification-of-rh.tex -->
