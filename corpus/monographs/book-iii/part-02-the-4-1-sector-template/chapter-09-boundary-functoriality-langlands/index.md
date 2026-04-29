---
layout: "corpus-monograph-chapter"
title: "Chapter 9: Boundary Functoriality (Langlands₀"
permalink: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-09-boundary-functoriality-langlands/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 2
part_display: "Part II"
part_slug: "part-02-the-4-1-sector-template"
chapter_number: 9
chapter_slug: "chapter-09-boundary-functoriality-langlands"
page_in_book: 47
prev_chapter_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-08-the-canonical-ladder-theorem/"
prev_chapter_title: "Chapter 8: The Canonical Ladder Theorem"
next_chapter_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-10-the-4/"
next_chapter_title: "Chapter 10: The 4+"
summary_short: "The boundary character space Char(𝕃) ≅ S¹×S¹ and the ℤ² character lattice support the boundary-to-interior functor Φ (Langlands₀, III.D12). The Sector Preservation Theorem (III.T05) maps χ₊-characters to the B-sector, χ₋-characters to the C-sector, and mixed characters to the ω-coupling sector."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/"
canonical_part_title: "The 4+1 Sector Template"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-02-the-4-1-sector-template/chapter-09-boundary-functoriality-langlands/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part II: The 4+1 Sector Template"
      url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part II"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 33
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Part I established the four-layer enrichment ladder and the universal layer template. Part II deploys that template for the first time, and this chapter provides the foundational mechanism. The algebraic lemniscate 𝕃 = S¹ ∨ S¹ has fundamental group π₁(𝕃) = ℤ ∗ ℤ and first homology H₁(𝕃; ℤ) ≅ ℤ², so its character space Char(𝕃) = Hom(π₁(𝕃), S¹) ≅ S¹ × S¹ is indexed by a lattice ℤ² whose two axes encode the multiplicative/Galois and additive/automorphic aspects of the series. The chapter constructs the boundary-to-interior functor Φ: Char(𝕃) → O(τ³) (*III.D12*) by stage-by-stage restriction at each primorial level, using the Central Theorem O(τ³) ≅ A_spec(𝕃) (*II.T40*) as the holomorphic extension mechanism. The central result is the Sector Preservation Theorem (*III.T05*, τ-effective): Φ maps χ₊-characters (m = 0) to the B-sector, χ₋-characters (n = 0) to the C-sector, and mixed characters (both m ≠ 0 and n ≠ 0) to the ω-coupling sector. This preservation is what we call Langlands₀, and the 4+1 sector decomposition of the next chapter is therefore not postulated from physical data but induced from the character theory of the lemniscate boundary.

## What this chapter contributes

**Definitions / Axioms**
- *Boundary character space* (*III.D11*): Char(𝕃) := Hom(π₁(𝕃), S¹) ≅ S¹ × S¹. Characters indexed by (m, n) ∈ ℤ²: χ_{(m,n)}(u₋, u₊) = u₋ᵐ · u₊ⁿ. The m-axis is the multiplicative/Galois direction; the n-axis is the additive/automorphic direction. Pure characters (m = 0 or n = 0) vs. mixed characters (both non-zero). At primorial depth k: Char_k(𝕃) ≅ (ℤ/M_kℤ)², recovered as inverse limit.
- *Boundary-to-interior functor* (*III.D12*, Langlands₀, τ-effective): Φ: Char(𝕃) → O(τ³), defined by Φ(χ_{(m,n)})_k = χ_{(m,n)}|_{Char_k(𝕃)}. On morphisms: lattice translations χ_{(a,b)}: χ_{(m,n)} → χ_{(m+a,n+b)} map to holomorphic multiplication. Φ is a functor — preserves composition and identity — not merely a function.
- *Boundary holonomy algebra*: H_∂ = ℤ[π₁(𝕃)]^{τ-adm} = lim← (ℤ/M_kℤ)[ℤ ∗ ℤ]. The abelianization of H_∂ is H_τ. Its one-dimensional S¹-representations are in canonical bijection with ℤ². The enrichment functor F_E acts on H_∂ to produce the E₁-level sector algebra.

**Key results**
- *Sector Preservation Theorem* (*III.T05*, τ-effective): (i) χ₊-characters (m = 0) map to B-sector: Φ(χ_{(0,n)}) = e₊·Φ(χ_{(0,n)})₊. (ii) χ₋-characters (n = 0) map to C-sector: Φ(χ_{(m,0)}) = e₋·Φ(χ_{(m,0)})₋. (iii) Mixed characters map to ω-coupling sector with both components non-trivial. Proved in three steps: stage-level verification, tower coherence via the left square of *I.T41*, and inverse-limit argument for the mixed case.
- *Φ commutes with F_E* (τ-effective): F_E ∘ Φ = Φ ∘ F_E|_{Char(𝕃)}. Enriching before extending equals extending before enriching. This is why the sector decomposition survives the E₀ → E₁ transition — the enrichment functor refines sectors without creating or destroying them.
- *Mutual Determination schema* (τ-effective): RH, Navier–Stokes, and Langlands₀ are three readings of a single boundary→interior→spectral diagram sharing the same functor Φ at the structural level. The 4+1 decomposition is a consequence of character theory, not an additional axiom.

**Notation**
- Char(𝕃) ≅ S¹ × S¹; χ_{(m,n)}(u₋, u₊) = u₋ᵐ · u₊ⁿ; Φ: Char(𝕃) → O(τ³) (Langlands₀); H_∂ = ℤ[π₁(𝕃)]^{τ-adm}; Φ = Φ_B ⊕ Φ_C ⊕ Φ_ω

**Dependencies**
- *I.T41* (Bi-square characterization), *I.D37* (Spectral characters χ₊, χ₋), *I.D83* (Primorial presheaf)
- *II.T40* (Central Theorem O(τ³) ≅ A_spec(𝕃)), *II.T49* (Geometric bi-square)
- *III.D04* (Enrichment functor F_E), *III.T04* (Canonical Ladder Theorem)

## Lean coverage

The boundary character space *III.D11* and boundary-to-interior functor *III.D12* are planned for `TauLib/BookIII/BoundaryFunctoriality.lean`. The Sector Preservation Theorem *III.T05* is τ-effective with an explicit three-step proof structure; the stage-level verification reduces to a finite computation over (ℤ/M_kℤ)² and is a strong candidate for early Lean 4 coverage. The commutativity F_E ∘ Φ = Φ ∘ F_E requires both the enrichment functor and the boundary functor formalizations and is therefore a secondary Lean target. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Chapter 10 uses the Sector Preservation Theorem to derive the 4+1 sector decomposition S_D ⊔ S_A ⊔ S_B ⊔ S_C ⊔ S_ω as a functorial consequence of the ℤ² character lattice — four primitive sectors plus the ω-coupling sector, which then receives its structural and conjectural physical interpretation.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part02/ch09-boundary-functoriality.tex -->
