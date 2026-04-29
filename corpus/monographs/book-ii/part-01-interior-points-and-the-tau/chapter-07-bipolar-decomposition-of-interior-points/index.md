---
layout: "corpus-monograph-chapter"
title: "Chapter 7: Bipolar Decomposition of Interior Points"
permalink: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-07-bipolar-decomposition-of-interior-points/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-interior-points-and-the-tau"
chapter_number: 7
chapter_slug: "chapter-07-bipolar-decomposition-of-interior-points"
page_in_book: 31
prev_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-06-the-tau-fibration-emerges/"
prev_chapter_title: "Chapter 6: The τ³ Fibration Emerges"
next_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-08-abcd-structure-replaces-quaternions/"
next_chapter_title: "Chapter 8: ABCD Structure Replaces Quaternions"
summary_short: "The bipolar idempotents e± earned on the boundary 𝕃 in Book I extend canonically to every interior point of τ³ via the fiber coordinates (B, C): the γ/η dominance assigns each τ-admissible point two orthogonal information channels, recovering the two lobes of 𝕃 and their node at the ω-limit."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
canonical_part_title: "Interior Points and the τ³"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-01-interior-points-and-the-tau/chapter-07-bipolar-decomposition-of-interior-points/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part I: Interior Points and the τ³"
      url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part I"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 20
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Book I earned the bipolar idempotents e± = (1 ± j)/2 as boundary structure on the algebraic lemniscate 𝕃: they decompose H_τ into two orthogonal sectors, satisfy e₊² = e₊, e₋² = e₋, e₊ · e₋ = 0, e₊ + e₋ = 1, and correspond to the B-dominant and C-dominant lobes of the bipolar spectral algebra (*I.D27*). This chapter extends the bipolar decomposition from the boundary to every interior point of τ³. The extension is not an additional axiom — it is a theorem. The fiber coordinates (B, C) of the ABCD chart already carry the γ/η dominance information needed for sector assignment: each τ-admissible point (D, A, B, C) decomposes into a B-channel component s₊ = e₊ · Ψ(B, A, D) and a C-channel component s₋ = e₋ · Ψ(C, A, D), where orthogonality e₊ · e₋ = 0 guarantees the channels are independent. At the ω-limit, B-dominant stabilization maps to the e₊-lobe of 𝕃, C-dominant stabilization maps to the e₋-lobe, and the crossing point (B ≈ C) maps to the node.

## What this chapter contributes

- **Definition *II.D08* — Interior bipolar decomposition:** each τ-admissible point (D, A, B, C) ∈ τ³ receives a canonical pair (s₊, s₋) with s₊ = e₊ · Ψ(B, A, D) and s₋ = e₋ · Ψ(C, A, D), reassembling as Ψ_int = s₊ + s₋ ∈ H_τ. The decomposition is canonical: idempotent orthogonality ensures independence, and completeness (e₊ + e₋ = 1) ensures no information is lost.
- **Two independent information channels:** the B-channel (e₊) carries γ-orbit data — how the prime A appears as a base in the tower structure; the C-channel (e₋) carries η-orbit data — how deeply exponentiation is iterated. Functions of B alone and C alone combine without interference, giving the canonical form f = e₊ · f₊(B) + e₋ · f₋(C) for bipolar-decomposed interior functions. This is the interior manifestation of the wave-equation sector decomposition from Chapter 2.
- **Proposition *II.P02* — Sector inheritance:** (1) the sector assignment at each finite stage is determined by the fiber coordinates via *II.D08*; (2) it is compatible with the idempotent decomposition of H_τ (e₊ · Ψ_int = s₊, e₋ · Ψ_int = s₋); and (3) at the ω-limit it recovers the polarity character χ̃ : ℙ_τ → {e₊, e₋} of the Prime Polarity Theorem (*I.T05*).
- **Boundary recovery:** the interior decomposition is a strict extension of the boundary structure — it does not redefine 𝕃 but shows that 𝕃's bipolar algebra is the ω-limit of the interior bipolar decomposition.

## Lean coverage

No Lean module is currently claimed. The idempotent arithmetic (properties of e± in H_τ) is in `TauLib.BookI`. The interior bipolar decomposition and *II.P02* are planned in `TauLib.BookII.Interior.BipolarDecomposition`.

## Where this leads

Chapter 8 (ABCD Structure Replaces Quaternions) closes Part I by explaining why a naive four-dimensional interior might suggest quaternionic algebra — and showing why that suggestion fails on three independent grounds, with the ABCD fibration and bipolar decomposition together providing the correct replacement.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part01/ch07-bipolar-interior.tex -->
