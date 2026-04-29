---
layout: "corpus-monograph-chapter"
title: "Chapter 23: The Source Sector: Structure Generation"
permalink: "/corpus/monographs/book-vi/part-04-source-plants-and-the-production-fiber/chapter-23-the-source-sector-structure-generation/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-source-plants-and-the-production-fiber"
chapter_number: 23
chapter_slug: "chapter-23-the-source-sector-structure-generation"
page_in_book: 131
prev_chapter_url: "/corpus/monographs/book-vi/part-03-agency-bacteria-and-the-spatial-axis/chapter-22-the-three-domains-sector-taxonomy-of-life/"
prev_chapter_title: "Chapter 22: The Three Domains: Sector Taxonomy of Life"
next_chapter_url: "/corpus/monographs/book-vi/part-04-source-plants-and-the-production-fiber/chapter-24-photosynthesis-quantum-coherence-and-carbon-fixation/"
next_chapter_title: "Chapter 24: Photosynthesis: Quantum Coherence and Carbon Fixation"
summary_short: "The source sector is defined as the γ-fiber subcategory of Loop_L, with the structure generation predicate requiring production, complexity increase, and autotrophy. Plants are the biological archetype."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-04-source-plants-and-the-production-fiber/"
canonical_part_title: "Source — Plants and the Production Fiber"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-04-source-plants-and-the-production-fiber/chapter-23-the-source-sector-structure-generation/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part IV: Source — Plants and the Production Fiber"
      url: "/corpus/monographs/book-vi/part-04-source-plants-and-the-production-fiber/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part IV"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 63
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

Parts II and III established the two base sectors — persistence (α) and agency (π) — acting on the base circle τ¹. Part IV moves to the fiber. The fibered product τ³ = τ¹ ×_f T² carries two fiber generators, γ and η, acting on the two circles of the fiber torus T² = S¹ × S¹. Where the base generators govern when and where a carrier exists, the fiber generators govern what it produces and what it recycles. The source sector, governed by γ, is the sector of production: its Life loop winds primarily along the γ-fiber, converting inorganic inputs into organic structural complexity. This chapter provides the formal definition of that sector, identifies the structure generation predicate that characterizes it, proves the equivalence theorem connecting γ-dominance to the predicate, and identifies plants as the biological archetype — the organisms that instantiate production in its most concentrated form.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D36 — Source Sector* (τ-effective): the full subcategory Src_γ of Loop_L consisting of Life loops whose winding number factorization satisfies w_γ(γ) > 0 and w_γ(γ) ≥ w_g(γ) for all generators g. *VI.D37 — Structure Generation Predicate* (τ-effective): three conditions on a carrier (X, D) — production (Life loop factors through Loop_src with w_γ > 0), complexity increase (Hodge capacity of output exceeds that of input, C(γ_src(1)) > C(γ_src(0))), and autotrophy or net contribution (carrier produces from inorganic precursors or contributes net complexity to the ecosystem).
- **Key results:** *VI.T20 — Source as γ-Fiber Production* (τ-effective): a Life loop belongs to Src_γ if and only if the underlying carrier satisfies the structure generation predicate. The forward direction extracts the predicate from γ-dominance and finiteness of the defect functional Δ_Src; the reverse direction shows that the factorization condition forces w_γ > 0, that complexity increase bounds Δ_Src, and that net production ensures γ-dominance over η. The source–closure duality (Src_γ dual to Cl_η on T²) is noted as a structural consequence.
- **Notation introduced:** Src_γ (source sector subcategory); Loop_src (source sub-class of the Life Loop Class); Δ_Src (defect functional for the source sector); Hodge capacity field C on the γ-fiber.
- **Dependencies:** VI.D36 depends on the Life Loop Class (ch. 09), the Metabolic Fiber Theorem (ch. 10), and the sector template (ch. 08); builds structurally parallel to VI.D24/VI.T16 (persistence, ch. 12) and VI.D29/VI.T18 (agency, ch. 17). The force-sector matching assigns Hodge and BSD as dominant forces of the source sector; Poincaré and Navier–Stokes are reassigned to the base sectors.

## Lean coverage

`TauLib.BookVI.Life.DefectFunctionals` contains the DeltaSrc entry underlying VI.T20. The source sector definition and its structural parallel to the persistence and agency sectors are formalized in `TauLib.BookVI.Life.SectorTemplate`. VI.D37 and VI.T20 are prose-derived in the current release; full Lean formalization is in progress alongside the other primitive-sector entries.

## Where this leads

Chapter 24 instantiates the structure generation predicate at molecular scale through photosynthesis — the source sector's canonical production act — while chapters 25 through 27 fill out the biological and mathematical content of the γ-fiber: the sessile architecture of plants, morphogenesis as Hodge gradient dynamics, and the genetic code as BSD motivic structure.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part04/ch23-source-sector.tex -->
