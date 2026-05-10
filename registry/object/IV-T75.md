---
layout: registry-object
lane: registry
title: IV.T75 — τ-Yang--Mills Mass Gap Theorem
permalink: /registry/object/IV.T75/
registry_id: IV.T75
object_type: theorem
book: IV
book_slug: book-iv
part: 5
chapter: 41
scope: tau-effective
formalization: formalized
lean_module: TauLib.BookIV.Strong.YangMillsGap
lean_name: Tau.BookIV.Strong.YangmillsMassGapTheorem
summary: 'The tau-Yang-Mills Mass Gap Theorem: in the C-sector at E1 level, the strong
  vacuum Gamma_s^*[omega] has a positive spectral gap delta_infinity^s > 0, the gap
  mode g[omega] exists, and the gap is non-decreasing and spectrally isolated from
  below.'
depends_on:
- IV.D03
- IV.T122
depended_by: []
dep_count: 2
rev_dep_count: 0
is_foundational: false
is_central: false
---

## Bridge-layer note

This theorem closes **kernel-only** against Mathlib + `native_decide` — it carries no custom-axiom dependency. It is **Internally addressed** inside τ.

The corresponding [Yang–Mills Existence and Mass Gap Challenge Response]({{ '/results/challenge-responses/mathematics/canonical-benchmarks/yang-mills-existence-mass-gap/' | relative_url }}) is marked **Structurally constrained** (Partial) — *not* because `IV.T75` itself is incomplete, but because the formal bridge between the τ-internal mass-gap statement and the [Clay Yang–Mills statement on ℝ⁴](https://www.claymath.org/millennium-problems/yang-mills-the-maths-gap) is treated separately and is not yet Lean-formalized. This is the same pattern as the τ-internal Critical Line Theorem (`III.T19`) versus the classical Riemann Hypothesis bridge: a kernel-clean τ-internal result plus an unproven bridge to the orthodox classical statement. See the [Yang–Mills note on the Custom Axiom Inventory]({{ '/verify/custom-axioms/#yang-mills-note' | relative_url }}) for the full split.
