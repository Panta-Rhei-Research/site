---
{
  "projection_kind": "taulib_declaration",
  "title": "table_12",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-inventory/table-12/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.Inventory`.",
  "declaration_id": "TauLib.BookII.Mirror.Inventory::table_12",
  "declaration_slug": "table-12",
  "kind": "theorem",
  "name": "table_12",
  "module_name": "TauLib.BookII.Mirror.Inventory",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-inventory/",
  "source_line_start": 195,
  "source_line_end": 196,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L195-L196",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.Inventory",
        "url": "/corpus/taulib/docs/book-ii-mirror-inventory/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L195-L196",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Mirror.Inventory](/corpus/taulib/docs/book-ii-mirror-inventory/)
- Source path: [`TauLib/BookII/Mirror/Inventory.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L195-L196)
- Source range: L195-L196
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D72` — The Rewiring Table

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- [II.D72] Table completeness
```

## Source Excerpt

```lean
theorem table_12 :
    full_rewiring_table.length = 12 := by native_decide
```
