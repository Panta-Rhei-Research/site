---
layout: "corpus-monograph-chapter"
title: "Chapter 34: Composition, Identity, Associativity"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-34-composition-identity-associativity/"
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
chapter_number: 34
chapter_slug: "chapter-34-composition-identity-associativity"
page_in_book: 169
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-33-evolution-operator-and-causal-arrow/"
prev_chapter_title: "Chapter 33: Evolution Operator and Causal Arrow"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-35-laurent-series-and-residues/"
next_chapter_title: "Chapter 35: Laurent Series and Residues"
summary_short: "Stagewise composition of ω-germ transformers is shown to be associative — not as an axiom but as a theorem lifted from the program monoid — forming the category HolEnd_τ (*II.D41*)."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-34-composition-identity-associativity/"
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

The preceding chapters of Part VI built objects (τ-admissible points), morphisms (ω-germ transformers), a lifting operator (BndLift_n), a unification theorem (Mutual Determination), and a dynamics (evolution operator). A category needs three more things: a composition operation, identity morphisms, and associativity of composition. In classical complex analysis, associativity of holomorphic composition is a routine observation — it follows immediately from set-theoretic function composition. In the τ-setting, composition must respect tower coherence at every finite stage, and tower coherence alone does not force associativity: it forces compatibility, not algebraic structure. The program monoid (*I.P02*, Book I) provides the missing ingredient by recording how every ω-germ transformer factors as a coherent lift of a word in the generators {ρ, μ, ν, θ}, and the monoid's combinatorially proved associativity then lifts to the holomorphic level via the faithful correspondence of *II.T27*.

## What this chapter contributes

- **Definitions:** *II.D39 — Composition*: (g ∘ f)_k := g_k ∘ f_k is stagewise composition of ω-germ transformers; tower coherence is preserved by a two-line diagram chase. *II.D40 — Identity Map*: id_x = {id_k} is the constant family assigning the identity on ℤ/P_kℤ at each stage; both left and right identity laws hold trivially. *II.D41 — HolEnd_τ Category*: objects are τ-admissible points, morphisms are ω-germ transformers, composition is stagewise, identity is the constant family; all category axioms are verified.
- **Key results:** *II.T29 — Associativity*: h ∘ (g ∘ f) = (h ∘ g) ∘ f. The proof has two steps: (1) stagewise equality follows from set-theoretic associativity of function composition on finite ℤ/P_kℤ; (2) coherent lift via the program monoid (*I.P02*, Book I) ensures that the equality lifts from words in the monoid to ω-germ transformers via the faithful correspondence provided by *II.T27*. Associativity is a theorem derived from axioms, not imported as a convention.
- **Structural results:** bipolar compatibility of composition — g ∘ f = e_+(g_+ ∘ f_+) + e_-(g_- ∘ f_-) — shows the B-channel and C-channel compose independently (idempotent orthogonality kills all cross-channel terms). The bipolar decomposition is functorial: the assignment f ↦ (f_+, f_-) defines a full and faithful functor HolEnd_τ → HolEnd_τ^(+) × HolEnd_τ^(-).
- **Dependencies:** *I.P02*, *I.D20*, *I.D47*, *I.D49*, *I.T10*, *I.T18*, *II.D01*, *II.D35*, *II.D36*, *II.D37*, *II.T25*, *II.T26*, *II.T27*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Hartogs.CategoryStructure` is planned.

## Where this leads

*HolEnd_τ* is the algebraic skeleton on which Parts VII–IX build. The immediate application is Chapter 35: the morphism spaces of *HolEnd_τ* carry a canonical Laurent expansion via bipolar spectral decomposition, and residues emerge as spectral coefficients at frequency n = −1 — computed by discrete Fourier transform rather than contour integration.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch33-composition-structure.tex -->
