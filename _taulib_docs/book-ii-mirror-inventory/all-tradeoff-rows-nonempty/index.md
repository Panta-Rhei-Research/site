---
{
  "projection_kind": "taulib_declaration",
  "title": "all_tradeoff_rows_nonempty",
  "permalink": "/verify/taulib/docs/book-ii-mirror-inventory/all-tradeoff-rows-nonempty/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.Inventory`.",
  "declaration_id": "TauLib.BookII.Mirror.Inventory::all_tradeoff_rows_nonempty",
  "declaration_slug": "all-tradeoff-rows-nonempty",
  "kind": "theorem",
  "name": "all_tradeoff_rows_nonempty",
  "module_name": "TauLib.BookII.Mirror.Inventory",
  "module_url": "/verify/taulib/docs/book-ii-mirror-inventory/",
  "source_line_start": 127,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L127-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L127-L128",
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
- Source path: [`TauLib/BookII/Mirror/Inventory.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L127-L128)
- Source range: L127-L128
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All trade-off descriptions are nonempty. -/
```

## Source Excerpt

```lean
theorem all_tradeoff_rows_nonempty :
    full_rewiring_table.all row_tradeoff_nonempty = true := by native_decide
```
