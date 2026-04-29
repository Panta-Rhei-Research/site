---
layout: "corpus-monograph-chapter"
title: "Chapter 13: The CR Address Space"
permalink: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-13-the-cr-address-space/"
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
chapter_number: 13
chapter_slug: "chapter-13-the-cr-address-space"
page_in_book: 69
prev_chapter_url: "/corpus/monographs/book-iv/part-01-the-joint-core-from-neutron-to-hydrogen/chapter-12-hydrogen-the-first-atom/"
prev_chapter_title: "Chapter 12: Hydrogen: The First Atom"
next_chapter_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-14-characters-as-quantum-addresses/"
next_chapter_title: "Chapter 14: Characters as Quantum Addresses"
summary_short: "The substrate τ³ is not merely a topological space—it carries a Cauchy–Riemann structure that makes holomorphic analysis possible. This CR-structure is…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
canonical_part_title: "Quantum Mechanics as Address Obstruction"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-13-the-cr-address-space/"
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

The substrate τ³ carries a Cauchy–Riemann structure that makes holomorphic analysis possible, and that structure is where quantum mechanics originates. A CR-manifold is a real manifold equipped with a horizontal distribution H ⊆ TM and a complex structure J: H → H satisfying J² = −id; τ³ instantiates this pattern exactly, with the T² torus fiber providing the horizontal distribution and the τ¹ worldline direction remaining "real." The CR-structure forces coupling between these two components: any configuration that claims to be holomorphic must have its torus behavior compatible with its worldline behavior. This compatibility requirement is not a mathematical technicality—it is the geometric origin of quantum constraints. We show that only character modes with m + n even survive the resulting holonomy condition (the CR parity constraint), cutting the admissible mode lattice Λ_CR to half the density of ℤ², and that the same CR-geometry naturally produces spin-½ representations through the SU(2) double cover of SO(3).

## What this chapter contributes

- **Definitions / Axioms:** *IV.D26 — CR-Manifold*. Real manifold with horizontal distribution H and complex structure J satisfying integrability.
- **Definitions / Axioms:** *IV.D27 — CR-Structure on τ³*. Horizontal distribution from T², complex structure J, complementary τ¹ direction; shown integrable.
- **Definitions / Axioms:** *IV.D28 — Four-Layer Architecture*. Combinatorics → polar Euclidean → complex plane → holomorphy; establishes that the complex plane is a derived, not primitive, layer.
- **Definitions / Axioms:** *IV.D29 — CR-Function*. Solution of ∂̄_b f = 0; holomorphic along T² fiber with τ¹-compatible variation.
- **Definitions / Axioms:** *IV.D30 — Character Modes*. χ_{m,n}(θ_γ, θ_η) = exp(i(mθ_γ + nθ_η)) on the lemniscate 𝕃.
- **Definitions / Axioms:** *IV.D31 — CR-Admissible Sublattice*. Λ_CR = {(m,n) ∈ ℤ² : m + n ≡ 0 (mod 2)}, a checkerboard sublattice of density 1/2.
- **Key results:** *IV.T01 — CR Parity Constraint* (τ-effective): only character modes with m + n even are CR-admissible on τ³; proved from holonomy (−1)^{m+n} = 1 around the lemniscate wedge.
- **Key results:** *IV.P01 — Energy as CR-Tension* (τ-effective): energy is the holomorphic coherence budget required to maintain CR-consistency between a configuration's T² torus shape and its τ¹ character motion.
- **Key results:** *IV.T02 — Emergence of Spin-½* (τ-effective): the CR-structure on τ³ naturally produces spin-½; a 2π physical rotation induces a 4π rotation of the internal character phase, giving the SU(2) double cover of SO(3).
- **Dependencies:** none — foundational for Part II.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 14 uses the CR-admissible sublattice established here to show that characters on 𝕃 are discrete quantum addresses, making the ℤ × ℤ structure of T² identical to quantization without additional postulates. The parity constraint propagates through all subsequent chapters of Part II.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part02/ch13-cr-address-space.tex -->
