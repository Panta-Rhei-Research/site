---
{
  "projection_kind": "taulib_declaration",
  "title": "CepheidCalibrator",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/cepheid-calibrator/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::CepheidCalibrator",
  "declaration_slug": "cepheid-calibrator",
  "kind": "structure",
  "name": "CepheidCalibrator",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 139,
  "source_line_end": 151,
  "registry_ids": [
    "V.D33"
  ],
  "related_registry_items": [
    {
      "id": "V.D33",
      "title": "Cepheid readout calibrator",
      "url": "/registry/object/V.D33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L139-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L139-L151",
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/verify/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L139-L151)
- Source range: L139-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D33` — Cepheid readout calibrator

## Immediate Comment / Docstring

```lean
/-- [V.D33] Cepheid readout calibrator: a stellar configuration whose
    period-luminosity relation arises from the (γ, D)-sector overlap.

    Period P and luminosity L are both determined by
    κ(D;1)/κ(B;1) = (1−ι_τ)/ι_τ². -/
```

## Source Excerpt

```lean
structure CepheidCalibrator where
  /-- Period index (τ-native pulsation frequency readout). -/
  period_numer : Nat
  /-- Period denominator. -/
  period_denom : Nat
  /-- Luminosity index (γ-sector energy flux readout). -/
  luminosity_numer : Nat
  /-- Luminosity denominator. -/
  luminosity_denom : Nat
  /-- Both denominators positive. -/
  period_denom_pos : period_denom > 0
  luminosity_denom_pos : luminosity_denom > 0
  deriving Repr
```
