---
{
  "projection_kind": "taulib_declaration",
  "title": "calibration_consistency_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/calibration-consistency-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CalibratedSplitComplex`.",
  "declaration_id": "TauLib.BookII.Hartogs.CalibratedSplitComplex::calibration_consistency_check",
  "declaration_slug": "calibration-consistency-check",
  "kind": "def",
  "name": "calibration_consistency_check",
  "module_name": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/",
  "source_line_start": 244,
  "source_line_end": 253,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L244-L253",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L244-L253",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookII/Hartogs/CalibratedSplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L244-L253)
- Source range: L244-L253
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D35` — Calibrated Split-Complex Codomain

## Immediate Comment / Docstring

```lean
/-- [II.D35] Full calibration consistency: all four constants are
    mutually consistent and the idempotents have correct geometric meaning.

    1. π, e, ι_τ in correct ranges
    2. j² = +1
    3. Idempotents: orthogonal, complete, idempotent
    4. Coupling: ι_τ = 2/(π+e)
    5. Geometric meaning: e₊ → B-channel, e₋ → C-channel -/
```

## Source Excerpt

```lean
def calibration_consistency_check : Bool :=
  pi_cal_range_check &&
  e_cal_range_check &&
  iota_cal_range_check &&
  j_squared_calibration_check &&
  orthogonality_check &&
  completeness_check &&
  idempotency_check &&
  coupling_check &&
  geometric_meaning_check 30
```
