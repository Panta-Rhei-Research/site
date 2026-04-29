---
layout: "corpus-monograph-chapter"
title: "Chapter 41: Pre-Yoneda Embedding"
permalink: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-41-pre-yoneda-embedding/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-regularity-and-mutual-determination"
chapter_number: 41
chapter_slug: "chapter-41-pre-yoneda-embedding"
page_in_book: 219
prev_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-40-regularity-as-positive-structure/"
prev_chapter_title: "Chapter 40: Regularity as Positive Structure"
next_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-42-code-decode-and-diagonal-protection/"
next_chapter_title: "Chapter 42: Code/Decode and Diagonal Protection"
summary_short: "Holomorphic functions on τ³ are themselves objects of τ³: the function space Hol_τ(τ³, H_τ) embeds canonically into the ω-germ space d(τ³), preserving bipolar decomposition and regularity — a self-enrichment property with no classical analogue."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
canonical_part_title: "Regularity and Mutual Determination"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-41-pre-yoneda-embedding/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VII: Regularity and Mutual Determination"
      url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 26
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

This chapter establishes a phenomenon with no classical analogue: holomorphic functions on τ³ are **themselves objects** of τ³. In classical complex analysis, the space O(ℂ) of entire functions is an infinite-dimensional Fréchet space — its elements are functions, not points of ℂ. The function space and the base space live in entirely different mathematical universes. In Category τ, the situation is radically different. Every τ-holomorphic function f : τ³ → H_τ determines an ω-germ transformer G_f in the ω-germ space d(τ³), and d(τ³) carries the same algebraic structure as τ³: bipolar decomposition, CRT factorization, stagewise finite expansion. The function f is not just a map — it is also a datum in the same structural universe as the points it acts on. The *Pre-Yoneda Embedding* (*II.D50*) is the canonical injection y : Hol_τ(τ³, H_τ) → d(τ³) that realizes this self-referential property. The embedding draws on two sources. From Book I, the Presheaf Characterization (I.T40) established algebraically that τ-holomorphy is naturality of the staging tower plus sector independence under the bipolar idempotents — a characterization on finite cyclic groups, with no topology. From Part VII, the Idempotent Decomposition Lemma (II.L07) and the positive regularity criterion (II.T34) provide the functional analytic upgrades needed to lift the algebraic characterization to the full ω-germ level. *II.P10* (*Functions as Objects*) formalizes the embedding's structure-preservation: y commutes with bipolar decomposition (y(f)_± = y(f_±)), maps regular functions to regular ω-germs, and preserves the full ABCD coordinate structure. *II.R12* (*Probe Naturality = Holomorphy*) connects probe naturality to holomorphy: f is τ-holomorphic if and only if probing by cylinder inclusions ι : C_N(p) ↪ τ³ yields natural transformations in the staging variable N. This is the deep structural reason why self-enrichment (functions are objects) and the Yoneda lemma (functions determine objects uniquely) will follow in Part VIII — the "functor of points" construction does not require leaving the category, because holomorphic functions are already embedded as points.

## What this chapter contributes

**Definitions / Axioms**
- *II.D50* — Pre-Yoneda Embedding: the canonical injection y : Hol_τ(τ³, H_τ) → d(τ³), sending each holomorphic function to its associated ω-germ transformer in the germ space

**Key results**
- *II.P10* — *Functions as Objects*: y commutes with bipolar decomposition (y(f)_± = y(f_±)), maps τ-regular functions to regular ω-germs, preserves the ABCD coordinate structure; y is structure-preserving in a precise sense
- *II.R12* — *Probe Naturality = Holomorphy*: f is τ-holomorphic iff probing by cylinder inclusions yields natural transformations in the staging variable; this grounds the self-enrichment and Yoneda program of Part VIII

**Notation**
- d(τ³) for the ω-germ space; y for the Pre-Yoneda embedding; G_f ∈ d(τ³) for the ω-germ transformer associated to f

**Dependencies**
- *I.T40* (Presheaf Characterization), *I.T41* (Bi-Square Characterization), *II.L07* (Idempotent Decomposition), *II.T33* (Holomorphic ↔ Idempotent-Supported), *II.D49* (τ-Regularity), *II.T34* (Regularity Criterion), *II.D47*, *II.T32*

## Lean coverage

`BookII.Regularity.PreYoneda` (planned). No Lean proofs present at this writing.

## Where this leads

The Pre-Yoneda embedding (II.D50) is the structural precondition for the full Yoneda lemma in Part VIII: once holomorphic functions are shown to live inside the same structural universe as points, Part VIII can prove that every object is determined by its functor of points — a theorem, not an axiom, in the τ setting. The Code/Decode bijection of Chapter 42 provides the explicit dictionary through which the embedding operates.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part07/ch40-pre-yoneda.tex -->
