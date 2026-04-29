---
{
  "projection_kind": "taulib_declaration",
  "title": "calibration_structural",
  "permalink": "/verify/taulib/docs/book-iv-calibration-shared-ontology/calibration-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.SharedOntology`.",
  "declaration_id": "TauLib.BookIV.Calibration.SharedOntology::calibration_structural",
  "declaration_slug": "calibration-structural",
  "kind": "theorem",
  "name": "calibration_structural",
  "module_name": "TauLib.BookIV.Calibration.SharedOntology",
  "module_url": "/verify/taulib/docs/book-iv-calibration-shared-ontology/",
  "source_line_start": 52,
  "source_line_end": 55,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L52-L55",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L52-L55",
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

- Module: [TauLib.BookIV.Calibration.SharedOntology](/verify/taulib/docs/book-iv-calibration-shared-ontology/)
- Source path: [`TauLib/BookIV/Calibration/SharedOntology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L52-L55)
- Source range: L52-L55
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P159` — Calibration is structural

## Immediate Comment / Docstring

```lean
/-- [IV.P159] Calibration is structural: determined by 5 sectors,
    governed by ι_τ alone. -/
```

## Source Excerpt

```lean
theorem calibration_structural :
    calibration_map.source_dim = 5 ∧
    calibration_map.no_knobs = true := by
  exact ⟨rfl, rfl⟩
```
