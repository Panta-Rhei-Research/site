---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_export_total",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/defect-export-total/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::defect_export_total",
  "declaration_slug": "defect-export-total",
  "kind": "theorem",
  "name": "defect_export_total",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 145,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L145-L146",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L145-L146",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L145-L146)
- Source range: L145-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The defect total is the sum of all 4 components. -/
```

## Source Excerpt

```lean
theorem defect_export_total (d : DefectTuple) :
    d.total = d.mobility + d.vorticity + d.compression + d.topological := rfl
```
