---
{
  "projection_kind": "taulib_declaration",
  "title": "a4_eq",
  "permalink": "/verify/taulib/docs/book-i-cf-window-algebra/a4-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::a4_eq",
  "declaration_slug": "a4-eq",
  "kind": "theorem",
  "name": "a4_eq",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/verify/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 136,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L136-L136",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.CF.WindowAlgebra",
        "url": "/verify/taulib/docs/book-i-cf-window-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L136-L136",
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

- Module: [TauLib.BookI.CF.WindowAlgebra](/verify/taulib/docs/book-i-cf-window-algebra/)
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L136-L136)
- Source range: L136-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- a₄ = 3 = dim(τ³) = window width. -/
```

## Source Excerpt

```lean
theorem a4_eq : cf_head.getD 4 0 = 3 := by native_decide
```
