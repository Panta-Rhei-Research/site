---
{
  "projection_kind": "taulib_declaration",
  "title": "hierarchy_resolution",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/hierarchy-resolution/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings2`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings2::hierarchy_resolution",
  "declaration_slug": "hierarchy-resolution",
  "kind": "theorem",
  "name": "hierarchy_resolution",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings2",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/",
  "source_line_start": 106,
  "source_line_end": 109,
  "registry_ids": [
    "IV.P165"
  ],
  "related_registry_items": [
    {
      "id": "IV.P165",
      "title": "Hierarchy Resolution",
      "url": "/registry/object/IV.P165/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L106-L109",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessCouplings2",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L106-L109",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessCouplings2](/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L106-L109)
- Source range: L106-L109
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P165` — Hierarchy Resolution

## Immediate Comment / Docstring

```lean
/-- [IV.P165] The gravitational self-coupling κ(D;1) = 1−ι_τ is the
    LARGEST primitive coupling. The apparent weakness of gravity
    is a readout artifact: G involves ι_τ² from the torus vacuum. -/
```

## Source Excerpt

```lean
theorem hierarchy_resolution :
    -- κ(D) > κ(A): gravity coupling > weak coupling
    kappa_DD.numer > kappa_AA.numer := by
  native_decide
```
