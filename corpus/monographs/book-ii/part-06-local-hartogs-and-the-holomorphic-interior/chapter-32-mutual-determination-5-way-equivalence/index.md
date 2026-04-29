---
layout: "corpus-monograph-chapter"
title: "Chapter 32: Mutual Determination (5-Way Equivalence)"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-32-mutual-determination-5-way-equivalence/"
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
chapter_number: 32
chapter_slug: "chapter-32-mutual-determination-5-way-equivalence"
page_in_book: 157
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-31-the-bndlift/"
prev_chapter_title: "Chapter 31: The BndLift"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-33-evolution-operator-and-causal-arrow/"
next_chapter_title: "Chapter 33: Evolution Operator and Causal Arrow"
summary_short: "Five apparently distinct descriptions of a holomorphic datum on τ³ — refinement tail, spectral tail, ω-germ, boundary character, Hartogs continuation — are proved canonically equivalent by II.T27."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-32-mutual-determination-5-way-equivalence/"
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

Parts I–V generated five distinct languages for holomorphic data on τ³: tower-coherent sequences, spectral decompositions, ω-germs at the profinite limit, boundary characters on the boundary ring, and Hartogs continuations via BndLift. Each language arose in a different context and appears to capture different information. This chapter proves they are the same thing, linked by a chain of four pairwise equivalences. The key structural fact enabling the proof is one algebraic identity: 1 = e_+ + e_-, the bipolar idempotent decomposition forced by j² = +1. Every description of holomorphic data splits along this decomposition into two one-dimensional real channels — and in one dimension, there is only one way to encode data. The five descriptions therefore agree channel by channel, and the whole chain collapses into a single equivalence class.

## What this chapter contributes

- **Key results:** *II.T27 — Mutual Determination Theorem*: the five descriptions (R) refinement tail, (S) spectral tail, (G) ω-germ, (C) boundary character, (H) Hartogs continuation are canonically equivalent via the chain (R) ⟺ (S) ⟺ (G) ⟺ (C) ⟺ (H). Each description determines all four others uniquely. The unifying mechanism is the bipolar idempotent decomposition 1 = e_+ + e_-: every description splits into two one-dimensional channels that independently determine each other.
- **Key results — lemma chain:** *II.L02* (Refinement ⟺ Spectral): tower-coherent sequences biject with stabilized spectral decompositions via DFT on CRT factors. *II.L03* (Spectral ⟺ ω-germ): stabilized spectral data biject with ω-germs via profinite limits. *II.L04* (ω-germ ⟺ Character): ω-germs biject with boundary characters via evaluation on R_τ. *II.L05* (Character ⟺ Hartogs): boundary characters biject with Hartogs continuations via iterated *BndLift_n*.
- **Structural consequences:** holomorphic data is finitely determined (finite spectral support at each stabilization stage); boundary determines interior uniquely (holographic principle as a theorem, not a conjecture); two channels suffice (bipolar independence encodes all holomorphic information). The equivalence fails for elliptic ℂ because j² = −1 yields no real idempotents and no bipolar channel structure.
- **Dependencies:** *I.D20*, *I.D21*, *I.T05*, *I.T10*, *I.P02*, *I.T18*, *II.D14*, *II.D32*, *II.D33*, *II.D35*, *II.D36*, *II.T25*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Hartogs.MutualDetermination` is planned.

## Where this leads

*II.T27* is the algebraic engine behind the Central Theorem O(τ³) ≅ A_spec(𝕃) proved in Part IX. Without it, the identification of interior holomorphic data with boundary spectral data has no foundation. Chapter 33 uses the (G) description to add dynamics — constructing the evolution operator from successive BndLifts and deriving the causal arrow from the B/C asymmetry.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch31-mutual-determination.tex -->
