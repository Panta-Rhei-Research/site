---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_decode",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact/tau-decode/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Hyperfact`.",
  "declaration_id": "TauLib.BookI.Coordinates.Hyperfact::tau_decode",
  "declaration_slug": "tau-decode",
  "kind": "def",
  "name": "tau_decode",
  "module_name": "TauLib.BookI.Coordinates.Hyperfact",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact/",
  "source_line_start": 82,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L82-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L82-L83",
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
- Source path: [`TauLib/BookI/Coordinates/Hyperfact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L82-L83)
- Source range: L82-L83
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Decoding: reconstruct X from its spine encoding. -/
```

## Source Excerpt

```lean
def tau_decode (enc : List (TauIdx × TauIdx × TauIdx) × TauIdx) : TauIdx :=
  list_tower_prod enc.1 * enc.2
```
