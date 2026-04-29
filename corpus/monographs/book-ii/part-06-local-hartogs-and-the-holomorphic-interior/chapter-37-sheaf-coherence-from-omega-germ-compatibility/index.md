---
layout: "corpus-monograph-chapter"
title: "Chapter 37: Sheaf Coherence from ω-Germ Compatibility"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-37-sheaf-coherence-from-omega-germ-compatibility/"
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
chapter_number: 37
chapter_slug: "chapter-37-sheaf-coherence-from-omega-germ-compatibility"
page_in_book: 187
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-36-the-canonical-holomorphic-basis-b/"
prev_chapter_title: "Chapter 36: The Canonical Holomorphic Basis B"
next_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-38-idempotent-decomposition-lemma/"
next_chapter_title: "Chapter 38: Idempotent Decomposition Lemma"
summary_short: "The holomorphic presheaf O_τ on cylinder domains satisfies both sheaf axioms (*II.T32*): locality from ultrametric separation, gluing from tower coherence — with no partition of unity and no analytic continuation required."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-37-sheaf-coherence-from-omega-germ-compatibility/"
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

A sheaf is a presheaf satisfying locality (a section vanishing on every element of a cover vanishes globally) and gluing (compatible local sections paste to a unique global section). Classical sheaf theory proves these axioms for holomorphic functions via analytic continuation and the identity theorem — both genuinely analytic arguments. In Category τ, the same axioms hold for a purely algebraic reason: cylinder domains are clopen in the ultrametric topology, so same-stage overlaps are either empty or identical, and gluing reduces to tower coherence with no interpolation needed.

## What this chapter contributes

- **Definitions:** *II.D47 — Holomorphic Presheaf* O_τ: assigns to each cylinder domain U the set of τ-holomorphic functions on U (satisfying all five conditions of *II.T27* restricted to U); restriction maps are ordinary function restriction. The presheaf axioms P1 (identity) and P2 (transitivity) are immediate.
- **Key results:** *II.T32 — Sheaf Axioms*: O_τ is a sheaf on the cylinder topology of τ³. Locality (S1): if f restricts to zero on every element of a cover, then f = 0 — proved by a pointwise argument needing only that the cover is exhaustive. Gluing (S2): given compatible local sections {f_i ∈ O_τ(U_i)}, there exists a unique f ∈ O_τ(U) restricting to f_i on each U_i. *II.L06 — Gluing Lemma*: the construction sets f(x) = f_i(x) for any i with x ∈ U_i (well-defined by compatibility), then verifies τ-holomorphicity using tower coherence and the key ultrametric fact that cylinder overlaps C_{k,a} ∩ C_{k,b} are either empty (a ≠ b) or identical (a = b) — no partial overlaps, no partition of unity.
- **Structural results:** the ω-germ reading translates sheaf compatibility into agreement of ω-germs on overlaps, a finite verification at each stage; local sections are uniquely described by their finite spectral support in B_τ (*II.T31*); transition functions between cylinder domains are trivial because the canonical basis is the same on every domain; sheaf cohomology H^q(C_{k,a}, O_τ) = 0 for q ≥ 1 on single cylinders (contractible clopen sets), with nontrivial cohomology a global-topology phenomenon reserved for Book III.
- **Dependencies:** *I.T10*, *I.T18*, *I.T36*, *I.D21*, *II.D10*, *II.D45*, *II.D46*, *II.T31*, *II.T27*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Holomorphy.SheafCoherence` is planned.

## Where this leads

The sheaf O_τ constructed here is the starting point for three developments in Book III: a de Rham-type cohomology adapted to the ultrametric setting, the relationship between H¹(τ³, O_τ) and spectral forces, and the connection to the Langlands program via automorphic sheaves. Part VI concludes by noting that the combination of split-complex codomain (j² = +1) and primorial tower domain is both necessary and sufficient for all six constructions of the part — calibration, BndLift, mutual determination, causal arrow, category, Laurent theory, canonical basis, and sheaf.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch36-sheaf-coherence.tex -->
