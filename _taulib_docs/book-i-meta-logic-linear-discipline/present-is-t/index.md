---
{
  "projection_kind": "taulib_declaration",
  "title": "present_is_T",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/present-is-t/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearDiscipline::present_is_T",
  "declaration_slug": "present-is-t",
  "kind": "theorem",
  "name": "present_is_T",
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/",
  "source_line_start": 217,
  "source_line_end": 218,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L217-L218",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearDiscipline",
        "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L217-L218",
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

- Module: [TauLib.BookI.MetaLogic.LinearDiscipline](/verify/taulib/docs/book-i-meta-logic-linear-discipline/)
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L217-L218)
- Source range: L217-L218
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The present state maps to T. -/
```

## Source Excerpt

```lean
theorem present_is_T :
    truth4_to_resource Tau.Logic.Truth4.T = .present := rfl
```
