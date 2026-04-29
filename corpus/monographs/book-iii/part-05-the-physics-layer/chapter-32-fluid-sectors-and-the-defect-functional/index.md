---
layout: "corpus-monograph-chapter"
title: "Chapter 32: Fluid Sectors and the Defect Functional"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-32-fluid-sectors-and-the-defect-functional/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-the-physics-layer"
chapter_number: 32
chapter_slug: "chapter-32-fluid-sectors-and-the-defect-functional"
page_in_book: 167
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-31-tau/"
prev_chapter_title: "Chapter 31: τ"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-33-the-hartogs-flow-operator/"
next_chapter_title: "Chapter 33: The Hartogs Flow Operator"
summary_short: "The 4+1 sector template is applied to τ-admissible fluid data, yielding the fluid sector decomposition *III.D38* and the contractive defect functional *III.D39*, whose decay drives the Positive Regularity Theorem."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-32-fluid-sectors-and-the-defect-functional/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part V: The Physics Layer"
      url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part V"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 36
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The 4+1 sector decomposition built in Chapter 10 for boundary characters on the lemniscate is here applied to τ-admissible fluid data, producing a sector-by-sector decomposition of the flow. Each of the five sectors — A, B, C, D, and the ω-coupling — inherits the split-complex structure via the idempotents e₊ and e₋, yielding ten scalar components in total. The chapter then introduces the defect functional *III.D39*, which measures at each primorial depth how far fluid data deviates from its canonical NF-stabilised form. The central result, Defect Contractivity (*III.P14*), shows that this deviation decreases by a fixed factor κ < 1 at every primorial refinement step — the key estimate that will power Chapter 34's capstone theorem.

## What this chapter contributes

The fluid sector decomposition (*III.D38*) is the unique splitting of τ-admissible fluid data into five orthogonal sector projections, obtained by restricting spectral content to the character sets of the 4+1 template. The ω-coupling sector mediates B/C energy transfer without introducing a new degree of freedom; setting it to zero decouples the two lobes entirely. The defect functional (*III.D39*) is a non-negative, computable quantity that vanishes exactly when all sector projections match their canonical forms. Its decomposition Δ = ΔA + ΔB + ΔC + ΔD + Δω is additive because the sector projections have disjoint spectral support. A decay hierarchy among per-sector defects is proved: the A-sector decays fastest (balanced polarity maximises cancellation) and the D-sector slowest (polarised spectral content). Defect contractivity (*III.P14*) is established via the CRT splitting at each primorial refinement: the new prime p_{n+1} contributes zero additional defect by NF confluence, giving contraction factor κ(k) ≤ 1 − c/p_{k+1}. The divergence of Σ 1/p then drives the telescoping product to zero. The physical interpretation is noted: the A-to-D decay ordering mirrors the hierarchy of physical coupling strengths, though that ordering is here a consequence of spectral polarity rather than coupling constants.

## Lean coverage

- *III.D38* — Fluid Sector Decomposition (τ-effective)
- *III.D39* — Defect Functional (τ-effective)
- *III.P14* — Defect Contractivity (τ-effective)

## Where this leads

Defect contractivity is condition (C3) of the 3-Condition Sufficiency proposition in Chapter 34 and the central engine behind the Positive Regularity Theorem (*III.T25*). The defect functional framework is reused in its entirety by the Yang–Mills block (Chapters 35–37) for the strong defect functional, and is exported to Parts VI and VII for BSD rank-discrepancy measurement and Langlands spectral data.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch35-fluid-sectors-and-the-defect-functional.tex -->
