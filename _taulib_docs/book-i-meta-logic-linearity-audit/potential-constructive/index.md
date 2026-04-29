---
{
  "projection_kind": "taulib_declaration",
  "title": "potential_constructive",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/potential-constructive/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.LinearityAudit`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearityAudit::potential_constructive",
  "declaration_slug": "potential-constructive",
  "kind": "theorem",
  "name": "potential_constructive",
  "module_name": "TauLib.BookI.MetaLogic.LinearityAudit",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/",
  "source_line_start": 353,
  "source_line_end": 356,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L353-L356",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearityAudit",
        "url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L353-L356",
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

- Module: [TauLib.BookI.MetaLogic.LinearityAudit](/verify/taulib/docs/book-i-meta-logic-linearity-audit/)
- Source path: [`TauLib/BookI/MetaLogic/LinearityAudit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L353-L356)
- Source range: L353-L356
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- After eliminating the 2 Classical.em sites, the potential constructive
    count rises to 81 (the funext kernel axiom remains). -/
```

## Source Excerpt

```lean
theorem potential_constructive :
    (census.filter (fun m => m.class_ == .constructive)).length +
    (census.filter (fun m => m.class_ == .classical)).length = 81 := by
  native_decide
```
