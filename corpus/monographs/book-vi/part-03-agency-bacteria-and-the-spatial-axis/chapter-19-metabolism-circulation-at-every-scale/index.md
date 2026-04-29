---
layout: "corpus-monograph-chapter"
title: "Chapter 19: Metabolism: Circulation at Every Scale"
permalink: "/corpus/monographs/book-vi/part-03-agency-bacteria-and-the-spatial-axis/chapter-19-metabolism-circulation-at-every-scale/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 3
part_display: "Part III"
part_slug: "part-03-agency-bacteria-and-the-spatial-axis"
chapter_number: 19
chapter_slug: "chapter-19-metabolism-circulation-at-every-scale"
page_in_book: 107
prev_chapter_url: "/corpus/monographs/book-vi/part-03-agency-bacteria-and-the-spatial-axis/chapter-18-bacteria-the-spatial-pioneers/"
prev_chapter_title: "Chapter 18: Bacteria: The Spatial Pioneers"
next_chapter_url: "/corpus/monographs/book-vi/part-03-agency-bacteria-and-the-spatial-axis/chapter-20-atp-the-universal-energy-currency/"
next_chapter_title: "Chapter 20: ATP: The Universal Energy Currency"
summary_short: "Metabolism is Poincaré circulation at every scale. Metabolic Circulation (VI.D31) formalizes the catabolism–anabolism oscillation with a closure condition that makes cycles thermodynamically preferred over linear pathways. The Krebs cycle is proved to be a concrete Loop_L instantiation (VI.P11). Blood flow extends this Navier–Stokes + Poincaré picture to the organismal scale."
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-03-agency-bacteria-and-the-spatial-axis/"
canonical_part_title: "Agency — Bacteria and the Spatial Axis"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-03-agency-bacteria-and-the-spatial-axis/chapter-19-metabolism-circulation-at-every-scale/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part III: Agency — Bacteria and the Spatial Axis"
      url: "/corpus/monographs/book-vi/part-03-agency-bacteria-and-the-spatial-axis/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part III"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 62
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

The agency sector requires energy. Spatial motility dissipates power continuously against viscous drag; without a replenishing energy supply the Life loop cannot close. This chapter develops the energetic infrastructure that makes agency possible, arguing that metabolism is not a list of reactions but organized circulation — the Poincaré force made molecular — and that cyclic pathways dominate central metabolism by structural necessity rather than evolutionary contingidence.

Metabolic Circulation (VI.D31) formalizes the catabolism–anabolism oscillation as a pair of flux fields (J_cat, J_ana) on the carrier's metabolite concentration space, satisfying complementarity (the two streams flow in opposite directions of molecular complexity), energetic coupling (|ΔG_cat| ≥ |ΔG_ana| > 0), and closure (the composite flux has at least one periodic orbit — the system returns to a state compatible with its distinction after a finite number of chemical transformations). Condition (iii), closure, is the structural requirement. A purely catabolic system degrades to equilibrium; a purely anabolic system stalls for lack of energy. The Circulation Stability principle then establishes that cyclic trajectories have lower free energy than linear alternatives on τ³: G[γ_cycle] < G[γ_linear]. The ubiquity of metabolic cycles — Krebs, Calvin, urea, pentose phosphate, folate, β-oxidation — is categorical necessity. Each regenerates its starting material (oxaloacetate, ribulose-1,5-bisphosphate, ornithine) and each is a Poincaré attractor in concentration space, with a Lyapunov stability condition requiring the product of forward rate constants to exceed the compound leakage rate.

The Krebs Cycle as Loop_L Instantiation proposition (VI.P11) verifies that the eight-step citric acid cycle constitutes a member of Loop_L: the distinction D (plasma membrane) is preserved throughout all eight enzymatic steps; the cycle is closed (oxaloacetate is regenerated at step 8, returning the system to its starting configuration); and the homotopy class has nonzero source winding (NADH, FADH₂, GTP produced) and nonzero closure winding (oxaloacetate recycled). Flux control is distributed across multiple enzymes (citrate synthase C¹_J ≈ 0.3, isocitrate dehydrogenase C³_J ≈ 0.4, α-ketoglutarate dehydrogenase C⁴_J ≈ 0.2), with no single point of failure — a signature of robust cyclic systems.

The chapter then traces the glycolytic pathway to the pyruvate branch point, where aerobic respiration yields ~30–32 ATP/glucose and fermentation (lactic or alcoholic) yields only 2 but operates without oxygen. Glycolysis itself is linear, but it is embedded in cyclic context at every scale: NAD⁺ must be regenerated, and gluconeogenesis closes the glucose–pyruvate loop at the organismal level. Blood flow completes the multi-scale picture: William Harvey's 1628 demonstration of circulation was the first recognition of Poincaré circulation at the organismal scale. Blood is a non-Newtonian fluid approximated as Newtonian in large vessels; Reynolds numbers span four orders of magnitude from the aorta (Re ~4000, transitional) to capillaries (Re ~0.01, Stokes flow). The cardiac pressure–volume loop is a Poincaré periodic orbit enclosing stroke work of ~1 J per beat.

## What this chapter contributes

- **Definitions / Axioms:** *VI.D31 — Metabolic Circulation* (τ-effective): a complementary, coupled, closed pair of flux fields on the carrier's metabolite concentration space.
- **Key results:** *VI.P11 — Krebs Cycle as Loop_L Instantiation* (τ-effective): verification that the eight-step citric acid cycle satisfies all three membership conditions of Loop_L, with nonzero source and closure winding numbers.
- **Notation introduced:** J_cat, J_ana (catabolic and anabolic flux fields); Lyapunov stability condition for metabolic cycles; Re (Reynolds number at biological scales).
- **Dependencies:** VI.D29 (agency sector, ch. 17); VI.D31 depends on Loop_L definition (ch. 09) and Metabolic Fiber Theorem (ch. 10); Navier–Stokes and Poincaré as dominant forces (ch. 17, ch. 08).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. VI.P11 is established by direct biochemical verification rather than formal Lean proof.

## Where this leads

Chapter 20 focuses on ATP — the molecule at the center of metabolic circulation — asking why life uses one universal energy currency rather than many, and deriving the ~30 kJ/mol hydrolysis quantum from the master constant ι_τ at τ-effective scope.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-06/part03/ch19-metabolism.tex -->
