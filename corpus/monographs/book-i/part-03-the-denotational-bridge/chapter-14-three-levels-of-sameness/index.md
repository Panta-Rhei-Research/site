---
layout: "corpus-monograph-chapter"
title: "Chapter 14: Three Levels of Sameness"
permalink: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-14-three-levels-of-sameness/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 3
part_display: "Part III"
part_slug: "part-03-the-denotational-bridge"
chapter_number: 14
chapter_slug: "chapter-14-three-levels-of-sameness"
page_in_book: 57
prev_chapter_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-13-the-program-monoid-composition-as-a-theorem/"
prev_chapter_title: "Chapter 13: The Program Monoid — Composition as a Theorem"
next_chapter_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-15-the-denotational-order-and-the-road-ahead/"
next_chapter_title: "Chapter 15: The Denotational Order and the Road Ahead"
summary_short: "tau has a stratified, decidable equality hierarchy: ontic identity (seed and depth), address equivalence (program NF), and shadow equality (ABCD coordinates)."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/"
canonical_part_title: "The Denotational Bridge"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-03-the-denotational-bridge/chapter-14-three-levels-of-sameness/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part III: The Denotational Bridge"
      url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part III"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 4
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

In standard mathematics, equality is monolithic: two objects are either equal or not, and the notion is not generally decidable (e.g., equality of real numbers). In τ, the ontic/denotational boundary induces a *hierarchy* of sameness. Because τ distinguishes objects (ontic layer) from their descriptions (denotational layer), the question "are these the same?" has three meaningfully different answers depending on what "same" means. The chapter formalizes all three levels: *ontic identity* at the deepest level (same seed and depth — the primitive, decidable notion), *address equivalence* at the middle level (same program normal form — derived from NF-Confluence, decidable), and *shadow equality* at the outermost level (same ABCD coordinates — derived from the Hyperfactorization Theorem, decidable). All three levels are decidable in τ, a feature of the countable, finitely generated universe that has no analogue in classical mathematics.

## What this chapter contributes

- Defines *I.D15* (Three-Level Equality): all three notions in a single registry entry — ontic identity =_{ont}, address equivalence ≡_{addr}, shadow equality ~_{sh}.
- Characterizes Level 1 (Ontic Identity): x =_{ont} y iff seed(x) = seed(y) and depth(x) = depth(y). This is the primitive ground truth. When "=" is written without qualification, it means =_{ont}.
- Characterizes Level 2 (Address Equivalence): P ≡_{addr} Q iff NF(P) = NF(Q), equivalently P(x) =_{ont} Q(x) for all x. Decidable by the NF-Confluence Lemma (Chapter 13). A concrete example: 2̲ × 3̲ and 3̲ × 2̲ are different programs but address-equivalent, both yielding 6̲.
- Characterizes Level 3 (Shadow Equality): x ~_{sh} y iff Φ(x) = Φ(y), where Φ is the ABCD coordinate map. Decidable once the ABCD chart is available (Part IV). Notes the key open question: the Hyperfactorization Theorem (Part V) will prove ~_{sh} implies =_{ont}, making the coordinate system faithful.
- Tabulates the three levels with their deciding procedures and notes the contrast with ZFC extensional equality (single notion, not generally decidable).
- Lean coverage: `TauLib.BookI.Denotation.Equality` (`ontic_eq`, `addr_equiv`, `addr_equiv_refl/symm/trans`, `shadow_eq`, `shadow_implies_ontic`). All proofs compile without `sorry`.

## Lean coverage

`TauLib.BookI.Denotation.Equality`

## Where this leads

Chapter 15 assembles the denotational order — extending the generator ordering K1 to a well-ordering on all of Obj(τ) with order type ω·4+1 — and surveys the road ahead through Parts IV–XV, showing how every subsequent result traces back to the six axioms K1–K6 and the single operator ρ. The three-level equality hierarchy established here also underpins the Hyperfactorization Theorem of Part V: shadow equality implies ontic identity, making the ABCD coordinate chart a faithful coordinate system rather than merely a total map.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part03/ch14-three-equality.tex -->
