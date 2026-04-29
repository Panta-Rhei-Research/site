---
layout: "corpus-monograph-chapter"
title: "Chapter 49: The Chemical Bond as Graph Transformation"
permalink: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-49-the-chemical-bond-as-graph-transformation/"
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
chapter_number: 49
chapter_slug: "chapter-49-the-chemical-bond-as-graph-transformation"
page_in_book: 287
prev_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-48-multi-electron-atoms-and-shell-structure/"
prev_chapter_title: "Chapter 48: Multi-Electron Atoms and Shell Structure"
next_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-50-molecular-orbitals-and-hybridization/"
next_chapter_title: "Chapter 50: Molecular Orbitals and Hybridization"
summary_short: "A chemical bond is a co-rotor merge: two atomic T² mode maps fuse into one molecular mode map when energy is gained by delocalisation. This chapter classifies all principal bond types and analyses H₂ as the paradigmatic example, recasting bond formation as a graph morphism in the τ³ fibration."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
canonical_part_title: "Atoms, Chemistry, and Molecular Structure"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-49-the-chemical-bond-as-graph-transformation/"
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

Stable atoms combine because sharing T² co-rotor modes lowers the total energy below the sum of isolated atomic energies. An isolated atom is a local energy minimum; mode sharing produces a deeper minimum. In Category τ, bond formation is a morphism μ : ℳ_A ⊔ ℳ_B → ℳ_AB — atomic mode maps merge into a molecular mode map — and the energy gain has three components: kinetic lowering through delocalisation (Ruedenberg's analysis shows this dominates in covalent bonds, contrary to the naive Coulomb-attraction picture), potential lowering from multi-centre nuclear attraction, and a counterbalancing nuclear–nuclear repulsion that sets the equilibrium bond length. Bond formation is not a contingent interaction between two independent objects: it is the morphism identifying co-rotor modes that were previously separate.

The chapter classifies the five principal bond types in this language. A covalent bond is a co-rotor merge with comparable amplitude on both centres. An ionic bond is a mode transfer: one atom absorbs the electron mode entirely, producing ions bound by Coulomb attraction V_ionic(R) = −e²/(4πε₀R) + V_repulsion. Metallic bonding delocalises valence modes across the full lattice — an "electron sea" of T² modes spanning macroscopic distances. Hydrogen bonds (~10–40 kJ/mol) arise when H bonded to an electronegative atom (O, N, F) interacts with a lone pair on a neighbouring molecule, controlling the structure of water and biological macromolecules. Van der Waals interactions scale as −1/R⁶ from correlated electron fluctuations and govern noble-gas condensation.

The hydrogen molecule H₂ is the paradigmatic case. Two 1s atomic orbitals φ_A and φ_B combine into bonding ψ₊ = (φ_A + φ_B)/√(2+2S) (enhanced inter-nuclear density, lower energy) and antibonding ψ₋ = (φ_A − φ_B)/√(2−2S) (nodal plane, higher energy), where S = ⟨φ_A|φ_B⟩. Both electrons fill ψ₊ with opposite spins, giving bond order b = (2−0)/2 = 1 and dissociation energy D₀ = 436 kJ/mol at equilibrium length R_e = 0.74 Å. He₂ places four electrons in (ψ₊, ψ₋), forcing bond order (2−2)/2 = 0: helium's T² modes are already saturated, with no unfilled mode available for sharing. Electronegativity difference Δχ (Pauling scale, anchored by F at 4.0) determines bond character — nonpolar covalent (Δχ ≈ 0), polar covalent (0.5–1.7), ionic (> 1.7) — and is the asymmetry parameter of the graph transformation weighting shared edges between two atomic vertices.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D56–IV.D61* (τ-effective): co-rotor merge morphism μ : ℳ_A ⊔ ℳ_B → ℳ_AB; covalent, ionic, metallic, hydrogen, and van der Waals bond types; bonding and antibonding orbitals ψ₊ and ψ₋ for H₂; bond order b = (n_b − n_a)/2; Pauling electronegativity χ.
- **Key results:** *IV.T19–IV.T20* (τ-effective): mode-sharing principle E_molecule < ΣE_atoms as the universal bond-formation criterion; He₂ non-bonding from saturated T² modes (bond order 0).
- **Dependencies:** Chapter 48 (T² saturation and Pauli exclusion); Chapter 45 (hydrogen 1s co-rotor mode).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 50 extends the two-centre picture to full molecular orbital theory: LCAO superpositions of many atomic modes, MO diagrams for diatomic molecules, hybridisation, and the HOMO/LUMO frontier orbitals that govern chemical reactivity.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part06/ch49-chemical-bond.tex -->
