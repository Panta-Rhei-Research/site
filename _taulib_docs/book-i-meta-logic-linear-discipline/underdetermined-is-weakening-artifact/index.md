---
{
  "projection_kind": "taulib_declaration",
  "title": "underdetermined_is_weakening_artifact",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/underdetermined-is-weakening-artifact/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearDiscipline::underdetermined_is_weakening_artifact",
  "declaration_slug": "underdetermined-is-weakening-artifact",
  "kind": "theorem",
  "name": "underdetermined_is_weakening_artifact",
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/",
  "source_line_start": 213,
  "source_line_end": 214,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L213-L214",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L213-L214",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L213-L214)
- Source range: L213-L214
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- N (underdetermined) is the weakening artifact: a resource whose
    status is unknown — this arises when a resource is discarded
    (weakened away) before its status is determined. -/
```

## Source Excerpt

```lean
theorem underdetermined_is_weakening_artifact :
    truth4_to_resource Tau.Logic.Truth4.N = .underdetermined := rfl
```
