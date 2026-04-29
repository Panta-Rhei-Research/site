---
layout: "corpus-monograph-chapter"
title: "Chapter 33: Evolution Operator and Causal Arrow"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-33-evolution-operator-and-causal-arrow/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-local-hartogs-and-the-holomorphic-interior"
chapter_number: 33
chapter_slug: "chapter-33-evolution-operator-and-causal-arrow"
page_in_book: 163
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-32-mutual-determination-5-way-equivalence/"
prev_chapter_title: "Chapter 32: Mutual Determination (5-Way Equivalence)"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-34-composition-identity-associativity/"
next_chapter_title: "Chapter 34: Composition, Identity, Associativity"
summary_short: "Composing successive BndLift operators defines the evolution operator ε_{n→m}. The B/C asymmetry from Prime Polarity selects a unique forward direction — the causal arrow — earning time as a structural theorem."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-33-evolution-operator-and-causal-arrow/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VI: Local Hartogs and the Holomorphic Interior"
      url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 25
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

The Mutual Determination Theorem (*II.T27*) is a static result: it establishes that five descriptions of holomorphic data are equivalent but says nothing about how data changes as one moves through the primorial tower. This chapter adds dynamics. The primorial tower has a natural direction — the projection maps from finer to coarser stages — but BndLift goes the other way, from coarser to finer. This pair of directions is the structural seed of dynamics. Composing successive BndLift operators produces a propagation family indexed by stage pairs, and the B/C asymmetry from Prime Polarity (*I.T05*) selects a canonical forward direction among all possible directions of propagation. The selection is not a convention: it is forced by the fact that exponentiation (B-channel, γ-orbit) must precede tetration (C-channel, η-orbit) in the peel-off sequence — tetration requires exponentiation as input, establishing B ≺ C as a structural datum independent of any external choice.

## What this chapter contributes

- **Definitions:** *II.D37 — Evolution Operator*: ε_{n→m} = BndLift_{m−1} ∘ … ∘ BndLift_n maps Hol_n(τ³) → Hol_m(τ³) for m > n. It satisfies the semigroup property ε_{n→ℓ} = ε_{m→ℓ} ∘ ε_{n→m}, the identity ε_{n→n} = id, and bipolar splitting into independent e_+ and e_- components. It is not a group: there is no inverse, because projection from stage m to n loses the ℤ/p_{n+1}ℤ × … × ℤ/p_mℤ spectral data. *II.D38 — Causal Arrow*: the preferred direction in the primorial tower selected by the B/C asymmetry, with forward = increasing refinement depth and information created rather than destroyed.
- **Key results:** *II.T28 — B/C Asymmetry Implies Time*: the B/C asymmetry from Prime Polarity (*I.T05*) induces a canonical time-like direction on τ³. The proof covers (i) existence via the forward-directed semigroup action, (ii) structural origin via the exponent–tetration hierarchy in the ABCD chart, (iii) elliptic impossibility (jj² = −1 yields no real idempotents, no null cone, no B/C ordering), and (iv) compatibility with the wave equation's null characteristics from *II.D22*.
- **Structural results:** ω-germ transport is well-defined on equivalence classes; refinement is proved irreversible (ε_{n→m} is injective but not surjective); forward propagation decomposes sectorwise along the two characteristic families F(ξ) and G(ζ). The null cone (*II.D22*) plus the causal arrow (*II.D38*) together constitute the complete causal structure of τ³.
- **Dependencies:** *I.T05*, *I.D21*, *I.T10*, *I.P02*, *II.D21*, *II.D22*, *II.D35*, *II.D36*, *II.T27*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Hartogs.EvolutionOperator` is planned.

## Where this leads

Chapter 34 uses the evolution operator's semigroup structure as input for verifying that ω-germ transformers form a category: associativity of holomorphic composition lifts from the program monoid associativity (*I.P02*) through tower coherence. In Book IV the algebraic causal arrow becomes physical time, the evolution operator becomes the quantum time-evolution operator, and B/C asymmetry becomes CPT structure.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch32-evolution-operator.tex -->
