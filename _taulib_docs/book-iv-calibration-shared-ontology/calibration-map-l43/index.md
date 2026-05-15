---
{
  "projection_kind": "taulib_declaration",
  "title": "calibration_map",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-shared-ontology/calibration-map-l43/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.SharedOntology`.",
  "declaration_id": "TauLib.BookIV.Calibration.SharedOntology::calibration_map",
  "declaration_slug": "calibration-map-l43",
  "kind": "def",
  "name": "calibration_map",
  "module_name": "TauLib.BookIV.Calibration.SharedOntology",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-shared-ontology/",
  "source_line_start": 43,
  "source_line_end": 48,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L43-L48",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.SharedOntology",
        "url": "/corpus/taulib/docs/book-iv-calibration-shared-ontology/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L43-L48",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIV.Calibration.SharedOntology](/corpus/taulib/docs/book-iv-calibration-shared-ontology/)
- Source path: [`TauLib/BookIV/Calibration/SharedOntology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SharedOntology.lean#L43-L48)
- Source range: L43-L48
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical calibration map. -/
```

## Source Excerpt

```lean
def calibration_map : CalibrationMap where
  source_dim := 5
  source_eq := rfl
  target_dim := 4  -- c, h, G, α
  no_knobs := true
  no_knobs_true := rfl
```
