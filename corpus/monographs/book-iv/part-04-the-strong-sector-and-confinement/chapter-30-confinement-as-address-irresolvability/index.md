---
layout: "corpus-monograph-chapter"
title: "Chapter 30: Confinement as Address Irresolvability"
permalink: "/corpus/monographs/book-iv/part-04-the-strong-sector-and-confinement/chapter-30-confinement-as-address-irresolvability/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 4
part_display: "Part IV"
part_slug: "part-04-the-strong-sector-and-confinement"
chapter_number: 30
chapter_slug: "chapter-30-confinement-as-address-irresolvability"
page_in_book: 159
prev_chapter_url: "/corpus/monographs/book-iv/part-04-the-strong-sector-and-confinement/chapter-29-the-strong-vacuum-and-color-holonomy/"
prev_chapter_title: "Chapter 29: The Strong Vacuum and Color Holonomy"
next_chapter_url: "/corpus/monographs/book-iv/part-04-the-strong-sector-and-confinement/chapter-31-the-tau-gap-meta-theorem/"
next_chapter_title: "Chapter 31: The τ-Gap Meta-Theorem"
summary_short: "Confinement is address irresolvability: an isolated color charge cannot be given a consistent CR address on T². The flux tube, linear potential, and strong CP resolution all follow as structural consequences."
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-04-the-strong-sector-and-confinement/"
canonical_part_title: "The Strong Sector and Confinement"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-04-the-strong-sector-and-confinement/chapter-30-confinement-as-address-irresolvability/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part IV: The Strong Sector and Confinement"
      url: "/corpus/monographs/book-iv/part-04-the-strong-sector-and-confinement/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part IV"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 46
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Confinement — the absence of isolated quarks or gluons in any experiment — is conventionally framed as a dynamical puzzle: the color potential grows linearly, flux tubes form, and string-breaking produces hadrons rather than free color charges. In Category τ, the question shifts register entirely. Confinement is not a property of the potential; it is address irresolvability. A mode carrying net color cannot be given a consistent CR address on 𝕃 = S¹ ∨ S¹, because the η-holonomy cycles branches R → G → B → R, making any single-valued boundary projection impossible. This is a theorem, not a conjecture: only color-neutral combinations — mesons (q̄q), baryons (qqq), and exotic hadrons — admit CR addresses. The (1 − ιτ)⁻¹ denominator in κ(C;3) = ιτ³/(1 − ιτ) is the algebraic signature of this structural impossibility, and the standard consequences — linear potential, flux tube, string breaking, area law for Wilson loops — all emerge as corollaries. The chapter also resolves the strong CP problem: the SA-i admissibility condition forces Δ(η-winding) ≡ 0 (mod 3) in all C-sector transitions, excluding instantons and setting θ_QCD = 0 exactly, without fine-tuning and without an axion.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D47 — CR Address* (τ-effective): a consistent assignment addr(f) : 𝕃 → ℂ satisfying the τ-CR equations, such that f is recovered by τ-Hartogs extension from its boundary values. *IV.D48 — Color Flux Tube* (τ-effective): the narrow channel of concentrated color field between a separating q̄q pair, with cross-section ∼1 fm², constant energy density, and total energy E(r) ∼ σr where σ ≈ 0.9 GeV/fm. *IV.D49 — Strong CP Resolution via SA-i* (τ-effective): the SA-i admissibility condition requiring η-winding be preserved mod 3, structurally forbidding topological charge Q_top ≠ 0.
- **Key results:** *IV.T16 — Color Address Irresolvability* (τ-effective): a mode carrying net color has no consistent CR address; addr(f) is multi-valued on 𝕃 because η-holonomy cycles branches. Only color-neutral combinations are CR-addressable. *IV.T17 — Observable States Are Color-Neutral* (τ-effective): mesons (q̄q), baryons (qqq), antibaryons, and exotic hadrons (tetraquarks, pentaquarks, glueballs) are the complete set of admissible states. *IV.T18 — θ_QCD = 0 from C-Sector SA-i* (τ-effective): topological charge Q_top = n₊ − n₋ = 0, because SA-i (axioms K3 + K5) forbids Δ(η-winding) = ±1; no fine-tuning and no Peccei–Quinn symmetry required. *IV.T19 — Neutron EDM = 0 Exactly* (τ-effective): d_n ∝ θ_QCD = 0, giving d_n = 0 exactly, consistent with the experimental bound |d_n| < 1.8 × 10⁻²⁶ e·cm and stronger than mere suppression.
- **Dependencies:** III.T27 (Yang–Mills/Mass Gap guarantee for C-sector NF-discreteness); III.T28 (Hodge/Addressability guarantee); Chapter 29 (C-sector structure and η-holonomy).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module.

## Where this leads

Chapter 31 takes the C-sector's confining structure as its input and proves the τ-gap meta-theorem: any NF-discrete tower with contractive defect functional and bounded sector extraction has a positive spectral gap. The Yang–Mills mass gap follows as a direct corollary applied to the C-sector.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part04/ch30-confinement-admissibility.tex -->
