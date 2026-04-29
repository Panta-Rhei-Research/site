---
layout: "corpus-monograph-chapter"
title: "Chapter 25: Spectral Purity and the Critical Line"
permalink: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-25-spectral-purity-and-the-critical-line/"
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
chapter_number: 25
chapter_slug: "chapter-25-spectral-purity-and-the-critical-line"
page_in_book: 139
prev_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-24-the-spectral-correspondence/"
prev_chapter_title: "Chapter 24: The Spectral Correspondence"
next_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-26-primorial-verification-of-rh/"
next_chapter_title: "Chapter 26: Primorial Verification of RH"
summary_short: "The Critical Line Theorem III.T19 is derived from self-adjointness: real eigenvalues of H_L force σ = ½ for non-trivial zeros; K5 Off-Diagonal Exclusion III.P10 shows bipolar symmetry forbids off-diagonal mixing that would allow off-critical zeros."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/"
canonical_part_title: "The Spectral Doors"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-04-the-spectral-doors/chapter-25-spectral-purity-and-the-critical-line/"
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

Chapter 24 established, conditional on conjecture O3, that non-trivial zeros of ζ_τ biject with eigenvalues of H_L via the spectral parameter Λ(s) = ι_τ²(s(1−s)−¼). This chapter harvests the constraint that self-adjointness of H_L imposes on those eigenvalues. The argument is four steps. Step 1: self-adjointness of H_L (Chapter 23) forces every eigenvalue λₙ to be real. Step 2: the Spectral Correspondence (Chapter 24, conditional on O3) gives Λ(ρ) = λₙ for every non-trivial zero ρ = σ + iγ. Step 3: since λₙ is real, Im(Λ(ρ)) = 0. Step 4: expanding Λ(ρ) = ι_τ²(ρ(1−ρ)−¼) and extracting the imaginary part yields Im(Λ) = ι_τ²·γ·(1−2σ); setting this to zero and using γ ≠ 0 (non-trivial zeros have non-zero imaginary part) forces σ = ½. The Critical Line Theorem follows immediately. The K5 Off-Diagonal Exclusion proposition provides the generator-axiom backing: axiom K5 forces H_L to be block-diagonal in the B/C split, forbidding the off-diagonal mixing that would be needed to produce a zero with σ ≠ ½. The chapter also interprets the critical line geometrically as the balance hyperplane where B-sector and C-sector spectral weights are equal — a balance forced by the bipolar symmetry of the boundary algebra. All results are τ-effective, conditional on O3; no stronger claim is made and the gap is not minimised.

## What this chapter contributes

- **Definitions / Axioms:** No new definitions; this chapter derives consequences from the structure built in Chapters 22–24.
- **Key results:** *III.T19 — Critical Line Theorem* (τ-effective, conditional on O3): every non-trivial zero ρ of ζ_τ satisfies Re(ρ) = ½; the complete deduction chain is self-adjointness → real eigenvalues → Im(Λ(ρ)) = 0 → γ(1−2σ) = 0 → σ = ½. *III.P10 — K5 Off-Diagonal Exclusion*: axiom K5 forces block-diagonal structure in H_L in the B/C split, structurally excluding off-diagonal mixing that would permit off-critical zeros.
- **Dependencies:** *III.T18* (Spectral Correspondence, conditional on O3); *III.T17* (Self-adjointness of H_L); *III.D29* (Spectral parameter Λ(s)); *III.D27* (Involution J and Fix(J)); K5 from Part I axiom list.

## Lean coverage

This chapter is prose-only at the current release; the Critical Line Theorem is conditional on O3 and does not yet have a TauLib formalisation.

## Where this leads

Chapter 26 shifts register from structural to computational: it specifies exactly what the τ-effective RH statement claims at each primorial depth k, provides a verifiable O(k³) algorithm, and itemises all six proof obligations O1–O6 — declaring O1, O2, O4, O5, O6 proved and O3 the single open gap.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part04/ch25-spectral-purity-and-the-critical-line.tex -->
