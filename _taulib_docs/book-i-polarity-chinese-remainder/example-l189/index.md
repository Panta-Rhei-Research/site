---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L189",
  "permalink": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l189/",
  "summary_short": "`example` declaration in `TauLib.BookI.Polarity.ChineseRemainder`.",
  "declaration_id": "TauLib.BookI.Polarity.ChineseRemainder::#eval:189",
  "declaration_slug": "example-l189",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.ChineseRemainder",
  "module_url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/",
  "source_line_start": 189,
  "source_line_end": 189,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L189-L189",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ChineseRemainder",
        "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L189-L189",
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

- Module: [TauLib.BookI.Polarity.ChineseRemainder](/verify/taulib/docs/book-i-polarity-chinese-remainder/)
- Source path: [`TauLib/BookI/Polarity/ChineseRemainder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L189-L189)
- Source range: L189-L189
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- e_1 (for p=3): e_1 mod 2 = 0, e_1 mod 3 = 1, e_1 mod 5 = 0
```

## Source Excerpt

```lean
example : crt_basis_check 3 1 0 = true := by native_decide
```
