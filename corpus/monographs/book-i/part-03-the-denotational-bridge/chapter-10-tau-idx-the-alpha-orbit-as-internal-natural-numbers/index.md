---
layout: "corpus-monograph-chapter"
title: "Chapter 10: τ-Idx — The Alpha-Orbit as Internal Natural Numbers"
permalink: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-10-tau-idx-the-alpha-orbit-as-internal-natural-numbers/"
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
chapter_number: 10
chapter_slug: "chapter-10-tau-idx-the-alpha-orbit-as-internal-natural-numbers"
page_in_book: 41
prev_chapter_url: "/corpus/monographs/book-i/part-02-orbit-generation-and-ontic-closure/chapter-09-rigidity-tau/"
prev_chapter_title: "Chapter 9: Rigidity — (τ) = \\\\"
next_chapter_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-11-the-swap-operator-sigma-and-the-first-arithmetic/"
next_chapter_title: "Chapter 11: The Swap Operator σ and the First Arithmetic"
summary_short: "The alpha-orbit O_alpha is tau-Idx: the earned natural numbers. Rank transfer maps RT_pi, RT_gamma, RT_eta biject tau-Idx onto the three solenoidal orbits."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/"
canonical_part_title: "The Denotational Bridge"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-03-the-denotational-bridge/chapter-10-tau-idx-the-alpha-orbit-as-internal-natural-numbers/"
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

The passage from generation to denotation begins with a single, sharp observation: the alpha-orbit O_α = {α, ρ(α), ρ²(α), …} *is* the natural numbers. Not by analogy, not by embedding, not by importation from set theory — but as an identity of structure. The alpha-orbit, populated by the generative act and governed by the kernel axioms, satisfies every Peano property: it has a distinguished zeroth element α, a successor function ρ, injectivity of ρ (from K4), no element whose successor is α (from K4's strict depth increase), and induction (from well-foundedness). This identification is named *τ-Idx* and forms the counting scaffold on which all denotational content will be built. Three rank transfer maps then establish canonical depth-preserving bijections between τ-Idx and each of the three solenoidal orbits.

## What this chapter contributes

- Defines *I.D07* (τ-Idx): the internal natural numbers as O_α, with notation n̲ = ρⁿ(α). The successor on τ-Idx is ρ itself — no new operation is introduced.
- Proves *I.P14* (τ-Idx satisfies the Peano properties): zeroth element (α), successor (ρ), injectivity (Proposition I.P02 from Chapter 4), non-circularity (depth strictly increases by K4), and countability (orbit countable from Part II). Induction is then available as well-foundedness of depth descent.
- Defines *I.D08* (Rank Transfer Maps *RT_π*, *RT_γ*, *RT_η*): for each solenoidal generator s ∈ {π, γ, η}, RT_s(n̲) := ρⁿ(s) — depth-preserving maps from τ-Idx to O_s.
- Proves that each rank transfer map is a bijection (injectivity from ρ-injectivity on O_s; surjectivity from the orbit ray definition). The three maps are depth-preserving and commute with ρ: RT_s(n̲ + 1) = ρ(RT_s(n̲)).
- Notes the contrast with the 1st Edition: the 2nd Edition has three rank transfer maps (one per solenoidal orbit), reflecting the 1+3 generator split, where the 1st Edition had two "rank transfer functors" p and q.
- Every object in τ can now be addressed by a pair (seed, depth), inaugurating the denotational layer.
- Lean coverage: `TauLib.BookI.Denotation.TauIdx` (`TauIdx`, `toAlphaOrbit`, `fromAlphaOrbit`) and `TauLib.BookI.Denotation.RankTransfer` (`RT`, `RT_inv`, `RT_injective`, `RT_surjective`, `RT_rho_comm`). All proofs compile without `sorry`.

## Lean coverage

`TauLib.BookI.Denotation.TauIdx`, `TauLib.BookI.Denotation.RankTransfer`

## Where this leads

With τ-Idx and rank transfer maps in place, Chapter 11 derives the first arithmetic operations: the swap operator σ, index addition as iterated ρ, and index multiplication by structural recursion — establishing (τ-Idx, +, ×, 0̲, 1̲) as a commutative semiring without importing any arithmetic from outside.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part03/ch10-tau-idx.tex -->
