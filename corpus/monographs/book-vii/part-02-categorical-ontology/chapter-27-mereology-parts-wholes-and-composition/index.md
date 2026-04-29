---
layout: "corpus-monograph-chapter"
title: "Chapter 27: Mereology: Parts, Wholes, and Composition"
permalink: "/corpus/monographs/book-vii/part-02-categorical-ontology/chapter-27-mereology-parts-wholes-and-composition/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 2
part_display: "Part II"
part_slug: "part-02-categorical-ontology"
chapter_number: 27
chapter_slug: "chapter-27-mereology-parts-wholes-and-composition"
page_in_book: 108
prev_chapter_url: "/corpus/monographs/book-vii/part-02-categorical-ontology/chapter-26-being-becoming-and-change/"
prev_chapter_title: "Chapter 26: Being, Becoming, and Change"
next_chapter_url: "/corpus/monographs/book-vii/part-02-categorical-ontology/chapter-28-abstract-objects-and-structural-realism/"
next_chapter_title: "Chapter 28: Abstract Objects and Structural Realism"
summary_short: "Parts compose wholes when colimits exist. Mereological composition is categorical colimit: the whole is the universal construction that receives morphisms from…"
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-02-categorical-ontology/"
canonical_part_title: "Categorical Ontology"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-02-categorical-ontology/chapter-27-mereology-parts-wholes-and-composition/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part II: Categorical Ontology"
      url: "/corpus/monographs/book-vii/part-02-categorical-ontology/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part II"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 70
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

The Special Composition Question — when do parts compose a whole? — has resisted principled resolution in the literature, with classical extensional mereology generating ontological profligacy and restricted composition theories lacking principled criteria. Category τ provides a structural answer: composition is colimit. The Mereological Composition as Colimit definition (*VII.D35*) specifies that a diagram D: J → C of parts composes into a whole when the colimit ∫lim D exists in the admissible subcategory C, with three conditions: universal reception of coprojection morphisms from each part (MC1), compatibility with part-to-part relations (MC2), and universality as the tightest such construction through which all others factor (MC3). The whole is not the mere collection of parts but the construction determined by the parts together with their mutual relations; using a colimit rather than a coproduct is what encodes genuine interaction between parts. The Special Composition Answer (*VII.P07*) states that parts compose when and only when the colimit exists in the relevant admissible category — neither unrestricted (not every diagram has a colimit) nor arbitrary (existence is determined by the categorical structure, not philosophical fiat). Emergence is demystified structurally: a colimit can possess properties absent from every individual part's morphism profile when those properties arise from the relational pattern among parts rather than any single coprojection source. Both mereological universalism (colimits always exist) and nihilism (no non-trivial colimits) are shown to be artefacts of overly permissive or restrictive ambient categories.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D35 — Mereological Composition as Colimit* (τ-effective): three conditions MC1–MC3 (universal reception, compatibility, universality) identifying mereological wholes with categorical colimits.
- **Key results:** *VII.P07 — Special Composition Answer* (τ-effective): parts compose when and only when the colimit exists in the admissible category; existence criterion, uniqueness (exact in τ by rigidity), and sufficiency without further metaphysical criteria.
- **Notation introduced:** ∫lim D (colimit of diagram D); ι_j: D(j) → ∫lim D (coprojection morphisms).
- **Dependencies:** Standard category theory (colimits, universal properties); Chapter 16 (relational primacy — wholes are relational constructions, not substances); Chapter 18 (internal constructibility).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 28 extends the structural analysis to abstract objects, showing that mathematical entities are positions in structures rather than independently existing substances, and previewing the Non-Dualistic Platonism developed fully in Chapter 32.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part02/ch27.tex -->
