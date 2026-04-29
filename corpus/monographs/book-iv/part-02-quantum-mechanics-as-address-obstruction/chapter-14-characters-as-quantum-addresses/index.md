---
layout: "corpus-monograph-chapter"
title: "Chapter 14: Characters as Quantum Addresses"
permalink: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-14-characters-as-quantum-addresses/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 2
part_display: "Part II"
part_slug: "part-02-quantum-mechanics-as-address-obstruction"
chapter_number: 14
chapter_slug: "chapter-14-characters-as-quantum-addresses"
page_in_book: 75
prev_chapter_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-13-the-cr-address-space/"
prev_chapter_title: "Chapter 13: The CR Address Space"
next_chapter_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-15-the-holomorphic-state-space/"
next_chapter_title: "Chapter 15: The Holomorphic State Space"
summary_short: "The lemniscate 𝕃 is where quantum numbers live. Characters—homomorphisms from fundamental groups to U(1)—enumerate the possible quantum states. This is…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
canonical_part_title: "Quantum Mechanics as Address Obstruction"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-14-characters-as-quantum-addresses/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part II: Quantum Mechanics as Address Obstruction"
      url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part II"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 44
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

The lemniscate 𝕃 is where quantum numbers live. A character is a homomorphism χ: π₁(X) → U(1) from a space's fundamental group to the unit circle, and on the torus T² = S¹ × S¹ these characters are labeled by integer pairs (m, n) ∈ ℤ × ℤ—the quantum numbers. Each character is therefore a quantum address: a discrete label specifying where a state lives in the CR-admissible mode space Λ_CR. The chapter shows that quantization is not imposed by postulate but emerges automatically from compact topology plus the CR-conditions of Chapter 13, and that the character variety Char(T²) is itself a torus. Two physically significant consequences follow: electric charge is the relative orientation of the double rotation on T² and is therefore topologically quantized, and the two energy formulas E = mc² and E = ℏω are the same spectral invariant viewed from mass-stiffness and frequency-circulation perspectives respectively—a duality secured by the Hodge/Addressability guarantee of Book III.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D32 — Character*. Homomorphism χ: π₁(X) → U(1); on T² labeled by (m, n) ∈ ℤ × ℤ.
- **Definitions / Axioms:** *IV.D33 — Geometric Charge*. Electric charge determined by relative orientation of the two fundamental T² rotations (poloidal vs toroidal); charge sign is geometric, not carried as an intrinsic property.
- **Definitions / Axioms:** *IV.D34 — Physical Character*. Character satisfying CR-conditions, parity constraint m + n ≡ 0 (mod 2), coupling constraint via ι_τ = 2/(π + e), and stability under the background expansion flow.
- **Key results:** *IV.T03 — Character Variety* (established): Char(T²) ≅ T²; the set of all characters on T² is itself a torus.
- **Key results:** *IV.P02 — Automatic Quantization* (τ-effective): physical characters form a discrete set Λ_CR ⊂ ℤ × ℤ as a consequence of CR-conditions and compact topology; discreteness is derived, not postulated.
- **Key results:** *IV.P03 — Energy Duality* (τ-effective): E = mc² (T² stiffness) and E = ℏω (τ¹ character circulation frequency) are the same holomorphic invariant viewed from two spectral representations.
- **Key results:** *IV.P04 — Quasi-Ergodic Coverage* (τ-effective): double rotation on T² with coupling ι_τ = 2/(π + e) produces pseudo-dense torus coverage without exact repetition, explaining why the neutron has no visible substructure.
- **Dependencies:** Chapter 13 (CR-address space, parity constraint, CR-admissible sublattice); Book III III.T28 (Hodge/Addressability, guaranteeing finite NF-addressability of every quantum character).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 15 uses the character modes established here as the orthonormal basis for the holomorphic Hilbert space H_τ, deriving Hilbert space from geometry rather than postulating it.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part02/ch14-characters-quantum-addresses.tex -->
