---
layout: "corpus-monograph-chapter"
title: "Chapter 27: The Weinberg Angle and CF Encodings"
permalink: "/corpus/monographs/book-iv/part-03-the-electroweak-arc/chapter-27-the-weinberg-angle-and-cf-encodings/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 3
part_display: "Part III"
part_slug: "part-03-the-electroweak-arc"
chapter_number: 27
chapter_slug: "chapter-27-the-weinberg-angle-and-cf-encodings"
page_in_book: 141
prev_chapter_url: "/corpus/monographs/book-iv/part-03-the-electroweak-arc/chapter-26-the-tau-higgs-mechanism/"
prev_chapter_title: "Chapter 26: The τ-Higgs Mechanism"
next_chapter_url: "/corpus/monographs/book-iv/part-03-the-electroweak-arc/chapter-28-electroweak-synthesis/"
next_chapter_title: "Chapter 28: Electroweak Synthesis"
summary_short: "CF[ι_τ] = [0; 2, 1, 13, 3, 1, 1, 1, 42, …] with hub a₃ = 13 encodes six electroweak NLO observables — Weinberg angle, V_ud, g_A, Δ_r, M_W, α_s."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-03-the-electroweak-arc/"
canonical_part_title: "The Electroweak Arc"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-03-the-electroweak-arc/chapter-27-the-weinberg-angle-and-cf-encodings/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part III: The Electroweak Arc"
      url: "/corpus/monographs/book-iv/part-03-the-electroweak-arc/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part III"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 45
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Chapter 25 derived sin²θ_W = ι_τ(1 − ι_τ) ≈ 0.2249. This chapter develops the arithmetic structure of that number through the continued-fraction expansions of sin²θ_W, cosθ_W, and the master constant ι_τ = 2/(π + e). The key structural feature is the large partial quotient a₃ = 13 in CF[ι_τ] = [0; 2, 1, 13, 3, 1, 1, 1, 42, …], signaling that 1/3 is an unusually good rational approximation; this hub appears in five of six NLO encodings. Window sums W₃(3) = 17, W₃(4) = 5, W₄(3) = 18 provide NLO correction coefficients for sin²θ_W (−0.7 ppm), M_W (−0.4 ppm), and α_s (+43 ppm): a Window Universality theorem. Six observables (Weinberg angle, |V_{ud}|, g_A, δ_A, Δ_r, M_W/m_n) collectively encode the CF[ι_τ] information at ~7.1 bits each, substantially below the Gauss–Kuzmin entropy of six independent draws — compressing one constant into six physics predictions with zero free parameters.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D75 — Weinberg Coupling Value* (τ-effective). sin²θ_W = ι_τ(1 − ι_τ) ≈ 0.22482 as tree-level κ(A,D). *IV.D76 — CF of the Weinberg Value* (τ-effective). sin²θ_W = [0; 4, 2, 4, 3, 6, 21, 1, 1, …]; best low-denominator convergent 9/40 = 0.2250. *IV.D77 — CF of the W/Z Mass Ratio* (τ-effective). cosθ_W = [0; 1, 7, 2, 1, 2, 1, 10, …]; second convergent 7/8 recovers the well-known M_W/M_Z ≈ 7/8 approximation. *IV.D78 — CF of the Master Constant* (τ-effective). ι_τ = [0; 2, 1, 13, 3, 1, 1, 1, 42, …]. *IV.D79 — CKM Element V_{ud}* (τ-effective). |V_{ud}| = 1 − ι_τ/a₃ = 1 − ι_τ/13 ≈ 0.97374 at 16 ppm from PDG. *IV.D80 — Axial Coupling g_A* (τ-effective). g_A = [(1 − ι_τ)²/ι_τ]·(1 + (8/17)α) ≈ 1.27561 at 621 ppm from PDG. *IV.D81 — Inner Radiative Correction δ_A* (τ-effective). δ_A = (8/677)ι_τ² ≈ 0.001376 at 3.6 ppm from Marciano–Sirlin. *IV.D82 — NLO Radiative Correction Δ_r* (τ-effective). Δ_r = (8/9)ι_τ³·(1 + ι_τ⁴/3) ≈ 0.03550 at 4,537 ppm from SM.
- **Key results:** *IV.T140 — NLO Weinberg Angle* (τ-effective): sin²θ_W^{NLO} = ι_τ(1−ι_τ)·(1 + (5/7)ι_τ³) ≈ 0.23120 at 86 ppm from MS-bar; coefficient 5/7 from CF window algebra. *IV.T140b — Window Universality W₃(4) = 5* (τ-effective): NLO corrections to sin²θ_W, M_W, and α_s all share the modulus W₃(4) = 5 = a₄ + a₅ + a₆; NNLO for sin²θ_W uses W₄(3) = 18. *IV.P01c — W Boson Mass Ratio* (τ-effective): M_W/m_n = (17/5)ι_τ⁻³ at 367 ppm from tree-level formula. *IV.T140c — CF Compression* (τ-effective): the first 13 CF partial quotients carry ~42.8 bits of information; six physics encodings account for ~7.1 bits each, well below the Gauss–Kuzmin entropy bound. Tree-level deviation 2.8% from MS-bar is consistent with one-loop EW radiative corrections; NLO one-loop calculation remains an open problem.
- **Notation introduced:** W_k(i) = a_i + ⋯ + a_{i+k−1} (sliding CF window sum); a₃ = 13 (CF hub of ι_τ); 9/40, 7/8 (CF convergent approximations); Gauss–Kuzmin distribution (CF entropy reference).
- **Dependencies:** Weinberg angle derivation from Chapter 25; window algebra applied in W mass formula (Chapter 25, IV.T177); CF structure of ι_τ.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 28 assembles the complete electroweak synthesis: all coupling constants derived from τ³ geometry in a five-tier cascade, with zero free parameters, and closes the arc with an ontological reclassification of particles as modes and forces as holonomies.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part03/ch27-weinberg-cf-encodings.tex -->
