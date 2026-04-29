---
layout: "corpus-monograph-chapter"
title: "Chapter 30: Split-Complex Codomain with Calibration"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-30-split-complex-codomain-with-calibration/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-local-hartogs-and-the-holomorphic-interior"
chapter_number: 30
chapter_slug: "chapter-30-split-complex-codomain-with-calibration"
page_in_book: 147
prev_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-29-iota-tau-confirmed-the-archimedean-non-archimedean-bridge/"
prev_chapter_title: "Chapter 29: ι<sub>τ</sub> Confirmed — The Archimedean-Non-Archimedean Bridge"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-31-the-bndlift/"
next_chapter_title: "Chapter 31: The BndLift"
summary_short: "Part V earned π, e, j, and ι_τ. This chapter installs all four constants into the split-complex codomain H_τ, producing H_τ^cal — the calibrated foundation for Part VI."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-30-split-complex-codomain-with-calibration/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VI: Local Hartogs and the Holomorphic Interior"
      url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 25
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Parts I–V constructed the primorial tower, earned the transcendental constants, and proved the bipolar split-complex structure — all without making the codomain H_τ numerically operative. The bipolar scalars (*I.D20*, Book I) were algebraic idempotents, e_± = (1 ± j)/2, correct in shape but empty of scale. The ring ℝ[j] with j² = +1 had the right algebraic skeleton — two complementary idempotents, a sector decomposition, multiplicative independence between B and C — but no numerical calibration. The ω-germ transformers were tower-coherent and formally holomorphic, yet their codomain values carried no concrete geometric meaning. Part V closed the gap: π calibrates angular periods (*II.T22*), e calibrates radial growth (*II.T23*), j is confirmed as the bipolar unit replacing i (*II.T24*), and ι_τ = 2/(π + e) couples the two measurement systems (*II.T25*). This chapter installs all four constants into H_τ at once, producing the calibrated split-complex codomain *H_τ^cal*.

## What this chapter contributes

- **Definitions:** *II.D35 — Calibrated H_τ*: the ring ℝ[j] equipped with the weighted geometric norm ‖z‖_τ = |z_+|^(π/(π+e)) · |z_-|^(e/(π+e)) and the calibration triple (π, e, ι_τ). The exponents are the angular weight and the growth weight; they sum to 1, making the norm multiplicative.
- **Key results:** *II.R10 — Geometric Meaning of e_±*: the idempotents acquire three-level meaning — algebraic (Book I), spectral (Part V), and geometric-analytic (this chapter). At the geometric-analytic level e_+ projects onto the angular sector calibrated by π, and e_- projects onto the growth sector calibrated by e; coupling is governed by ι_τ.
- **Structural results:** sector independence (B-channel and C-channel are algebraically decoupled under multiplication), tower coherence of calibrated ω-germ values (the calibrated stage values form Cauchy sequences converging in H_τ^cal), and the observation that zero divisors e_+ · e_- = 0 are a structural feature enabling sector projection, not a pathology.
- **Dependencies:** *I.D19*, *I.D20*, *I.D21*, *I.D24*, *I.T10*, *I.T18*, *II.D01*, *II.D08*, *II.D32*, *II.D33*, *II.D34*, *II.T22*, *II.T23*, *II.T24*, *II.T25*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Hartogs.CalibratedSplitComplex` is planned.

## Where this leads

Every subsequent construction in Part VI — *II.D36* (BndLift), *II.T27* (Mutual Determination), and the category *II.D41* (HolEnd_τ) — takes H_τ^cal as its codomain. Without calibration the constructions are formally valid but numerically empty; with it they produce concrete functions computable to arbitrary precision. Chapter 31 opens that program immediately by defining the boundary lift operator whose sector decomposition runs entirely through e_± in H_τ^cal.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch29-split-complex-calibrated.tex -->
