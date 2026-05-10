---
layout: challenge-response-entry
title: Yang–Mills Existence and Mass Gap — Challenge Response
short_title: Yang–Mills Existence and Mass Gap
permalink: /results/challenge-responses/mathematics/canonical-benchmarks/yang-mills-existence-mass-gap/
lane: results
v2_lane: results
type: Challenge Response
status: Canonical
domain: mathematics
domain_slug: mathematics
display_domain: Mathematics
cluster: canonical-benchmarks
challenge_family: canonical_benchmark
structural_challenge_id: CB-YANG-MILLS
challenge_slug: yang-mills-existence-mass-gap
challenge_url: /agenda/structural-challenge-ledger/mathematics/canonical-benchmarks/yang-mills-existence-mass-gap/
response_id: response-CB-YANG-MILLS
response_status: structurally_constrained
response_status_label: Structurally constrained
response_summary: The Corpus currently constrains, reframes, or materially supports an account of this problem.
response_rationale: Registry evidence gives a direct Corpus account or constraint.
registry_item_ids:
- IV.D176
- IV.D177
- IV.D179
- IV.D579
- IV.T75
registry_items:
- registry_id: IV.D176
  title: YM sector coupling
  relation: direct_problem_account
  confidence: high
  url: /registry/object/IV.D176/
  registry_path: registry/book-04/IV.D176-ym-sector-coupling.md
  rationale: Conservative domain scan matched Yang-Mills Existence and Mass Gap to Registry item IV.D176 through the rule
    terms yang, mills.
- registry_id: IV.D177
  title: Gap quantum
  relation: direct_problem_account
  confidence: high
  url: /registry/object/IV.D177/
  registry_path: registry/book-04/IV.D177-gap-quantum.md
  rationale: Conservative domain scan matched Yang-Mills Existence and Mass Gap to Registry item IV.D177 through the rule
    terms yang, mills.
- registry_id: IV.D179
  title: Orthodox Bridge Conjecture
  relation: direct_problem_account
  confidence: high
  url: /registry/object/IV.D179/
  registry_path: registry/book-04/IV.D179-orthodox-bridge-conjecture.md
  rationale: Conservative domain scan matched Yang-Mills Existence and Mass Gap to Registry item IV.D179 through the rule
    terms yang, mills.
- registry_id: IV.D579
  title: Yang--Mills on tau3
  relation: direct_problem_account
  confidence: high
  url: /registry/object/IV.D579/
  registry_path: registry/book-04/IV.D579-yang-mills-on-tau3.md
  rationale: Conservative domain scan matched Yang-Mills Existence and Mass Gap to Registry item IV.D579 through the rule
    terms yang, mills.
- registry_id: IV.T75
  title: τ-Yang--Mills Mass Gap Theorem
  relation: direct_problem_account
  confidence: high
  url: /registry/object/IV.T75/
  registry_path: registry/book-04/IV.T75-yang-mills-mass-gap-theorem.md
  rationale: Conservative domain scan matched Yang-Mills Existence and Mass Gap to Registry item IV.T75 through the rule terms
    yang, mills.
result_refs: []
verification_route: formal_proof_checking
verification_status: pending_external_review
external_status: externally_open
external_review_boundary: External mathematical review of the τ formulation, comparison against orthodox proofs/disproofs,
  and assessment of the bridge between τ-internal results and standard mathematical statements.
legacy_provenance:
  v1_problem_ledger_id: math-yang-mills-existence-mass-gap
  v1_provenance_kind: promoted_one_to_one
  v1_answer_recovered_from: f534b3fb^
tags:
- challenge-response
- mathematics
summary_short: The Corpus currently constrains, reframes, or materially supports an account of this problem.
---

The τ-internal mass-gap theorem `IV.T75` closes **kernel-only** against Mathlib + `native_decide` alone — no custom-axiom dependency. The reason this Challenge Response carries a **Structurally constrained** status rather than **Internally addressed** is the *bridge layer*: the formal correspondence between the τ-formulation of Yang–Mills and the [Clay Yang–Mills statement on ℝ⁴](https://www.claymath.org/millennium-problems/yang-mills-the-maths-gap) is treated separately and not yet formally bridged via Lean. This is the same pattern as the Master Schema → classical Riemann Hypothesis split: a τ-internal kernel-only result plus an unproven bridge to the orthodox classical statement. See the [Yang–Mills note on the Custom Axiom Inventory]({{ '/verify/custom-axioms/#yang-mills-note' | relative_url }}) for the full split, and [`IV.T75`]({{ '/registry/object/IV.T75/' | relative_url }}) for the kernel-only theorem itself. The bridge layer is the program's open work; `IV.T75` is not axiom-dependent.
