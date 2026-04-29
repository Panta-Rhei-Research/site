---
layout: "corpus-monograph-chapter"
title: "Chapter 50: Molecular Orbitals and Hybridization"
permalink: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-50-molecular-orbitals-and-hybridization/"
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
chapter_number: 50
chapter_slug: "chapter-50-molecular-orbitals-and-hybridization"
page_in_book: 291
prev_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-49-the-chemical-bond-as-graph-transformation/"
prev_chapter_title: "Chapter 49: The Chemical Bond as Graph Transformation"
next_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-51-molecular-geometry/"
next_chapter_title: "Chapter 51: Molecular Geometry"
summary_short: "LCAO molecular orbital theory is T² mode superposition: atomic harmonics combine into delocalised molecular harmonics spanning multiple nuclear centres. This chapter derives MO diagrams for key diatomics — including O₂'s predicted paramagnetism — and develops sp³/sp²/sp hybridisation and HOMO/LUMO frontier orbital reactivity."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
canonical_part_title: "Atoms, Chemistry, and Molecular Structure"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-50-molecular-orbitals-and-hybridization/"
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

Molecular orbital theory constructs delocalised electronic states as linear combinations of atomic orbitals, ψ_MO = Σ cᵢφᵢ, with coefficients determined by the variational principle via the secular equation det(H_ij − E S_ij) = 0. In the co-rotor framework this is T² mode superposition: atomic harmonics localised at individual nuclear centres combine into molecular harmonics spanning the entire molecule. The coefficients encode the electron-density distribution; for heteronuclear pairs the more electronegative atom contributes more amplitude to the bonding MO.

Bonding MOs (in-phase superposition) have enhanced inter-nuclear density and energy below either constituent atomic orbital; antibonding MOs (out-of-phase, marked *) have a nodal plane between nuclei and energy above. The bond-order formula b = (n_b − n_a)/2 converts electron counts into stability: H₂ (b = 1, stable), He₂ (b = 0, unbound), N₂ (b = 3, triple bond, the strongest common diatomic). Molecular orbital theory's most famous triumph is O₂: Hund's rule applied to the degenerate π_2p* level places two electrons with parallel spins, predicting paramagnetism — a result that Lewis structures and valence-bond theory both miss. The homonuclear diatomic MO series (H₂ through F₂) illustrates how bond order and magnetic character are read off a single diagram.

Bond geometry is classified as σ (axial symmetry about the internuclear axis, free rotation, from s–s, s–p, or head-on p–p overlap) or π (nodal plane through the axis, restricted rotation, from side-on p–p overlap). A single bond is 1σ; a double bond is 1σ + 1π; a triple bond is 1σ + 2π. Hybridisation mixes s and p valence orbitals to optimise bonding geometry: sp³ (four equivalent hybrids, tetrahedral at 109.5°) for methane; sp² (three hybrids + one unhybridised p_z, trigonal planar at 120°) for ethylene; sp (two hybrids + two unhybridised p, linear at 180°) for acetylene. Promotion energy (e.g., 2s → 2p for carbon, ~4 eV) is more than offset by the additional bonding energy when bonds are strong — the basis of carbon's unmatched structural versatility. Frontier orbital theory closes the chapter: chemical reactivity is controlled by the HOMO (highest occupied MO) and LUMO (lowest unoccupied MO); nucleophilic attack transfers electron density from the nucleophile's HOMO to the electrophile's LUMO. The HOMO–LUMO gap determines absorption wavelength, electrical conductivity, and kinetic stability.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D62–IV.D69* (τ-effective): LCAO molecular orbital; bonding MO ψ₊; antibonding MO ψ₋ (σ*, π*); σ bond (axial symmetry); π bond (nodal plane); sp³/sp²/sp hybrid orbitals; HOMO and LUMO.
- **Key results:** *IV.T21–IV.T22* (τ-effective): bond-order formula b = (n_b − n_a)/2 as the universal stability metric; frontier orbital reactivity theorem (nucleophile HOMO → electrophile LUMO); O₂ paramagnetism from Hund's rule applied to degenerate π* MOs.
- **Dependencies:** Chapter 49 (bonding/antibonding pairs for H₂, bond order); Chapter 48 (Pauli exclusion and Hund's rule).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 51 takes the three-dimensional consequence of MO theory and hybridisation: the VSEPR model determines molecular geometry by minimising electron-pair repulsion, and molecular shape in turn controls every macroscopic chemical and biological property.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part06/ch50-molecular-orbitals.tex -->
