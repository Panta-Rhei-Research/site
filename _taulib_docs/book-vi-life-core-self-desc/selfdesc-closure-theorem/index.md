---
{
  "projection_kind": "taulib_declaration",
  "title": "selfdesc_closure_theorem",
  "permalink": "/corpus/taulib/docs/book-vi-life-core-self-desc/selfdesc-closure-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.SelfDesc`.",
  "declaration_id": "TauLib.BookVI.LifeCore.SelfDesc::selfdesc_closure_theorem",
  "declaration_slug": "selfdesc-closure-theorem",
  "kind": "theorem",
  "name": "selfdesc_closure_theorem",
  "module_name": "TauLib.BookVI.LifeCore.SelfDesc",
  "module_url": "/corpus/taulib/docs/book-vi-life-core-self-desc/",
  "source_line_start": 59,
  "source_line_end": 63,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L59-L63",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.SelfDesc",
        "url": "/corpus/taulib/docs/book-vi-life-core-self-desc/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L59-L63",
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

- Module: [TauLib.BookVI.LifeCore.SelfDesc](/corpus/taulib/docs/book-vi-life-core-self-desc/)
- Source path: [`TauLib/BookVI/LifeCore/SelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L59-L63)
- Source range: L59-L63
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem selfdesc_closure_theorem :
    closure_thm.basin_correction = true ∧
    closure_thm.code_integrity = true ∧
    closure_thm.closure_under_eval = true :=
  ⟨rfl, rfl, rfl⟩
```
