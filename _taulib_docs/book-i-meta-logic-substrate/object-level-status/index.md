---
{
  "projection_kind": "taulib_declaration",
  "title": "ObjectLevelStatus",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-substrate/object-level-status/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.Substrate`.",
  "declaration_id": "TauLib.BookI.MetaLogic.Substrate::ObjectLevelStatus",
  "declaration_slug": "object-level-status",
  "kind": "inductive",
  "name": "ObjectLevelStatus",
  "module_name": "TauLib.BookI.MetaLogic.Substrate",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-substrate/",
  "source_line_start": 42,
  "source_line_end": 47,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L42-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.Substrate",
        "url": "/verify/taulib/docs/book-i-meta-logic-substrate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L42-L47",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.MetaLogic.Substrate](/verify/taulib/docs/book-i-meta-logic-substrate/)
- Source path: [`TauLib/BookI/MetaLogic/Substrate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L42-L47)
- Source range: L42-L47
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The object-level status of a structural rule under K5's diagonal discipline. -/
```

## Source Excerpt

```lean
inductive ObjectLevelStatus where
  | refused    -- Rule is refused at the object level
  | preserved  -- Rule is preserved at the object level
  deriving DecidableEq, Repr

open ObjectLevelStatus
```
