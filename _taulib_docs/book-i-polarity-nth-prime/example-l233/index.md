---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L233",
  "permalink": "/verify/taulib/docs/book-i-polarity-nth-prime/example-l233/",
  "summary_short": "`example` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::#eval:233",
  "declaration_slug": "example-l233",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/verify/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 233,
  "source_line_end": 233,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L233-L233",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.NthPrime",
        "url": "/verify/taulib/docs/book-i-polarity-nth-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L233-L233",
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

- Module: [TauLib.BookI.Polarity.NthPrime](/verify/taulib/docs/book-i-polarity-nth-prime/)
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L233-L233)
- Source range: L233-L233
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Freshness checks
```

## Source Excerpt

```lean
example : primorial 1 % nth_prime 2 ≠ 0 := by native_decide
```
