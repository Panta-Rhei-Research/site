---
layout: "corpus-monograph-chapter"
title: "Chapter 44: Yoneda Embedding as Theorem"
permalink: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
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
chapter_number: 44
chapter_slug: "chapter-44-yoneda-embedding-as-theorem"
page_in_book: 245
prev_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-43-tau-enriches-over-itself/"
prev_chapter_title: "Chapter 43: τ Enriches Over Itself"
next_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-45-2-categories-from-iterated-enrichment/"
next_chapter_title: "Chapter 45: 2-Categories from Iterated Enrichment"
summary_short: "The Yoneda embedding y: τ ↪ [τᵒᵖ,τ] is a theorem in Category τ, not an abstract generality: probe naturality, holomorphy, and Yoneda representability are proved to be identical."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/"
canonical_part_title: "Self-Enrichment, Yoneda, and Higher Categories"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
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

In classical category theory the Yoneda lemma holds for any locally small category — it is purely formal, requiring nothing about the objects or morphisms beyond their existence. In Category τ, the Yoneda embedding y: τ ↪ [τᵒᵖ, τ] is a theorem, not an abstract generality. Three features distinguish the τ-Yoneda from its classical cousin: the target functor category [τᵒᵖ, τ] lives inside τ itself via self-enrichment *II.D53* rather than in an external universe of sets; the embedding preserves the bipolar structure from *II.P11*; and fullness is witnessed by the Code/Decode bijection *II.T35*, which provides computable finite-stage certificates. The proof rests on identifying probe naturality — the condition that characterized holomorphy in Part II — with precisely the Yoneda naturality condition: a natural transformation between representable functors is exactly a holomorphic map.

## What this chapter contributes

*Definitions:* No new registry definitions in this chapter; the embedding itself is the main result.

*Key results:* *II.T36* (Yoneda Embedding Theorem: the functor y: τ → [τᵒᵖ, τ] is full, faithful, and holomorphic; CODE = Yoneda embedding; tau-exponential [A,–] is the representing object), *II.L11* (Probe-Yoneda Lemma: probe naturality is exactly the Yoneda condition, so holomorphy ⟺ probe naturality ⟺ Yoneda representability are three names for one structural phenomenon).

*Notation:* y(A) = Hom_τ(–, A) for the representable functor; [A,–] for the τ-exponential.

*Dependencies:*
- Self-enrichment *II.D53* and internal Hom objects *II.D54* from Chapter 43
- Code/Decode bijection *II.T35* from Part VII
- Probe naturality *II.R12* from Part II
- Pre-Yoneda embedding *II.D50* from Part VII

## Lean coverage

Module `BookII.SelfEnrichment.YonedaAsTheorem`. Key declarations: `yoneda_full_faithful` (fullness and faithfulness of y in τ), `probe_yoneda_lemma` (*II.L11*: probe naturality ↔ Yoneda condition), `code_eq_yoneda` (CODE is identified with the Yoneda embedding *II.T36*). All sorry-free; fullness reduces to Code/Decode surjectivity from *II.T35*.

## Where this leads

With the Yoneda embedding established as a theorem grounded in holomorphy rather than set-theoretic formalism, the framework is ready to iterate: Chapter 45 applies self-enrichment a second time to produce the strict 2-category τ₂, and Chapter 51 invokes Yoneda again to identify ω-germ transformers with holomorphic functions as the final step toward the Central Theorem.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part08/ch43-yoneda-theorem.tex -->
