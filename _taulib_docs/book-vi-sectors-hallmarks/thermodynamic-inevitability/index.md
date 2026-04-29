---
{
  "projection_kind": "taulib_declaration",
  "title": "ThermodynamicInevitability",
  "permalink": "/verify/taulib/docs/book-vi-sectors-hallmarks/thermodynamic-inevitability/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.Hallmarks`.",
  "declaration_id": "TauLib.BookVI.Sectors.Hallmarks::ThermodynamicInevitability",
  "declaration_slug": "thermodynamic-inevitability",
  "kind": "structure",
  "name": "ThermodynamicInevitability",
  "module_name": "TauLib.BookVI.Sectors.Hallmarks",
  "module_url": "/verify/taulib/docs/book-vi-sectors-hallmarks/",
  "source_line_start": 65,
  "source_line_end": 69,
  "registry_ids": [
    "VI.P08"
  ],
  "related_registry_items": [
    {
      "id": "VI.P08",
      "title": "Thermodynamic Inevitability of Life",
      "url": "/registry/object/VI.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Hallmarks.lean#L65-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.Hallmarks",
        "url": "/verify/taulib/docs/book-vi-sectors-hallmarks/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Hallmarks.lean#L65-L69",
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

- Module: [TauLib.BookVI.Sectors.Hallmarks](/verify/taulib/docs/book-vi-sectors-hallmarks/)
- Source path: [`TauLib/BookVI/Sectors/Hallmarks.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Hallmarks.lean#L65-L69)
- Source range: L65-L69
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P08` — Thermodynamic Inevitability of Life

## Immediate Comment / Docstring

```lean
/-- [VI.P08] Thermodynamic inevitability (conjectural). -/
```

## Source Excerpt

```lean
structure ThermodynamicInevitability where
  is_attractor : Bool := true
  positive_measure : Bool := true
  scope : String := "conjectural"
  deriving Repr
```
