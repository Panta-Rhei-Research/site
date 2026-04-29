---
{
  "projection_kind": "taulib_declaration",
  "title": "inter_sector_web_connected",
  "permalink": "/verify/taulib/docs/book-vi-closure-ecosystem/inter-sector-web-connected/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Closure.Ecosystem`.",
  "declaration_id": "TauLib.BookVI.Closure.Ecosystem::inter_sector_web_connected",
  "declaration_slug": "inter-sector-web-connected",
  "kind": "theorem",
  "name": "inter_sector_web_connected",
  "module_name": "TauLib.BookVI.Closure.Ecosystem",
  "module_url": "/verify/taulib/docs/book-vi-closure-ecosystem/",
  "source_line_start": 53,
  "source_line_end": 55,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L53-L55",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.Ecosystem",
        "url": "/verify/taulib/docs/book-vi-closure-ecosystem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L53-L55",
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

- Module: [TauLib.BookVI.Closure.Ecosystem](/verify/taulib/docs/book-vi-closure-ecosystem/)
- Source path: [`TauLib/BookVI/Closure/Ecosystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L53-L55)
- Source range: L53-L55
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
theorem inter_sector_web_connected :
    isw.connected = true ∧ isw.source_closure_dual = true :=
  ⟨rfl, rfl⟩
```
