---
layout: "corpus-monograph-chapter"
title: "Chapter 4: τ"
permalink: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-04-tau/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-interior-points-and-the-tau"
chapter_number: 4
chapter_slug: "chapter-04-tau"
page_in_book: 15
prev_chapter_url: "/corpus/monographs/book-ii/part-00-from-kernel-to-interior/chapter-03-roadmap-and-inverted-dependency/"
prev_chapter_title: "Chapter 3: Roadmap and Inverted Dependency"
next_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-05-the-omega-readout-and-the-lemniscate/"
next_chapter_title: "Chapter 5: The Omega Readout and the Lemniscate"
summary_short: "The full point set τ³ is defined purely algebraically as the set of τ-admissible ABCD quadruples satisfying five explicit constraints, completed to include limit points via the profinite inverse system; no ambient space, no topology, and no Hartogs invocation are required."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
canonical_part_title: "Interior Points and the τ³"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-01-interior-points-and-the-tau/chapter-04-tau/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part I: Interior Points and the τ³"
      url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part I"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 20
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Book I built the ABCD coordinate chart Φ : Obj(τ) → τ-Idx⁴ as a total, injective address system for every finite object of τ, with the normal form X = ((A ↑↑ C)^B) · D and uniqueness guaranteed by Hyperfactorization (*I.T04*). The chart is defined on finite objects; it assigns degenerate addresses to indices 0 and 1, and at ω the coordinates diverge without internal structure. This chapter closes that gap by defining the full point set τ³. The key insight is that τ³ is not defined by importing an ambient space or invoking Global Hartogs Extension — it is defined purely algebraically as the set of **τ-admissible ABCD quadruples**, those satisfying the five constraints implicit in the Hyperfactorization Theorem, together with their profinite limit points arising from the CRT inverse system of Book I.

## What this chapter contributes

- **Definition *II.D03* — Constraint lattice:** the conjunction of five conditions on a quadruple (A, B, C, D) ∈ τ-Idx⁴: (C1) prime constraint (A ∈ ℙ_τ ∪ {1}); (C2) non-negativity (B, C, D ≥ 0); (C3) remainder constraint (every prime factor of D is strictly less than A); (C4) tower constraint (A = 1 forces B = C = 0); (C5) normalization (B and C are the outputs of the greedy peel-off algorithm, no under-extraction permitted).
- **Definition *II.D02* — τ-admissible point:** a quadruple satisfying all five constraints. The finite admissible points τ³_fin are in natural bijection with Obj(τ) via Φ (*I.T04*), and τ³_fin is countably enumerable in the index ordering.
- **Limit points and profinite completion:** coherent families of finite ABCD tuples under the CRT reduction maps (*I.T18*) that are not eventually constant constitute τ³_lim. The primorial tower Φ(P_k) = (p_k, 1, 1, P_{k-1}) provides an explicit non-trivial limit point. Together τ³ = τ³_fin ∪ τ³_lim.
- **Theorem *II.T01* — Point Set Well-Defined:** τ³ is a well-defined set whose finite part bijects with Obj(τ), whose limit part is non-empty, and which is closed under CRT reduction maps. At this stage τ³ carries no topology, no holomorphic structure, and no complex structure — each must be earned in subsequent parts.

## Lean coverage

The Lean formalization is planned in `TauLib.BookII.Interior.TauAdmissible` (marked as planned in the source). The constraint lattice conditions (C1)–(C5) are decidable predicates on τ-Idx⁴ and are straightforward to formalize once the primorial CRT ring from `TauLib.BookI` is in scope. No verified module is currently claimed for this chapter.

## Where this leads

Chapter 5 (The Omega Readout and the Lemniscate) asks what happens to the ABCD readout as one approaches ω along different paths in τ³. The answer — base coordinates collapse to a single point while fiber coordinates trace the algebraic lemniscate 𝕃 — makes the fibered product structure τ³ = τ¹ ×_f T² structurally visible for the first time.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part01/ch04-tau-admissible-points.tex -->
