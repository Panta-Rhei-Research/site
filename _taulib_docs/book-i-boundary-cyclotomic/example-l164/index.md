---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L164",
  "permalink": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l164/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.Cyclotomic`.",
  "declaration_id": "TauLib.BookI.Boundary.Cyclotomic::#eval:164",
  "declaration_slug": "example-l164",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_url": "/verify/taulib/docs/book-i-boundary-cyclotomic/",
  "source_line_start": 164,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L164-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L164-L164",
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
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L164-L164)
- Source range: L164-L164
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 2 is a 3rd root of unity mod 7 (since 2^3 = 8 ≡ 1 mod 7). -/
```

## Source Excerpt

```lean
example : IsRootOfUnity 3 2 7 := by native_decide
```
