---
{
  "projection_kind": "taulib_declaration",
  "title": "export_ladder",
  "permalink": "/verify/taulib/docs/book-ii-closure-forward-book3/export-ladder/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.ForwardBook3`.",
  "declaration_id": "TauLib.BookII.Closure.ForwardBook3::export_ladder",
  "declaration_slug": "export-ladder",
  "kind": "theorem",
  "name": "export_ladder",
  "module_name": "TauLib.BookII.Closure.ForwardBook3",
  "module_url": "/verify/taulib/docs/book-ii-closure-forward-book3/",
  "source_line_start": 177,
  "source_line_end": 178,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L177-L178",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.ForwardBook3",
        "url": "/verify/taulib/docs/book-ii-closure-forward-book3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L177-L178",
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

- Module: [TauLib.BookII.Closure.ForwardBook3](/verify/taulib/docs/book-ii-closure-forward-book3/)
- Source path: [`TauLib/BookII/Closure/ForwardBook3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L177-L178)
- Source range: L177-L178
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
theorem export_ladder :
    (compute_e1_export 3 15 3).enrichment_ladder_verified = true := by native_decide
```
