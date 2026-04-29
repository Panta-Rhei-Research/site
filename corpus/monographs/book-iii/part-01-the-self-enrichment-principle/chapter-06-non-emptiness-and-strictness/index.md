---
layout: "corpus-monograph-chapter"
title: "Chapter 6: Non-Emptiness and Strictness"
permalink: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-06-non-emptiness-and-strictness/"
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
chapter_number: 6
chapter_slug: "chapter-06-non-emptiness-and-strictness"
page_in_book: 29
prev_chapter_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-05-the-layer-template/"
prev_chapter_title: "Chapter 5: The Layer Template"
next_chapter_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/chapter-07-saturation-at-e/"
next_chapter_title: "Chapter 7: Saturation at E₃"
summary_short: "Non-Emptiness (III.T01) and Strictness (III.T02) — two of the three pillars of the Canonical Ladder Theorem. The E₁ witness (III.P01) is the bipolar Hom object [A,B] carrying irreducible split-complex module structure absent from E₀. Defect hierarchy: primordial ⊂ spectral ⊂ code ⊂ model."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-01-the-self-enrichment-principle/"
canonical_part_title: "The Self-Enrichment Principle"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-01-the-self-enrichment-principle/chapter-06-non-emptiness-and-strictness/"
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

The Canonical Ladder Theorem rests on three pillars: each enrichment layer is non-empty, each inclusion is proper, and the tower saturates at E₃. Chapter 5 defined the four-component layer template; this chapter earns the first two pillars. Non-emptiness (*III.T01*) requires constructive witnesses at each layer: at E₀ and E₁ explicit objects are produced, while E₂ and E₃ carry precise forward references to Parts VI and VII. Strictness (*III.T02*) requires obstruction arguments — for each step from E_{k−1} to E_k the chapter exhibits a characteristic object, obstructs any attempt to reduce it to E_{k−1} data by identifying an irreducible type mismatch, and classifies the new defect class that first becomes non-empty at E_k. At E₁ the obstruction is fully proved: the bipolar Hom object [A,B] = e₊·[A,B]₊ + e₋·[A,B]₋ carries split-complex module structure that cannot be expressed as a scalar NF address — module type versus scalar type is an irreducible mismatch. The same schema (exhibit → obstruct → classify) applies at E₂ (operational closure vs. passive structure) and E₃ (second-order vs. first-order fixed point), yielding the defect hierarchy primordial ⊂ spectral ⊂ code ⊂ model.

## What this chapter contributes

**Definitions / Axioms**
- *Defect hierarchy*: E₀ admits primordial defects (failures of tower coherence, detected by CRT); E₁ adds spectral defects δ_spec(f) = e₊·f·e₋ + e₋·f·e₊ (off-diagonal mixing between bipolar sectors — the spectral purity condition of τ-RH is δ_spec = 0 on the critical locus); E₂ adds code defects (non-termination, bit-flip, null phenotype — failures of the code→execute→code cycle); E₃ adds model defects (self-reference paradox, model incompleteness, observer drift). Each layer inherits all prior defect classes.

**Key results**
- *Non-Emptiness Theorem* (*III.T01*, τ-effective at levels 0–1, forward reference at 2–3): (1) E₀ inhabited — any τ-object with NF address, witness: α with NF(α) = (1), plus tower-coherent reduction maps. (2) E₁ inhabited — H_τ-enriched Hom object [A,B] for A, B in distinct spectral sectors of the ABCD chart; by *I.T12* both [A,B]₊ ≠ 0 and [A,B]₋ ≠ 0; enriched composition maps are E₁-morphisms (*II.D53*). (3) E₂ inhabited (preview, Part VI) — rational point on a BSD curve of positive rank, satisfying the operational closure cycle. (4) E₃ inhabited (preview, Book VII) — self-modelling code with consistent interpretation functor.
- *E₁ Strictness Witness* (*III.P01*, τ-effective): let A, B ∈ E₀ lie in distinct spectral sectors. Then [A,B] ∈ E₁ with non-trivial bipolar decomposition ([A,B]₊ ≠ 0, [A,B]₋ ≠ 0), but [A,B] ∉ E₀. Proof: (i) self-enrichment (*II.D53*) provides H_τ-module structure; (ii) *I.T12* (spectral decomposition) guarantees both components are non-zero for cross-sector objects; (iii) the NF address of [A,B] as an E₀-object records which object it is but carries no idempotent splitting, no j²=+1 unit, no bipolar projection — the type mismatch (scalar vs. module) is irreducible.
- *Strictness Theorem* (*III.T02*, τ-effective at k=1, forward reference at k=2,3): E₀ ⊊ E₁ ⊊ E₂ ⊊ E₃. The proof schema is uniform: exhibit (construct x_k ∈ E_k with characteristic feature φ_k), obstruct (φ_k cannot be encoded in E_{k−1} data types), classify (identify new defect class non-empty at E_k and vacuous at E_{k−1}).
- *Connection to spectral defects and RH* (τ-effective, remark): the spectral purity condition δ_spec(f) = 0 on the critical locus — the τ-effective Riemann Hypothesis — is precisely the condition that spectral defects vanish at the boundary, preventing bipolar leakage that would destroy the local-to-global gluing of bulk projections.

**Notation**
- δ_spec(f) = e₊·f·e₋ + e₋·f·e₊ (spectral defect); E₀ ⊊ E₁ ⊊ E₂ ⊊ E₃; proof schema: exhibit → obstruct → classify; defect hierarchy: primordial ⊂ spectral ⊂ code ⊂ model

**Dependencies**
- *I.T04* (Hyperfactorization), *I.T12* (Spectral decomposition), *I.D18* (Algebraic lemniscate)
- *II.T36* (Yoneda embedding), *II.D53* (Self-enrichment structure), *III.D05* (Layer template)

## Lean coverage

The Non-Emptiness Theorem *III.T01* (levels 0 and 1) and E₁ Strictness Witness *III.P01* are planned for `TauLib/BookIII/NonEmptinessStrictness.lean`. The E₁ witness proof (*III.P01*) is the highest-priority Lean target: the type-mismatch argument is fully explicit and constructive at each primorial depth k, reducing to a check that (ℤ/M_kℤ) scalar data cannot represent (ℤ/M_kℤ)[j]/(j²−1) module structure. The spectral defect formula δ_spec is a straightforward algebraic computation in H_τ and is a secondary Lean target. Levels 2 and 3 of *III.T01* carry forward references and have no planned Lean entry in Book III. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Chapter 7 proves the third and deepest pillar — Saturation (*III.T03*): a hypothetical E₄ = [E₃ᵒᵖ, E₃] collapses back into E₃ because the 4-orbit closure of ρ ensures no fifth orbit channel exists for genuinely new structure.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part01/ch06-non-emptiness-and-strictness.tex -->
