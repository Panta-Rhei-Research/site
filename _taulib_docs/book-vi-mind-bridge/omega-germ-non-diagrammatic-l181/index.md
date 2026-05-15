---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_germ_non_diagrammatic",
  "permalink": "/corpus/taulib/docs/book-vi-mind-bridge/omega-germ-non-diagrammatic-l181/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::omega_germ_non_diagrammatic",
  "declaration_slug": "omega-germ-non-diagrammatic-l181",
  "kind": "theorem",
  "name": "omega_germ_non_diagrammatic",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/corpus/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 181,
  "source_line_end": 184,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L181-L184",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/corpus/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L181-L184",
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

- Module: [TauLib.BookVI.Mind.Bridge](/corpus/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L181-L184)
- Source range: L181-L184
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
theorem omega_germ_non_diagrammatic :
    omega_germ_nd.non_diagrammatic = true ∧
    omega_germ_nd.existence_not_structure = true :=
  ⟨rfl, rfl⟩
```
