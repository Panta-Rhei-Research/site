---
{
  "projection_kind": "taulib_declaration",
  "title": "part_xi_entry_count",
  "permalink": "/verify/taulib/docs/book-ii-mirror-inventory/part-xi-entry-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.Inventory`.",
  "declaration_id": "TauLib.BookII.Mirror.Inventory::part_xi_entry_count",
  "declaration_slug": "part-xi-entry-count",
  "kind": "theorem",
  "name": "part_xi_entry_count",
  "module_name": "TauLib.BookII.Mirror.Inventory",
  "module_url": "/verify/taulib/docs/book-ii-mirror-inventory/",
  "source_line_start": 160,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L160-L161",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L160-L161",
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
- Source path: [`TauLib/BookII/Mirror/Inventory.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L160-L161)
- Source range: L160-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Part XI has 11 formal entries total. -/
```

## Source Excerpt

```lean
theorem part_xi_entry_count :
    part_xi_total_entries = 11 := by native_decide
```
