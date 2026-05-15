---
{
  "projection_kind": "taulib_declaration",
  "title": "truth4_to_resource_injective",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearDiscipline::truth4_to_resource_injective",
  "declaration_slug": "truth4-to-resource-injective",
  "kind": "theorem",
  "name": "truth4_to_resource_injective",
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/",
  "source_line_start": 191,
  "source_line_end": 193,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L191-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L191-L193",
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
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L191-L193)
- Source range: L191-L193
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Injectivity of truth4_to_resource. -/
```

## Source Excerpt

```lean
theorem truth4_to_resource_injective (a b : Tau.Logic.Truth4)
    (h : truth4_to_resource a = truth4_to_resource b) : a = b := by
  cases a <;> cases b <;> simp [truth4_to_resource] at h <;> rfl
```
