---
{
  "projection_kind": "taulib_declaration",
  "title": "ModuleEntry",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-linearity-audit/module-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.LinearityAudit`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearityAudit::ModuleEntry",
  "declaration_slug": "module-entry",
  "kind": "structure",
  "name": "ModuleEntry",
  "module_name": "TauLib.BookI.MetaLogic.LinearityAudit",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-linearity-audit/",
  "source_line_start": 38,
  "source_line_end": 42,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L38-L42",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearityAudit",
        "url": "/corpus/taulib/docs/book-i-meta-logic-linearity-audit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L38-L42",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.MetaLogic.LinearityAudit](/corpus/taulib/docs/book-i-meta-logic-linearity-audit/)
- Source path: [`TauLib/BookI/MetaLogic/LinearityAudit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L38-L42)
- Source range: L38-L42
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A census entry for a single TauLib module. -/
```

## Source Excerpt

```lean
structure ModuleEntry where
  name : String
  directory : String
  class_ : ModuleClass
  deriving DecidableEq, Repr
```
