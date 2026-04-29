---
{
  "projection_kind": "taulib_declaration",
  "title": "response",
  "permalink": "/verify/taulib/docs/book-vi-sectors-hallmarks/response/",
  "summary_short": "`def` declaration in `TauLib.BookVI.Sectors.Hallmarks`.",
  "declaration_id": "TauLib.BookVI.Sectors.Hallmarks::response",
  "declaration_slug": "response",
  "kind": "def",
  "name": "response",
  "module_name": "TauLib.BookVI.Sectors.Hallmarks",
  "module_url": "/verify/taulib/docs/book-vi-sectors-hallmarks/",
  "source_line_start": 50,
  "source_line_end": 52,
  "registry_ids": [
    "VI.T13"
  ],
  "related_registry_items": [
    {
      "id": "VI.T13",
      "title": "Response = SelfDesc Adjustment",
      "url": "/registry/object/VI.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Hallmarks.lean#L50-L52",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.Hallmarks",
        "url": "/verify/taulib/docs/book-vi-sectors-hallmarks/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Hallmarks.lean#L50-L52",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookVI.Sectors.Hallmarks](/verify/taulib/docs/book-vi-sectors-hallmarks/)
- Source path: [`TauLib/BookVI/Sectors/Hallmarks.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Hallmarks.lean#L50-L52)
- Source range: L50-L52
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VI.T13` — Response = SelfDesc Adjustment

## Immediate Comment / Docstring

```lean
/-- [VI.T13] Response = SelfDesc Adjustment. -/
```

## Source Excerpt

```lean
def response : Hallmark where
  classical := "response"
  formal := "selfdesc-adjustment"
```
