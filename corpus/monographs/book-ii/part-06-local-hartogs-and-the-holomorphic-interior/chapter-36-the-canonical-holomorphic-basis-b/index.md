---
layout: "corpus-monograph-chapter"
title: "Chapter 36: The Canonical Holomorphic Basis B"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-36-the-canonical-holomorphic-basis-b/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-local-hartogs-and-the-holomorphic-interior"
chapter_number: 36
chapter_slug: "chapter-36-the-canonical-holomorphic-basis-b"
page_in_book: 181
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-35-laurent-series-and-residues/"
prev_chapter_title: "Chapter 35: Laurent Series and Residues"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-37-sheaf-coherence-from-omega-germ-compatibility/"
next_chapter_title: "Chapter 37: Sheaf Coherence from ω-Germ Compatibility"
summary_short: "CRT decomposition, bipolar idempotents, and NF addressing together force a unique basis B_τ for τ-holomorphic functions — cylinder generators E_{k,v}^(σ) replacing classical monomials with finite spectral support guaranteed by *II.T31*."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-36-the-canonical-holomorphic-basis-b/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VI: Local Hartogs and the Holomorphic Interior"
      url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 25
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Classical holomorphic functions expand in the monomial basis {z^n}, but that basis depends on a coordinate convention: a different local chart produces different Taylor coefficients. Category τ has no ambient complex plane and no coordinate freedom. The algebraic structure of τ³ — the CRT tower (*I.T18*), the bipolar idempotent pair (*I.D21*), and the NF normal-form addressing of cylinder domains (*II.D10*) — forces a unique spanning set. This chapter constructs it explicitly and proves its essential properties.

## What this chapter contributes

- **Definitions:** *II.D46 — Cylinder Generator*: E_{k,v}^(σ) : ℤ/P_kℤ → A_τ^(σ) is the indicator function of the residue class v (mod p) in channel σ ∈ {B, C} at stage k, where e_B = e_+ and e_C = e_-; generators in different channels are orthogonal via e_+ · e_- = 0, and generators targeting different residue classes of the same prime are orthogonal via disjoint support. *II.D45 — Canonical Holomorphic Basis* B_τ: the full collection {E_{k,v}^(σ) | k ≥ 1, p | P_k, v ∈ ℤ/pℤ, σ ∈ {B,C}} — canonical meaning forced by structure, not chosen by convention.
- **Key results:** *II.T31 — Finite Spectral Support*: every τ-holomorphic function activates only finitely many basis elements at each stage. Stage-wise finiteness follows from the finiteness of ℤ/P_kℤ; no uncountable collection is needed because Book I's unique infinity theorem (*I.T36*) ensures the global spectral support is at most countable — and each stage's contribution is finite. *II.P08 — Projection Formula*: φ_{p,v}^(σ) = (1/|F_p|) Σ_{x ∈ F_p(v)} e_σ · f_k(x) — a discrete Fourier average over the fiber F_p(v), recovering spectral coefficients without contour integration.
- **Structural results:** spectral coherence across stages (coefficients at stage k and k+1 agree for shared primes; new spectral data enters only from p_{k+1}); basis cardinality |Λ_k| = 2 Σ p_i grows as k² ln k; transition functions between cylinder domains are trivial because the forced basis is identical on every domain; the split-complex structure j² = +1 is load-bearing — the elliptic codomain ℂ has no nontrivial idempotents and admits no channel separation.
- **Dependencies:** *I.T10*, *I.T18*, *I.T36*, *I.D21*, *II.D10*, *II.T27*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Holomorphy.CanonicalBasis` is planned.

## Where this leads

The canonical basis and its trivial transition functions make the sheaf axioms in Chapter 37 immediate. Because same-stage cylinder domains are either disjoint or identical, gluing compatible local sections requires no partition of unity and no analytic continuation — only tower coherence and the clopen overlap structure of the ultrametric topology.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch35-canonical-basis.tex -->
