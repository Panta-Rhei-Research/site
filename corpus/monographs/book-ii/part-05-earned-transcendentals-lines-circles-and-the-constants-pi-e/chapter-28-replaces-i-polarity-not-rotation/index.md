---
layout: "corpus-monograph-chapter"
title: "Chapter 28: Replaces i — Polarity, Not Rotation"
permalink: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-28-replaces-i-polarity-not-rotation/"
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
chapter_number: 28
chapter_slug: "chapter-28-replaces-i-polarity-not-rotation"
page_in_book: 135
prev_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-27-e-earned-the-self-reproducing-growth-base/"
prev_chapter_title: "Chapter 27: e Earned — The Self-Reproducing Growth Base"
next_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-29-iota-tau-confirmed-the-archimedean-non-archimedean-bridge/"
next_chapter_title: "Chapter 29: ι<sub>τ</sub> Confirmed — The Archimedean-Non-Archimedean Bridge"
summary_short: "The split-complex unit j (j² = +1, j ≠ ±1) is earned as the B/C fiber-swap operator forced by the discrete ℤ/2 symmetry of τ³; no continuous SO(2) action exists, so the classical imaginary unit i has no τ-internal avatar."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
canonical_part_title: "Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-28-replaces-i-polarity-not-rotation/"
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

Chapters 26 and 27 earned the transcendental constants π and e. This chapter earns the **algebraic** constant j — the split-complex unit satisfying j² = +1, j ≠ ±1. The classical imaginary unit i (i² = −1) never arises in Category τ, and the reason is structural rather than a choice. The fiber T² of the fibered product τ³ = τ¹ ×_f T² carries two coordinates B and C. These are profinite discrete sequences: there is no smooth path from the B-axis to the C-axis, only a discrete **swap** σ : (B,C) ↦ (C,B) generating a ℤ/2 involution. Polarity — exchanging two sectors — gives j² = +1. Rotation — smoothly cycling a single circle — would require a connected group SO(2) acting on the fiber, but any continuous homomorphism from a connected group to the discrete group ℤ/2 = Aut_ABCD(T²) must be trivial. This is the content of *II.R08* (*Polarity vs. Rotation*): τ has polarity, not rotation. *II.D32* (*j unit*) defines j as the coordinate-swap automorphism (D,A,B,C) ↦ (D,A,C,B), well-defined at every finite stage and trivially extending to the profinite limit. Unlike π and e, j is algebraic — a root of x² − 1 — and requires no approximation sequence. From j one constructs the *bipolar idempotents* (*II.D33*): e_± = (1 ± j)/2. These are idempotent (e_±² = e_±), orthogonal (e_+ · e_− = 0), and complete (e_+ + e_− = 1); e_+ projects onto the B-channel, e_− onto the C-channel. The sector decomposition z = z_+ e_+ + z_− e_− reproduces the spectral decomposition of the boundary ring (I.D19, I.D21, Book I). *II.T24* (*j Replaces i*) formalizes the replacement: (i) σ is the unique non-trivial ABCD-preserving fiber automorphism; (ii) every ℤ/2-equivariant algebra on the fiber is isomorphic to ℝ[j]; (iii) no SO(2) action is compatible with the ABCD structure; (iv) e_± recover the spectral boundary decomposition. The ring isomorphism ℝ[j] ≅ ℝ × ℝ via a + bj ↦ (a+b, a−b) makes the zero-divisor structure explicit: (1+j)(1−j) = 0. The imaginary unit i appears in Book II only as a notational device in the orthodox bridge target language, not as a τ-internal element.

## What this chapter contributes

**Definitions / Axioms**
- *II.D32* — j unit: the B/C fiber-swap automorphism of τ³, satisfying j² = +1, j ≠ ±1; generates the ℤ/2 involution of T²
- *II.D33* — Bipolar idempotents e_± = (1 ± j)/2: idempotent, orthogonal, complete sector projections onto B-channel (e_+) and C-channel (e_−)

**Key results**
- *II.T24* — *j Replaces i*: σ is the unique fiber automorphism preserving ABCD; the equivariant algebra is ℝ[j]; no SO(2) action exists; e_± recover the spectral decomposition
- *II.R08* — *Polarity vs. Rotation*: structural dichotomy between the discrete ℤ/2 polarity of τ (j² = +1) and the continuous SO(2) rotation that would produce i² = −1

**Notation**
- j for the split-complex unit; e_± for bipolar idempotents; z_± = a ± b for sector components of z = a + bj; ℝ[j] = ℝ[x]/(x² − 1) for the split-complex ring

**Dependencies**
- *I.D20*, *I.D21* (bipolar idempotents Book I), *I.T05* (Prime Polarity), *I.T10* (split-complex forcing), *I.D19* (boundary ring), *II.D14*, *II.D15*, *II.T20*, *II.T21*, *II.T22* (π), *II.T23* (e)

## Lean coverage

`BookII.Transcendentals.JReplacesI` (planned). No Lean proofs present at this writing.

## Where this leads

With j and the idempotents e_± established, Chapter 29 can confirm ι_τ = 2/(π + e) as the coupling between angular and radial calibrations. The idempotents e_± are the load-bearing structural elements of Parts VI–VII, where the Idempotent Decomposition Lemma (II.L07) lifts them from scalars to holomorphic function spaces.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part05/ch27-j-replaces-i.tex -->
