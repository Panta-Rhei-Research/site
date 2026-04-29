---
layout: "corpus-monograph-chapter"
title: "Chapter 49: Hartogs Extension in H_τ"
permalink: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/"
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
chapter_number: 49
chapter_slug: "chapter-49-hartogs-extension-in-h-tau"
page_in_book: 287
prev_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-48-boundary-characters-via-idempotent-support/"
prev_chapter_title: "Chapter 48: Boundary Characters via Idempotent Support"
next_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-50-extensions-are-omega-germ-transformers/"
next_chapter_title: "Chapter 50: Extensions Are ω-Germ Transformers"
summary_short: "Each idempotent-supported boundary character extends uniquely into the interior of τ³ via the BndLift operator; uniqueness follows from Code/Decode and Mutual Determination independently."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/"
canonical_part_title: "The Central Theorem and Categoricity"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/"
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

Chapter 48 organized every spectral character as an idempotent-supported object with canonical decomposition χ = e₊·χ₊ + e₋·χ₋. This chapter proves that each such character extends uniquely to the interior of τ³ as a τ-holomorphic function valued in the split-complex codomain H_τ — not classical ℂ. The construction proceeds in two stages: the Extension Lemma *II.L12* builds the extension channel-by-channel using the BndLift operator *II.D36* from Part VI, and then the Hartogs Extension Uniqueness Theorem *II.T37* proves that the extended function is the only one whose boundary restriction coincides with χ. Uniqueness is established via two independent arguments — the Code/Decode bijection *II.T35* and, more illuminatingly, the Mutual Determination Theorem *II.T27* — both of which exploit bipolar channel independence: the B-channel and C-channel extensions are each determined separately by their boundary data with no room for an alternative. The map Φ: A_spec(𝕃) → 𝒪(τ³) sending characters to their Hartogs extensions is injective; this chapter establishes the boundary→interior direction of the Central Theorem.

## What this chapter contributes

*Definitions:* No new registry definitions; the chapter deploys BndLift *II.D36* in the character context.

*Key results:* *II.T37* (Hartogs Extension in H_τ: every idempotent-supported boundary character extends uniquely to a τ-holomorphic function on τ³; the extension map Φ is injective), *II.L12* (Extension Lemma: channel-by-channel construction of the Hartogs extension via BndLift, with explicit stagewise formula at each primorial level k).

*Notation:* Φ: A_spec(𝕃) → 𝒪(τ³) for the extension map; BndLift for the boundary-to-interior lifting operator *II.D36*.

*Dependencies:*
- Boundary characters *II.D59* and character decomposition *II.P14* from Chapter 48
- BndLift operator *II.D36* from Part VI
- Code/Decode bijection *II.T35* from Part VII
- Mutual Determination Theorem *II.T27* from Part VII
- Idempotent Decomposition Lemma *II.L07* from Part VII

## Lean coverage

Module `BookII.CentralTheorem.HartogsExtension`. Key declarations: `extension_lemma` (*II.L12*: BndLift channel construction), `hartogs_uniqueness` (*II.T37*: the extended function is unique), `phi_injective` (Φ: A_spec(𝕃) → 𝒪(τ³) is injective), `two_proofs_uniqueness` (Code/Decode and Mutual Determination both witness uniqueness independently). All sorry-free; injectivity reduces to channel independence plus Code/Decode bijectivity.

## Where this leads

The injective leg Φ is now established. Chapter 50 reinterprets Hartogs extensions as regular ω-germ transformers, and Chapter 51 uses Yoneda to identify ω-germ transformers with holomorphic functions, closing the loop for the full isomorphism in Chapter 52.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part09/ch48-hartogs-extension-h-tau.tex -->
