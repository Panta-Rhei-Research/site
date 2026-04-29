---
layout: "corpus-monograph-chapter"
title: "Chapter 19: Betweenness from Ultrametric"
permalink: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-19-betweenness-from-ultrametric/"
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
chapter_number: 19
chapter_slug: "chapter-19-betweenness-from-ultrametric"
page_in_book: 89
prev_chapter_url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/chapter-18-connectivity-via-coherence-the-two-readout-principle/"
prev_chapter_title: "Chapter 18: Connectivity via Coherence: The Two-Readout Principle"
next_chapter_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/chapter-20-congruence-from-canonical-distance/"
next_chapter_title: "Chapter 20: Congruence from Canonical Distance"
summary_short: "Tarski's axiomatization of Euclidean geometry rests on two primitive relations — betweenness and congruence — both assumed as undefined in classical treatments. In Category τ, betweenness is *derived* from the ultrametric distance and *proved* to satisfy axioms T1–T3."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-04-geometry-the-tarski-program/"
canonical_part_title: "Geometry: The Tarski Program"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-04-geometry-the-tarski-program/chapter-19-betweenness-from-ultrametric/"
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

Tarski's 1959 axiomatization of Euclidean geometry rests on two primitive relations — **betweenness** and **congruence** — which classical treatments *assume* as undefined. Part IV opens by doing something different: it *derives* betweenness from the ultrametric distance d(x,y) = 2^{−δ(x,y)} already present in τ³, then *proves* that the derived relation satisfies all three of Tarski's betweenness axioms T1–T3. The key definition (*II.D19*) reads: y is between x and z when d(x,z) = max(d(x,y), d(y,z)), or equivalently, δ(x,z) = min(δ(x,y), δ(y,z)). In the primorial tower, this means y agrees with both endpoints to at least the depth at which x and z first disagree — betweenness is a depth-of-agreement condition, not a spatial one. Every step from CRT reductions through first disagreement depth to this definition is forced; no geometric intuition is imported.

## What this chapter contributes

The chapter registers two new entries. Definition *II.D19* gives the betweenness relation on τ³ in terms of the ultrametric distance (*II.D13*). Theorem *II.T15* then verifies the three Tarski betweenness axioms: T1 (identity — B(x,y,x) implies x = y), T2 (transitivity — B(x,y,z) and B(y,z,w) imply B(x,y,w)), and T3 (connectivity — for any triple, at least one of the three betweenness arrangements holds). Each axiom is proved by a direct calculation with disagreement depths and the ultrametric triangle inequality (*II.T05*). No real numbers, no spatial embedding, and no geometric axioms are invoked. The proofs are finitary: betweenness is decidable at each finite stage k, and the passage to the profinite limit is covered by compactness (*II.T07*).

A notable strengthening over Tarski's original: his T3 requires the hypothesis of collinearity, but in the ultrametric *every* triple satisfies at least one betweenness relation. The isosceles property of ultrametric triangles — any triangle has its two longer sides equal — means no scalene triples exist to obstruct connectivity. Equilateral triples simultaneously satisfy all three betweenness orderings, a distinctly non-Euclidean feature of the tree structure underlying τ³.

## Lean coverage

Lean coverage: *BookII.Geometry.Betweenness* (planned). The decidability of betweenness — compute three pairwise depths, check one min-equality — makes the formalization straightforward once the ultrametric infrastructure (*II.D13*, *II.T05*) is in place. The three axiom proofs each reduce to a case analysis on depth orderings.

## Where this leads

*II.D19* and *II.T15* are the entry point of the Tarski program for Category τ. Chapter 20 earns congruence from the same canonical distance, completing the two primitive relations. Chapter 21 proves the Pasch axiom and the parallel postulate. With betweenness in hand, Part IV is committed to a specific logical plan: nine of Tarski's thirteen axioms will be theorems before the wave-causal structure of Chapter 22 adds dynamics, and the denotation bridge of Chapter 23 connects τ-geometry to classical ℝ⁴.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part04/ch18-betweenness.tex -->
