---
layout: "corpus-monograph-chapter"
title: "Chapter 5: The Omega Readout and the Lemniscate"
permalink: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-05-the-omega-readout-and-the-lemniscate/"
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
chapter_number: 5
chapter_slug: "chapter-05-the-omega-readout-and-the-lemniscate"
page_in_book: 21
prev_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-04-tau/"
prev_chapter_title: "Chapter 4: τ"
next_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-06-the-tau-fibration-emerges/"
next_chapter_title: "Chapter 6: The τ³ Fibration Emerges"
summary_short: "Computing the limit of ABCD readouts along paths to ω reveals a sharp dichotomy: base coordinates collapse universally to a single point (Ω, Ω), while fiber coordinates trace the algebraic lemniscate 𝕃 = S¹ ∨ S¹ — the boundary is not imported but is the fiber readout of the point at infinity."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
canonical_part_title: "Interior Points and the τ³"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-01-interior-points-and-the-tau/chapter-05-the-omega-readout-and-the-lemniscate/"
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

Book I's ABCD chart handles ω as a degenerate case: the point at infinity has coordinates that diverge, so no finite four-tuple captures it. This chapter resolves that gap by computing the limit of ABCD readouts along paths in τ³ whose primorial depth grows without bound. The primorial tower Φ(P_n) = (p_n, 1, 1, P_{n-1}) is the canonical probe: it approaches ω with uniformly trivial fiber coordinates B_n = C_n = 1, the "flattest" possible path. Other paths — tower paths (X_n = p_n^{p_n}), exponential paths (X_n = 2^n), tetration paths (X_n = ⁿ2) — explore the full B/C space in the fiber. The resulting structure is a sharp dichotomy: the base coordinates (D, A) collapse universally to a single point (Ω, Ω) regardless of path, while the fiber coordinates (B, C) retain one-dimensional structure whose totality is exactly the algebraic lemniscate 𝕃 = S¹ ∨ S¹, recovered here as a coordinate limit rather than imported.

## What this chapter contributes

- **Definition *II.D04* — Omega readout Φ_ω:** the map from paths to ω to the product {(Ω, Ω)} × 𝕃. For every path, the base component is the universal collapse (Ω, Ω); the fiber component is determined by the asymptotic B/C dominance: B_m/C_m → ∞ gives the e₊-lobe, C_m/B_m → ∞ gives the e₋-lobe, and B_m/C_m → 1 (balanced) gives the crossing-point node ω_𝕃 of *I.D18*.
- **Theorem *II.T02* — Fiber Degeneration at Omega:** at the ω-limit, (1) the base readout collapses (2D → 0D), (2) the fiber readout degenerates to a 1D locus — 𝕃 — via the B/C competition locked by the primorial CRT structure (*I.T18*), and (3) the degeneration is forced: the two-dimensional fiber loses one degree of freedom because the polarity character χ̃ couples B and C along each path.
- **Proposition *II.P01* — Lemniscate as Coordinate Limit:** 𝕃 ≅ pr_fiber(Φ_ω) as algebras with involution. The bipolar sectors e₊H_τ / e₋H_τ of *I.D27* correspond to B-dominated / C-dominated fiber limits; the crossing point corresponds to balanced paths; the polarity involution σ : j ↦ −j corresponds to the B/C swap. Book I's algebraic construction (*I.D18*) and this chapter's coordinate construction are independent and yield the same object.
- **Three views of 𝕃:** (1) algebraic (bipolar spectral algebra, Book I Part VII), (2) coordinate (fiber readout at ω, this chapter — now proven equivalent to view 1), (3) topological (torus degeneration T² → S¹ ∨ S¹, deferred to Part III Chapter 17).

## Lean coverage

No Lean module is claimed for this chapter. The primorial CRT computations underlying the fiber degeneration trace back to *I.T18*, verified in `TauLib.BookI`. The omega readout construction and *II.T02* are planned in `TauLib.BookII.Interior.OmegaReadout`.

## Where this leads

Chapter 6 (The τ³ Fibration Emerges) assembles the base τ¹ = (D, A) and fiber T² = (B, C) into the formal fibered product τ³ = τ¹ ×_f T², explaining why the coupling is a genuine fibration (not a Cartesian product) and why neither τ¹ nor T² exists as an independent category.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part01/ch05-omega-readout-lemniscate.tex -->
