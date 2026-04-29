---
{
  "projection_kind": "taulib_declaration",
  "title": "readout_properties",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-properties/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::readout_properties",
  "declaration_slug": "readout-properties",
  "kind": "theorem",
  "name": "readout_properties",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 88,
  "source_line_end": 90,
  "registry_ids": [
    "IV.P168"
  ],
  "related_registry_items": [
    {
      "id": "IV.P168",
      "title": "Readout Properties",
      "url": "/registry/object/IV.P168/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L88-L90",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L88-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L88-L90)
- Source range: L88-L90
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P168` — Readout Properties

## Immediate Comment / Docstring

```lean
/-- [IV.P168] Readout properties: order preservation + complement preservation. -/
```

## Source Excerpt

```lean
theorem readout_properties :
    -- The readout functor preserves the power hierarchy at every scale
    (ReadoutFunctor.mk 10 rfl 10 rfl true rfl).order_preserving = true := rfl
```
