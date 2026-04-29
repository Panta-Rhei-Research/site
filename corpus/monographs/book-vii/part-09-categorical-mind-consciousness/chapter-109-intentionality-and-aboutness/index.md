---
layout: "corpus-monograph-chapter"
title: "Chapter 109: Intentionality and Aboutness"
permalink: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/chapter-109-intentionality-and-aboutness/"
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
chapter_number: 109
chapter_slug: "chapter-109-intentionality-and-aboutness"
page_in_book: 386
prev_chapter_url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/chapter-108-consciousness-as-global-section/"
prev_chapter_title: "Chapter 108: Consciousness as Global Section"
next_chapter_url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/chapter-110-qualia-and-subjective-experience/"
next_chapter_title: "Chapter 110: Qualia and Subjective Experience"
summary_short: "Intentionality is formalised as an aboutness morphism φ : R → O in the mind-topos, separating content (morphism structure) from reference (anchoring to external τ³ patterns) and dissolving the problems of non-existent objects and misrepresentation."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-09-categorical-mind-consciousness/"
canonical_part_title: "Categorical Mind & Consciousness"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-09-categorical-mind-consciousness/chapter-109-intentionality-and-aboutness/"
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

Mental states are directed: beliefs are about facts, desires are about goals, fears are about threats. This chapter formalises this directedness — Brentano's mark of the mental — as structure internal to the mind-topos. An aboutness morphism is an internal arrow φ : R → O from a representation type R to an intentional object O; its directional, compositional, and internally available character (conditions i–iii of Definition VII.D84) captures the pointing-at character of intentionality without positing a mysterious external relation. Content and reference are cleanly separated: content is the internal morphism structure of φ, while reference is settled by an anchoring map 𝓔 : 𝓜 → Sh(τ³) that assigns external patterns to some internal objects when such correspondence exists. With this separation, misrepresentation is straightforward (φ fixes what is about what; the anchoring assessment determines correctness), and thinking about non-existent objects — unicorns, round squares — is equally unproblematic: the intentional object O exists inside 𝓜 even when 𝓔(O) fails to exist in τ³.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D84 — Intentionality as Morphism* (τ-effective). An aboutness morphism φ : R → O in 𝓜, with directional structure, compositional closure, and internal availability; the anchoring map 𝓔 : 𝓜 → Sh(τ³) as a structure-preserving translation to external patterns.
- **Key results:** none in formal-derivation form; this chapter establishes Brentano's thesis reformulated in categorical language, the content/object distinction, the dissolution of non-existent-object and misrepresentation puzzles, a Fregean sense/reference treatment via distinct morphisms converging on one target, and the threading of intentionality across all four registers (Reg_D, Reg_E, Reg_P, Reg_C).
- **Dependencies:** *VII.D82 — Mind as Internal Topos* (Chapter 106); *VII.T41* (Chapter 108) for the relation of unconscious intentionality to the global section.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The Intentionality as Morphism definition and the anchoring map construction are formulated in mathematical prose and await Lean formalisation.

## Where this leads

The aboutness morphism framework provides the propositional-attitude vocabulary (belief, desire, intention) used in subsequent chapters, and the anchoring map connects internal content to external grounding — a distinction that resurfaces in Chapter 114's discussion of LLMs and world-anchoring.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part09/ch109.tex -->
