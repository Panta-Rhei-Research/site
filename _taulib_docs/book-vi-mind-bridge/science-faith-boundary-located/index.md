---
{
  "projection_kind": "taulib_declaration",
  "title": "science_faith_boundary_located",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/science-faith-boundary-located/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::science_faith_boundary_located",
  "declaration_slug": "science-faith-boundary-located",
  "kind": "theorem",
  "name": "science_faith_boundary_located",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 207,
  "source_line_end": 213,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L207-L213",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/verify/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L207-L213",
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

- Module: [TauLib.BookVI.Mind.Bridge](/verify/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L207-L213)
- Source range: L207-L213
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
theorem science_faith_boundary_located :
    sci_faith.structurally_located = true ∧
    sci_faith.not_agnosticism = true ∧
    sci_faith.not_fideism = true :=
  ⟨rfl, rfl, rfl⟩

end Tau.BookVI.Bridge
```
