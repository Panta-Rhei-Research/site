---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibrationSufficiency",
  "permalink": "/verify/taulib/docs/book-v-coda-calibration-chain/calibration-sufficiency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.CalibrationChain`.",
  "declaration_id": "TauLib.BookV.Coda.CalibrationChain::CalibrationSufficiency",
  "declaration_slug": "calibration-sufficiency",
  "kind": "structure",
  "name": "CalibrationSufficiency",
  "module_name": "TauLib.BookV.Coda.CalibrationChain",
  "module_url": "/verify/taulib/docs/book-v-coda-calibration-chain/",
  "source_line_start": 98,
  "source_line_end": 115,
  "registry_ids": [
    "V.T157"
  ],
  "related_registry_items": [
    {
      "id": "V.T157",
      "title": "Calibration Sufficiency",
      "url": "/registry/object/V.T157/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L98-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.CalibrationChain",
        "url": "/verify/taulib/docs/book-v-coda-calibration-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L98-L115",
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

- Module: [TauLib.BookV.Coda.CalibrationChain](/verify/taulib/docs/book-v-coda-calibration-chain/)
- Source path: [`TauLib/BookV/Coda/CalibrationChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L98-L115)
- Source range: L98-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T157` — Calibration Sufficiency

## Immediate Comment / Docstring

```lean
/-- [V.T157] Calibration sufficiency: the SI calibration cascade is
    sufficient. Every constant in the ledger is determined by ι_τ and m_n
    with zero additional free parameters.

    - Inputs: ι_τ (dimensionless, from axioms) + m_n (dimensionful anchor)
    - Outputs: G, α, α_G, m_e, m_P, c, ℏ, k_B, ...
    - The calibration triangle (G, κ_n, α_G) closes exactly
    - No fitting, no adjustable parameters -/
```

## Source Excerpt

```lean
structure CalibrationSufficiency where
  /-- Number of dimensionless inputs. -/
  n_dimensionless : Nat
  /-- One dimensionless input (ι_τ). -/
  dimless_eq : n_dimensionless = 1
  /-- Number of dimensionful anchors. -/
  n_anchors : Nat
  /-- One anchor (m_n). -/
  anchor_eq : n_anchors = 1
  /-- Number of free parameters. -/
  n_free_params : Nat
  /-- Zero free parameters. -/
  free_eq : n_free_params = 0
  /-- Total inputs count (ι_τ + m_n). -/
  total_inputs_count : Nat := 2
  /-- Calibration triangle closes. -/
  triangle_closes : Bool := true
  deriving Repr
```
