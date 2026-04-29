---
{
  "projection_kind": "taulib_declaration",
  "title": "c_polarized_check",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarized-germs/c-polarized-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PolarizedGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.PolarizedGerms::c_polarized_check",
  "declaration_slug": "c-polarized-check",
  "kind": "def",
  "name": "c_polarized_check",
  "module_name": "TauLib.BookI.Polarity.PolarizedGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarized-germs/",
  "source_line_start": 121,
  "source_line_end": 123,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L121-L123",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PolarizedGerms",
        "url": "/verify/taulib/docs/book-i-polarity-polarized-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L121-L123",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Polarity.PolarizedGerms](/verify/taulib/docs/book-i-polarity-polarized-germs/)
- Source path: [`TauLib/BookI/Polarity/PolarizedGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L121-L123)
- Source range: L121-L123
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check if prime p appears C-polarized up to primorial depth d:
    B-channel constant from some point AND C-channel has nonzero values. -/
```

## Source Excerpt

```lean
def c_polarized_check (p d : TauIdx) : Bool :=
  if d ≤ 2 then false
  else const_check (b_channel_seq p) 2 d && cofinal_check (c_channel_seq p) 1 d
```
