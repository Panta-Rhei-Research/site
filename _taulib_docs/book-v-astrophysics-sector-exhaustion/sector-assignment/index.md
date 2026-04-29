---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_assignment",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-assignment/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::sector_assignment",
  "declaration_slug": "sector-assignment",
  "kind": "theorem",
  "name": "sector_assignment",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 127,
  "source_line_end": 129,
  "registry_ids": [
    "V.P86"
  ],
  "related_registry_items": [
    {
      "id": "V.P86",
      "title": "Coupling Budget Completeness",
      "url": "/registry/object/V.P86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L127-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L127-L129",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L127-L129)
- Source range: L127-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P86` — Coupling Budget Completeness

## Immediate Comment / Docstring

```lean
/-- [V.P86] Each phenomenon has a non-empty sector assignment. -/
```

## Source Excerpt

```lean
theorem sector_assignment (p : AstroPhenomenon) :
    (primarySectors p).length > 0 := by
  cases p <;> native_decide
```
