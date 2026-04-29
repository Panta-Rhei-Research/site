---
layout: "corpus-monograph-chapter"
title: "Chapter 4: Orbit-Seeded Generation and the No-Jump Principle"
permalink: "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-04-orbit-seeded-generation-and-the-no-jump-principle/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-coherence-kernel"
chapter_number: 4
chapter_slug: "chapter-04-orbit-seeded-generation-and-the-no-jump-principle"
page_in_book: 15
prev_chapter_url: "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-03-the-iterator-rho-and-the-omega-beacon/"
prev_chapter_title: "Chapter 3: The Iterator ρ and the Omega Beacon"
next_chapter_url: "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-05-the-object-closure-axiom-and-the-static-kernel-tau/"
next_chapter_title: "Chapter 5: The Object Closure Axiom and the Static Kernel τ₀"
summary_short: "K3 seeds each non-omega generator as an infinite orbit ray; K4 enforces cover so rho is the immediate successor. Per-orbit injectivity follows as a theorem."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-01-the-coherence-kernel/"
canonical_part_title: "The Coherence Kernel"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-01-the-coherence-kernel/chapter-04-orbit-seeded-generation-and-the-no-jump-principle/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part I: The Coherence Kernel"
      url: "/corpus/monographs/book-i/part-01-the-coherence-kernel/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part I"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 2
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

Chapters 2 and 3 established the signature Σ_τ = (α, π, γ, η, ω, ρ, <) and three kernel axioms: *K1* (strict order on generators), *K2* (ω absorbs ρ), and *K5* (ω is unreachable). The present chapter introduces the two axioms governing how ρ generates new objects from the non-ω generators. *K3* (Orbit-Seeded Generation) declares that each generator g ∈ {α, π, γ, η} seeds an orbit ray O_g = {g, ρ(g), ρ²(g), …} and that ρ maps every O_g into itself — ensuring the ray's existence and stability without yet claiming infiniteness, disjointness, or exhaustiveness. *K4* (No-Jump / Cover) asserts that ρ acts as the *immediate* successor within each ray: ρ(ρⁿ(g)) = ρⁿ⁺¹(g) with no element strictly between consecutive depths. From K4 alone, injectivity of ρ per orbit follows as a derived proposition, eliminating the need for a separate injectivity axiom that burdened the 1st Edition.

## What this chapter contributes

- States *I.K3* (Orbit-Seeded Generation): each non-ω generator g ∈ {α, π, γ, η} belongs to its own orbit ray, and ρ maps that ray into itself. Explains precisely what K3 does *not* claim: infiniteness, disjointness, and exhaustiveness require further axioms.
- States *I.K4* (No-Jump / Cover): ρ(ρⁿ(g)) = ρⁿ⁺¹(g) for all n ≥ 0. The non-trivial content is the cover clause: no element of O_g lies strictly between consecutive depths. Each orbit ray thereby acquires the structure of a discrete linear order — the Hasse diagram of (ℕ, ≤).
- Defines the cover relation x ⋖ y ⟺ y = ρ(x), giving a clean presentation of the orbit order.
- Proves *I.P02* (ρ Injectivity Per Orbit): if ρ(ρⁿ(g)) = ρ(ρᵐ(g)) then n = m, derived from K4 alone. Notes the contrast with the 1st Edition, where injectivity was an independent axiom (INJ); the 2nd Edition's economy reduces nine axioms to six.
- Identifies three open questions left for subsequent chapters: object closure (no rogue objects exist), pairwise disjointness of orbits (deferred to Part II), and the static kernel τ₀ (assembled in Chapter 5).
- Lean coverage: `TauLib.BookI.Kernel.Axioms` (`K3_orbit_seeded`, `K4_no_jump`, `rho_injective`). All proofs compile without `sorry`.

## Lean coverage

`TauLib.BookI.Kernel.Axioms`

## Where this leads

Five of the six kernel axioms are now in place (K1–K5). Chapter 5 states the final axiom K6 (Object Closure), seals the universe, and assembles the complete static kernel τ₀. Once τ₀ is in hand, Part II will bring it to life via the single generative act.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part01/ch03-generation-cover.tex -->
