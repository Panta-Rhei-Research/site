---
title: "Structural Challenge Ledger v2.0"
date: 2026-05-04
change_type: "site-release"
summary_short: "Replaced the v1 Problem Ledger with the v2.0 Structural Challenge Ledger — 214 canonical items across mathematics, physics, life, and metaphysics, source-of-truth in the corpus repo with site projection."
affected_lanes:
  - program
  - results
  - corpus
right_rail:
  toc: false
  related:
    - title: "Structural Challenge Ledger"
      url: /agenda/structural-challenge-ledger/
    - title: "Research Agenda"
      url: /program/research-agenda/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

- **Agenda lane**: Promoted the [Structural Challenge Ledger]({{ '/agenda/structural-challenge-ledger/' | relative_url }}) — 214 canonical items across four domains (38 mathematics, 117 physics including 15 τ-native challenges, 29 life, 30 metaphysics).
- **Source-of-truth**: Items live in the corpus repo at `corpus/structural-challenge-ledger/items/<domain>/<cluster>/` alongside the registry, bibliography, and recovery requirements. The site is now a projection rather than the authoritative source.
- **Schema**: Each item carries domain-prefixed IDs (P001–P102, PN-01–PN-15, LIFE-SC-01–29, M-E3-01–29, MRC-01, S4–S18, F1–F18, CB-*), cluster + ring depth (R0–R6 for physics) or τ-register + ontic requirement (Reg_E/P/D/C, OR1–OR6 for metaphysics), challenge types, and cross-domain links between paired entries.
- **v1 retirement — clean cut**: Retired the v1 Problem Ledger and Problem Ledger Answers. All v1 URLs (`/program/research-agenda/problem-ledger/*`, `/results/problem-ledger-answers/*`) 301-redirect to the corresponding v2 SCL surfaces. Full v1 snapshot archived in `atlas/archive/problem-ledger-v1-snapshot-2026-05-04/`.
- **Cross-domain links**: 17 paired-entry cross-domain handoffs surface where the same problem appears in two domains (e.g. Yang-Mills as both a math Clay problem and a physics R0 foundational entry; abiogenesis on both physics R6 boundary and life origin clusters).
- **Navigation**: Added the Structural Challenge Ledger to the Agenda left-rail tree alongside other agenda surfaces.
