---
{
  "projection_kind": "taulib_declaration",
  "title": "rows_orthodox",
  "permalink": "/verify/taulib/docs/book-ii-mirror-inventory/rows-orthodox/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.Inventory`.",
  "declaration_id": "TauLib.BookII.Mirror.Inventory::rows_orthodox",
  "declaration_slug": "rows-orthodox",
  "kind": "theorem",
  "name": "rows_orthodox",
  "module_name": "TauLib.BookII.Mirror.Inventory",
  "module_url": "/verify/taulib/docs/book-ii-mirror-inventory/",
  "source_line_start": 199,
  "source_line_end": 200,
  "registry_ids": [
    "II.D72"
  ],
  "related_registry_items": [
    {
      "id": "II.D72",
      "title": "The Rewiring Table",
      "url": "/registry/object/II.D72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L199-L200",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.Inventory",
        "url": "/verify/taulib/docs/book-ii-mirror-inventory/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L199-L200",
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

- Module: [TauLib.BookII.Mirror.Inventory](/verify/taulib/docs/book-ii-mirror-inventory/)
- Source path: [`TauLib/BookII/Mirror/Inventory.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L199-L200)
- Source range: L199-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D72` — The Rewiring Table

## Immediate Comment / Docstring

```lean
-- [II.D72] All rows have nonempty descriptions
```

## Source Excerpt

```lean
theorem rows_orthodox :
    full_rewiring_table.all row_orthodox_nonempty = true := by native_decide
```
