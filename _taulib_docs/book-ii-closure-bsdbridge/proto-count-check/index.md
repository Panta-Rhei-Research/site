---
{
  "projection_kind": "taulib_declaration",
  "title": "proto_count_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/proto-count-check/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::proto_count_check",
  "declaration_slug": "proto-count-check",
  "kind": "theorem",
  "name": "proto_count_check",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 223,
  "source_line_end": 224,
  "registry_ids": [
    "II.D65"
  ],
  "related_registry_items": [
    {
      "id": "II.D65",
      "title": "Proto-Rationality",
      "url": "/registry/object/II.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L223-L224",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.BSDbridge",
        "url": "/verify/taulib/docs/book-ii-closure-bsdbridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L223-L224",
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

- Module: [TauLib.BookII.Closure.BSDbridge](/verify/taulib/docs/book-ii-closure-bsdbridge/)
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L223-L224)
- Source range: L223-L224
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D65` — Proto-Rationality

## Immediate Comment / Docstring

```lean
-- Count checks [II.D65]
```

## Source Excerpt

```lean
theorem proto_count_check :
    proto_rational_count_check = true := by native_decide
```
