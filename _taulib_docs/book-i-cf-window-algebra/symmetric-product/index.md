---
{
  "projection_kind": "taulib_declaration",
  "title": "symmetric_product",
  "permalink": "/verify/taulib/docs/book-i-cf-window-algebra/symmetric-product/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::symmetric_product",
  "declaration_slug": "symmetric-product",
  "kind": "theorem",
  "name": "symmetric_product",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/verify/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 97,
  "source_line_end": 99,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L97-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L97-L99",
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
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L97-L99)
- Source range: L97-L99
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The product 5 × 7 = 35 from the symmetric recipe. -/
```

## Source Excerpt

```lean
theorem symmetric_product :
    windowSum cf_head 3 4 * (windowSum cf_head 3 3 - 2 * windowSum cf_head 3 4) = 35 := by
  native_decide
```
