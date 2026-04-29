---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L75",
  "permalink": "/verify/taulib/docs/book-i-denotation-growth-escape/example-l75/",
  "summary_short": "`example` declaration in `TauLib.BookI.Denotation.GrowthEscape`.",
  "declaration_id": "TauLib.BookI.Denotation.GrowthEscape::#eval:75",
  "declaration_slug": "example-l75",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Denotation.GrowthEscape",
  "module_url": "/verify/taulib/docs/book-i-denotation-growth-escape/",
  "source_line_start": 75,
  "source_line_end": 75,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L75-L75",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.GrowthEscape",
        "url": "/verify/taulib/docs/book-i-denotation-growth-escape/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L75-L75",
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

- Module: [TauLib.BookI.Denotation.GrowthEscape](/verify/taulib/docs/book-i-denotation-growth-escape/)
- Source path: [`TauLib/BookI/Denotation/GrowthEscape.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L75-L75)
- Source range: L75-L75
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Already at c=4, tetration escapes the 5-prime tower
```

## Source Excerpt

```lean
example : tetration 2 4 % primorial 5 ≠ tetration 2 4 := by native_decide
```
