---
{
  "projection_kind": "taulib_declaration",
  "title": "recycling_all_hold",
  "permalink": "/verify/taulib/docs/book-vi-closure-closure-sector/recycling-all-hold/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Closure.ClosureSector`.",
  "declaration_id": "TauLib.BookVI.Closure.ClosureSector::recycling_all_hold",
  "declaration_slug": "recycling-all-hold",
  "kind": "theorem",
  "name": "recycling_all_hold",
  "module_name": "TauLib.BookVI.Closure.ClosureSector",
  "module_url": "/verify/taulib/docs/book-vi-closure-closure-sector/",
  "source_line_start": 93,
  "source_line_end": 97,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L93-L97",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.ClosureSector",
        "url": "/verify/taulib/docs/book-vi-closure-closure-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L93-L97",
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

- Module: [TauLib.BookVI.Closure.ClosureSector](/verify/taulib/docs/book-vi-closure-closure-sector/)
- Source path: [`TauLib/BookVI/Closure/ClosureSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L93-L97)
- Source range: L93-L97
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem recycling_all_hold :
    struct_recycle.net_reduction = true ∧
    struct_recycle.hodge_gradient_negative = true ∧
    struct_recycle.energy_to_base = true :=
  ⟨rfl, rfl, rfl⟩
```
