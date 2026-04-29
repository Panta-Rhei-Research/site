---
layout: "corpus-monograph-chapter"
title: "Chapter 32: Healing, Regeneration, and the Repair Budget"
permalink: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-32-healing-regeneration-and-the-repair-budget/"
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
chapter_number: 32
chapter_slug: "chapter-32-healing-regeneration-and-the-repair-budget"
page_in_book: 189
prev_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-31-symbiosis-and-ecosystems-the-inter-sector-web/"
prev_chapter_title: "Chapter 31: Symbiosis and Ecosystems: The Inter-Sector Web"
next_chapter_url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-33-the-consumer-mixer-uniqueness-on-gamma-eta/"
next_chapter_title: "Chapter 33: The Consumer Mixer: Uniqueness on (γ, η)"
summary_short: "The repair budget B(X) is the supremum of cumulative defect perturbation the carrier can absorb while maintaining distinction; wound healing is a four-phase sector sequence; metamorphosis preserves SelfDesc (VI.P17) even as it radically restructures carrier material."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/"
canonical_part_title: "Closure — Fungi and the Recycling Fiber"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-32-healing-regeneration-and-the-repair-budget/"
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

Chapter 30 showed that death is a theorem for every finite-lineage carrier with bounded repair capacity. This chapter examines the interval between injury and death — the carrier's active resistance to closure through healing, regeneration, and programmed restructuring. Healing is not the opposite of closure; it is a partial, bounded, energy-consuming reversal of the closure sector's local action. The chapter is organized around four topics. First, the repair budget B(X): the supremum of cumulative defect perturbation (Σ||δ_k||) the carrier can absorb while the evaluator continues to restore D_n; determined by SelfDesc fidelity, stem cell reserve, metabolic free energy, and replicative capacity (Hayflick limit). B(X) is a monotonically decreasing resource — each repair event consumes a portion that is not fully replenished. Second, wound healing in four phases that recapitulate the sector structure: hemostasis (seconds to minutes, damage containment — Δ stabilized); inflammation (hours to days, local closure — macrophages recycle damaged tissue, Δ transiently increases); proliferation (days to weeks, local source — fibroblasts deposit collagen, keratinocytes advance at ~0.5–1.0 mm/day, Δ decreases); remodeling (weeks to years, boundary optimization — type III to type I collagen, final tensile strength ~80% of original, Δ → local minimum that is suboptimal compared with pre-injury state). Third, the regeneration spectrum from Planaria (whole-body, B(X) ≈ ∞, neoblast pool self-renewing) through salamander limb regeneration (blastema-mediated, five-stage, dedifferentiation controlled by p53/Rb suppression) and zebrafish cardiac regeneration to mammalian liver (compensatory hyperplasia within ±3% of target mass) — with the regeneration–complexity trade-off: strong tumor suppression enables large complex multicellular organisms at the cost of reduced regenerative capacity. Fourth, metamorphosis: during holometabolous insect pupation, ~85% of larval tissue is dissolved by histolysis and rebuilt from imaginal discs. Yet the organism is the same individual — same genome, same metabolic continuity, and retained learned behaviors (Blackiston et al. 2008).

## What this chapter contributes

- **Definitions / Axioms:** *VI.D45 — Repair Budget* (τ-effective): B(X) = sup{Σ||δ_k|| | evaluator restores D_n after each δ_k for all n}; determined by SelfDesc fidelity, stem cell reserve, metabolic resources, and replicative capacity; B(X) < ∞ for all finite-lineage carriers subject to VI.P16.
- **Key results:** *VI.P17 — Metamorphosis Preserves SelfDesc* (τ-effective): three claims. Code identity: code(D_larva)[ω] = code(D_adult)[ω] — metamorphosis does not alter the genome, which is the profinite carrier of the ω-germ. Evaluator continuity: a continuous path of evaluators {Eval_t}_{t∈[0,1]} exists such that Eval_t reconstructs D_t from code(D)[ω] at every instant, including during histolysis (imaginal disc cells are metabolically active throughout the pupal stage and mushroom body neurons partially persist). SelfDesc persistence: for all t, (X_t, D_t, Eval_t) is a SelfDesc triple. The proposition grounds the Ship of Theseus resolution: identity resides in the ω-germ code and its continuous reading, not in the material substrate.
- **Notation introduced:** B(X) (repair budget); scarring as weak-attractor return; regeneration as strong-attractor return; the regeneration–complexity trade-off table (planaria/hydra → potentially immortal; lobster → very large budget; salamander → large; zebrafish → moderate; human/mouse → moderate/small).
- **Dependencies:** VI.D45 depends on the SelfDesc Closure Theorem (ch. 05) and the defect functional (ch. 05). VI.P17 depends on the SelfDesc predicate (ch. 05), the ω-germ definition (ch. 05), and the closure sector (ch. 28). The wound healing analysis connects to the Hodge boundary interpretation of the distinction D.

## Lean coverage

Prose chapter; no Lean formalization target. VI.D45 is a quantitative extension of the repair concept implicit in the SelfDesc Closure Theorem. VI.P17 is formalized informally in `TauLib.BookVI.Life.SectorTemplate` as a SelfDesc-preservation record. The dedifferentiation–tumor-suppression trade-off is biological content without τ-axiom dependencies.

## Where this leads

Part V is complete. Part VI opens with chapter 33, which defines the consumer (mixer) sector as the unique sector with mixed (γ, η)-winding on the fiber torus, with animals as the biological archetype — closing the five-sector primitive framework.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part05/ch32-healing-regeneration.tex -->
