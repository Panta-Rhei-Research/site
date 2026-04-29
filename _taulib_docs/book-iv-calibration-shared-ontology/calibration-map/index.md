---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibrationMap",
  "permalink": "/verify/taulib/docs/book-iv-calibration-shared-ontology/calibration-map/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.SharedOntology`.",
  "declaration_id": "TauLib.BookIV.Calibration.SharedOntology::CalibrationMap",
  "declaration_slug": "calibration-map",
  "kind": "structure",
  "name": "CalibrationMap",
  "module_name": "TauLib.BookIV.Calibration.SharedOntology",
  "module_url": "/verify/taulib/docs/book-iv-calibration-shared-ontology/",
  "source_line_start": 31,
  "source_line_end": 40,
  "registry_ids": [
    "IV.P159"
  ],
  "related_registry_items": [
    {
      "id": "IV.P159",
      "title": "Calibration is structural",
      "url": "/registry/object/IV.P159/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L31-L40",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.SharedOntology",
        "url": "/verify/taulib/docs/book-iv-calibration-shared-ontology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L31-L40",
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

- Module: [TauLib.BookIV.Calibration.SharedOntology](/verify/taulib/docs/book-iv-calibration-shared-ontology/)
- Source path: [`TauLib/BookIV/Calibration/SharedOntology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L31-L40)
- Source range: L31-L40
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P159` — Calibration is structural

## Immediate Comment / Docstring

```lean
/-- [IV.P159] The translation between τ-native units and SI units at E₁
    is a definable map within the boundary holonomy algebra.
    It is not an ad-hoc fitting procedure: the map is forced by
    the categorical structure. -/
```

## Source Excerpt

```lean
structure CalibrationMap where
  /-- Source: τ-native coupling space (dim = number of sectors). -/
  source_dim : Nat
  source_eq : source_dim = 5
  /-- Target: SI measurable quantities. -/
  target_dim : Nat
  /-- The map is determined by ι_τ alone (No Knobs). -/
  no_knobs : Bool
  no_knobs_true : no_knobs = true
  deriving Repr
```
