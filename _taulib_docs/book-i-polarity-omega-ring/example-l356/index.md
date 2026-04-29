---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L356",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-ring/example-l356/",
  "summary_short": "`example` declaration in `TauLib.BookI.Polarity.OmegaRing`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaRing::#eval:356",
  "declaration_slug": "example-l356",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.OmegaRing",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-ring/",
  "source_line_start": 356,
  "source_line_end": 356,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L356-L356",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaRing",
        "url": "/verify/taulib/docs/book-i-polarity-omega-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L356-L356",
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

- Module: [TauLib.BookI.Polarity.OmegaRing](/verify/taulib/docs/book-i-polarity-omega-ring/)
- Source path: [`TauLib/BookI/Polarity/OmegaRing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L356-L356)
- Source range: L356-L356
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Compatible_add for canonical tails matches nat_to_tail of sum
```

## Source Excerpt

```lean
example : (mk_omega_tail_add 7 42 5).components = (mk_omega_tail 49 5).components := by native_decide
```
