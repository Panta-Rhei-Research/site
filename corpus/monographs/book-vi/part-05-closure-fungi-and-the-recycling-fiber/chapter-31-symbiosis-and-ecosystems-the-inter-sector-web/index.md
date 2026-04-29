---
layout: "corpus-monograph-chapter"
title: "Chapter 31: Symbiosis and Ecosystems: The Inter-Sector Web"
permalink: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-31-symbiosis-and-ecosystems-the-inter-sector-web/"
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
chapter_number: 31
chapter_slug: "chapter-31-symbiosis-and-ecosystems-the-inter-sector-web"
page_in_book: 183
prev_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-30-death-decomposition-and-aging/"
prev_chapter_title: "Chapter 30: Death, Decomposition, and Aging"
next_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-32-healing-regeneration-and-the-repair-budget/"
next_chapter_title: "Chapter 32: Healing, Regeneration, and the Repair Budget"
summary_short: "An ecosystem is formally an inter-sector web with sector coverage, coupling closure, and material return; every biogeochemical cycle is a Poincaré circulation; symbiosis is classified as inter-sector coupling; ecological communities are Nash equilibria on carrier configuration space."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/"
canonical_part_title: "Closure — Fungi and the Recycling Fiber"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-31-symbiosis-and-ecosystems-the-inter-sector-web/"
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

An ecosystem is not a list of species but a dynamical web in which all five Life sectors interact simultaneously. The preceding chapters developed each sector individually — persistence (archaea), agency (bacteria), source (plants), closure (fungi) — and characterized individual carriers within each sector. This chapter asks how those sectors couple into stable, self-sustaining networks. Four structural levels are addressed. First, the inter-sector web itself: a formal network of Life loops with a coupling matrix C specifying energy–material flows, satisfying three ecosystem conditions (sector coverage, coupling closure, material return). The classical trophic structure (Producer → Consumer → Decomposer) maps directly to Source → Consumer → Closure in sector language, with the 10% rule describing coupling efficiency at each transfer. Second, nutrient cycles as Poincaré circulations: the carbon cycle (~120 Gt C/yr photosynthesis ≈ ~60 Gt C/yr respiration + ~60 Gt C/yr decomposition), nitrogen cycle (six-step N₂ → NH₃ → NO₃⁻ → organic-N → NH₃ → N₂ loop dominated by Rhizobium–legume fixation at ~140 Tg N/yr), and phosphorus cycle (no atmospheric phase; geological timescale of 10⁷–10⁸ years for full cycling) are each shown to be closed orbits in the coupling graph. Third, symbiosis as inter-sector coupling: mutualism (C_ij > 0, C_ji > 0 — mycorrhizae, coral–zooxanthellae, legume–Rhizobium), commensalism (C_ij > 0, C_ji ≈ 0), and parasitism (C_ij > 0, C_ji < 0); lichens are a colimit carrier coupling closure and source in a single composite organism. Fourth, ecological communities as Nash equilibria: the Lotka–Volterra predator–prey oscillation as a Poincaré periodic orbit; competitive exclusion (Gause's principle) as dynamic instability at the same configuration-space point; niche partitioning as the Nash requirement that each carrier occupy a distinct stable point in the carrier configuration space M.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D44 — Inter-Sector Web* (τ-effective): the pair W = ({(D_i, γ_i, h_i)}_i, C) satisfying sector coverage (at least three distinct sectors), coupling closure (Σ_j C_ij > 0 for every i), and material return (directed path from every source carrier to a closure carrier and back).
- **Key results:** *VI.T24 — Ecosystem as Multi-Scale Poincaré Circulation* (τ-effective): the material return condition of VI.D44 implies that every biogeochemical element traces a closed orbit — a Poincaré circulation — in the coupling graph of W; multi-scale structure arises from nested cycles (daily photosynthesis–respiration vs. millennial sedimentation–volcanism). *VI.R18 — Nash Equilibria in Ecological Communities* (τ-effective): a community {x₁, …, x_n} in carrier configuration space M is a Nash equilibrium if Fitness(x_i | x_{-i}) ≥ Fitness(x_i' | x_{-i}) for all alternative strategies x_i'; species–area relationship S = cA^z (z ≈ 0.25) reflects growing available configuration space with habitat area.
- **Notation introduced:** W (inter-sector web); C = (C_ij) (coupling matrix); M (carrier configuration space); x_i ∈ M (ecological niche of carrier i); alternative stable states and regime shifts (transitions between distinct attractor basins in M); biodiversity as the count of occupied stable points.
- **Dependencies:** VI.D44/VI.T24 depend on all four primitive sector definitions (ch. 12, 17, 23, 28) and the consumer sector (ch. 33, referenced forward). VI.R18 depends on the coupling matrix formalism. The Poincaré force (Book III, Part II) supplies the circulation vocabulary for nutrient cycles. The lichen-as-colimit analysis uses the colimit construction from Book I, Part VII.

## Lean coverage

Prose chapter; no Lean formalization target. VI.D44 and VI.T24 are noted as ecosystem-level structural entries in `TauLib.BookVI.Life.SectorTemplate`. The Nash equilibrium remark (VI.R18) is a standard game-theoretic result applied to the carrier configuration space formalism without τ-specific axioms.

## Where this leads

Chapter 32 examines healing and regeneration — the carrier's active partial reversal of the closure sector's action — formalizing the repair budget and proving that metamorphosis preserves SelfDesc even as it radically restructures the carrier.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part05/ch31-ecosystems.tex -->
