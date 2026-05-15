---
{
  "projection_kind": "taulib_declaration",
  "title": "w3_at_3",
  "permalink": "/corpus/taulib/docs/book-i-cf-window-algebra/w3-at-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::w3_at_3",
  "declaration_slug": "w3-at-3",
  "kind": "theorem",
  "name": "w3_at_3",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/corpus/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 67,
  "source_line_end": 67,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L67-L67",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.CF.WindowAlgebra",
        "url": "/corpus/taulib/docs/book-i-cf-window-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L67-L67",
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

- Module: [TauLib.BookI.CF.WindowAlgebra](/corpus/taulib/docs/book-i-cf-window-algebra/)
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L67-L67)
- Source range: L67-L67
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [CF.05] W₃(3) = a₃ + a₄ + a₅ = 13 + 3 + 1 = 17.
    The g_A NLO denominator: δ_A = (8/17)·ι². -/
```

## Source Excerpt

```lean
theorem w3_at_3 : windowSum cf_head 3 3 = 17 := by native_decide
```
