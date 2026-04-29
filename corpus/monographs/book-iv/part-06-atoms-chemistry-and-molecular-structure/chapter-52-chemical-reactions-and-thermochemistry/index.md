---
layout: "corpus-monograph-chapter"
title: "Chapter 52: Chemical Reactions and Thermochemistry"
permalink: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-52-chemical-reactions-and-thermochemistry/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-atoms-chemistry-and-molecular-structure"
chapter_number: 52
chapter_slug: "chapter-52-chemical-reactions-and-thermochemistry"
page_in_book: 299
prev_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-51-molecular-geometry/"
prev_chapter_title: "Chapter 51: Molecular Geometry"
next_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-53-organic-chemistry-and-aromatic-systems/"
next_chapter_title: "Chapter 53: Organic Chemistry and Aromatic Systems"
summary_short: "A chemical reaction is a τ² mode rearrangement: reactant modes destabilise, pass through a transition-state saddle on the potential energy surface, and settle into product modes. Thermodynamics (ΔG = ΔH − TΔS), kinetics (Arrhenius), catalysis, and equilibrium (ΔG° = −RT ln K) are all developed from this perspective."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
canonical_part_title: "Atoms, Chemistry, and Molecular Structure"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-52-chemical-reactions-and-thermochemistry/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part VI: Atoms, Chemistry, and Molecular Structure"
      url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part VI"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 48
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

A chemical reaction is, at its core, a rearrangement of bonds: old τ² modes decouple, the system traverses a saddle point on the potential energy surface (PES), and new modes settle into the product configuration. Every reaction simultaneously answers three questions — thermodynamic (which direction is favoured?), kinetic (how fast?), mechanistic (by what pathway?) — and this chapter develops all three.

The PES E(q₁, …, q_N) maps total electronic energy over all nuclear coordinates; reactant and product configurations are local minima, the transition state is a first-order saddle point, and the activation energy Eₐ = E_TS − E_reactants is the minimum energy input required. Kinetically, the Arrhenius equation k = A exp(−Eₐ/RT) gives the rate constant as a Boltzmann-weighted passage over this barrier: a 10 K temperature rise approximately doubles the rate for many room-temperature reactions. The linearised form ln k vs. 1/T has slope −Eₐ/R, enabling experimental determination of Eₐ. Diamond is thermodynamically unstable relative to graphite yet effectively stable because Eₐ is enormous at ambient conditions — thermodynamics sets the direction, kinetics sets the pace.

Catalysts provide an alternative τ² rearrangement pathway with lower Eₐ, leaving ΔG and K unchanged; enzymes achieve rate enhancements of 10⁶–10¹² through geometric and electronic complementarity between active site and substrate. Thermodynamically, enthalpy H = U + PV tracks heat flow at constant pressure (q_P = ΔH); Hess's law guarantees path-independence (enthalpy is a state function), allowing complex ΔH values to be assembled from measurable steps. Entropy S = k_B ln Ω counts accessible microstates and increases for any spontaneous process in the universe. Gibbs free energy G = H − TS unifies both: ΔG < 0 for spontaneity, ΔG = 0 at equilibrium. The equilibrium condition ΔG° = −RT ln K links free energy to the ratio of product to reactant configurations; the van 't Hoff equation d ln K/dT = ΔH°/RT² quantifies how temperature shifts equilibrium. In the τ³ reading, equilibrium is the stationary point of the τ² mode system where forward and reverse mode-creation rates balance.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D56–IV.D62* (τ-effective): potential energy surface E(q₁,…,q_N); reaction coordinate ξ; transition state (saddle point); activation energy Eₐ = E_TS − E_reactants; enthalpy H = U + PV; entropy S = k_B ln Ω; Gibbs free energy G = H − TS; catalyst.
- **Key results:** *IV.T53–IV.T55* (τ-effective): Arrhenius equation k = A exp(−Eₐ/RT); Gibbs–equilibrium relation ΔG° = −RT ln K; *IV.P53–IV.P54* (τ-effective): Hess's law (enthalpy path-independence); van 't Hoff equation d ln K/dT = ΔH°/RT² (Le Chatelier coupling to temperature).
- **Dependencies:** Chapter 51 (enzyme–substrate geometric complementarity); Chapter 48 (Boltzmann statistics and mode counting).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 53 applies the bond-formation and reaction machinery to carbon chemistry, where catenation generates over ten million compounds and cyclic π-delocalisation produces the aromatic stability central to both industrial chemistry and the molecular biology of DNA.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part06/ch52-chemical-reactions.tex -->
