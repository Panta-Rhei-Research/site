---
layout: "corpus-monograph-chapter"
title: "Chapter 20: Congruence from Canonical Distance"
permalink: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-20-congruence-from-canonical-distance/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-geometry-the-tarski-program"
chapter_number: 20
chapter_slug: "chapter-20-congruence-from-canonical-distance"
page_in_book: 93
prev_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-19-betweenness-from-ultrametric/"
prev_chapter_title: "Chapter 19: Betweenness from Ultrametric"
next_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-21-pasch-and-the-parallel-postulate/"
next_chapter_title: "Chapter 21: Pasch and the Parallel Postulate"
summary_short: "Chapter 19 earned betweenness from the ultrametric ordering. This chapter earns **congruence** from the same canonical distance, then verifies all six Tarski congruence axioms C1–C6 — bringing the total to nine of Tarski's thirteen axioms proved as theorems in τ."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
canonical_part_title: "Geometry: The Tarski Program"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-04-geometry-the-tarski-program/chapter-20-congruence-from-canonical-distance/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part IV: Geometry: The Tarski Program"
      url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part IV"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 23
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapter 19 earned betweenness as a theorem from the ultrametric ordering on CRT prefixes. This chapter earns the second Tarski primitive — **congruence** — from the *same* canonical distance d(x,y) = 2^{−δ(x,y)} (*II.D13*). The definition (*II.D20*) is direct: segment AB is congruent to segment CD when d(A,B) = d(C,D), or equivalently when δ(A,B) = δ(C,D). Congruence is a depth-equality condition — two segments are the same length precisely when their endpoints first disagree at the same stage of the primorial tower. The base of the exponential is irrelevant: λ^{−a} = λ^{−b} for any λ > 1 if and only if a = b, so only the first disagreement depth matters, and that depth is forced by the CRT tower with no choices. One canonical distance yields both Tarski primitives.

## What this chapter contributes

Definition *II.D20* registers congruence. Theorem *II.T16* verifies all six Tarski congruence axioms. Axioms C1–C3 (reflexivity, identity of congruence, transitivity) hold in any metric space and follow immediately from the symmetry and identity-of-indiscernibles properties of d. The structural weight falls on C4–C6. C4 (segment construction: given any segment and ray, a congruent copy can be laid off) uses the surjectivity of CRT fiber maps — for each target depth m there exist points at exactly that distance, because the stage-(m+1) fibers over any stage-m residue always branch. C5 (the five-segment axiom, Tarski's version of SAS) and C6 (inner transitivity) both exploit the isosceles triangle property of ultrametric spaces: every ultrametric triangle has its two longer sides equal, forcing depth configurations that are uniquely determined by four depth values. Together T1–T3 (*II.T15*) and C1–C6 (*II.T16*) account for nine of Tarski's thirteen axioms — all proved as theorems in τ with no geometric import.

The philosophical inversion is worth marking: the axioms C1–C6 are first-order statements about the existence and equality of distances. They require neither a continuous metric nor an Archimedean field. A non-Archimedean base — all triangles isosceles, distances discrete — is fully sufficient. Euclidean congruence emerges from a structure that looks nothing like Euclidean space.

## Lean coverage

Lean coverage: *TauLib.BookII.Geometry.Congruence* (planned). C1–C3 formalize directly from metric axioms. C4 depends on the branching lemma for CRT fibers (Book I). C5–C6 require the isosceles triangle property already needed for the betweenness axioms.

## Where this leads

With nine axioms verified, Chapter 21 turns to the two structurally harder ones — Pasch and the parallel postulate — which make Tarski's system specifically Euclidean rather than merely absolute. After Chapter 21 completes the Tarski program, Chapter 22 adds dynamics via the split-complex wave equation, and Chapter 23 constructs the denotation bridge that translates all τ-internal Euclidean geometry into classical ℝ⁴.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part04/ch19-congruence.tex -->
