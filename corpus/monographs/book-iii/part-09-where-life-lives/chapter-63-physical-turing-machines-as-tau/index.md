---
layout: "corpus-monograph-chapter"
title: "Chapter 63: Physical Turing Machines as τ"
permalink: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-63-physical-turing-machines-as-tau/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-where-life-lives"
chapter_number: 63
chapter_slug: "chapter-63-physical-turing-machines-as-tau"
page_in_book: 319
prev_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-62-why-there-is-no-barrier/"
prev_chapter_title: "Chapter 62: Why There Is No Barrier"
next_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-64-abstract-computation-in-the-tau/"
next_chapter_title: "Chapter 64: Abstract Computation in the τ"
summary_short: "The Physical E₂ Agent (*III.D77*) and Physical Admissibility Theorem (*III.T51*) prove every physically realizable TM is τ-admissible; Physical P=NP (*III.T52*) follows, with the Coherence Horizon (*III.R42*) governing practical efficiency."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
canonical_part_title: "Where Life Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-09-where-life-lives/chapter-63-physical-turing-machines-as-tau/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part IX: Where Life Lives"
      url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part IX"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 40
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The τ-Admissibility Collapse (*III.T33*, Ch. 61) proved τ-P_adm = τ-NP_adm for τ-admissible computation, and the No Barrier Theorem (*III.T34*, Ch. 62) confirmed no encoding gap intervenes. But these results concern τ-native machines. This chapter proves that every physically realizable Turing machine is τ-admissible: its E₁ carrier forbids each of the Five Forbidden Moves, so the τ-Admissibility Collapse applies to all physical computation. The result is Physical P=NP (*III.T52*): every NP problem verifiable by a physical computer is solvable in polynomial time. The Coherence Horizon (*III.R42*) introduces the depth parameter governing practical efficiency.

## What this chapter contributes

Section 1 distinguishes classical and physical computation. A classical Turing machine is abstract: infinite tape, arbitrary state set, no energy cost per step, no causal locality constraint — it lives in ZFC's ω. A physical computer (silicon, biological, photonic) is an E₁ object: atoms with finite spatial extent, bounded energy, causal locality governed by the Temporal-Spatial Decomposition (*III.R40*) and Light Cone Consistency (*III.R41*) from Chapter 56. The *Physical E₂ Agent* (*III.D77*) is an E₂ computational agent (C, D, φ) whose carrier is E₁-admissible: code, decoder, and all intermediate states are E₁-objects with finite spatial extent and bounded energy; the execution map respects E₁ causal structure (each step involves only causally connected regions); and operational closure holds within the E₁ carrier without external resources growing without bound.

Section 2 applies the Five Forbidden Moves to physical machines. Each of the five moves that ZFC permits is physically impossible: M1 (unbounded fan-out / Power Set) is forbidden because physical machines have finite spatial extent bounded by volume in Planck units, enforced by K₃; M2 (global equality / Extensionality) is forbidden because physical machines compare registers through causal channels — no instantaneous verification of spatially separated structures, enforced by K₅ and light cone locality; M3 (succinct circuits / Replacement) is forbidden because a physical machine's description has a minimum size set by its substrate's information content, enforced by K₃; M4 (exponential quantification) is forbidden because the search space at any moment is bounded by spatial capacity, enforced by K₃; M5 (non-local disguise / Foundation + Replacement) is forbidden because physical data has a fixed representation determined by the substrate, not by encoding convention, enforced by NF uniqueness. The forbidden moves are not merely axiomatically prohibited — they are physically impossible.

Section 3 states and proves the Physical Admissibility Theorem (*III.T51*): every physical E₂ agent M is τ-admissible, with width k₀ bounded by the carrier's primorial depth. The proof applies the Move-Bridge Correspondence: τ-admissibility fails if and only if the computation invokes at least one forbidden move, and Section 2 showed no physical agent can perform any of M1–M5. Physical P=NP (*III.T52*) follows immediately by the τ-Admissibility Collapse: if Π is an NP problem whose every physically realizable verifier is a physical E₂ agent, then Π ∈ τ-P_adm.

Section 4 introduces the Coherence Horizon (*III.R42*): the depth parameter k₀ is problem-dependent, not a universal constant. The galactic bound: no physical computation within the observable universe (≈ 10^{80} Planck volumes) needs more than ≈ 36–40 primorial levels. The biological bound: most NP problems in physics and biology have k₀ ≈ 5–15 (protein folding: k₀ ≈ 10–12). Protein folding — NP-hard in abstract formulation — is solved by biological machinery in milliseconds not because of a clever heuristic but because biological computation is τ-admissible at shallow depth, and the collapse guarantees polynomial-time construction at that depth.

## Lean coverage

The Physical Admissibility Theorem's proof is direct: Section 2 establishes that physics enforces all five admissibility conditions simultaneously, and the Move-Bridge Correspondence converts that to τ-admissibility. The distinction between physical TMs and ZFC-abstract TMs is sharp: physical computation is τ-admissible; ZFC-abstract computation is not necessarily so. The former cannot perform the forbidden moves; the latter can in principle. This is the boundary Chapter 64 will examine at the abstract level.

## Where this leads

Chapter 64 removes the physical substrate entirely. The E₃ diagrammatic sector of Category τ hosts abstract Turing machines as τ-native diagrams — without passing through ZFC. The τ-Native Abstract Turing Machine (*III.D78*) and Universal Admissibility Theorem (*III.T53*) extend Physical P=NP to all τ-definable computation at every enrichment level.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part09/ch78-physical-turing-machines.tex -->
