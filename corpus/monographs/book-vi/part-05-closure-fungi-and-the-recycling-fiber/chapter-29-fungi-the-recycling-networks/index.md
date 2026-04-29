---
layout: "corpus-monograph-chapter"
title: "Chapter 29: Fungi: The Recycling Networks"
permalink: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-29-fungi-the-recycling-networks/"
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
chapter_number: 29
chapter_slug: "chapter-29-fungi-the-recycling-networks"
page_in_book: 169
prev_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-28-the-closure-sector-decomposition-and-nutrient-return/"
prev_chapter_title: "Chapter 28: The Closure Sector: Decomposition and Nutrient Return"
next_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-30-death-decomposition-and-aging/"
next_chapter_title: "Chapter 30: Death, Decomposition, and Aging"
summary_short: "Fungi are the closure archetype: sessile heterotrophs with w_π = 0 and w_γ = 0 whose small-world mycelial networks decompose structural polymers, hold a monopoly on lignin degradation, and bridge source and closure sectors through mycorrhizal exchange."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/"
canonical_part_title: "Closure — Fungi and the Recycling Fiber"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-29-fungi-the-recycling-networks/"
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

Chapter 28 gave the formal sector definition; this chapter fills it with biology. The ~144,000 described fungal species (with estimated total diversity of 2–4 million) share a single metabolic strategy: absorptive heterotrophy — external digestion followed by nutrient absorption through hyphal cell membranes. Every fungus has w_π = 0 (sessile) and w_γ = 0 (no photosynthetic production); the Life loop winds only on η and α, making fungi the purest closure-sector organisms in the same way that plants are the purest source-sector organisms. The chapter develops four areas. First, fungal body architecture: hyphae (2–10 μm tubular filaments growing by apical extension from a Spitzenörper vesicle cluster) aggregate into mycelia that anastomose into small-world graphs with high local clustering and short average path length — a topology that maximizes absorptive surface area and provides redundant transport routes. Second, saprotrophic decomposition: cellulases, ligninases, proteases, lipases, and amylases dismantle structural polymers extracellularly; only white-rot Basidiomycota can fully depolymerize lignin, a biochemical monopoly whose evolutionary timing (~290–300 Mya) accounts for the Carboniferous coal deposits — dead wood accumulated for ~60 Myr because no organism could recycle it. Third, mycorrhizal symbiosis: ~80–90% of land plant species form associations in which fungi provide phosphorus, nitrogen, and water in exchange for photosynthetic carbon, coupling Cl_η directly to Src_γ at the root–hypha interface; the Wood Wide Web (common mycorrhizal networks) extends this to inter-plant nutrient and defense-signal transfer. Fourth, ecological strategies: saprotrophic (pure closure), mycorrhizal (closure–source coupled), parasitic (premature closure on living tissue), and lichenized (closure–source composite carrier).

## What this chapter contributes

- **Definitions / Axioms:** *VI.R16 — Fungi as Closure Archetype* (τ-effective): Fungi instantiates all three structure recycling conditions — extracellular hydrolysis and oxidation (decomposition), polymers → CO₂/H₂O/mineral ions (complexity decrease, ΔC < 0 per digestion cycle), nutrients released in plant-available forms (material return). *VI.R17 — Mycelial Network Topology* (τ-effective): the mycelial graph (V, E) is a small-world network with degree distribution, clustering coefficient, and average path length empirically confirmed in Phanerochaete velutina; high clustering maximizes local enzyme concentration; short path length ensures rapid nutrient transport.
- **Key results:** No new theorems. The carbon-cycle dual (photosynthesis ↔ decomposition at stoichiometric level: 6CO₂ + 6H₂O + light ↔ C₆H₁₂O₆ + 6O₂) is made explicit. Global balance: land NPP ~120 Gt C/yr ≈ total heterotrophic respiration + decomposition. The Carboniferous coal gap serves as a geological-record proof that Src_γ without Cl_η is an open cycle — source without closure accumulates structure rather than recycling it.
- **Notation introduced:** w_π = 0, w_γ = 0 (pure closure condition); four fungal strategies mapped to distinct η-fiber operational modes; total fungal biomass ~12 Gt C (~2% of land plant biomass), reflecting rapid-turnover strategy vs. structural accumulation.
- **Dependencies:** VI.R16/VI.R17 depend on VI.D41/VI.D42/VI.T23 (ch. 28). Mycorrhizal symbiosis anticipates the inter-sector web formalization (ch. 31). The Carboniferous section connects to the source archetype narrative (ch. 25).

## Lean coverage

Prose chapter; no Lean formalization target. VI.R16 and VI.R17 are informal instantiation records in `TauLib.BookVI.Life.SectorTemplate`, parallel to VI.R14/VI.R15 for plants.

## Where this leads

Chapter 30 turns the closure sector's logic inward: every finite-lineage carrier is itself eventually recycled. Death is formalized as distinction collapse, aging as monotonic defect accumulation, and post-mortem decomposition as the five-stage return of elemental material to the nutrient pool.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part05/ch29-fungi.tex -->
