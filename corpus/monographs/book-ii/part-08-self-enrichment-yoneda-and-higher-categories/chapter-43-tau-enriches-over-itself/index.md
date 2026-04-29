---
layout: "corpus-monograph-chapter"
title: "Chapter 43: τ Enriches Over Itself"
permalink: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-43-tau-enriches-over-itself/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 8
part_display: "Part VIII"
part_slug: "part-08-self-enrichment-yoneda-and-higher-categories"
chapter_number: 43
chapter_slug: "chapter-43-tau-enriches-over-itself"
page_in_book: 237
prev_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-42-code-decode-and-diagonal-protection/"
prev_chapter_title: "Chapter 42: Code/Decode and Diagonal Protection"
next_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
next_chapter_title: "Chapter 44: Yoneda Embedding as Theorem"
summary_short: "τ enriches over itself: every morphism space Hom(A,B) is a τ-object with NF-address, split-complex values, and bipolar decomposition inherited from the primorial tower."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/"
canonical_part_title: "Self-Enrichment, Yoneda, and Higher Categories"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-43-tau-enriches-over-itself/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
      url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VIII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 27
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

In most categories, morphism spaces are external: Hom(A,B) is a set living in Set rather than in the category under study. An enriched category replaces these external sets with internal Hom objects that are themselves objects of the category. This chapter proves that Category τ enriches over itself: for any two objects A, B ∈ Obj(τ), the morphism space Hom_τ(A,B) is itself a τ-object with an NF-address, split-complex values, and tower-coherent structure inherited from the primorial tower ℤ/P_kℤ. The proof proceeds stagewise — defining [A,B]_k = Hom(A_k, B_k) at each primorial level and showing these stages cohere under the inverse limit — then invokes the Idempotent Decomposition Lemma to establish the bipolar splitting of every Hom object.

## What this chapter contributes

*Definitions:* *II.D53* (τ is self-enriched: composition and identity maps are τ-morphisms), *II.D54* (Hom object [A,B] as the τ-holomorphic function space with stagewise tower-coherence [A,B]_k = Hom(A_k, B_k)).

*Key results:* *II.P11* (Bipolar Hom Decomposition: [A,B] = e₊·[A,B]₊ + e₋·[A,B]₋, because holomorphic maps between τ-objects are themselves holomorphic objects and the Idempotent Decomposition Lemma *II.L07* applies at the level of morphism spaces).

*Notation:* e₊ = (1+j)/2 and e₋ = (1−j)/2 for the bipolar idempotents from *I.D21*; [A,B] for internal Hom objects.

*Dependencies:*
- Bipolar idempotents e± from *I.D21* and holomorphic maps in H_τ (j²=+1 codomain)
- Pre-Yoneda embedding *II.D50*: holomorphic functions are objects, so function spaces are objects
- Idempotent Decomposition Lemma *II.L07* applied at the morphism-space level
- Primorial tower coherence and inverse limit construction from Part I

## Lean coverage

Module `BookII.SelfEnrichment.TauEnrichesOverItself`. Key declarations: `tau_self_enriched` (instance of enriched category structure on τ), `hom_object_bipolar` (the bipolar decomposition *II.P11* for internal Hom objects), `stagewise_coherence` (tower coherence of [A,B]_k under CRT reduction maps). All sorry-free; the bipolar splitting reduces to *II.L07* applied fiberwise.

## Where this leads

Self-enrichment is the structural prerequisite for the Yoneda embedding theorem: once Hom spaces are internal objects, functors into them become morphisms in τ, enabling the identification of probe naturality with holomorphy. Chapter 44 lifts this to the full Yoneda theorem *II.T36*, and Chapter 45 iterates the enrichment to build the strict 2-category τ₂.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part08/ch42-tau-self-enrichment.tex -->
