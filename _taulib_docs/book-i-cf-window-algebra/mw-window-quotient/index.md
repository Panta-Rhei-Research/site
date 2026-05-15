---
{
  "projection_kind": "taulib_declaration",
  "title": "mw_window_quotient",
  "permalink": "/corpus/taulib/docs/book-i-cf-window-algebra/mw-window-quotient/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::mw_window_quotient",
  "declaration_slug": "mw-window-quotient",
  "kind": "theorem",
  "name": "mw_window_quotient",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/corpus/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 107,
  "source_line_end": 109,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L107-L109",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L107-L109",
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
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L107-L109)
- Source range: L107-L109
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [CF.06] The 17/5 quotient: W₃(3)/W₃(4) = 17/5.
    This is the coefficient in M_W/m_n = (17/5)·ι⁻³. -/
```

## Source Excerpt

```lean
theorem mw_window_quotient :
    windowSum cf_head 3 3 = 17 ∧ windowSum cf_head 3 4 = 5 := by
  exact ⟨w3_at_3, w3_at_4⟩
```
