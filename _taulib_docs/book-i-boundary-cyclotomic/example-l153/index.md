---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L153",
  "permalink": "/corpus/taulib/docs/book-i-boundary-cyclotomic/example-l153/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.Cyclotomic`.",
  "declaration_id": "TauLib.BookI.Boundary.Cyclotomic::#eval:153",
  "declaration_slug": "example-l153",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_url": "/corpus/taulib/docs/book-i-boundary-cyclotomic/",
  "source_line_start": 153,
  "source_line_end": 153,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L153-L153",
  "formal_status": "example",
  "declaration_role": "example check",
  "formal_status_label": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Cyclotomic",
        "url": "/corpus/taulib/docs/book-i-boundary-cyclotomic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L153-L153",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "role": "example check",
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

- Module: [TauLib.BookI.Boundary.Cyclotomic](/corpus/taulib/docs/book-i-boundary-cyclotomic/)
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L153-L153)
- Source range: L153-L153
- Kind: `example`
- Public role: `example check`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 3 is a 6th root of unity mod 7. -/
```

## Source Excerpt

```lean
example : IsRootOfUnity 6 3 7 := by native_decide
```
