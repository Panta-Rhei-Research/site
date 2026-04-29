---
layout: "corpus-monograph-chapter"
title: "Chapter 11: Holomorphic Implies Continuous (The Inverted Dependency)"
permalink: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-11-holomorphic-implies-continuous-the-inverted-dependency/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 2
part_display: "Part II"
part_slug: "part-02-local-domains-cylinders-as-prefix-predicates"
chapter_number: 11
chapter_slug: "chapter-11-holomorphic-implies-continuous-the-inverted-dependency"
page_in_book: 51
prev_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-10-the-ultrametric-and-first-disagreement-depth/"
prev_chapter_title: "Chapter 10: The Ultrametric and First Disagreement Depth"
next_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-12-split-complex-structure-not-yet-load-bearing/"
next_chapter_title: "Chapter 12: Split-Complex Structure Not Yet Load-Bearing"
summary_short: "In classical complex analysis topology precedes holomorphy as a logical prerequisite. Category τ inverts this: holomorphy is defined combinatorially without topology, and continuity is the theorem that follows. The proof is a three-line lemma from naturality."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/"
canonical_part_title: "Local Domains: Cylinders as Prefix Predicates"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-11-holomorphic-implies-continuous-the-inverted-dependency/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part II: Local Domains: Cylinders as Prefix Predicates"
      url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part II"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 21
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

In classical complex analysis the logical chain runs: topology ⇒ limits ⇒ differentiability ⇒ holomorphy. Continuity is a *prerequisite*; holomorphy is a strengthening condition imposed on a substrate that is already continuous — the Cauchy–Riemann equations cannot even be stated without topology in place. In Category τ this chain is inverted. Holomorphy — defined combinatorially in Book I via ω-germ transformer naturality (*I.D47*) — requires only finite cyclic groups, CRT reduction maps, and commutativity of a tower diagram: that the induced maps f_k : ℤ/P_k → ℤ/P_k intertwine the reduction maps π_{k,n} for all k ≤ n. No open sets, no limits, no ε-δ arguments appear in the definition. Continuity is a *consequence*. The inversion is genuine, not a matter of presentation: classical holomorphy *cannot be defined* without topology, whereas τ-holomorphy is defined in a universe where "open set" has not yet been mentioned. This chapter proves the core inversion: every ω-germ transformer on τ³ is continuous with respect to the cylinder topology, and in fact uniformly continuous and 1-Lipschitz with respect to the ultrametric.

## What this chapter contributes

Lemma *II.L01* (Naturality Forces Cylinder Compatibility: f(C_k(x)) ⊆ C_k(f(x)) for every stage k and point x) and Theorem *II.T06* (Holomorphic Implies Continuous). The proof of *II.L01* is three equalities: if y ∈ C_k(x) then π_k(y) = π_k(x), tower coherence of f gives π_k(f(y)) = f_k(π_k(y)) = f_k(π_k(x)) = π_k(f(x)), and hence f(y) ∈ C_k(f(x)). Naturality does all the work. The main theorem follows in two dual formulations: open-preimage (preimage of every basis set is open) and ultrametric (f is 1-Lipschitz, so δ(f(x), f(y)) ≥ δ(x, y)). The chapter also shows the converse fails: continuous maps need not be tower-coherent, so holomorphy is strictly stronger than continuity.

## Lean coverage

*BookII.Domains.HolImpliesCont* (planned). *II.L01* is a short algebraic lemma and should be among the first formal proofs in Book II's Lean development.

## Where this leads

The 1-Lipschitz bound established here is the primary input to Part III: it shows the cylinder topology is the *unique* topology making all ω-germ transformers continuous, since the translation maps x ↦ x + a (mod P_k) are ω-germ transformers whose continuity forces every stage-k equivalence class to be open (Chapter 14, Remark on forced topology). The full inverted dependency chain — holomorphy ⇒ continuity ⇒ topology ⇒ geometry ⇒ transcendentals — propagates through the remainder of Book II, with this chapter establishing its first and most fundamental link. At no subsequent point does the chain import topology from an external source; every topological fact about τ³ is downstream from the holomorphic structure earned in Book I.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part02/ch11-hol-implies-cont.tex -->
