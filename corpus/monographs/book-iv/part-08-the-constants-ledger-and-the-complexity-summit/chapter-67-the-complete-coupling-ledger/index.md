---
layout: "corpus-monograph-chapter"
title: "Chapter 67: The Complete Coupling Ledger"
permalink: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-67-the-complete-coupling-ledger/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "IV"
book_slug: "book-iv"
part_number: 8
part_display: "Part VIII"
part_slug: "part-08-the-constants-ledger-and-the-complexity-summit"
chapter_number: 67
chapter_slug: "chapter-67-the-complete-coupling-ledger"
page_in_book: 361
prev_chapter_url: "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/chapter-66-the-unified-regime-table/"
prev_chapter_title: "Chapter 66: The Unified Regime Table"
next_chapter_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-68-the-ontological-layer-architecture/"
next_chapter_title: "Chapter 68: The Ontological Layer Architecture"
summary_short: "Every inter-sector coupling in the microcosm is a rational function of a single constant: ι<sub>τ</sub> = 2/(π + e) ≈ 0.341304. There are exactly four self-couplings…"
canonical_book_url: "/corpus/monographs/book-iv/"
canonical_book_title: "Book IV: Categorical Microcosm"
canonical_part_url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/"
canonical_part_title: "The Constants Ledger and the Complexity Summit"
publication_book_url: "/publications/books/book-iv/"
legacy_publication_url: "/publications/books/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/chapter-67-the-complete-coupling-ledger/"
right_rail:
  related:
    -
      title: "Book IV: Categorical Microcosm"
      url: "/corpus/monographs/book-iv/"
    -
      title: "Part VIII: The Constants Ledger and the Complexity Summit"
      url: "/corpus/monographs/book-iv/part-08-the-constants-ledger-and-the-complexity-summit/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iv/"
    -
      title: "Registry"
      url: "/registry/books/book-iv/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book IV"
    part: "Part VIII"
    layer: "E₁ Physics (Microcosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 50
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Every inter-sector coupling in the microcosm is a rational function of a single constant: ι_τ = 2/(π + e) ≈ 0.341304. There are exactly four self-couplings — one per primitive sector {D, A, B, C} — and six cross-couplings covering every unordered pair, for a total of ten entries. No fitted parameters appear anywhere in the ledger. The Standard Model, by contrast, requires 19 or more free parameters fitted to experiment. This chapter gathers all ten τ³ formulas into one canonical presentation, proves the three structural theorems that constrain them (Temporal Complement, Multiplicative Closure, Power Hierarchy), establishes positivity and the strict ordering of self-couplings, and states the No-Running Principle that sets τ³ apart from orthodox quantum field theory. The result is a derivation chain with a layered dependency DAG: from ι_τ at Layer 0, through the self-couplings at Layer 1, to the fine structure constant α and eventually the gravitational coupling α_G at deeper layers — all derived, none fitted.

## What this chapter contributes

- **Definitions / Axioms:** *IV.D04 — Self-Coupling Ledger* (τ-effective); *IV.D05 — Cross-Coupling Ledger* (τ-effective); *IV.D07 — No-Running Principle* (τ-effective). The self-couplings are κ(D;1) = 1 − ι_τ, κ(A;1) = ι_τ, κ(B;2) = ι_τ², κ(C;3) = ι_τ³/(1 − ι_τ); the six cross-couplings are products of the relevant self-couplings, inheriting the confinement denominator from the C-sector where appropriate.
- **Key results:** *IV.T01 — Temporal Complement* (τ-effective): κ(A;1) + κ(D;1) = 1 — gravity and the weak force partition the depth-1 coupling budget without remainder. *IV.T02 — Temporal Multiplicative Closure* (τ-effective): κ(A,D) = κ(A;1)·κ(D;1), so the weak–gravity cross-coupling carries no independent information beyond the self-couplings. *IV.P01 — Power Hierarchy* (τ-effective): κ(B;2) = κ(A;1)², κ(A,B) = κ(A;1)³ — primorial depth literally exponentiates the master constant. *IV.P03 — All Couplings Positive and Strictly Ordered* (τ-effective): κ(C) < κ(B) < κ(A) < κ(D), inverting the conventional force-strength ordering because the "strong" force operates at the deepest primorial level.
- **Notation introduced:** ι_τ for the master constant; κ(S;d) for self-couplings at sector S, primorial depth d; κ(S_i, S_j) for cross-couplings.
- **Dependencies:** Book I axioms K0–K6 (sector structure); Book III No Knobs Principle (all couplings from ι_τ alone); Chapter 66 (import of sector template from Book III).

## Lean coverage

`CouplingFormulas.lean` contains `temporal_complement`, `temporal_multiplicative`, `em_is_weak_squared`, `weak_strong_is_multiplicative`, `all_formulas_positive`, and `self_coupling_order` — all proved without sorry. The complete ledger is mechanically verified at the level of rational arithmetic in ι_τ.

## Where this leads

With the full coupling table in hand, Chapter 68 introduces the three-layer ontological architecture that explains where these formulas live and why they are scale-invariant, setting up the Running vs. Readout resolution of Chapter 69.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-04/part08/ch67-complete-coupling-ledger.tex -->
