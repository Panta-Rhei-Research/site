---
layout: program-doc
title: "Formalization Status"
permalink: /verify/taulib/status/
lane: verify
summary_short: "Per-book statistics, axiom inventory, and sorry inventory for TauLib."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  - title: Scope Labels
    url: /verify/taulib/scope-labels/
  meta:
    type: "Dashboard"
    status: "Frozen"
    updated: "April 2026"
---

## Build Pin

{% assign build = site.data.verify.build %}

| Source | Revision | Reference |
|--------|----------|-----------|
| **TauLib** ({{ build.taulib.repo }}) | [`{{ build.taulib.commit_short }}`]({{ build.taulib.url }}/commit/{{ build.taulib.commit_sha }}) &middot; {{ build.taulib.commit_date }} | Apache&nbsp;2.0 &middot; [LICENSE]({{ build.taulib.license_url }}) |
| **Lean** | `{{ build.lean.version }}` | [lean-lang.org]({{ build.lean.url }}) |
| **Mathlib** | [`{{ build.mathlib.commit_short }}`]({{ build.mathlib.url }}/commit/{{ build.mathlib.commit_sha }}) | {{ build.mathlib.policy }} |

The 445 API-doc pages in `/verify/taulib/docs/` were generated from TauLib commit `{{ build.taulib.commit_short }}` via `scripts/import_taulib_docs.py` + `scripts/convert_taulib_html_to_md.py`. To reproduce locally, clone the repo at that commit and run `lake build`.

---

## Summary

| Metric | Value |
|--------|------:|
| Total modules | 445 |
| Total lines | 127,440 |
| Theorems and lemmas | 4,332 |
| Definitions | 3,542 |
| Structures and types | 1,685 |
| Computations (`#eval`) | 3,721 |
| Examples | 350 |
| Axioms | 3 |
| Sorry | 0 |

## Per-Book Breakdown

| Book | Modules | Lines | Theorems | #eval | Axioms | Sorry |
|------|--------:|------:|---------:|------:|-------:|------:|
| I — Foundations | 94 | 20,554 | ~900 | ~700 | 0 | **0** |
| II — Holomorphy | 65 | 18,069 | ~700 | ~500 | 0 | **0** |
| III — Spectrum | 70 | 16,807 | ~600 | ~450 | 3 | **0** |
| IV — Microcosm | 89 | 29,730 | ~1,000 | ~900 | 0 | **0** |
| V — Macrocosm | 80 | 28,394 | ~900 | ~850 | 0 | **0** |
| VI — Life | 30 | 5,221 | ~200 | ~200 | 0 | **0** |
| VII — Metaphysics | 7 | 4,278 | ~120 | ~100 | 0 | **0** |
| Tour | 8 | ~1,850 | — | — | 0 | **0** |
| **Total** | **443 + 2** | **127,440** | **~4,332** | **~3,721** | **3** | **0** |

*443 per-book modules + 2 shared infrastructure modules = 445 total (matching generated API docs).*

## Axiom Inventory

TauLib contains exactly **3 axioms**, each explicitly declared and documented.

### Conjectural Axioms (3)

These follow the "compute-then-axiomatize" pattern: a decidable check function is verified computationally via `native_decide` at all tested finite bounds. The axiom asserts the property holds universally.

| # | Axiom | Module | What It Asserts |
|---|-------|--------|-----------------|
| 1 | `bridge_functor_exists` | `BookIII.Bridge.BridgeAxiom` | The bridge functor from the canonical enrichment ladder to the spectral decomposition exists for all n |
| 2 | `spectral_correspondence_O3` | `BookIII.Doors.SpectralCorrespondence` | The O(3) spectral correspondence holds universally |
| 3 | `grand_grh_adelic` | `BookIII.Doors.GrandGRH` | The adelic Generalized Riemann Hypothesis (used for spectral completeness) |

### Retired axiom (v1 → v2)

A fourth axiom `central_theorem_physical : True` (in `BookIV.Arena.BoundaryHolonomy`) was declared in the v1 release pinned at commit `181a59e`. It was retired in `peer-review-fixes-v1` (2026-04-19) as a no-op: an `axiom : True` adds no content because `True` is already inhabited by `trivial`. The physical interpretation of the Book II Central Theorem is now carried by the algebraic statement and its guided tour in `TauLib/Tour/CentralTheorem.lean`; no Book IV axiom mediates it.

See [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}) for the `native_decide` dependencies that appear on `#print axioms` output for theorems that rely on finite-check functions (including the Book II Central Theorem and the three Book III conjectural-axiom finite-check theorems).

## Sorry Inventory

TauLib contains **zero `sorry`** across all seven books.

Pre-peer-review-fixes-v1, Book VII shipped three declarations of the form `theorem X : True := sorry` encoding methodological commitments. These were identified as performative — `True` is provable by `trivial`, so `theorem X : True := sorry` is a marker, not an incomplete proof — and were replaced in `peer-review-fixes-v1` with inspectable `def : Commitment` values that carry structural data (`statement`, `warrant`, `registry_id`) rather than pretending to be proof debt.

| # | Prior (v1) declaration | Replaced by | Module |
|---|------------------------|-------------|--------|
| 1 | `omega_point_theorem : True := sorry` | `omega_point_commitment : Commitment` | `BookVII.Logos.Sector` |
| 2 | `science_faith_boundary : True := sorry` | `science_faith_boundary_commitment : Commitment` | `BookVII.Logos.Sector` |
| 3 | `no_forced_stance : True := sorry` | `no_forced_stance_commitment : Commitment` | `BookVII.Final.Boundary` |

The `Commitment` record is defined in `BookVII.Meta.Commitment`. Each commitment value is a piece of inspectable data — the reader can read what the program is committing to, rather than infer it from a methodological `sorry` tag.
