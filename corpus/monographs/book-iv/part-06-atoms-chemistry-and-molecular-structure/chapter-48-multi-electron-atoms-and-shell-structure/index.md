---
layout: "corpus-monograph-chapter"
title: "Chapter 48: Multi-Electron Atoms and Shell Structure"
permalink: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-48-multi-electron-atoms-and-shell-structure/"
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
chapter_number: 48
chapter_slug: "chapter-48-multi-electron-atoms-and-shell-structure"
page_in_book: 283
prev_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-47-hyperfine-structure-and-the-role-of-iota-tau/"
prev_chapter_title: "Chapter 47: Hyperfine Structure and the Role of ι<sub>τ</sub>"
next_chapter_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-49-the-chemical-bond-as-graph-transformation/"
next_chapter_title: "Chapter 49: The Chemical Bond as Graph Transformation"
summary_short: "Shell structure emerges as T² mode saturation: each principal quantum number n supports 2n² co-rotor slots. This chapter builds the periodic table as a physical map of T² mode filling, from helium's inert closed shell through the f-block lanthanides."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-06-atoms-chemistry-and-molecular-structure/"
canonical_part_title: "Atoms, Chemistry, and Molecular Structure"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-06-atoms-chemistry-and-molecular-structure/chapter-48-multi-electron-atoms-and-shell-structure/"
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

Hydrogen admits an exact solution; every other atom does not. The culprit is electron–electron repulsion V_ee = e²/(4πε₀|r₁ − r₂|), which couples the two-body problem irreducibly — no change of coordinates disentangles it. In Category τ, this is the structural consequence of overlapping T² modes: when two electrons share the same fiber, their modes interact, and Pauli exclusion forces them into orthogonal states. The chapter develops the multi-electron atom beginning with helium (Z = 2, 1s², two slots of the n = 1 shell filled), where the repulsion raises the energy by +29.8 eV relative to the non-interacting limit of −108.8 eV, giving the measured −79.0 eV. Z_eff ≈ 1.69 from variational screening captures the partial shielding one electron exerts on the other. Helium's complete T² saturation (2n² = 2 modes for n = 1) explains its chemical inertness and its bosonic character under ⁴He superfluidity.

Shell structure emerges as mode saturation: each principal shell n supports Nₙ = 2n² co-rotor slots, derived by summing the subshell capacities 2(2ℓ+1) over ℓ = 0, …, n−1 — itself the sum of the first n odd integers times 2. The subshell capacities 2, 6, 10, 14 for s, p, d, f respectively encode the T² harmonic degeneracies. Noble gases mark complete saturation at each tier: He (2), Ne (10), Ar (18), Kr (36), Xe (54). The aufbau (Madelung) rule orders filling by increasing (n+ℓ), with ties broken by lower n; the deviation of 4s before 3d follows from s-orbital radial penetration giving a lower effective energy. Hund's rule fills degenerate subshells with parallel spins before pairing, minimising electron–electron repulsion by maximising spatial separation. All major periodic trends — ionisation energy ∝ Z_eff²/n², electronegativity ∝ (I₁ + A)/2, atomic radius ∝ n²/Z_eff — derive from the single parameter Z_eff = Z − σ, where σ is the Slater screening constant. The periodic table as a T² mode-filling map gives the blocks (s, p, d, f) their physical meaning: each block is a subshell type, each row a new principal shell, and the row lengths 2, 8, 8, 18, 18, 32, 32 directly encode the T² harmonic degeneracies.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D49–IV.D55* (τ-effective): helium atom (Z = 2, 1s²) as first closed-shell co-rotor; effective nuclear charge Z_eff = Z − σ; periodic table as T² mode map with s/p/d/f blocks corresponding to ℓ = 0/1/2/3.
- **Key results:** *IV.T16–IV.T18* (τ-effective): aufbau (Madelung) filling order; shell capacity Nₙ = 2n² proved by summing subshell degeneracies; periodic trends (ionisation energy ∝ Z_eff²/n², electronegativity ∝ (I₁ + A)/2, radius ∝ n²/Z_eff) derived from Z_eff.
- **Dependencies:** Chapter 45 (hydrogen co-rotor and Pauli principle); Chapter on holomorphic state space (Pauli exclusion for fermionic T² modes).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The shell-capacity proof and aufbau ordering are stated as theorems without formal Lean mechanisation.

## Where this leads

Chapter 49 takes the first step beyond isolated atoms: mode-sharing between two atoms produces the chemical bond, understood as a co-rotor merge that lowers energy through delocalisation — the mechanism that drives all of chemistry.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part06/ch48-multi-electron-atoms.tex -->
