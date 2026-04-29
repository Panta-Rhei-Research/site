---
layout: "corpus-monograph-chapter"
title: "Chapter 35: The Strong Sector and NF Discreteness"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-35-the-strong-sector-and-nf-discreteness/"
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
chapter_number: 35
chapter_slug: "chapter-35-the-strong-sector-and-nf-discreteness"
page_in_book: 179
prev_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-34-positive-regularity/"
prev_chapter_title: "Chapter 34: Positive Regularity"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-36-the-tau/"
next_chapter_title: "Chapter 36: The τ"
summary_short: "The C-sector is isolated as the strong sector *III.D43* at enrichment level E₁, and the NF Discreteness Lemma *III.P16* proves that at most Prim(k) distinct gauge configurations exist at each primorial depth — the granularity that will prevent the mass gap from closing."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-35-the-strong-sector-and-nf-discreteness/"
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

This chapter opens the Yang–Mills block (Chapters 35–37) by isolating the strong sector — the C-sector from the 4+1 decomposition, instantiated at enrichment level E₁. The Yang–Mills problem is structurally different from Navier–Stokes: it lives in a single sector rather than across all five. The C-sector is governed by generator η and carries χ₋-dominant spectral content; its isolation from the B-sector is guaranteed by the B/C non-collapse theorem from Chapter 19. The chapter then proves the NF Discreteness Lemma (*III.P16*) — the granularity result that is the structural prerequisite for the mass gap — and defines τ-admissible gauge data (*III.D44*) as the Yang–Mills analogue of τ-admissible fluid data.

## What this chapter contributes

The strong sector at E₁ (*III.D43*) is the full subcategory of objects whose spectral support lies entirely in Sector(C), with χ₋-dominant content (the C₋ component dominates C₊). The B/C non-collapse theorem (*III.T*) from Part IV guarantees that the strong sector is genuinely distinct from the EM sector at all enrichment levels — there is no limiting process that could merge C into B. This isolation is what makes a sector-specific mass gap meaningful: a gap in a sector that could be continuously deformed into another sector would not survive the deformation.

The NF Discreteness Lemma (*III.P16*) establishes that at primorial depth k the number of distinct NF configurations in the strong sector is at most Prim(k) — and that this bound is sharp, achieved by the primorial orbit of the generator η. The result is earned from K3 divisibility, not imposed externally: the generator η acts by divisibility relations on the primorial tower, which are intrinsically discrete. A continuum limit is structurally unavailable within the C-sector of Category τ, because any two distinct configurations differ by at least one divisibility class at some prime in the tower. Discreteness at each finite depth implies discreteness in the profinite limit by compactness.

τ-Admissible gauge data (*III.D44*) is a triple (clopen cylinder domain, C-sector ω-germ assignment, bounded C-extraction) parallel to the NS admissibility definition (*III.D36*), with the key difference that the A, B, D, and ω components are identically zero. This simplification is structural, not a restriction: genuine Yang–Mills gauge data has no fluid-sector content. The finite spectrum of the C-sector Hamiltonian at each primorial depth is verified, with the gap lower bound δ_k ≥ c/Prim(k) stated; the profinite limit argument that converts this into the global gap constant Γ*_s > 0 is deferred to Chapter 36.

## Lean coverage

- *III.D43* — Strong Sector at E₁ (τ-effective)
- *III.D44* — τ-Admissible Gauge Data (τ-effective)
- *III.P16* — NF Discreteness Lemma (τ-effective)

## Where this leads

NF discreteness hypothesis (H1) and τ-admissible gauge data are the two inputs to the τ-Gap Meta-Theorem in Chapter 36. The strong sector structure is exported to Part VI, where the C-sector becomes one vertex of the enriched bi-square. τ-Admissible gauge data propagates to Parts VI, IX, and X as the input class for all strong-sector arguments.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch38-the-strong-sector-and-nf-discreteness.tex -->
