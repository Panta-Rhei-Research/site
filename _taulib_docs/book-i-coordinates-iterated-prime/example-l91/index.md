---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L91",
  "permalink": "/verify/taulib/docs/book-i-coordinates-iterated-prime/example-l91/",
  "summary_short": "`example` declaration in `TauLib.BookI.Coordinates.IteratedPrime`.",
  "declaration_id": "TauLib.BookI.Coordinates.IteratedPrime::#eval:91",
  "declaration_slug": "example-l91",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Coordinates.IteratedPrime",
  "module_url": "/verify/taulib/docs/book-i-coordinates-iterated-prime/",
  "source_line_start": 91,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L91-L91",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.IteratedPrime",
        "url": "/verify/taulib/docs/book-i-coordinates-iterated-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L91-L91",
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

- Module: [TauLib.BookI.Coordinates.IteratedPrime](/verify/taulib/docs/book-i-coordinates-iterated-prime/)
- Source path: [`TauLib/BookI/Coordinates/IteratedPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L91-L91)
- Source range: L91-L91
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Level 1 (π-orbit): nthPrime (0-indexed)
-- nthPrime 0 = 2, nthPrime 1 = 3, nthPrime 2 = 5, nthPrime 4 = 11
```

## Source Excerpt

```lean
example : iteratedPrime 1 0 = 2 := by native_decide
```
