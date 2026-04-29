---
{
  "projection_kind": "taulib_declaration",
  "title": "agency_sector",
  "permalink": "/verify/taulib/docs/book-vi-sectors-four-plus-one/agency-sector/",
  "summary_short": "`def` declaration in `TauLib.BookVI.Sectors.FourPlusOne`.",
  "declaration_id": "TauLib.BookVI.Sectors.FourPlusOne::agency_sector",
  "declaration_slug": "agency-sector",
  "kind": "def",
  "name": "agency_sector",
  "module_name": "TauLib.BookVI.Sectors.FourPlusOne",
  "module_url": "/verify/taulib/docs/book-vi-sectors-four-plus-one/",
  "source_line_start": 35,
  "source_line_end": 38,
  "registry_ids": [
    "VI.D17"
  ],
  "related_registry_items": [
    {
      "id": "VI.D17",
      "title": "Agency Sector (π-base)",
      "url": "/registry/object/VI.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L35-L38",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.FourPlusOne",
        "url": "/verify/taulib/docs/book-vi-sectors-four-plus-one/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L35-L38",
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

- Module: [TauLib.BookVI.Sectors.FourPlusOne](/verify/taulib/docs/book-vi-sectors-four-plus-one/)
- Source path: [`TauLib/BookVI/Sectors/FourPlusOne.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L35-L38)
- Source range: L35-L38
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VI.D17` — Agency Sector (π-base)

## Immediate Comment / Docstring

```lean
/-- [VI.D17] Agency sector (π-base). Archetype: Bacteria. -/
```

## Source Excerpt

```lean
def agency_sector : LifeSector where
  generator := "pi"
  is_primitive := true
  archetype := "Bacteria"
```
