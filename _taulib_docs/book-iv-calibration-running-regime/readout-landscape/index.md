---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutLandscape",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-landscape/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::ReadoutLandscape",
  "declaration_slug": "readout-landscape",
  "kind": "structure",
  "name": "ReadoutLandscape",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 157,
  "source_line_end": 164,
  "registry_ids": [
    "IV.D304"
  ],
  "related_registry_items": [
    {
      "id": "IV.D304",
      "title": "Readout landscape",
      "url": "/registry/object/IV.D304/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L157-L164",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.RunningRegime",
        "url": "/verify/taulib/docs/book-iv-calibration-running-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L157-L164",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L157-L164)
- Source range: L157-L164
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D304` — Readout landscape

## Immediate Comment / Docstring

```lean
/-- [IV.D304] The readout landscape R = {R_μ}_{μ>0}: the family of
    readout functors indexed by energy scale. Encodes the totality
    of scale-dependent physics. -/
```

## Source Excerpt

```lean
structure ReadoutLandscape where
  /-- Number of sector-specific readout factors. -/
  factor_count : Nat
  factor_eq : factor_count = 5
  /-- Uniquely determined by boundary holonomy. -/
  determined : Bool
  determined_true : determined = true
  deriving Repr
```
