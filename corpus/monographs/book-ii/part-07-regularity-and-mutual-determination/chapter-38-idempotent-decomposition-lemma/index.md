---
layout: "corpus-monograph-chapter"
title: "Chapter 38: Idempotent Decomposition Lemma"
permalink: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-38-idempotent-decomposition-lemma/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-regularity-and-mutual-determination"
chapter_number: 38
chapter_slug: "chapter-38-idempotent-decomposition-lemma"
page_in_book: 193
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-37-sheaf-coherence-from-omega-germ-compatibility/"
prev_chapter_title: "Chapter 37: Sheaf Coherence from ω-Germ Compatibility"
next_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-39-the-3-lemma-chain/"
next_chapter_title: "Chapter 39: The 3-Lemma Chain"
summary_short: "The bipolar idempotents e_± = (1 ± j)/2, already established algebraically in Book I, are shown to lift from scalars to holomorphic function spaces: every τ-holomorphic f decomposes canonically and functorially as f = e_+ f_+ + e_− f_−."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
canonical_part_title: "Regularity and Mutual Determination"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-38-idempotent-decomposition-lemma/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VII: Regularity and Mutual Determination"
      url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 26
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Part VI established the sheaf O_τ and its coherence properties; Part VII now turns to the **internal structure** of a τ-holomorphic function. The central observation is that the bipolar idempotents e_± = (1 ± j)/2, proved algebraically in Book I (I.D21), decompose not only scalars in H_τ but also functions. Given any τ-holomorphic f : τ³ → H_τ, define f_± := e_± · f. Because e_+² = e_+, e_−² = e_−, and e_+ · e_− = 0, the components f_± are orthogonal, and because e_+ + e_− = 1 they reconstruct f: the decomposition f = f_+ + f_− is exact. The content of *II.L07* (*Idempotent Decomposition Lemma*) is that f_± are themselves τ-holomorphic — holomorphicity is preserved by the idempotent projection. This is not obvious: the projection operator e_+ is a ring element, not a morphism of the ambient category, so passing holomorphicity through it requires checking the CRT coherence and staging conditions for the projected map. The proof uses the idempotent identities (I1)–(I4): idempotence ensures no information is lost, orthogonality ensures no channel leaks into the other, and completeness ensures reconstruction is lossless. The decomposition is **canonical** (no choices are made — e_± are fixed by the algebraic structure) and **functorial**: for composable holomorphic maps g ∘ f, the components satisfy (g ∘ f)_± = g_± ∘ f_±, so the B and C channels do not mix under composition. *II.D48* (*Canonical Decomposition*) formalizes the data, and *II.P09* establishes the functoriality. This lemma is the engine for the three-lemma chain in Chapter 39: it converts the algebraic idempotent splitting of H_τ into a functional splitting of O_τ(τ³), enabling the holomorphic ↔ idempotent-supported equivalence.

## What this chapter contributes

**Definitions / Axioms**
- *II.D48* — Canonical Decomposition: the unique splitting f = e_+ f_+ + e_− f_− for any τ-holomorphic f, with f_± := e_± · f τ-holomorphic

**Key results**
- *II.L07* — *Idempotent Decomposition Lemma*: the algebraic idempotent splitting of H_τ lifts to a canonical, functorial, complete functional splitting of the holomorphic function space O_τ(τ³)
- *II.P09* — Functoriality: (g ∘ f)_± = g_± ∘ f_±; the bipolar channels do not mix under composition

**Notation**
- f_± := e_± · f for the B/C channel components of a holomorphic function; O_τ(τ³) for the holomorphic function space on τ³

**Dependencies**
- *I.T05* (Prime Polarity), *I.T10* (split-complex forcing), *I.D20*, *I.D21* (bipolar idempotents Book I), *II.D35* (calibrated split-complex codomain), *II.T27* (Mutual Determination), *II.D37* (evolution operator), *II.D45* (canonical holomorphic basis), *II.T31*

## Lean coverage

`BookII.Regularity.IdempotentDecomposition` (planned). No Lean proofs present at this writing.

## Where this leads

II.L07 is the direct prerequisite for the three-lemma chain (Chapter 39), which uses Branch Factorization, Prime-Split Support, and Polarity Symmetry to prove the full equivalence τ-holomorphic ↔ idempotent-supported (II.T33). That equivalence in turn grounds the positive regularity criterion (Chapter 40) and the Pre-Yoneda embedding (Chapter 41).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part07/ch37-idempotent-decomposition.tex -->
