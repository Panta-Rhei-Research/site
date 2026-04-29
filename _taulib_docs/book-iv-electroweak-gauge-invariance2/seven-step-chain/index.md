---
{
  "projection_kind": "taulib_declaration",
  "title": "SevenStepChain",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/seven-step-chain/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::SevenStepChain",
  "declaration_slug": "seven-step-chain",
  "kind": "structure",
  "name": "SevenStepChain",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 284,
  "source_line_end": 292,
  "registry_ids": [
    "IV.P43"
  ],
  "related_registry_items": [
    {
      "id": "IV.P43",
      "title": "Categorical Derivation of Gauge Structure",
      "url": "/registry/object/IV.P43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L284-L292",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L284-L292",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L284-L292)
- Source range: L284-L292
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P43` — Categorical Derivation of Gauge Structure

## Immediate Comment / Docstring

```lean
/-- [IV.P43] Seven-step derivation chain from axioms to EM gauge theory:
    K0-K6 → τ³ → T² → U(1) → A_μ → F_μν → gauge invariance.
    Each step is constructive (no postulates beyond K0-K6). -/
```

## Source Excerpt

```lean
structure SevenStepChain where
  /-- Number of steps in the derivation. -/
  steps : Nat
  steps_eq : steps = 7
  /-- Each step is constructive (no external postulates). -/
  all_constructive : Bool := true
  /-- The chain terminates at gauge invariance. -/
  terminates_at_gauge : Bool := true
  deriving Repr
```
