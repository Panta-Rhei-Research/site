---
layout: "corpus-monograph-chapter"
title: "Chapter 107: The Self as Story Functor"
permalink: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/chapter-107-the-self-as-story-functor/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-categorical-mind-consciousness"
chapter_number: 107
chapter_slug: "chapter-107-the-self-as-story-functor"
page_in_book: 380
prev_chapter_url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/chapter-106-minds-as-internal-topoi/"
prev_chapter_title: "Chapter 106: Minds as Internal Topoi"
next_chapter_url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/chapter-108-consciousness-as-global-section/"
next_chapter_title: "Chapter 108: Consciousness as Global Section"
summary_short: "The self is formalised as a story functor — a structure-preserving map from a category of lived episodes to the mind-topos — and personal identity over time is maintained precisely when the functor admits coherent natural revisions."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/"
canonical_part_title: "Categorical Mind & Consciousness"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-09-categorical-mind-consciousness/chapter-107-the-self-as-story-functor/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part IX: Categorical Mind & Consciousness"
      url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part IX"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 77
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Chapter 106 established that a mind is an internal topos 𝓜 — but the topos, by itself, does not pick out a subject. This chapter fills that gap by formalising the self as a story functor 𝒜 : Exp → 𝓜: a structure-preserving map from a category of lived episodes (objects = experienced events; morphisms = temporal, causal, and explanatory relations among them) into the mind-topos. Three positions in philosophy of mind are canvassed — substance self, bundle self, and narrative self — and the categorical approach refines the third: the "story" is not a metaphor but a functor, one that carries episodes and their relations into internal representations while maintaining a distinguished self-object 𝒮 to which self-attribution morphisms are anchored. The narrative genotype (the stable core of deep commitments invariant under admissible revisions) connects directly to the commitment register Reg_C: the deepest commitments are precisely the invariants of the story functor across all admissible natural transformations.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D83 — Story Functor* (τ-effective). A functor 𝒜 : Exp → 𝓜 satisfying object mapping, morphism mapping, and self-relevance conditions (i)–(iii).
- **Key results:** *VII.T40 — Narrative Identity as Functor*: personal identity over time holds when a coherent natural transformation η : 𝒜 ⇒ 𝒜' exists connecting the earlier and later story functors; identity fragments when no such transformation exists; personal growth corresponds to a non-trivial but natural η.
- **Dependencies:** *VII.D82 — Mind as Internal Topos* (Chapter 106); commitment register Reg_C from Book VII Part I; no additional axioms.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The story functor definition and the Narrative Identity Theorem are stated in categorical prose and await Lean formalisation.

## Where this leads

The story functor grounds the self-object 𝒮 used in Chapter 111's self-recognition loop and in Chapter 113's address-persistence account of personal identity. The narrative genotype / phenotype distinction also supplies vocabulary for the commitment register discussion in Chapter 118.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part09/ch107.tex -->
