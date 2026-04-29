---
{
  "projection_kind": "taulib_declaration",
  "title": "cofinal_check",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarized-germs/cofinal-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PolarizedGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.PolarizedGerms::cofinal_check",
  "declaration_slug": "cofinal-check",
  "kind": "def",
  "name": "cofinal_check",
  "module_name": "TauLib.BookI.Polarity.PolarizedGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarized-germs/",
  "source_line_start": 86,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L86-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L86-L87",
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
- Source path: [`TauLib/BookI/Polarity/PolarizedGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L86-L87)
- Source range: L86-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
def cofinal_check (f : Nat → Nat) (from_depth to_depth : Nat) : Bool :=
  cofinal_check_go f from_depth to_depth (to_depth - from_depth + 1)
```
