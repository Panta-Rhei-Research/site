---
{
  "projection_kind": "taulib_declaration",
  "title": "relational_units",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/relational-units-l76/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::relational_units",
  "declaration_slug": "relational-units-l76",
  "kind": "def",
  "name": "relational_units",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 76,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L76-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L76-L84",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L76-L84)
- Source range: L76-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical relational units. -/
```

## Source Excerpt

```lean
def relational_units : RelationalUnits where
  mass_is_neutron := true
  mass_true := rfl
  unit_count := 5
  count_eq := rfl
  si_base := 7
  si_eq := rfl
  free_params := 1
  free_eq := rfl
```
