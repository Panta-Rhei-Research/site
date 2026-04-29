---
layout: "corpus-monograph-chapter"
title: "Chapter 39: The 3-Lemma Chain"
permalink: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-39-the-3-lemma-chain/"
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
chapter_number: 39
chapter_slug: "chapter-39-the-3-lemma-chain"
page_in_book: 201
prev_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-38-idempotent-decomposition-lemma/"
prev_chapter_title: "Chapter 38: Idempotent Decomposition Lemma"
next_chapter_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/chapter-40-regularity-as-positive-structure/"
next_chapter_title: "Chapter 40: Regularity as Positive Structure"
summary_short: "Three lemmas — Branch Factorization, Prime-Split Support, Polarity Symmetry — chain together to prove the Part VII characterization theorem: a function f : τ³ → H_τ is τ-holomorphic if and only if it is idempotent-supported."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-07-regularity-and-mutual-determination/"
canonical_part_title: "Regularity and Mutual Determination"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-39-the-3-lemma-chain/"
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

Chapter 38 established the Idempotent Decomposition Lemma (*II.L07*): every τ-holomorphic f : τ³ → H_τ decomposes canonically as f = e_+ f_+ + e_− f_−. That forward direction — holomorphic implies idempotent-decomposable — is only half the story. This chapter proves the **converse**: if f admits a decomposition f = e_+ f_+ + e_− f_− with each component satisfying the right support and coherence conditions, then f is τ-holomorphic. The proof chains three lemmas, each attacking a different structural layer. **Lemma 1** (*Branch Factorization*, *II.L08*): every ω-germ transformer factors through the bipolar idempotents e_±. This is the decomposition step — it shows that any putative holomorphic map must split along the B and C channels, with no cross-sector mixing. **Lemma 2** (*Prime-Split Support*, *II.L09*): the e_+-component is supported on B-channel primes (the γ-orbit), and the e_−-component on C-channel primes (the η-orbit), forced by Prime Polarity (I.T05, Book I). This is the localization step — it pins each component to the correct prime partition in the primorial tower, ruling out spurious support. **Lemma 3** (*Polarity Symmetry*, *II.L10*): the j-involution interchanges the two sectors, σ_j(G_+) = G_− and σ_j(G_−) = G_+, so the B and C channels carry symmetric information with no preferred status. This is the symmetry step — it ensures neither channel can dominate or absorb the other. The three steps combine as decomposition + localization + symmetry to characterize holomorphicity completely. *II.T33* (*Holomorphic ↔ Idempotent-Supported*) packages the equivalence: a function is τ-holomorphic if and only if its ω-germ transformer factors through the idempotents, has prime-split support, and respects polarity symmetry. This unifies the analytic viewpoint (holomorphy = complex-analytic regularity in the τ sense) with the algebraic viewpoint (idempotent support structure = membership in the correct two-sided ideal), completing the regularity program initiated in Chapter 38.

## What this chapter contributes

**Definitions / Axioms**
- (Idempotent-supported function, defined inline): a function f admitting f = e_+ f_+ + e_− f_− with f_± supported on the correct channel primes and satisfying tower coherence

**Key results**
- *II.L08* — *Branch Factorization*: every ω-germ transformer factors through the bipolar idempotents e_±
- *II.L09* — *Prime-Split Support*: e_+-component supported on B-channel (γ-orbit) primes; e_−-component on C-channel (η-orbit) primes, forced by Prime Polarity (I.T05)
- *II.L10* — *Polarity Symmetry*: j-involution σ_j interchanges G_+ and G_−; the two sectors carry symmetric information
- *II.T33* — *Holomorphic ↔ Idempotent-Supported*: full biconditional characterization of τ-holomorphy via idempotent support structure

**Notation**
- G_+, G_− for the B-channel and C-channel idempotent eigenspaces; σ_j for the j-involution on the function space

**Dependencies**
- *I.T05* (Prime Polarity), *I.D21*, *I.D22*, *I.D23* (spectral characters), *II.L07* (Idempotent Decomposition), *II.D48* (Canonical Decomposition), *II.T27* (Mutual Determination), *II.D37* (evolution operator), *II.D45* (canonical basis)

## Lean coverage

`BookII.Regularity.ThreeLemmaChain` (planned). No Lean proofs present at this writing.

## Where this leads

II.T33 is the direct prerequisite for the positive regularity criterion (Chapter 40, II.T34) and for the Pre-Yoneda embedding (Chapter 41, II.D50): holomorphicity must be characterized before it can be shown that holomorphic functions are themselves objects of τ³ and before regularity at a point can be defined as a stabilization condition.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part07/ch38-three-lemma-chain.tex -->
