---
{
  "projection_kind": "taulib_declaration",
  "title": "encoding_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact/encoding-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Hyperfact`.",
  "declaration_id": "TauLib.BookI.Coordinates.Hyperfact::encoding_check",
  "declaration_slug": "encoding-check",
  "kind": "def",
  "name": "encoding_check",
  "module_name": "TauLib.BookI.Coordinates.Hyperfact",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact/",
  "source_line_start": 86,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L86-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Hyperfact",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L86-L87",
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

- Module: [TauLib.BookI.Coordinates.Hyperfact](/verify/taulib/docs/book-i-coordinates-hyperfact/)
- Source path: [`TauLib/BookI/Coordinates/Hyperfact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L86-L87)
- Source range: L86-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check that encoding is a left inverse of decoding. -/
```

## Source Excerpt

```lean
def encoding_check (x : TauIdx) : Bool :=
  tau_decode (tau_encode x) == x
```
