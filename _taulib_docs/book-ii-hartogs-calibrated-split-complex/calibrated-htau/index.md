---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibratedHTau",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/calibrated-htau/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Hartogs.CalibratedSplitComplex`.",
  "declaration_id": "TauLib.BookII.Hartogs.CalibratedSplitComplex::CalibratedHTau",
  "declaration_slug": "calibrated-htau",
  "kind": "structure",
  "name": "CalibratedHTau",
  "module_name": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/",
  "source_line_start": 59,
  "source_line_end": 68,
  "registry_ids": [
    "II.D35"
  ],
  "related_registry_items": [
    {
      "id": "II.D35",
      "title": "Calibrated Split-Complex Codomain",
      "url": "/registry/object/II.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L59-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
        "url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L59-L68",
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

- Module: [TauLib.BookII.Hartogs.CalibratedSplitComplex](/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/)
- Source path: [`TauLib/BookII/Hartogs/CalibratedSplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L59-L68)
- Source range: L59-L68
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D35` — Calibrated Split-Complex Codomain

## Immediate Comment / Docstring

```lean
/-- [II.D35] Calibrated split-complex codomain H_τ^cal.
    Stores the four earned transcendental constants as scaled integers.
    Each field represents the constant multiplied by SCALE = 10^6.

    The calibration is canonical: there is exactly one CalibratedHTau
    instance derived from the earned pi, e, j, iota_tau. -/
```

## Source Excerpt

```lean
structure CalibratedHTau where
  /-- π scaled by 10^6: π * 10^6 ≈ 3141592. -/
  pi_cal    : Nat
  /-- e scaled by 10^6: e * 10^6 ≈ 2718281. -/
  e_cal     : Nat
  /-- j² = +1 indicator: 1 means j² = +1 (split-complex), 0 would mean i² = -1. -/
  j_cal     : Nat
  /-- ι_τ scaled by 10^6: ι_τ * 10^6 ≈ 341304. -/
  iota_cal  : Nat
  deriving Repr, DecidableEq
```
