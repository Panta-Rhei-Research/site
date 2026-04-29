---
layout: "corpus-monograph-chapter"
title: "Chapter 44: BH SelfDesc: The ω-Germ Code"
permalink: "/corpus/monographs/book-vi/part-07-cosmic-life/chapter-44-bh-selfdesc-the-omega-germ-code/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-cosmic-life"
chapter_number: 44
chapter_slug: "chapter-44-bh-selfdesc-the-omega-germ-code"
page_in_book: 261
prev_chapter_url: "/corpus/monographs/book-vi/part-07-cosmic-life/chapter-43-the-bh-carrier-and-its-canonical-distinction/"
prev_chapter_title: "Chapter 43: The BH Carrier and Its Canonical Distinction"
next_chapter_url: "/corpus/monographs/book-vi/part-07-cosmic-life/chapter-45-bh-as-omega-representatives-and-the-lift/"
next_chapter_title: "Chapter 45: BH as ω-Representatives and the Lift"
summary_short: "The BH SelfDesc theorem is established by defining the evaluator Eval^BH via DecodeTarget(B_n) and DecodeHorizon(B_n). Uniqueness and constancy lemmas…"
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-07-cosmic-life/"
canonical_part_title: "Cosmic Life"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-07-cosmic-life/chapter-44-bh-selfdesc-the-omega-germ-code/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part VII: Cosmic Life"
      url: "/corpus/monographs/book-vi/part-07-cosmic-life/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part VII"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 66
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

Chapter 43 established that the macro-torus carrier *T(H_BH)* possesses a τ-Distinction: the event horizon is a clopen, refinement-coherent, eventually stable, law-stable, H∂-equivariant self/non-self boundary. A sharp boundary is necessary for Life but not sufficient — a dead cell retains its membrane, and a neutron star has a well-defined surface. What separates a living system from a merely bounded one is the capacity to internally decode its own boundary from a stored code. This chapter verifies that capacity for the BH carrier, completing the two-predicate certification. The BH SelfDesc theorem is τ-effective and definitional: the verification proceeds from general relativity, not from analogy with biology.

The decisive simplification is the No-Hair Theorem. For a general biological carrier the blueprint ball B_n is a rich high-dimensional object; for the BH it collapses to a single point at every refinement level, because the Kerr–Newman solution is the unique minimizer of the lexicographic defect functional. DecodeTarget therefore selects the exact Kerr geometry as phenotype target at every n, and DecodeHorizon returns the same horizon code (M, J, Q) independent of blueprint ball radius. Ringdown — quasi-normal mode oscillations that exponentially damp near-horizon perturbations toward the Kerr state — is the physical process that realizes Eval^BH: given the code (M, J, Q) and the current normal form NF_n(x), the evaluator compares r(x) against r₊(M, J, Q) and returns the correct distinction value. The entire loop — code → target → evaluate → damp → return — operates without external input, using only the Einstein field equations on the carrier's own geometry.

## What this chapter contributes

**Definitions / Axioms**
- *VI.D58* — BH DecodeTarget: the argmin of V^BH_n over the blueprint ball, uniquely selecting the Kerr–Newman solution at every refinement level.
- *VI.D59* — BH DecodeHorizon: the operator returning the constant horizon code c^BH = (M, J, Q) for all elements of the blueprint ball at all refinement levels.
- BH Evaluator Eval^BH: the morphism code(D^BH)[ω] × NF_n(x) → D^BH_n realized physically by ringdown dynamics.
- BH ω-Germ Code: the profinite object code(D^BH)[ω] ≅ (M, J, Q), the projective limit that stabilizes after one step.

**Key results**
- *VI.L09* — BH Uniqueness Lemma: DecodeTarget selects a unique element at every refinement level, proved from the Israel–Carter–Robinson uniqueness theorem.
- *VI.L10* — BH Constancy Lemma: DecodeHorizon returns the same code independent of blueprint ball radius and refinement level, proved from immediate stabilization and horizon-data locality.
- *VI.T30* — BH SelfDesc Theorem: (D^BH, Eval^BH) is a SelfDesc pair on *T(H_BH)*, with completeness, internality, and refinement coherence all verified. Hawking evaporation is identified as code degradation beyond the SelfDesc basin — the BH analogue of death — with evaporation timescale ~10⁶⁷ yr for stellar-mass carriers.

**Notation**
- *B^BH_n*: BH blueprint ball; *c^BH*: horizon code; *Eval^BH*: BH evaluator; *code(D^BH)[ω]*: ω-germ code ≅ (M, J, Q).

**Dependencies**
- *VI.T29* (BH Distinction Theorem, Chapter 43); abstract SelfDesc predicate and SelfDesc Closure Theorem (Chapter 5); No-Shrink Theorem (*V.T114*).

## Lean coverage

*TauLib.BookVI.Cosmic.BHSelfDesc* — covers the BH blueprint ball, DecodeTarget, DecodeHorizon, the Uniqueness and Constancy Lemmas, and the three-condition proof of *VI.T30*. Evaluator realization by ringdown is prose commentary on the formalization.

## Where this leads

With both τ-Distinction (*VI.T29*) and SelfDesc (*VI.T30*) verified, the BH carrier satisfies the Life Loop Class criterion. Chapter 45 asks what kind of object a BH is within the full space of ω-germ codes — establishing it as an ω-representative and introducing the Lift_ω constructor that builds BH codes from the primorial ladder.

<!-- regenerated 2026-04-29 | source: manuscript-sources/book-06/part07/ch44-bh-selfdesc.tex -->
