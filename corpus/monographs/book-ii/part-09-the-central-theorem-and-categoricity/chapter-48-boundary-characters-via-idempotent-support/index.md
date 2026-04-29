---
layout: "corpus-monograph-chapter"
title: "Chapter 48: Boundary Characters via Idempotent Support"
permalink: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-48-boundary-characters-via-idempotent-support/"
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
chapter_number: 48
chapter_slug: "chapter-48-boundary-characters-via-idempotent-support"
page_in_book: 279
prev_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-47-foundation-for-book-iii-s-self-enrichment-ladder/"
prev_chapter_title: "Chapter 47: Foundation for Book~III's Self-Enrichment Ladder"
next_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/"
next_chapter_title: "Chapter 49: Hartogs Extension in H_τ"
summary_short: "Every spectral character valued in H_τ decomposes uniquely as χ = e₊·χ₊ + e₋·χ₋; A_spec(𝕃) is exactly the algebra of idempotent-supported characters, setting up the Central Theorem input."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/"
canonical_part_title: "The Central Theorem and Categoricity"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-09-the-central-theorem-and-categoricity/chapter-48-boundary-characters-via-idempotent-support/"
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

Part IX opens by turning the Idempotent Decomposition Lemma *II.L07* inward onto the spectral characters themselves. Part VII showed that holomorphy is equivalent to idempotent support (*II.T33*): every holomorphic map f splits as f = e₊·f₊ + e₋·f₋. This chapter restates Book I's boundary ring ℤ_τ spectral characters (*I.D19*, *I.D22*–*I.D23*) in that language, proving that every spectral character valued in calibrated H_τ (*II.D35*) admits a unique canonical decomposition χ = e₊·χ₊ + e₋·χ₋. The character algebra A_spec(𝕃) is precisely the algebra of idempotent-supported characters — there are no others. The product decomposition A_spec(𝕃) ≅ A_spec(𝕃)₊ × A_spec(𝕃)₋ follows directly. This chapter organizes the input side of the Central Theorem: boundary characters fully structured by bipolar support, ready for the Hartogs extension in Chapter 49.

## What this chapter contributes

*Definitions:* *II.D59* (Boundary Characters: spectral characters χ: 𝕃 → H_τ valued in calibrated H_τ, organized by idempotent decomposition χ = e₊·χ₊ + e₋·χ₋).

*Key results:* *II.P14* (Character Decomposition: every spectral character valued in H_τ decomposes uniquely into bipolar components; A_spec(𝕃) is the full algebra of idempotent-supported characters; product decomposition A_spec(𝕃) ≅ A_spec(𝕃)₊ × A_spec(𝕃)₋).

*Notation:* χ₊ = e₊·χ, χ₋ = e₋·χ for the bipolar projections of a character; A_spec(𝕃) for the full spectral character algebra.

*Dependencies:*
- Idempotent Decomposition Lemma *II.L07* from Part VII
- Holomorphic ⟺ idempotent-supported *II.T33* from Part VII
- Spectral characters *I.D19*, *I.D22*–*I.D23* from Book I
- Calibrated H_τ *II.D35* from Part VII

## Lean coverage

Module `BookII.CentralTheorem.BoundaryCharacters`. Key declarations: `boundary_character_decomp` (*II.P14*: uniqueness of χ = e₊·χ₊ + e₋·χ₋), `a_spec_full_algebra` (A_spec(𝕃) contains all idempotent-supported characters and no others), `product_decomposition` (A_spec(𝕃) ≅ A_spec(𝕃)₊ × A_spec(𝕃)₋). All sorry-free; the decomposition reduces to *II.L07* applied to character maps.

## Where this leads

With boundary characters fully organized by idempotent support, Chapter 49 applies the Hartogs extension *II.T37* to lift each character channel-by-channel into a holomorphic function on τ³, establishing the injective leg of the Central Theorem correspondence.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part09/ch47-boundary-characters-idempotent.tex -->
