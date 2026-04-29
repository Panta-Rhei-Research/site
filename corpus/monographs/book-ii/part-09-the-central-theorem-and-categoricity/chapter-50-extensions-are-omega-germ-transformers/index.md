---
layout: "corpus-monograph-chapter"
title: "Chapter 50: Extensions Are ω-Germ Transformers"
permalink: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-50-extensions-are-omega-germ-transformers/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-the-central-theorem-and-categoricity"
chapter_number: 50
chapter_slug: "chapter-50-extensions-are-omega-germ-transformers"
page_in_book: 295
prev_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/"
prev_chapter_title: "Chapter 49: Hartogs Extension in H_τ"
next_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-51-yoneda-applied-omega-germs-are-holomorphic-functions/"
next_chapter_title: "Chapter 51: Yoneda Applied — ω-Germs Are Holomorphic Functions"
summary_short: "Hartogs extensions are proved to be exactly the regular ω-germ transformers; stagewise naturality over the primorial tower establishes the canonical bijection, the second link in the Central Theorem chain."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/"
canonical_part_title: "The Central Theorem and Categoricity"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-09-the-central-theorem-and-categoricity/chapter-50-extensions-are-omega-germ-transformers/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part IX: The Central Theorem and Categoricity"
      url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part IX"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 28
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapter 49 proved that every idempotent-supported boundary character extends uniquely to a holomorphic function on τ³ valued in H_τ. This chapter proves that these Hartogs extensions are exactly the regular ω-germ transformers from Book I (*I.D45*–*I.D47*). The identification is not a metaphor: the extension f_χ of a boundary character χ determines, and is determined by, a unique element of End(d(τ³)), the endomorphism monoid of the ω-germ space. The key technical ingredient is Stagewise Naturality *II.L13*: because the boundary character is tower-coherent by construction, its Hartogs extension commutes with the CRT reduction maps at every stage of the primorial tower ℤ/P_kℤ. In the inverse limit, that coherent system of stage-k actions assembles into an ω-germ transformer. The converse direction — every regular ω-germ transformer arises from a Hartogs extension — closes the second link in the Central Theorem chain: boundary characters ↔ Hartogs extensions ↔ ω-germ transformers.

## What this chapter contributes

*Definitions:* No new registry definitions; this chapter establishes a canonical identification between objects already defined in Book I and Part IX.

*Key results:* *II.T38* (Extensions Are ω-Germ Transformers: canonical bijection between Hartogs extensions and regular ω-germ transformers in End(d(τ³))), *II.L13* (Stagewise Naturality: the Hartogs extension commutes with CRT reduction at every stage; the stage-k actions form a coherent inverse system yielding an ω-germ transformer in the limit).

*Notation:* End(d(τ³)) for the endomorphism monoid of the ω-germ space; ω-GT for the set of regular ω-germ transformers.

*Dependencies:*
- Hartogs Extension *II.T37* and Extension Lemma *II.L12* from Chapter 49
- ω-germ transformers *I.D45*–*I.D47* from Book I
- Primorial tower coherence and CRT reduction from Part I
- BndLift *II.D36* from Part VI

## Lean coverage

Module `BookII.CentralTheorem.ExtensionsOmegaGerms`. Key declarations: `stagewise_naturality` (*II.L13*: the Hartogs extension commutes with CRT reduction at each level k), `extensions_eq_omega_germs` (*II.T38*: the bijection between Hartogs extensions and regular ω-germ transformers), `canonical_basis` (ω-germ transformers are finitely presented via the canonical basis at each primorial stage). All sorry-free; the bijection reduces to the inverse limit construction applied to the stagewise naturality data.

## Where this leads

With ω-germ transformers identified as Hartogs extensions, Chapter 51 applies the Yoneda embedding *II.T36* to prove that ω-germ transformers are holomorphic functions, completing the three-way bijection and enabling Chapter 52 to assemble the full Central Theorem isomorphism.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part09/ch49-extensions-omega-germs.tex -->
