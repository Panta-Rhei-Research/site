---
layout: "corpus-monograph-chapter"
title: "Chapter 3: Roadmap and Inverted Dependency"
permalink: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/chapter-03-roadmap-and-inverted-dependency/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 0
part_display: "Prologue"
part_slug: "part-00-from-kernel-to-interior"
chapter_number: 3
chapter_slug: "chapter-03-roadmap-and-inverted-dependency"
page_in_book: 11
prev_chapter_url: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/chapter-02-the-elliptic-to-split-complex-shift/"
prev_chapter_title: "Chapter 2: The Elliptic-to-Split-Complex Shift"
next_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-04-tau/"
next_chapter_title: "Chapter 4: τ"
summary_short: "Book II's eleven-part structure advances from Book I's five exports to the Central Theorem O(τ³) ≅ A_spec(𝕃) by inverting every classical dependency arrow: holomorphy precedes continuity, continuity precedes topology, topology precedes geometry, geometry precedes the transcendental constants."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/"
canonical_part_title: "From Kernel to Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-00-from-kernel-to-interior/chapter-03-roadmap-and-inverted-dependency/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Prologue: From Kernel to Interior"
      url: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Prologue"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 19
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

This chapter maps the full terrain of Book II: a Prologue plus ten Parts, 58 chapters, advancing from Book I's five exports to the Central Theorem O(τ³) ≅ A_spec(𝕃). The central structural insight is the **inverted dependency chain** — the logical order of the five classical layers of analysis is exactly reversed in Category τ. Where orthodoxy flows transcendentals → geometry → topology → continuity → holomorphy, Book II flows holomorphy → continuity → topology → geometry → transcendentals, and each arrow is a theorem, not a convention. Holomorphy is primitive in τ (ω-germ coherence, an algebraic condition with no reference to limits); continuity is a consequence (every ω-germ transformer respects the cylinder topology); topology is earned as the unique structure making normal-form recursion continuous; geometry follows from the ultrametric induced by the cylinder topology; and the transcendental constants π, e, j, ι_τ are earned from the resulting Euclidean and spectral structure. Three pivot points mark qualitative shifts in the argument, and five deliberate exclusions define the boundary of the book.

## What this chapter contributes

- **Remark *II.R03* — Inverted Dependency Chain:** formally records the five-link inversion holomorphy ⟹ continuity ⟹ topology ⟹ geometry ⟹ transcendentals as a structural remark. Each arrow traces through *I.T04* (Hyperfactorization), *I.T10* (Split-Complex Forced), and *I.T31* (Global Hartogs Extension).
- **Eleven-Part roadmap:** Prologue (Ch. 1–3) + Parts I–X (Ch. 4–58), with key results at each stage: τ³ as τ-admissible ABCD quadruples (Part I), cylinder topology (Part II), Stone space and dim_τ = 4 (Part III), Tarski-axiomatic geometry (Part IV), earned transcendentals π, e, j, ι_τ (Part V), Mutual Determination five-way equivalence (Part VI), 3-lemma chain (Part VII), Yoneda as theorem (Part VIII), Central Theorem (Part IX), closure and bridge to Book III (Part X).
- **Three pivot points:** Part V crosses from discrete-algebraic to Archimedean (countable structure earns continuous constants); Part VI makes split-complex holomorphy load-bearing via Mutual Determination; Part IX assembles all threads into the Central Theorem with moduli space = {*}.
- **Negative scope:** no imported ℝ or ℂ, no imported topology, no imported category theory, no Millennium Problem proofs (those belong to Book III), no ZFC axioms or uncountable sets.

## Lean coverage

No Lean module is claimed for this chapter. The roadmap is expository. The individual theorems named here — *I.T04*, *I.T10*, *I.T31* — are verified in `TauLib.BookI`; the new results of Book II are planned across `TauLib.BookII.*` and are marked as forthcoming at each chapter's entry.

## Where this leads

Chapter 4 (τ-Admissible Points from ABCD Readouts) opens Part I by giving the first constructive definition in Book II: the point set τ³ as the set of τ-admissible ABCD quadruples satisfying the five constraints of the constraint lattice, completed by the profinite inverse limit.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part00/ch03-roadmap-inverted-dependency.tex -->
