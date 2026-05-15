---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L80",
  "permalink": "/corpus/taulib/docs/book-i-denotation-growth-escape/example-l80/",
  "summary_short": "`example` declaration in `TauLib.BookI.Denotation.GrowthEscape`.",
  "declaration_id": "TauLib.BookI.Denotation.GrowthEscape::#eval:80",
  "declaration_slug": "example-l80",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Denotation.GrowthEscape",
  "module_url": "/corpus/taulib/docs/book-i-denotation-growth-escape/",
  "source_line_start": 80,
  "source_line_end": 80,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L80-L80",
  "formal_status": "example",
  "declaration_role": "example check",
  "formal_status_label": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.GrowthEscape",
        "url": "/corpus/taulib/docs/book-i-denotation-growth-escape/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L80-L80",
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

- Module: [TauLib.BookI.Denotation.GrowthEscape](/corpus/taulib/docs/book-i-denotation-growth-escape/)
- Source path: [`TauLib/BookI/Denotation/GrowthEscape.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L80-L80)
- Source range: L80-L80
- Kind: `example`
- Public role: `example check`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- But tetration 2 4 = 65536 escapes (65536 > 30)
```

## Source Excerpt

```lean
example : tetration 2 4 % primorial 3 ≠ tetration 2 4 := by native_decide
```
