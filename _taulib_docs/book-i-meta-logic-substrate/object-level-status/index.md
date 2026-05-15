---
{
  "projection_kind": "taulib_declaration",
  "title": "ObjectLevelStatus",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-substrate/object-level-status/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.Substrate`.",
  "declaration_id": "TauLib.BookI.MetaLogic.Substrate::ObjectLevelStatus",
  "declaration_slug": "object-level-status",
  "kind": "inductive",
  "name": "ObjectLevelStatus",
  "module_name": "TauLib.BookI.MetaLogic.Substrate",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-substrate/",
  "source_line_start": 42,
  "source_line_end": 47,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L42-L47",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.Substrate",
        "url": "/corpus/taulib/docs/book-i-meta-logic-substrate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L42-L47",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.MetaLogic.Substrate](/corpus/taulib/docs/book-i-meta-logic-substrate/)
- Source path: [`TauLib/BookI/MetaLogic/Substrate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/Substrate.lean#L42-L47)
- Source range: L42-L47
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

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
