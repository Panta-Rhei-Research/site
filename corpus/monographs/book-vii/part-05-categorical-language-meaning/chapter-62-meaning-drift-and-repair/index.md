---
layout: "corpus-monograph-chapter"
title: "Chapter 62: Meaning Drift and Repair"
permalink: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-62-meaning-drift-and-repair/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-categorical-language-meaning"
chapter_number: 62
chapter_slug: "chapter-62-meaning-drift-and-repair"
page_in_book: 233
prev_chapter_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-61-translation-and-universality/"
prev_chapter_title: "Chapter 61: Translation and Universality"
next_chapter_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/chapter-63-public-language-and-law/"
next_chapter_title: "Chapter 63: Public Language and Law"
summary_short: "Semantic drift is formalized as perturbation of the natural transformation η_t : Φ_t ⇒ Φ_{t+Δt} between time-indexed readout functors. Drift is gradual and accumulates; the kernel is rigid while the readout functor is not. Repair mechanisms—dictionaries, institutions, normative correction—are gluing-condition enforcement that constrains the functor against perturbation."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/"
canonical_part_title: "Categorical Language & Meaning"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-05-categorical-language-meaning/chapter-62-meaning-drift-and-repair/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part V: Categorical Language & Meaning"
      url: "/corpus/monographs/book-vii/part-05-categorical-language-meaning/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part V"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 73
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Meanings are not fixed. The English "nice" once meant "ignorant"; "awful" once meant "inspiring awe"; "silly" once meant "blessed." These are not isolated curiosities but instances of a systematic process amenable to structural analysis. This chapter models semantic drift as perturbation of the natural transformation η_t : Φ_t ⇒ Φ_{t+Δt} between the readout functors of successive historical epochs. Drift is quantified as drift(w, Δt) = d(ref_t(w), ref_{t+Δt}(w)), a metric distance between the kernel positions addressed by the same word at two times. Two structural causes are identified: the readout functor is learned rather than innate (each generation acquires it from usage, not from direct kernel access, so copying errors accumulate), and the carrier has its own phonological, morphological, and syntactic dynamics that exert independent pressure. Five recurrent mechanisms of semantic change are characterized as perturbation types: metaphor extension (exploiting a structural morphism k → k' in Kern), generalization and narrowing (relaxation or tightening of the reference morphism's specificity), and amelioration and pejoration (migration to kernel positions of higher or lower evaluative valence). Repair mechanisms counteract drift: dictionaries are sections of the readout functor (partial inverses recording intended kernel positions); legal, scientific, and educational institutions enforce gluing conditions (ensuring that local readout functors agree on overlaps); and everyday normative corrections are distributed gluing-condition checks. Some drift is irreversible: when the accumulated perturbation moves the current carrier-level expression beyond reach of the old kernel position, repair is no longer possible. The fundamental asymmetry is: the kernel is rigid (determined by the axioms of Category τ); the readout functor is not. Language is a living map from a fixed structure to a changing carrier.

## What this chapter contributes

- **Definitions / Axioms:** none introduced as stand-alone definitions; the chapter applies natural-transformation perturbation to the diachronic readout functor.
- **Key results:** *VII.R26 — Meaning Drift as Perturbation* (τ-effective): the perturbation η_t : Φ_t ⇒ Φ_{t+Δt} has three structural features—graduality (small drift per time step), accumulation (large total drift over many steps), and non-rigidity (η_t ≠ id in general).
- **Dependencies:** readout-functor framework; *VII.D52* (subsymbolic presheaf, Chapter 55); translation losses as non-extendable local sections (Chapter 61); gluing condition (Part II).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. Remark VII.R26 is developed textually; a formalization of time-indexed readout functors and their perturbation metrics is planned.

## Where this leads

The analysis of repair mechanisms as gluing-condition enforcement leads directly into Chapter 63, where public language and legal language are examined as institutional systems for coordinating and stabilizing the readout functor across a community of speakers.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part05/ch62.tex -->
