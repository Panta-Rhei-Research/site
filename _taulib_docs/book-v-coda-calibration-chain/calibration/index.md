---
{
  "projection_kind": "taulib_declaration",
  "title": "calibration",
  "permalink": "/verify/taulib/docs/book-v-coda-calibration-chain/calibration/",
  "summary_short": "`def` declaration in `TauLib.BookV.Coda.CalibrationChain`.",
  "declaration_id": "TauLib.BookV.Coda.CalibrationChain::calibration",
  "declaration_slug": "calibration",
  "kind": "def",
  "name": "calibration",
  "module_name": "TauLib.BookV.Coda.CalibrationChain",
  "module_url": "/verify/taulib/docs/book-v-coda-calibration-chain/",
  "source_line_start": 118,
  "source_line_end": 124,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L118-L124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L118-L124",
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

- Module: [TauLib.BookV.Coda.CalibrationChain](/verify/taulib/docs/book-v-coda-calibration-chain/)
- Source path: [`TauLib/BookV/Coda/CalibrationChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L118-L124)
- Source range: L118-L124
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical calibration sufficiency. -/
```

## Source Excerpt

```lean
def calibration : CalibrationSufficiency where
  n_dimensionless := 1
  dimless_eq := rfl
  n_anchors := 1
  anchor_eq := rfl
  n_free_params := 0
  free_eq := rfl
```
