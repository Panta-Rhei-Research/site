---
{
  "projection_kind": "taulib_declaration",
  "title": "symmetric_recipe",
  "permalink": "/verify/taulib/docs/book-i-cf-window-algebra/symmetric-recipe/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::symmetric_recipe",
  "declaration_slug": "symmetric-recipe",
  "kind": "theorem",
  "name": "symmetric_recipe",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/verify/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 90,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L90-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L90-L94",
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
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L90-L94)
- Source range: L90-L94
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [CF.06] The symmetric recipe for 5/7:
    numerator = W₃(4) = 5, denominator = W₃(3) − 2·W₃(4) = 17 − 10 = 7.
    Both sides use the same W₃ window family. -/
```

## Source Excerpt

```lean
theorem symmetric_recipe :
    let w34 := windowSum cf_head 3 4  -- 5
    let denom := windowSum cf_head 3 3 - 2 * windowSum cf_head 3 4  -- 17 - 10 = 7
    w34 = 5 ∧ denom = 7 := by
  native_decide
```
