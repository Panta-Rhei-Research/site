---
layout: "corpus-monograph-chapter"
title: "Chapter 4: The Self-Enrichment Functor"
permalink: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-04-the-self-enrichment-functor/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-self-enrichment-principle"
chapter_number: 4
chapter_slug: "chapter-04-the-self-enrichment-functor"
page_in_book: 17
prev_chapter_url: "/corpus/monographs/book-iii/part-00-where-does-physics-live/chapter-03-the-reader-s-compass/"
prev_chapter_title: "Chapter 3: The Reader's Compass"
next_chapter_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-05-the-layer-template/"
next_chapter_title: "Chapter 5: The Layer Template"
summary_short: "Category τ enriches over itself via H_τ = ℤ[j]/(j²−1): Hom(A,B) ∈ Obj(τ) for all A, B. The enrichment functor F_E (III.D04) iterates this to produce E₀→E₁→E₂→E₃, absorbing one ABCD orbit per step before saturating at E₃."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/"
canonical_part_title: "The Self-Enrichment Principle"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-01-the-self-enrichment-principle/chapter-04-the-self-enrichment-functor/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part I: The Self-Enrichment Principle"
      url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part I"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 32
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

A category enriches over itself when its morphism spaces are objects of the same category. Book II, Part VIII proved that Category τ has exactly this property: Hom(A, B) ∈ Obj(τ) for every pair A, B, and the morphism spaces carry the same bipolar χ₊/χ₋ decomposition as the objects they connect. This chapter receives that result as the Book II handoff (*III.R05*), extracts its structural content, and defines the *enrichment functor* F_E (*III.D04*) that iterates self-enrichment to produce new layers. F_E takes a τ-category and promotes each Hom object one enrichment level higher; the objects do not change, but the morphism spaces acquire new internal structure. Each application absorbs one additional ABCD orbit: E₀→E₁ absorbs the (γ, η)-fiber splitting; E₁→E₂ absorbs the α-parity splitting; E₂→E₃ absorbs the π-winding splitting. After three iterations all four orbits are absorbed into the enrichment structure, and F_E produces nothing new. The ladder saturates.

## What this chapter contributes

**Definitions / Axioms**
- *Book II handoff* (*III.R05*, τ-effective): four results exported by Book II Part VIII — (1) self-enrichment structure (*II.D53*): internal Hom objects [A, B] ∈ Obj(τ); (2) composition internalized: ∘_{A,B,C}: [B,C] ⊗ [A,B] → [A,C] is a τ-morphism; (3) identity internalized: id_A: 1 → [A,A] is a τ-morphism from the terminal object; (4) Yoneda embedding (*II.T36*): y: τ ↪ [τᵒᵖ, τ] is fully faithful, so self-enrichment is non-degenerate.
- *Enrichment functor F_E* (*III.D04*, τ-effective): F_E: Cat_τ → Cat_τ. Given a τ-category C, F_E(C) has the same objects; for A, B ∈ Obj(C), Hom_{F_E(C)}(A,B) = [Hom_C(A,B)]_τ, the internal Hom of τ applied to C's Hom objects. Composition and identity are inherited from τ's internal structure. F_E preserves monoidal structure and the Yoneda embedding. Starting from E₀ = τ, the layers are E_{k+1} = F_E(E_k).

**Key results**
- *Bipolar composition law* (τ-effective): [A,B] = e₊·[A,B]₊ + e₋·[A,B]₋ where e₊ = ½(1+j), e₋ = ½(1−j), j² = +1. In sector form: (g ∘ f) = e₊(g₊f₊) + e₋(g₋f₋) — the two sectors multiply independently. In graded form: (g ∘ f)₀ = g₀f₀ + g₁f₁, (g ∘ f)₁ = g₀f₁ + g₁f₀. This gives the ℤ/2ℤ super-category structure: even ∘ even = even, even ∘ odd = odd, odd ∘ odd = even. Both forms are equivalent under the change of basis g₊ = g₀ + g₁, g₋ = g₀ − g₁.
- *New structure at each layer* (τ-effective): E_{k+1} ≇ E_k for k = 0, 1, 2; saturation at k = 3. At each step the Hom objects acquire the bipolar decomposition of one additional ABCD orbit, making each inclusion strict. The ladder saturates because after three iterations all four orbits are absorbed and F_E(E₃) = E₃.
- *Self-enrichment as self-similarity*: at E₃ the category is uniformly self-similar — it looks the same at every categorical depth — because every layer of relationship (objects, morphisms, transformations, modifications) carries the full four-fold ABCD structure.

**Notation**
- H_τ = ℤ[j]/(j²−1); e₊ = ½(1+j), e₋ = ½(1−j); [A,B] = e₊[A,B]₊ + e₋[A,B]₋; F_E: Cat_τ → Cat_τ; E_{k+1} = F_E(E_k)

**Dependencies**
- *II.D53* (Self-enrichment structure), *II.T36* (Yoneda embedding), *II.T40* (Central Theorem)
- *I.T04* (Hyperfactorization), *I.T12* (Spectral decomposition), *I.D18* (Algebraic lemniscate)

## Lean coverage

The enrichment functor *III.D04* and the bipolar composition law are planned for `TauLib/BookIII/SelfEnrichment.lean`. The bipolar composition law (Proposition in Section 4 of the LaTeX source) is fully algebraic and reduces at each finite primorial level k to explicit arithmetic in (ℤ/M_kℤ)[j]/(j²−1), making it a strong Lean 4 candidate. The Yoneda embedding *II.T36* provides the non-degeneracy argument; its Book II Lean counterpart, once available, makes the full self-enrichment formalization tractable. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Chapter 5 asks why every enrichment layer looks the same from the inside, and answers with the uniform four-component layer template E_k = (Carrier_k, Predicate_k, Decoder_k, Invariant_k) — inherited from the ABCD decomposition — instantiated for all four layers.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part01/ch04-the-self-enrichment-functor.tex -->
