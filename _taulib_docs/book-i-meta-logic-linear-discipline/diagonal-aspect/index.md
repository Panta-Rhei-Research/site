---
{
  "projection_kind": "taulib_declaration",
  "title": "DiagonalAspect",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearDiscipline::DiagonalAspect",
  "declaration_slug": "diagonal-aspect",
  "kind": "inductive",
  "name": "DiagonalAspect",
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/",
  "source_line_start": 43,
  "source_line_end": 49,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L43-L49",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearDiscipline",
        "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L43-L49",
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

- Module: [TauLib.BookI.MetaLogic.LinearDiscipline](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/)
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L43-L49)
- Source range: L43-L49
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three aspects of K5's diagonal discipline. -/
```

## Source Excerpt

```lean
inductive DiagonalAspect where
  | noUnearnedDiagonals  -- K5.1: no unearned diagonal maps
  | channelConsumption   -- K5.2: each rewiring consumes a channel
  | saturation           -- K5.3: the iterator ladder saturates at 3 levels
  deriving DecidableEq, Repr

open LinearAspect DiagonalAspect
```
