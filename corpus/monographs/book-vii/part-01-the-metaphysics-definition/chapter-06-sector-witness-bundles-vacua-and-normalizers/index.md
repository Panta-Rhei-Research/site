---
layout: "corpus-monograph-chapter"
title: "Chapter 6: Sector Witness Bundles, Vacua, and Normalizers"
permalink: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-06-sector-witness-bundles-vacua-and-normalizers/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-metaphysics-definition"
chapter_number: 6
chapter_slug: "chapter-06-sector-witness-bundles-vacua-and-normalizers"
page_in_book: 22
prev_chapter_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-05-the-4-1-sector-decomposition-at-e/"
prev_chapter_title: "Chapter 5: The 4+1 Sector Decomposition at E₃"
next_chapter_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/chapter-07-the-canonical-ladder-theorem/"
next_chapter_title: "Chapter 7: The Canonical Ladder Theorem"
summary_short: "Each E₃ sector receives a witness bundle, a defect-minimising vacuum, and an NF-coded normaliser; Shadow Soundness and Rigidity complete the machinery."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/"
canonical_part_title: "The Metaphysics Definition"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-01-the-metaphysics-definition/chapter-06-sector-witness-bundles-vacua-and-normalizers/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part I: The Metaphysics Definition"
      url: "/corpus/monographs/book-vii/part-01-the-metaphysics-definition/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part I"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 69
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

The sector decomposition of Chapter 5 classifies E₃-admissible content but does not yet specify how membership is certified, what the ground state of each sector looks like, or how the coherence verdict is computed. This chapter supplies the three missing pieces. A witness bundle is a fibred collection of typed evidences over each sector: empirical test protocols, universalisability certificates for norms, finite proof chains for diagrammatic content, and sustained-commitment demonstrations for the commitment sector. A sector vacuum is the canonical minimiser of the sector's defect functional — the ideally coherent configuration to which the sector's dynamics tend. A normaliser is the NF-coded bounded pipeline that checks a witnessed content pair and returns an accept, reject, or undetermined verdict. Two shadow families — the VM/ZFC-PA shadow and the epistemic/pragmatic shadow — are introduced as non-prescriptive readout functors that translate τ-internal sector results into classical foundational and epistemological languages without back-propagating their assumptions into the kernel.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D12 — Sector Witness Bundle* (τ-effective): the fibred collection W_X → S_X of typed witnesses certifying sector membership; five witness types covering the four pure sectors and the Logos sector with its mutually witnessing (π, s) pairs. *VII.D13 — Sector Vacuum* (τ-effective): the defect functional Δ_X: S_X → [0, ∞) and its minimiser v_X, characterised for each of the five sectors. *VII.D14 — Sector Normaliser* (τ-effective): the NF-coded bounded pipeline N_X: W_X → {accept, reject, undetermined} satisfying boundedness (N1), soundness (N2), and determinism (N3).
- **Key results:** *VII.L02 — Shadow Soundness* (τ-effective): if N_X(c, w) = accept, then the shadow image Σ(c) is coherent within the target formalism; proved for both shadow families via structure-preservation of the shadow functors. *VII.T04 — Rigidity Corollary* (τ-effective): the vacuum satisfies N_X(v_X, w₀) = accept and Δ_X(v_X) = 0; and re-typing content from S_X to S_Y (X ≠ Y, outside S_L) either changes the coherence verdict or renders the content ill-typed.
- **Notation introduced:** W_X for witness bundles; Δ_X for defect functionals; v_X for vacua; N_X for normalisers; Σ_VM and Σ_EP for the two shadow functors.
- **Dependencies:** Sector Decomposition Theorem (Chapter 5, VII.T03); Register Independence Theorem (Chapter 3, VII.T01); abstract sector template (Book III, Part II).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The normaliser boundedness condition (N1) is structurally aligned with the NF-linearity discipline formalised in `TauLib.BookI`.

## Where this leads

The witness bundles, vacua, and normalisers constitute the operational machinery that the Canonical Ladder Theorem (Chapter 7) and the Saturation Theorem (Chapter 8) use to prove non-emptiness and strictness across enrichment levels. The shadow families reappear whenever τ-internal results are translated into set-theoretic or classical epistemological language throughout the book.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part01/ch06.tex -->
