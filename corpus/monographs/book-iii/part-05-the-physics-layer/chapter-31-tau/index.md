---
layout: "corpus-monograph-chapter"
title: "Chapter 31: τ"
permalink: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-31-tau/"
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
chapter_number: 31
chapter_slug: "chapter-31-tau"
page_in_book: 163
prev_chapter_url: "/corpus/monographs/book-iii/part-04-the-spectral-doors/chapter-30-the-master-schema/"
prev_chapter_title: "Chapter 30: The Master Schema"
next_chapter_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/chapter-32-fluid-sectors-and-the-defect-functional/"
next_chapter_title: "Chapter 32: Fluid Sectors and the Defect Functional"
summary_short: "τ-admissible fluid data and clopen cylinder domains open Part V's Navier–Stokes treatment: regularity means stabilised ω-germ existence, not blow-up absence, with scope boundary *III.R17* governing all subsequent chapters."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-05-the-physics-layer/"
canonical_part_title: "The Physics Layer"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-05-the-physics-layer/chapter-31-tau/"
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

We define the initial data and spatial domains for the τ-internal approach to Navier–Stokes regularity. The classical problem asks whether smooth initial data produce smooth solutions for all time; the τ-internal reformulation replaces "smooth" with "stabilised ω-germ" and replaces ℝ³ with clopen cylinders in τ³. This chapter introduces τ-admissible fluid data (*III.D36*) and clopen cylinder domains (*III.D37*), and states the NS scope boundary (*III.R17*) that governs all of Part V. Regularity is a positive predicate — the existence of a stabilised germ — not the absence of a singularity. Every admissibility check is a finite computation at a given primorial depth, and the tower coherence of admissible data is proved immediately.

## What this chapter contributes

The chapter supplies the two definitions that ground the entire NS block. τ-Admissible fluid data (*III.D36*) specifies a triple — clopen cylinder domain, ω-germ assignment, bounded ABCD extraction — satisfying explicit primorial-level norm bounds at each depth k. The norm bounds are computable: at depth k, the ABCD extraction must lie in a ball of radius r_k = c/Prim(k) in the profinite metric. The tower coherence of admissible data is proved immediately from the tower restriction maps: if a datum is admissible at depth k, its restriction to depth k−1 is admissible at depth k−1.

Clopen cylinder domains (*III.D37*) in τ³ are defined via simultaneous residue-class conditions on all primes up to a primorial cutoff: a clopen cylinder at depth k is a product of k residue classes, one per prime p_i ≤ Prim(k), in each of the three spatial dimensions. These cylinders form a Boolean algebra closed under intersection, union, and complement — the τ³ analogue of the Borel field. Boundary conditions between adjacent cylinders are recast as sheaf-gluing conditions; at lemniscate crossing points they take the form of a Kirchhoff-type conservation law that decomposes independently in the e₊ and e₋ idempotent channels, enforcing independent B-sector and C-sector flux conservation. The conservation law is the τ-internal substitute for the divergence-free condition of classical NS.

The NS scope boundary (*III.R17*) is stated with full precision: Part V proves regularity for τ-admissible data on clopen cylinder domains; the bridge to Schwartz-class data on ℝ³ is a representability question — does every Schwartz-class datum have a τ-admissible approximation tower? — that is explicitly deferred to Part X. The scope boundary is designed to be referenced in every subsequent NS-block chapter without repetition.

## Lean coverage

- *III.D36* — τ-Admissible Fluid Data (τ-effective)
- *III.D37* — Clopen Cylinder Domain (τ-effective)
- *III.R17* — NS Scope Boundary

## Where this leads

The admissibility predicate and cylinder algebra defined here are consumed immediately by Chapter 32 (fluid sector decomposition and defect functional) and Chapter 33 (Hartogs flow operator). The bounded ABCD extraction condition reappears in Chapter 34 as the mechanism that prevents germ divergence, and the Kirchhoff conservation law seeds the K5 sector-isolation argument. The scope boundary is referenced in every subsequent NS-block chapter and in Part X when the conjectural classical bridge is addressed.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part05/ch34-tau-admissible-fluid-data.tex -->
