---
{
  "projection_kind": "taulib_declaration",
  "title": "frontier_status_count",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/frontier-status-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.StructuralExclusion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.StructuralExclusion::frontier_status_count",
  "declaration_slug": "frontier-status-count",
  "kind": "theorem",
  "name": "frontier_status_count",
  "module_name": "TauLib.BookI.MetaLogic.StructuralExclusion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/",
  "source_line_start": 160,
  "source_line_end": 160,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L160-L160",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.StructuralExclusion",
        "url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L160-L160",
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

- Module: [TauLib.BookI.MetaLogic.StructuralExclusion](/verify/taulib/docs/book-i-meta-logic-structural-exclusion/)
- Source path: [`TauLib/BookI/MetaLogic/StructuralExclusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L160-L160)
- Source range: L160-L160
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- There are exactly 3 frontier statuses. -/
```

## Source Excerpt

```lean
theorem frontier_status_count : allFrontierStatuses.length = 3 := by rfl
```
