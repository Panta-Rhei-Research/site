---
{
  "projection_kind": "taulib_declaration",
  "title": "rewiring_table_complete",
  "permalink": "/verify/taulib/docs/book-ii-mirror-inventory/rewiring-table-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.Inventory`.",
  "declaration_id": "TauLib.BookII.Mirror.Inventory::rewiring_table_complete",
  "declaration_slug": "rewiring-table-complete",
  "kind": "theorem",
  "name": "rewiring_table_complete",
  "module_name": "TauLib.BookII.Mirror.Inventory",
  "module_url": "/verify/taulib/docs/book-ii-mirror-inventory/",
  "source_line_start": 103,
  "source_line_end": 104,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L103-L104",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L103-L104",
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
- Source path: [`TauLib/BookII/Mirror/Inventory.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L103-L104)
- Source range: L103-L104
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D72` — The Rewiring Table

## Immediate Comment / Docstring

```lean
/-- [II.D72] The rewiring table has exactly 12 rows. -/
```

## Source Excerpt

```lean
theorem rewiring_table_complete :
    full_rewiring_table.length = 12 := by native_decide
```
