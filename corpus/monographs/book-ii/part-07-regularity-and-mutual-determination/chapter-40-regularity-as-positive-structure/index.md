---
layout: "corpus-monograph-chapter"
title: "Chapter 40: Regularity as Positive Structure"
permalink: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-40-regularity-as-positive-structure/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-regularity-and-mutual-determination"
chapter_number: 40
chapter_slug: "chapter-40-regularity-as-positive-structure"
page_in_book: 211
prev_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-39-the-3-lemma-chain/"
prev_chapter_title: "Chapter 39: The 3-Lemma Chain"
next_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-41-pre-yoneda-embedding/"
next_chapter_title: "Chapter 41: Pre-Yoneda Embedding"
summary_short: "τ-regularity is redefined as a positive existence condition — stabilization of the ω-germ sequence at a finite primorial stage — replacing the classical negative definition by complement of singular set; the clopen ultrametric topology makes removable singularities structurally impossible."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
canonical_part_title: "Regularity and Mutual Determination"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-40-regularity-as-positive-structure/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VII: Regularity and Mutual Determination"
      url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 26
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

In classical complex analysis, regularity is a negative condition: a function is regular at a point if no singularity occurs there — if the point is not a pole, not a branch point, not an essential singularity. One first catalogs what can go wrong, then declares the complement to be regular. Classical theory also admits removable singularities, where the singularity is an artifact of presentation, not function — Riemann's theorem says boundedness near the suspect point suffices to fill it in. This negative-and-patchable picture depends on the epsilon-delta structure of ℂ: singularities can be "approached" from infinitely many directions because the continuum is dense. Category τ has no such structure. Cylinders in the ultrametric topology are **clopen** — simultaneously open and closed — so there is no notion of "approaching" a singularity from within a cylinder without already being at a given stage. Either the ω-germ stabilizes at a finite stage, or it never stabilizes. There is no epsilon-delta wiggle room, and no Riemann-style patching. This forces a fundamentally different definition. *II.D49* (*τ-Regularity*) defines a point p ∈ τ³ to be **τ-regular** for a function f if the sequence of ω-germ restrictions to cylinders C_N(p) stabilizes at some finite N — if the germ transformer "settles" on a value using only finitely much boundary data. This is a positive existence condition: there must exist a stabilizing stage, not merely an absence of pathology. *II.T34* (*Regularity Criterion*) establishes a **sharp dichotomy**: every point p is either τ-regular (stabilization at finite stage) or genuinely singular (the germ sequence diverges and no finite stage suffices). The dichotomy is provably exhaustive and mutually exclusive — no removable-singularity middle ground exists. *II.R11* (*Positive vs. Negative Regularity*) articulates the structural reason: classical removable singularities exist because the continuum supports limit-and-patch; τ's clopen cylinders cannot support such patching. The key dependencies feeding into II.T34 are the Global Hartogs Theorem (I.T31), which guarantees that boundary data determines interior data; the Idempotent Decomposition Lemma (II.L07); the holomorphic ↔ idempotent-supported equivalence (II.T33); and the evolution operator (II.D37), which propagates ω-germ data through the staging tower.

## What this chapter contributes

**Definitions / Axioms**
- *II.D49* — τ-Regularity: p ∈ τ³ is τ-regular for f if the ω-germ restriction sequence to cylinders C_N(p) stabilizes at a finite primorial stage N; a positive existence condition, not the complement of a singular set

**Key results**
- *II.T34* — *Regularity Criterion*: sharp dichotomy — every point is either τ-regular (stabilization at finite N) or genuinely singular (germ diverges); the two cases are exhaustive and mutually exclusive; no removable-singularity intermediate
- *II.R11* — *Positive vs. Negative Regularity*: structural explanation for why removable singularities have no τ-analogue — clopen cylinder topology admits no epsilon-delta approach, so singularities cannot be "filled in"

**Notation**
- C_N(p) for the stage-N cylinder centered at p; τ-Reg(f) for the set of τ-regular points of f; the stabilization stage N(p, f) for the first stage at which the germ settles

**Dependencies**
- *I.T31* (Global Hartogs Extension), *II.L07* (Idempotent Decomposition), *II.T33* (Holomorphic ↔ Idempotent-Supported), *II.T27* (Mutual Determination), *II.D37* (evolution operator), *II.T28*, *II.D10* (cylinder structure)

## Lean coverage

`BookII.Regularity.PositiveRegularity` (planned). No Lean proofs present at this writing.

## Where this leads

The positive regularity criterion (II.T34) is an essential input for the Pre-Yoneda embedding (Chapter 41): in order to show that holomorphic functions are themselves objects of τ³, one must know exactly which functions are regular in the τ sense. The dichotomy also shapes the Code/Decode framework (Chapter 42), where the stabilization condition directly corresponds to having a well-defined bipolar boundary coefficient stream.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part07/ch39-regularity-positive.tex -->
