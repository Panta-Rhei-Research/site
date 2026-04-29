---
layout: "corpus-monograph-chapter"
title: "Chapter 1: The Boundary-First Paradigm"
permalink: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/chapter-01-the-boundary-first-paradigm/"
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
chapter_number: 1
chapter_slug: "chapter-01-the-boundary-first-paradigm"
page_in_book: 3
next_chapter_url: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/chapter-02-the-elliptic-to-split-complex-shift/"
next_chapter_title: "Chapter 2: The Elliptic-to-Split-Complex Shift"
summary_short: "Category τ inverts the classical SCV flow: where orthodox analysis derives boundary values from interior holomorphic functions, Book II earns interior structure from the algebraic lemniscate 𝕃 — the boundary object constructed in Book I."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/"
canonical_part_title: "From Kernel to Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-00-from-kernel-to-interior/chapter-01-the-boundary-first-paradigm/"
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

Classical several complex variables flows from interior to boundary: one begins with holomorphic functions on an open domain, applies the Cauchy integral formula, and reads off boundary values as derived traces. Category τ inverts this flow entirely. Book I earned the algebraic lemniscate 𝕃 = S¹ ∨ S¹ as a boundary object before any interior point was defined, constructed a complete holomorphic calculus on 𝕃 using the split-complex unit j² = +1, and culminated in the Global Hartogs Extension theorem (*I.T31*), which guarantees that boundary data determines interior structure uniquely. This chapter explains why the inversion is not a stylistic preference but a structural consequence of the coherence kernel, catalogues the five exports from Book I that power all of Book II, identifies the four structural features that force the boundary-first direction, and states the Boundary-First Principle as a formal remark (*II.R01*).

## What this chapter contributes

- **Registry entry:** *II.R01 — Boundary-First Principle*: in Category τ, boundary structure is primary and interior structure is derived. Interior points of τ³ are Hartogs continuations from 𝕃; the topology, geometry, and holomorphic analysis of the interior are all inherited from the boundary via the idempotent splitting e±.
- **Five exports from Book I** that form the dependency chain powering Book II: (1) the ABCD coordinate chart (*I.D17*, dim_τ = 4), (2) hyperfactorization (*I.T04*, uniqueness of the chart), (3) the algebraic lemniscate (*I.D18*), (4) split-complex holomorphy (*I.D47–I.D49*), and (5) Global Hartogs Extension (*I.T31*).
- **Four structural reasons the inversion is forced:** bipolarity of 𝕃 via idempotents e±; the wave-type PDE character of H_τ (hyperbolic, not elliptic); the polarity flip j swaps channels rather than rotating; and diagonal discipline (K₅) forbids unearned self-maps that would build interior from interior rather than from boundary.
- **Conceptual orientation:** the Boundary-First Principle is not a single theorem but an organizing commitment — every construction in Book II begins at 𝕃 and propagates inward, culminating in the Central Theorem O(τ³) ≅ A_spec(𝕃).

## Lean coverage

The formal statement of *II.R01* is a remark, not a theorem with a mechanically verified proof. No Lean module is claimed for this chapter. The five imports from Book I on which *II.R01* rests — *I.D18*, *I.T31*, and associated results — are verified in `TauLib.BookI`. The chapter is expository; its formal content lives in the chapters that follow.

## Where this leads

Chapter 2 (The Elliptic-to-Split-Complex Shift) takes the first structural consequence of the Boundary-First Principle and makes it algebraically precise: the bipolar boundary 𝕃 forces split-complex scalars j² = +1 over elliptic scalars i² = −1, a replacement whose justification is the subject of the next chapter.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part00/ch01-boundary-first-paradigm.tex -->
