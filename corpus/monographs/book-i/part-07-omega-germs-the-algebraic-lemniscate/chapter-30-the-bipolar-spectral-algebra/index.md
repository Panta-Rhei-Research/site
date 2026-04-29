---
layout: "corpus-monograph-chapter"
title: "Chapter 30: The Bipolar Spectral Algebra"
permalink: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-30-the-bipolar-spectral-algebra/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-omega-germs-the-algebraic-lemniscate"
chapter_number: 30
chapter_slug: "chapter-30-the-bipolar-spectral-algebra"
page_in_book: 115
prev_chapter_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-29-polarized-omega-germs/"
prev_chapter_title: "Chapter 29: Polarized Omega-Germs"
next_chapter_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-31-finite-witnesses-the-road-ahead/"
next_chapter_title: "Chapter 31: Finite Witnesses & the Road Ahead"
summary_short: "Three requirements force split-complex scalars (j² = +1) over elliptic ones. The boundary local ring ℤ̂_τ (*I.D28*), the bipolar spectral algebra H_τ (*I.D27*), and the algebraic lemniscate ℒ (*I.D18*) are assembled from the primorial inverse system."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/"
canonical_part_title: "Omega-Germs & the Algebraic Lemniscate"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-30-the-bipolar-spectral-algebra/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part VII: Omega-Germs & the Algebraic Lemniscate"
      url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part VII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 8
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

The polarized omega-germs of Chapter 29 partition the boundary data of τ into three families: B-polarized, C-polarized, and the unique crossing-point germ. To do analysis on this boundary — to speak of functions, transformations, and holomorphic structure — a scalar ring is needed in which boundary functions take values. What ring is it? Three requirements constrain the answer: the scalars must encode the B/C partition as an intrinsic structural feature; they must arise from the primorial inverse system rather than be imported from classical analysis; and they must be compatible with the diagonal-free discipline of Book I Part I. This chapter proves that these three requirements, jointly, force split-complex scalars with j² = +1 (*I.T10*) — not elliptic scalars with i² = −1. The scalar ring is then the boundary local ring ℤ̂_τ = lim← ℤ/M_kℤ (*I.D28*), and the bipolar spectral algebra is H_τ = ℤ̂_τ[j] with canonical idempotents e_± = (1 ± j)/2 (*I.D27*). Together with the crossing-point germ ω_ℒ and the polarity involution σ, these assemble the algebraic lemniscate ℒ = (H_τ, ω_ℒ, σ) (*I.D18*).

## What this chapter contributes

The chapter delivers four major constructions, all verified in Lean. First, the boundary local ring (*I.D28*) is the primorial inverse limit ℤ̂_τ with stagewise ring operations; the Chinese Remainder Theorem at each stage decomposes ℤ/M_kℤ into a product of B-sector fields and C-sector fields, with the CRT isomorphism and Teichmüller lifts all formalized. Second, the Split-Complex Forced Theorem (*I.T10*) shows that elliptic complexification ℤ̂_τ[i] fails all three requirements (it is structurally unipolar, its holomorphy yields the diffusion equation rather than the wave equation, and it lacks the zero-divisor structure that the diagonal-free discipline manages). Split-complex extension ℤ̂_τ[j] with j² = +1 satisfies all three. Third, the bipolar spectral algebra (*I.D27*) H_τ = ℤ̂_τ ⊕ j·ℤ̂_τ carries canonical idempotents with e_+² = e_+, e_-² = e_-, e_+ · e_- = 0, and e_+ + e_- = 1. The polarity character χ̃: ℙ_τ → {e_+, e_-} assigns each prime its sector idempotent and extends multiplicatively to all of τ-Idx. Fourth, the Algebraic Lemniscate Theorem (*I.D18*) assembles ℒ: the bipolar spectral algebra, the unique crossing-point germ as identity, and the polarity involution σ that swaps the two sectors. Holomorphic functions are defined as primitive: omega-germ transformers valued in H_τ satisfying algebraic naturality, defined before topology exists. Nine Lean modules formalize this chapter, all compiling without `sorry`.

## Lean coverage

Formalized across nine modules: `TauLib.BookI.Polarity.ModArith`, `OmegaRing`, `PrimeBridge`, `ExtGCD`, `ChineseRemainder`, `NthPrime`, `CRTBasis`, `TeichmuellerLift`, and `BipolarAlgebra`. Key results include `split_complex_forced`, `e_plus_idem`, `e_minus_idem`, `e_orthogonal`, `e_partition`, `chi_split`, and `algebraic_lemniscate_exists`. The module `TauLib.BookI.Polarity.Lemniscate` proves `canonical_swaps_sectors` and `split_complex_zero_divisor`. All proofs compile with zero `sorry`.

## Where this leads

Chapter 31 reflects on the hinge block as a whole, explains the local–global bridge from finite prime polarity computations to the infinite algebraic lemniscate, and previews Parts VIII–XVI. Part XI (this part's numerical parallel for τ-Logic) will use the idempotent decomposition of H_τ to earn four truth values. The algebraic lemniscate is the key object of the Central Theorem of Book II: 𝒪(τ³) ≅ A_spec(ℒ).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part07/ch30-bipolar-algebra.tex -->
