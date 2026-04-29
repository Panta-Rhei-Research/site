---
layout: "corpus-monograph-chapter"
title: "Chapter 64: Abstract Computation in the τ"
permalink: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-64-abstract-computation-in-the-tau/"
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
chapter_number: 64
chapter_slug: "chapter-64-abstract-computation-in-the-tau"
page_in_book: 323
prev_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-63-physical-turing-machines-as-tau/"
prev_chapter_title: "Chapter 63: Physical Turing Machines as τ"
next_chapter_url: "/corpus/monographs/book-iii/part-09-where-life-lives/chapter-65-the-zfc-provability-horizon/"
next_chapter_title: "Chapter 65: The ZFC Provability Horizon"
summary_short: "The τ-Native Abstract TM (*III.D78*) defines computation as an E₃ diagrammatic object without ZFC; the Universal Admissibility Theorem (*III.T53*) proves τ-P = τ-NP universally; *III.R43* diagnoses ZFC's openness as an artifact of actual infinity."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-09-where-life-lives/"
canonical_part_title: "Where Life Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-09-where-life-lives/chapter-64-abstract-computation-in-the-tau/"
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

{% raw %}
Chapter 63 embedded computation in physics: a physical E₂ agent hosted on E₁ hardware inherits τ-admissibility (*III.T51*) and therefore Physical P=NP (*III.T52*). This chapter removes the physical substrate entirely. The E₃ diagrammatic sector of Category τ hosts abstract Turing machines as τ-native diagrams — without passing through ZFC. The τ-Native Abstract Turing Machine (*III.D78*) defines computation directly as a compatible family of finite functions on the primorial tower; the Universal Admissibility Theorem (*III.T53*) proves τ-P = τ-NP universally within Category τ at all enrichment levels. The chapter also diagnoses ZFC's P vs NP openness as an artifact of actual infinity (*III.R43*): ZFC's proliferating infinity enables the Five Forbidden Moves; Category τ's earned algebraic infinity blocks them at every level.

## What this chapter contributes

Section 1 situates the E₃ diagrammatic sector. At E₃, proof theory is formalised as a mathematical object: formal systems — including ZFC — are E₂ virtual machines, visible as objects within the E₃ diagrammatic sector. Category τ at E₃ can define abstract computation directly as a categorical diagram in the primorial tower, without first encoding programs as ZFC sets.

Section 2 defines the τ-Native Abstract Turing Machine (*III.D78*). A TATM is a tuple (Q, Σ, δ, q₀, q_acc, q_rej, Tape) whose components are E₃-diagrammatic objects. The tape is a τ-presheaf on the primorial tower: a compatible family of finite functions {f_k: {1, …, Prim(k)} → Σ}_{k≥1} with f_{k+1}|_{{1,…,Prim(k)}} = f_k. The full tape is the inverse limit — potential infinity, not actual infinity. No single f_k is infinite; the infinity is in the tower of levels, not in any one level. This contrasts directly with a classical TM, whose tape ℕ → Σ requires the Axiom of Infinity for ω as a completed set.

Section 3 proves tower boundedness blocks all Five Forbidden Moves even at E₃ without physical hosting. At depth k: fan-out is bounded by Prim(k) through K₃ (not 2^n); succinct circuits are ruled out by K₃-bounded description length; quantifiers range over {1, …, Prim(k)} (not ω or uncountable sets); global equality is blocked by K₅ (sector-local equality); and non-local disguise is blocked by NF uniqueness. This uniformity across all enrichment levels is the content of *III.R43* (Actual vs Potential Infinity): the Five Forbidden Moves share a common root — they require actual infinity, a completed infinite set available for manipulation in one step. ZFC's Axiom of Infinity provides exactly this. Category τ has only potential infinity (the primorial tower is unbounded, but no single τ-object is infinite).

Section 4 states and proves Universal Admissibility (*III.T53*): every τ-native computational agent at any enrichment level E_n (n ∈ {0,1,2,3}) is τ-admissible, and τ-P = τ-NP universally within τ for all τ-definable problems. The proof assembles three steps: tower boundedness (at depth k, all objects have at most Prim(k) addresses, all transitions read O(1) channels, all quantifiers range over Prim(k)); forbidden moves blocked (the boundedness of step 1 prevents all five moves uniformly); admissibility (the Move-Bridge Correspondence then gives τ-admissibility, and the Admissibility Collapse *III.T33* applies). The three instantiations are: E₂ TTMs (Chapter 61), E₁-hosted physical TMs (*III.T51*, Chapter 63), and E₃ TATMs (this chapter). All share the same mechanism.

## Lean coverage

The terminological irony noted in *III.R43* is precise: in Category τ, the generator ω is a specific algebraic object — the unique crossing point of the lemniscate, a concrete τ-address — that *is* the one genuine actual infinity in the earned sense. In ZFC, ω begets 𝒫(ω) begets 𝒫(𝒫(ω)) — an unbounded hierarchy, each stage larger, none unique, none final. ZFC's infinity is paradoxically potential in the Aristotelian sense. Chapter 65 develops this inversion into the provability analysis.

## Where this leads

Chapter 65 asks whether the τ-native P=NP results — physical (*III.T52*) and abstract (*III.T53*) — can be stated and proved within ZFC. The Physical Realizability Predicate (*III.D79*) quantifies over all E₁ instantiations of a Turing machine — a host-level property that ZFC, operating at E₂, cannot capture. The asymmetric provability result follows: P ≠ NP cannot be a theorem of a sound ZFC, while the status of P = NP in ZFC remains open — likely independent, as the Continuum Hypothesis is.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part09/ch79-abstract-computation-in-tau.tex -->
{% endraw %}
