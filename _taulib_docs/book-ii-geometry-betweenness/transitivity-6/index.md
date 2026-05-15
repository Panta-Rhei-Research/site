---
{
  "projection_kind": "taulib_declaration",
  "title": "transitivity_6",
  "permalink": "/corpus/taulib/docs/book-ii-geometry-betweenness/transitivity-6/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Geometry.Betweenness`.",
  "declaration_id": "TauLib.BookII.Geometry.Betweenness::transitivity_6",
  "declaration_slug": "transitivity-6",
  "kind": "theorem",
  "name": "transitivity_6",
  "module_name": "TauLib.BookII.Geometry.Betweenness",
  "module_url": "/corpus/taulib/docs/book-ii-geometry-betweenness/",
  "source_line_start": 116,
  "source_line_end": 118,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L116-L118",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.Betweenness",
        "url": "/corpus/taulib/docs/book-ii-geometry-betweenness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L116-L118",
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

- Module: [TauLib.BookII.Geometry.Betweenness](/corpus/taulib/docs/book-ii-geometry-betweenness/)
- Source path: [`TauLib/BookII/Geometry/Betweenness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L116-L118)
- Source range: L116-L118
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
theorem transitivity_6 : between_transitivity_check 6 5 = true := by native_decide

end Tau.BookII.Geometry
```
