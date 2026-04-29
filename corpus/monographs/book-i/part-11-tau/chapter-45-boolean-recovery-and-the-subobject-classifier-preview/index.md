---
layout: "corpus-monograph-chapter"
title: "Chapter 45: Boolean Recovery and the Subobject Classifier Preview"
permalink: "/corpus/monographs/book-i/part-11-tau/chapter-45-boolean-recovery-and-the-subobject-classifier-preview/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 11
part_display: "Part XI"
part_slug: "part-11-tau"
chapter_number: 45
chapter_slug: "chapter-45-boolean-recovery-and-the-subobject-classifier-preview"
page_in_book: 193
prev_chapter_url: "/corpus/monographs/book-i/part-11-tau/chapter-44-the-explosion-barrier/"
prev_chapter_title: "Chapter 44: The Explosion Barrier"
next_chapter_url: "/corpus/monographs/book-i/part-12-holomorphic-transformers/chapter-46-d-holomorphy-and-the-cauchy-riemann-analog/"
next_chapter_title: "Chapter 46: D-Holomorphy and the Cauchy–Riemann Analog"
summary_short: "The bipolar Fourier transform (*I.D40*) and the crossing point (*I.D39*) of the algebraic lemniscate; the Boolean Recovery Theorem (*I.P13*) showing when Truth4 collapses losslessly to Bool; and the definition of Ω_τ := Truth4 as the subobject classifier (*I.D41*)."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-11-tau/"
canonical_part_title: "τ"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-11-tau/chapter-45-boolean-recovery-and-the-subobject-classifier-preview/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part XI: τ"
      url: "/corpus/monographs/book-i/part-11-tau/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part XI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 12
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

Chapter 43 earned the four truth values {T, F, B, N} from the bipolar character structure, and Chapter 44 proved the Explosion Barrier showing that the overdetermined value B cannot propagate across orthogonal sectors. This chapter asks the complementary question: when is the full four-valued apparatus necessary, and when does classical two-valued logic suffice? The answer is given by the Boolean Recovery Theorem (*I.P13*): the forgetful map f: Truth4 → Bool that sends B ↦ T and N ↦ F is lossless precisely when the spectral decomposition assigns only T or F to the predicate in question — when neither overdetermination nor underdetermination arises. The chapter also formalizes the bipolar Fourier transform (*I.D40*) and the algebraic crossing point (*I.D39*), placing Truth4 within the broader analytic framework of ℒ and defining Ω_τ := Truth4 as the subobject classifier (*I.D41*) that will serve as the truth-value object of the earned topos in Part XIII.

## What this chapter contributes

The chapter delivers four interlocking results. First, the crossing point of the algebraic lemniscate is defined as ω_× = 1 = e_+ + e_- (*I.D39*): the unique element whose spectral coefficients satisfy χ_+(ω_×) = χ_-(ω_×) = 1. It is algebraically singular in the precise sense that it is the only element projecting nontrivially onto both sectorial ideals; near it (in the profinite crossing neighborhoods U_k), both characters are congruent to 1 modulo M_k, so the sectorial separation vanishes to higher order as k → ∞. This algebraic singularity previews the geometric node of S¹ ∨ S¹ that will be earned in Book II. Second, the bipolar Fourier transform (*I.D40*) is defined as ℱ: ℒ → ℤ̂_τ × ℤ̂_τ, ℱ(a + bj) = (a + b, a − b), with inverse ℱ⁻¹(α, β) = (α + β)/2 + ((α − β)/2)j. The transform is a ring isomorphism; it converts split-complex multiplication into componentwise multiplication, making the bipolar decomposition of any element explicit. The polarity involution σ corresponds under ℱ to swapping components, and the crossing point maps to the diagonal (1, 1). Third, the Boolean Recovery Theorem (*I.P13*) identifies the exact condition for lossless collapse of Truth4 to Bool: when the spectral decomposition assigns a predicate only T or F values, the forgetful map f: Truth4 → Bool is a bijection on that predicate's range, so no information is lost. Fourth, Ω_τ := Truth4 is established as the subobject classifier (*I.D41*), with the bipolar Fourier transform providing the verification machinery — sector membership can be read off as the Fourier image of an element. Lean formalization is in `TauLib.BookI.Boundary.Fourier`.

## Lean coverage

Formalized in `TauLib.BookI.Boundary.Fourier`. Key results: `crossing_point` (*I.D39*), `crossing_iff_chi_equal`, `fourier` (*I.D40*), `fourier_invertible`, `fourier_sigma_swap`, `fourier_e_plus_sc` and `fourier_e_minus_sc` (ℱ(e_±) = basis vectors), and `fourier_parseval` (Parseval identity for sector norms). All proofs compile with zero `sorry`.

## Where this leads

Part XI is now complete: Truth4 is earned from the spectral structure of ℒ, the explosion barrier ensures non-triviality, boolean recovery identifies the classical regime, and Ω_τ is defined for Part XIII's topos construction. Part XII builds the holomorphic transformer framework: split-complex holomorphy on the fibered product τ³, using the omega-germ naturality conditions formalized in Parts VII–XI as its input data.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part11/ch45-crossing-point.tex -->
