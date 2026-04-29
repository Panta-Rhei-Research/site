---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L167",
  "permalink": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l167/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.Cyclotomic`.",
  "declaration_id": "TauLib.BookI.Boundary.Cyclotomic::#eval:167",
  "declaration_slug": "example-l167",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_url": "/verify/taulib/docs/book-i-boundary-cyclotomic/",
  "source_line_start": 167,
  "source_line_end": 167,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L167-L167",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Cyclotomic",
        "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L167-L167",
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

- Module: [TauLib.BookI.Boundary.Cyclotomic](/verify/taulib/docs/book-i-boundary-cyclotomic/)
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L167-L167)
- Source range: L167-L167
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT verification: 6^2 ≡ 1 mod 5 and 6^2 ≡ 1 mod 7, so 6^2 ≡ 1 mod 35. -/
```

## Source Excerpt

```lean
example : IsRootOfUnity 2 6 5 := by native_decide
```
