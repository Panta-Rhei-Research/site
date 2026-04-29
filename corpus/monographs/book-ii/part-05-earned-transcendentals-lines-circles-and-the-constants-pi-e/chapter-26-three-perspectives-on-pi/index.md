---
layout: "corpus-monograph-chapter"
title: "Chapter 26: Three Perspectives on π"
permalink: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-26-three-perspectives-on-pi/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e"
chapter_number: 26
chapter_slug: "chapter-26-three-perspectives-on-pi"
page_in_book: 123
prev_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-25-circles-from-solenoidal-structure/"
prev_chapter_title: "Chapter 25: Circles from Solenoidal Structure"
next_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-27-e-earned-the-self-reproducing-growth-base/"
next_chapter_title: "Chapter 27: e Earned — The Self-Reproducing Growth Base"
summary_short: "Three independent τ-internal constructions — topological (lemniscate half-period), geometric (primorial Archimedes polygon sequence), and spectral (B-channel phase accumulation) — all converge to π = 3.14159…, proved equal by theorem rather than assumed."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
canonical_part_title: "Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-26-three-perspectives-on-pi/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part V: Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
      url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part V"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 24
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapters 24 and 25 earned lines and circles from the primorial tower — ℝ as the Archimedean shadow of the radial α-ray (II.T20) and S¹ as the Archimedean shadow of the solenoidal circle (II.T21). Both objects are now available within Category τ as limit objects, not imported continua. This chapter earns the first transcendental constant π = 3.14159… from three independent τ-internal routes, and proves their numerical agreement as a theorem rather than a definition. The **topological** route takes π_top to be the half-period of the lemniscate ℒ = S¹ ∨ S¹ (I.T05, Book I): traversing both lobes of the figure-eight path sweeps total angle 2π, so the half-period is π, calibrated against the angular denotation map. The **geometric** route defines the *Archimedes polygon sequence* (*II.D29*): at stage k the level circle Λ_k^X is a regular Q_k^X-gon, and the inscribed and circumscribed perimeters P_k^in, P_k^out squeeze toward 2π from below and above. The squeeze gap is O(1/(Q_k^X)²), shrinking super-exponentially because Q_k^X grows as the product of angular-direction primes — so four primorial stages already surpass Archimedes' 96-gon bound. *Geometric π* (*II.D28*) is the common limit π_geo = lim P_k^in/2. The **spectral** route reads off the normalized phase accumulation of B-channel characters on the boundary ring (I.D19, Book I), yielding π_spec via equidistribution of multiplicative character values on the unit circle. *II.T22* (*Three Perspectives on π*) proves π_top = π_geo = π_spec = 3.14159…: the agreement is structural, not circular — the Archimedes perimeters are computed from CRT coordinates via the denotation map, with π as output, not input. The chapter also notes the inverted dependency chain: primorial tower → solenoidal circle → π, rather than ℝ → circle → π. This sets up e (Chapter 27) and the master constant ι_τ = 2/(π + e) (Chapter 29).

## What this chapter contributes

**Definitions / Axioms**
- *II.D28* — Geometric π: the circumference-to-diameter ratio of the earned S¹, computed as the common limit of the Archimedes polygon sequence
- *II.D29* — Archimedes Polygon Sequence: inscribed and circumscribed regular Q_k^X-gons built from solenoidal level circles, converging super-exponentially to 2π

**Key results**
- *II.T22* — *Three Perspectives on π*: π_top (lemniscate half-period) = π_geo (circumference/diameter) = π_spec (B-channel phase accumulation) = 3.14159265…; proved from τ-internal data without circular import

**Notation**
- π_top, π_geo, π_spec for the three independent constructions; Q_k^X = ∏ p_{j(m)} for cumulative angular-direction prime product; P_k^in, P_k^out for inscribed/circumscribed polygon perimeters

**Dependencies**
- *I.T04*, *I.T05* (Prime Polarity / lemniscate), *I.T18*, *I.T35*, *I.D19* (boundary ring), *II.D13*, *II.D14*, *II.D15*, *II.T11*, *II.D26* (solenoidal circle), *II.T21* (S¹ as profinite limit), *II.T20*

## Lean coverage

`BookII.Transcendentals.Pi` (planned). No Lean proofs present at this writing.

## Where this leads

With π earned, Chapter 27 earns e from the ν-iterator in the generator ladder. Together they produce the master constant ι_τ = 2/(π + e) confirmed in Chapter 29, which is the coupling ratio between the angular calibration (π) and the growth calibration (e) and mediates the Archimedean-Non-Archimedean bridge throughout Parts VI–IX.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part05/ch25-pi-earned.tex -->
