---
{
  "projection_kind": "taulib_declaration",
  "title": "ecosystem_poincare",
  "permalink": "/corpus/taulib/docs/book-vi-closure-ecosystem/ecosystem-poincare-l83/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Closure.Ecosystem`.",
  "declaration_id": "TauLib.BookVI.Closure.Ecosystem::ecosystem_poincare",
  "declaration_slug": "ecosystem-poincare-l83",
  "kind": "theorem",
  "name": "ecosystem_poincare",
  "module_name": "TauLib.BookVI.Closure.Ecosystem",
  "module_url": "/corpus/taulib/docs/book-vi-closure-ecosystem/",
  "source_line_start": 83,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L83-L87",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.Ecosystem",
        "url": "/corpus/taulib/docs/book-vi-closure-ecosystem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L83-L87",
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

- Module: [TauLib.BookVI.Closure.Ecosystem](/corpus/taulib/docs/book-vi-closure-ecosystem/)
- Source path: [`TauLib/BookVI/Closure/Ecosystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L83-L87)
- Source range: L83-L87
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
theorem ecosystem_poincare :
    eco_poincare.major_cycles ≥ 3 ∧
    eco_poincare.all_closed = true ∧
    eco_poincare.multi_scale = true :=
  ⟨eco_poincare.cycles_ge, rfl, rfl⟩
```
