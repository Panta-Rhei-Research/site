---
layout: "corpus-monograph-chapter"
title: "Chapter 13: The No Knobs Principle"
permalink: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-13-the-no-knobs-principle/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 2
part_display: "Part II"
part_slug: "part-02-the-4-1-sector-template"
chapter_number: 13
chapter_slug: "chapter-13-the-no-knobs-principle"
page_in_book: 75
prev_chapter_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-12-the-parity-bridge-theorem/"
prev_chapter_title: "Chapter 12: The Parity Bridge Theorem"
next_chapter_url: "/corpus/monographs/book-iii/part-03-the-spectral-algebra/chapter-14-the-primorial-ladder/"
next_chapter_title: "Chapter 14: The Primorial Ladder"
summary_short: "Capstone of Part II: all 10 inter-sector couplings are canonically determined by ι_τ = 2/(π+e). The No Knobs Principle (III.T08) proves the framework has no free parameters; the No Knobs Ledger (III.D18) catalogs all couplings as rational functions of ι_τ. Part II export contracts delivered."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/"
canonical_part_title: "The 4+1 Sector Template"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-02-the-4-1-sector-template/chapter-13-the-no-knobs-principle/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part II: The 4+1 Sector Template"
      url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part II"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 33
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Part II has derived the 4+1 sector template and proved the Parity Bridge Theorem. One structural question remains: how strong is each inter-sector coupling? This chapter proves there is no freedom in the answer. Every coupling between the four primitive sectors is a canonical rational function of the master constant ι_τ = 2/(π + e) ≈ 0.341304 evaluated at a specific primorial depth. The mechanism is the crossing point x₀ ∈ 𝕃: every boundary character's value at x₀ is a power of ι_τ — χ_{(m,n)}(x₀) = ι_τ^{|m|+|n|} — and the Langlands₀ functor Φ, being monoidal, extends this to all interior couplings. Four primitive sectors admit C(4,2) + 4 = 10 distinct couplings; the No Knobs Ledger (*III.D18*) catalogs all 10 as κ(S_i, S_j) = f_{ij}(ι_τ, M_d), where f_{ij} is determined by the character exponents and M_d is the stabilization primorial. The master constant ι_τ is not a parameter but a consequence of axioms K0–K6 — the canonical combination of the topological invariant of the boundary (π) and the eigenvalue of the iterator (e). The 10 ledger entries are 10 projections of a single datum, the crossing-point value, not 10 independent quantities.

## What this chapter contributes

**Definitions / Axioms**
- *Coupling function*: κ(S_i, S_j) = f_{ij}(ι_τ, M_d), where f_{ij} is a rational function determined by the character exponents of generators g_i and g_j, and M_d is the stabilization primorial depth. As d → ∞, f_{ij}(ι_τ, M_d) → ι_τ^{|g_i|+|g_j|} (pure power). Each coupling is computable at any finite depth as a rational number via explicit CRT arithmetic.
- *No Knobs Ledger* (*III.D18*, τ-effective): complete catalog of all 10 sector coupling functions — 4 self-couplings (D–D, A–A, B–B, C–C) of the form ι_τ^{2|g|} · r_k(M_d), and 6 cross-couplings (D–A, D–B, D–C, A–B, A–C, B–C) of the form ι_τ^{|g_i|+|g_j|} · r_k(M_d). Ledger is symmetric (κ(S_i, S_j) = κ(S_j, S_i)) and exhaustive. The B–C entry (Entry 10) is the original Book II crossing-point coupling extended to all pairs.

**Key results**
- *Universality of the crossing coupling* (τ-effective): every sector coupling factors through the crossing point x₀ ∈ 𝕃. Monoidality of Φ reduces ⟨Φ(χ_{g_i}), Φ(χ_{g_j})⟩ to χ_{g_i}(x₀) · χ_{g_j}(x₀) = ι_τ^{|m_i|+|n_i|+|m_j|+|n_j|}. No coupling depends on any parameter other than ι_τ and the primorial index.
- *No Knobs Principle* (*III.T08*, τ-effective): (i) Determination — every sector coupling is determined by ι_τ as κ(S_i, S_j) = f_{ij}(ι_τ, M_d). (ii) Completeness — the ledger contains all 10 distinct couplings and no coupling exists between primitive sectors not listed (the ω-sector mediates but does not constitute a sector of its own). (iii) Rigidity — no deformation κ' is compatible with Langlands₀ and the 4+1 decomposition unless κ' = κ (the inner product is fixed by the split-complex structure of H_τ and boundary holonomy normalization, both axiomatic).
- *One constant rules all* (τ-effective): the 10 ledger entries are 10 projections of a single datum — ι_τ — not 10 independent quantities. The apparent multiplicity of coupling constants is an artifact of sector decomposition of the character lattice.
- *Physical constants preview* (conjectural, firewall-separated): at E₁, B–B → α_EM ≈ 1/137; D–D → G_N; A–A → g_W; C–C → g_S; cross-couplings → mixing parameters. Values are outputs, not inputs. No physical constant appears as a mathematical object in Book III.
- *Part II export contracts* (*III.R07*): Parts IV–VI import the 4+1 template (*III.D13*); Part VI imports Langlands₀ (*III.D12*), Langlands₁ (*III.D15*), Parity Bridge (*III.T07*), and spectral polarity (*III.D17*); Part VII imports the No Knobs Ledger (*III.D18*) and Principle (*III.T08*); Books IV–V import the coupling functions κ(S_i, S_j).

**Notation**
- ι_τ = 2/(π + e) ≈ 0.341304 (master constant); χ_{(m,n)}(x₀) = ι_τ^{|m|+|n|} (crossing-point value); κ(S_i, S_j) = f_{ij}(ι_τ, M_d) (coupling function); No Knobs Ledger: 4 self-couplings + 6 cross-couplings = 10 total

**Dependencies**
- *III.D11* (Boundary character space), *III.D12* (Langlands₀), *III.T05* (Sector preservation)
- *III.D13* (4+1 decomposition), *III.D14* (ω-coupling), *III.D15* (Langlands₁), *III.T06* (Template invariance), *III.T07* (Parity Bridge), *III.D17* (Spectral polarity)
- *I.T41* (Bi-square), *II.T40* (Central Theorem)

## Lean coverage

The No Knobs Ledger *III.D18* is planned for `TauLib/BookIII/NoKnobs.lean` as a finite data structure: 10 coupling functions computable at each primorial depth. The universality of crossing coupling and Determination clause (i) of *III.T08* are the highest-priority Lean targets — both reduce to monoidality of Φ and the crossing-point formula. Completeness clause (ii) reduces to orbit counting. Rigidity clause (iii) requires the split-complex inner product characterization and is a secondary target. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Part III (beginning at Chapter 14) develops the spectral algebra — primorial ladder, CRT decomposition, Hensel lifting, local fields, and adelic embedding — that transforms the abstract coupling functions f_{ij}(ι_τ, M_d) into explicit rational numbers at each primorial depth, providing the computational engine for evaluating the No Knobs Ledger.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part02/ch13-the-no-knobs-principle.tex -->
