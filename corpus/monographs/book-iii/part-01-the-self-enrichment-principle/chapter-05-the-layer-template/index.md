---
layout: "corpus-monograph-chapter"
title: "Chapter 5: The Layer Template"
permalink: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-05-the-layer-template/"
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
chapter_number: 5
chapter_slug: "chapter-05-the-layer-template"
page_in_book: 23
prev_chapter_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-04-the-self-enrichment-functor/"
prev_chapter_title: "Chapter 4: The Self-Enrichment Functor"
next_chapter_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-06-non-emptiness-and-strictness/"
next_chapter_title: "Chapter 6: Non-Emptiness and Strictness"
summary_short: "The uniform four-component template E_k = (Carrier, Predicate, Decoder, Invariant) — inherited from ABCD — organises all four enrichment layers (III.D05–D09). The invariant-to-carrier handoff links layers cumulatively; the decoder column shows monotone increase in self-reference."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/"
canonical_part_title: "The Self-Enrichment Principle"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-01-the-self-enrichment-principle/chapter-05-the-layer-template/"
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

The enrichment ladder has four rungs. At first glance, each looks different: E₀ speaks of NF addresses, E₁ of sectors and couplings, E₂ of codes and phenotypes, E₃ of observers and meaning. Beneath these differences, every layer is organised by the same four-component structure inherited from the ABCD decomposition. The hyperfactorization theorem (*I.T04*) assigns every τ-object a unique quadruple Φ(x) = (A, B, C, D), where each component plays a distinct structural role: A = π(x) is the carrier, B = γ(x) the predicate, C = η(x) the decoder, D = α(x) the invariant. This four-fold structure is not a modelling choice but the unique decomposition guaranteed by the axioms — and the enrichment functor F_E preserves it. Each layer's invariant flows into the next layer's carrier (the handoff chain), and the decoder column shows a monotone increase in self-reference from external (E₀) to spectral (E₁) to internal (E₂) to self-modelling (E₃). The enrichment tower is cumulative: each layer contains all previous layers.

## What this chapter contributes

**Definitions / Axioms**
- *Layer template* (*III.D05*, τ-effective): E_k = (Carrier_k, Predicate_k, Decoder_k, Invariant_k). Carrier = raw material (class of objects at depth k). Predicate = admissibility gate (selection condition on well-formed objects). Decoder = canonical instrument (map extracting invariant information). Invariant = stable output (datum that survives passage to the next layer). The four slots correspond to ABCD: A → Carrier, B → Predicate, C → Decoder, D → Invariant. The template has exactly four slots because the ABCD decomposition has exactly four independent orbits (*I.T04*).
- *E₀ layer — Mathematics* (*III.D06*, τ-effective): E₀ = (Obj(τ) with NF addressing, NF-addressability, peel map Φ, O(τ³)). The invariant O(τ³) ≅ A_spec(𝕃) (*II.T40*) is the holomorphic structure that flows into E₁'s carrier.
- *E₁ layer — Physics* (*III.D07*, τ-effective): E₁ = (H_τ-enriched objects, sector admissibility (4+1), spectral projection P_α ⊕ P_π ⊕ P_γ ⊕ P_η ⊕ P_ω, sector couplings as canonical lifts of ι_τ). No free parameters — the "No Knobs" principle. Physical constants firewall: values in Books IV–V only.
- *E₂ layer — Computation* (*III.D08*, conjectural): E₂ = (self-referential codes, operational closure, phenotype map, error-correction capacity). The code–execute–code cycle: code → product → code. Life is computation physically instantiated. Full instantiation requires Books IV–VI.
- *E₃ layer — Metaphysics* (*III.D09*, conjectural): E₃ = (observers, self-model consistency, interpretation, self-awareness capacity). Saturation: a hypothetical E₄ collapses back to E₃ because self-modelling of self-modelling adds no new structure.

**Key results**
- *Template invariance* (τ-effective): the enrichment functor F_E preserves the four-component structure. (i) E_{k+1} has exactly carrier, predicate, decoder, invariant. (ii) The handoff holds: Invariant_k → Carrier_{k+1}. (iii) The predicate, decoder, and invariant at E_{k+1} are determined by the ABCD decomposition applied to Carrier_{k+1}. Proof: F_E is τ-internal and respects the ABCD decomposition; the four orbits of ρ are preserved under any internal functor.
- *Handoff chain*: O(τ³) → H_τ-enriched objects (E₀→E₁); sector couplings → self-referential codes (E₁→E₂); error-correction capacity → observers (E₂→E₃). No information from Invariant_k is lost in the passage to Carrier_{k+1} — the tower is cumulative.
- *Increasing self-reference*: external decoder (Φ acts from outside, E₀) → spectral decoder (projectors in enriched Hom spaces, E₁) → internal decoder (code carries its own reader, E₂) → self-modelling decoder (observer models decoding itself, E₃). Each step increases the degree of self-reference by one; saturation at E₃ says self-modelling of self-modelling adds nothing new.

**Notation**
- E_k = (Carrier_k, Predicate_k, Decoder_k, Invariant_k); A→Carrier, B→Predicate, C→Decoder, D→Invariant; handoff chain: Invariant_k → Carrier_{k+1}; four-layer reference table with books I–III/IV–V/VI/VII

**Dependencies**
- *I.T04* (Hyperfactorization), *I.T31* (Global Hartogs), *I.T41* (Bi-square), *I.D18* (Algebraic lemniscate)
- *II.T40* (Central Theorem), *III.D04* (Enrichment functor F_E)

## Lean coverage

The layer template *III.D05* and the four instantiations *III.D06*–*III.D09* are planned for `TauLib/BookIII/LayerTemplate.lean`. The E₀ definition (*III.D06*) and the template invariance result are τ-effective with explicit finite-depth formulations and are the highest-priority Lean targets in this chapter. The E₂ and E₃ definitions (*III.D08*, *III.D09*) are conjectural and have no planned Lean entry in Book III — their formalization depends on Books IV–VII content. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Chapter 6 earns two of the three pillars of the Canonical Ladder Theorem: Non-Emptiness (*III.T01*, every layer is inhabited with explicit constructive witnesses) and Strictness (*III.T02*, each inclusion is proper with irreducible type-mismatch obstructions). Saturation — the claim that E₄ collapses to E₃ — is proved in Chapter 7.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part01/ch05-the-layer-template.tex -->
