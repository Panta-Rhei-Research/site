---
layout: "corpus-monograph-chapter"
title: "Chapter 15: The Holomorphic State Space"
permalink: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-15-the-holomorphic-state-space/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 2
part_display: "Part II"
part_slug: "part-02-quantum-mechanics-as-address-obstruction"
chapter_number: 15
chapter_slug: "chapter-15-the-holomorphic-state-space"
page_in_book: 79
prev_chapter_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-14-characters-as-quantum-addresses/"
prev_chapter_title: "Chapter 14: Characters as Quantum Addresses"
next_chapter_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-16-holomorphic-quantization/"
next_chapter_title: "Chapter 16: Holomorphic Quantization"
summary_short: "Quantum mechanics lives in Hilbert space. But where does Hilbert space come from? In τ³, it emerges naturally: the space of CR-functions satisfying…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
canonical_part_title: "Quantum Mechanics as Address Obstruction"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-02-quantum-mechanics-as-address-obstruction/chapter-15-the-holomorphic-state-space/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part II: Quantum Mechanics as Address Obstruction"
      url: "/corpus/monographs/book-iv/part-02-quantum-mechanics-as-address-obstruction/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part II"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 44
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Standard quantum mechanics opens with the postulate that states are vectors in a complex Hilbert space, but offers no geometric reason why. In τ³ that reason is structural: the space CR(τ³) of functions satisfying the tangential Cauchy–Riemann equations ∂̄_b f = 0 is already an infinite-dimensional complex algebra determined by its boundary values on 𝕃, and the fibration τ³ = τ¹ ×_f T² carries a natural measure dμ from which a canonical inner product ⟨f, g⟩ = ∫ f̄ g dμ follows immediately. The L² completion of CR(τ³) under this norm gives the holomorphic Hilbert space H_τ, which is complete, separable, and infinite-dimensional—exactly the properties quantum mechanics requires. The character modes χ_{m,n} indexed by Λ_CR form an orthonormal basis, so any state expands as f = Σ c_{m,n} χ_{m,n}; superposition is just linearity. Multi-particle entanglement enters as non-factorizability of coefficient tensors in H_τ ⊗ H_τ, dissolving the EPR puzzle: the correlations are encoded in a joint CR-function on T² × T², not transmitted by any signal.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D35 — Space of CR-Functions*. CR(τ³) = {f : τ³ → ℂ | ∂̄_b f = 0}; an algebra determined by boundary values on 𝕃.
- **Definitions / Axioms:** *IV.D36 — Canonical Inner Product*. ⟨f, g⟩ = ∫_{τ³} f̄ g dμ, where dμ is the fibered product measure from τ¹ arclength and T² Haar measure.
- **Definitions / Axioms:** *IV.D37 — Holomorphic Hilbert Space*. H_τ = CR(τ³)^{‖·‖}, the L² completion of CR(τ³); this is the quantum state space of τ³.
- **Definitions / Axioms:** *IV.D38 — Separable and Entangled States*. A two-particle state in H_τ ⊗ H_τ is separable if its coefficient tensor factors; otherwise entangled.
- **Key results:** *IV.T04 — Hilbert Space Properties* (established): H_τ is complete, separable (character modes are a countable dense subset), and infinite-dimensional.
- **Key results:** *IV.T05 — Orthonormal Basis* (established): {χ_{m,n} : (m,n) ∈ Λ_CR} is an orthonormal basis for H_τ with ⟨χ_{m,n}, χ_{m',n'}⟩ = δ_{mm'} δ_{nn'}.
- **Key results:** *IV.P05 — Spectral Completeness* (established): any CR-function expands as f = Σ c_{m,n} χ_{m,n} with c_{m,n} = ⟨χ_{m,n}, f⟩.
- **Dependencies:** Chapter 13 (CR-functions, CR-structure on τ³), Chapter 14 (character modes, Λ_CR); Book II Central Theorem (holographic determination of bulk by lemniscate boundary).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 16 equips H_τ with operators derived from holomorphic vector fields on τ³, uses the Lie bracket to obtain commutators geometrically, and derives Planck's constant ℏ_τ = 1/4 as a unit-conversion factor of bi-rotation geometry.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part02/ch15-holomorphic-state-space.tex -->
