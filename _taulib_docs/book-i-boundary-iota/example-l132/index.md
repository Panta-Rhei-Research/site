---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L132",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota/example-l132/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.Iota`.",
  "declaration_id": "TauLib.BookI.Boundary.Iota::#eval:132",
  "declaration_slug": "example-l132",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.Iota",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota/",
  "source_line_start": 132,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L132-L132",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Iota",
        "url": "/verify/taulib/docs/book-i-boundary-iota/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L132-L132",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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

- Module: [TauLib.BookI.Boundary.Iota](/verify/taulib/docs/book-i-boundary-iota/)
- Source path: [`TauLib/BookI/Boundary/Iota.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L132-L132)
- Source range: L132-L132
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- B is the minority channel for large enough n (iota_tau < 0.5)
-- Note: at small bounds (n=50), B can be majority; minority emerges asymptotically
```

## Source Excerpt

```lean
example : b_minority_check 100 1000 = true := by native_decide
```
