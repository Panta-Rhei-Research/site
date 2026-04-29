---
layout: "corpus-monograph-chapter"
title: "Chapter 8: The 4+"
permalink: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-08-the-4/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-life-definition"
chapter_number: 8
chapter_slug: "chapter-08-the-4"
page_in_book: 41
prev_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-07-the-life-loop-class-and-metabolic-geometry/"
prev_chapter_title: "Chapter 7: The Life Loop Class and Metabolic Geometry"
next_chapter_url: "/corpus/monographs/book-vi/part-01-the-life-definition/chapter-09-the-seven-hallmarks-derived/"
next_chapter_title: "Chapter 9: The Seven Hallmarks Derived"
summary_short: "The 4+1 sector template from Book III is instantiated at E₂. Four primitive sectors — Persistence (α), Agency (π), Source (γ), Closure (η) — plus one mixed Consumer sector on (γ, η) exhaust the Life-layer classification. Generator Adequacy is proven; Eukarya is identified as carrier technology, not a sector."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
canonical_part_title: "The Life Definition"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-01-the-life-definition/chapter-08-the-4/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part I: The Life Definition"
      url: "/corpus/monographs/book-vi/part-01-the-life-definition/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part I"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 60
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

The Life Loop Class established in Chapter 7 assigns to every living system a homotopy class in the space of SelfDesc-preserving endomorphisms. This chapter uses the base-fiber geometry of τ³ = τ¹ ×_f T² to read the dominant winding of that homotopy class and thereby assign every Life loop to exactly one of five Life sectors. A Life sector is a pair (g, P_g) — a generator of τ³ together with a dominance predicate on Loop_L. The base generators α (temporal) and π (spatial) give the worldline sectors: Persistence, whose carriers invest primarily in temporal endurance, exemplified by extremophile Archaea; and Agency, whose carriers invest primarily in spatial motility and environmental response, exemplified by motile Bacteria. The fiber generators γ and η give the metabolic sectors: Source, whose carriers dominantly produce new structure from non-living precursors, exemplified by autotrophic Plants; and Closure, whose carriers dominantly recycle existing biological material, exemplified by saprotrophic Fungi. The Consumer sector occupies the unique mixed position on the fiber pair (γ, η): co-dominant winding around both γ and η, acquiring structure and energy from other Life, exemplified by Animals. Generator Adequacy proves that these five sectors are exhaustive and disjoint — every Life loop belongs to exactly one — by combining the Loop Factorization Lemma's unique homotopy decomposition with the Metabolic Fiber Theorem's nontriviality guarantee. The No Fifth Primitive Sector lemma closes the classification: the fibration map f is a structural map, not a winding generator, so π₁(τ³) ≅ π₁(τ¹) × ℤ² admits exactly four independent primitive directions. The chapter concludes with a full correction of the first edition: Eukarya is not a sector but a fiber-enabled regime — the carrier technology produced by endosymbiosis that internalises the full (γ, η) metabolic fiber into End(X), allowing eukaryotic cells to run any of the five sectors.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D13 — Life Sector* (τ-effective): the (g, P_g) pair with dominance predicate on Loop_L. *VI.D14 — Persistence Sector* (α-base). *VI.D15 — Agency Sector* (π-base). *VI.D16 — Source Sector* (γ-fiber). *VI.D17 — Closure Sector* (η-fiber). *VI.D18 — Consumer Mixed Sector* ((γ, η)-fiber pair, co-dominance criterion).
- **Key results:** *VI.T07 — Generator Adequacy at E₂*: Loop_L = S_α ⊔ S_π ⊔ S_γ ⊔ S_η ⊔ S_(γ,η); the partition is exhaustive and disjoint. *VI.L04 — No Fifth Primitive Sector*: the fibration map f contributes no ℤ-factor to π₁(τ³); four generators exhaust the primitive assignments.
- **Dependencies:** Chapter 7 (Life Loop Class, Metabolic Fiber Theorem, Consumer Mixer Uniqueness); Book III (4+1 template, signature rigidity, τ³ fibration).

## Lean coverage

`TauLib.BookVI.Life.SectorTemplate`

## Where this leads

With the five sectors defined and proven exhaustive, Chapter 9 derives the seven classical hallmarks of life as theorems from the formal machinery, showing that each hallmark is a necessary consequence of the Distinction–SelfDesc pair rather than an independent postulate.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part01/ch08-sector-template.tex -->
