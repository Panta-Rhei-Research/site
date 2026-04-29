---
layout: "corpus-monograph-chapter"
title: "Chapter 28: The Closure Sector: Decomposition and Nutrient Return"
permalink: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-28-the-closure-sector-decomposition-and-nutrient-return/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 5
part_display: "Part V"
part_slug: "part-05-closure-fungi-and-the-recycling-fiber"
chapter_number: 28
chapter_slug: "chapter-28-the-closure-sector-decomposition-and-nutrient-return"
page_in_book: 165
prev_chapter_url: "/corpus/monographs/book-vi/part-04-source-plants-and-the-production-fiber/chapter-27-the-genetic-code-bsd-structure-and-replication/"
prev_chapter_title: "Chapter 27: The Genetic Code: BSD Structure and Replication"
next_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-29-fungi-the-recycling-networks/"
next_chapter_title: "Chapter 29: Fungi: The Recycling Networks"
summary_short: "The closure sector is defined as the η-fiber subcategory of Loop_L, with the structure recycling predicate requiring decomposition, complexity decrease, and material return. Fungi are the biological archetype; the sector is the exact dual of the source sector."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/"
canonical_part_title: "Closure — Fungi and the Recycling Fiber"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-28-the-closure-sector-decomposition-and-nutrient-return/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part V: Closure — Fungi and the Recycling Fiber"
      url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part V"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 64
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

Parts II through IV defined the persistence sector (α-base), agency sector (π-base), and source sector (γ-fiber). Part V completes the fiber torus T² = S¹ × S¹ by turning to its second generator. Where the source sector winds primarily along γ and builds structural complexity from simpler inputs, the closure sector winds primarily along η and dismantles existing complexity back into simpler reusable forms. The two fiber sectors are exact duals in every formal respect: the source sector produces (Hodge capacity increases), the closure sector returns (Hodge capacity decreases); autotrophy in the source sector has saprotrophy as its closure counterpart; plants and fungi are the respective biological archetypes. This chapter follows the logical template of chapters 12, 17, and 23 — formal definition, characteristic predicate, equivalence theorem, biological archetype — closing the four-sector primitive framework before the consumer sector (chapter 33) introduces mixed-winding coupling.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D41 — Closure Sector* (τ-effective): the full subcategory Cl_η of Loop_L consisting of Life loops with w_η(γ) > 0 and w_η(γ) ≥ w_g(γ) for all generators g. The condition w_η > 0 ensures nontrivial recycling; η-dominance means recycling governs the dynamics. *VI.D42 — Structure Recycling Predicate* (τ-effective): three conditions on a carrier (X, D) — decomposition (Life loop factors through Loop_rec with w_η > 0), complexity decrease (C(γ_rec(1)) < C(γ_rec(0))), and material return (outputs released in forms available for reuse by source carriers). The duality table (source ↔ closure: structure generation ↔ structure recycling; complexity increase ↔ complexity decrease; autotrophy ↔ saprotrophy; plants ↔ fungi; Hodge+BSD ↔ Riemann+Navier–Stokes) is explicit in the chapter.
- **Key results:** *VI.T23 — Closure as η-Fiber Return* (τ-effective): a Life loop belongs to Cl_η if and only if the underlying carrier satisfies the structure recycling predicate. The proof structure is the exact dual of VI.T20: η-dominance extracts decomposition and material return from the factorization through Loop_rec and finiteness of the defect functional Δ_Rec; conversely, factorization gives w_η > 0, complexity decrease bounds Δ_Rec, and material return ensures η-dominance over γ.
- **Notation introduced:** Cl_η (closure sector subcategory); Loop_rec (recycler sub-class of the Life Loop Class); Δ_Rec (defect functional for the closure sector); the composition Cl_η ∘ Src_γ on T² as the formal statement that the material cycle is closed.
- **Dependencies:** VI.D41/VI.D42/VI.T23 depend on the Life Loop Class (ch. 09), the Metabolic Fiber Theorem (ch. 10), and the sector template (ch. 08). The force-sector matching assigns Riemann (energy extraction from organic bonds during decomposition) and Navier–Stokes (fluid transport of decomposition products) as dominant forces of the closure sector.

## Lean coverage

`TauLib.BookVI.Life.DefectFunctionals` contains the DeltaRec entry underlying VI.T23, in formal parallel to DeltaSrc. The sector definition and equivalence theorem are formalized in `TauLib.BookVI.Life.SectorTemplate` alongside the persistence, agency, and source entries. VI.D42 and VI.T23 are prose-derived in the current release; full Lean coverage is scheduled with the other primitive-sector entries.

## Where this leads

Chapter 29 fills the closure archetype with biology, developing fungal mycelial network topology, saprotrophic decomposition chemistry (including the fungi's monopoly on lignin degradation), and mycorrhizal symbiosis as a direct inter-sector bridge between Cl_η and Src_γ.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part05/ch28-closure-sector.tex -->
