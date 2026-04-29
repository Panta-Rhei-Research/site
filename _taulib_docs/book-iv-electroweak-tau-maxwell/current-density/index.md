---
{
  "projection_kind": "taulib_declaration",
  "title": "CurrentDensity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/current-density/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::CurrentDensity",
  "declaration_slug": "current-density",
  "kind": "structure",
  "name": "CurrentDensity",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 390,
  "source_line_end": 396,
  "registry_ids": [
    "IV.P46"
  ],
  "related_registry_items": [
    {
      "id": "IV.P46",
      "title": "Current as Defect Transport",
      "url": "/registry/object/IV.P46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L390-L396",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L390-L396",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L390-L396)
- Source range: L390-L396
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P46` — Current as Defect Transport

## Immediate Comment / Docstring

```lean
/-- [IV.P46] Spatial current density J^i: transport of charged defects
    through space. J = ρv for uniform charge motion. -/
```

## Source Excerpt

```lean
structure CurrentDensity where
  /-- Spatial components (3). -/
  components : Nat
  comp_eq : components = 3
  /-- Is transport of charged defects. -/
  is_defect_transport : Bool := true
  deriving Repr
```
