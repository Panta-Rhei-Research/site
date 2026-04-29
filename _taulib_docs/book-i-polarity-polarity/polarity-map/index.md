---
{
  "projection_kind": "taulib_declaration",
  "title": "polarity_map",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarity/polarity-map/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Polarity`.",
  "declaration_id": "TauLib.BookI.Polarity.Polarity::polarity_map",
  "declaration_slug": "polarity-map",
  "kind": "def",
  "name": "polarity_map",
  "module_name": "TauLib.BookI.Polarity.Polarity",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarity/",
  "source_line_start": 121,
  "source_line_end": 121,
  "registry_ids": [
    "I.T05"
  ],
  "related_registry_items": [
    {
      "id": "I.T05",
      "title": "Prime Polarity Theorem",
      "url": "/registry/object/I.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L121-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Polarity",
        "url": "/verify/taulib/docs/book-i-polarity-polarity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L121-L121",
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

- Module: [TauLib.BookI.Polarity.Polarity](/verify/taulib/docs/book-i-polarity-polarity/)
- Source path: [`TauLib/BookI/Polarity/Polarity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L121-L121)
- Source range: L121-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.T05` — Prime Polarity Theorem

## Immediate Comment / Docstring

```lean
/-- [I.T05] The polarity map at bound N: returns true (B-dominant) or false (C-dominant)
    based on the spectral signature comparison B_max > C_max. -/
```

## Source Excerpt

```lean
def polarity_map (p N : TauIdx) : Bool := pol_at p N
```
