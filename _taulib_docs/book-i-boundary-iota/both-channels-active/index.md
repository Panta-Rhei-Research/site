---
{
  "projection_kind": "taulib_declaration",
  "title": "both_channels_active",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota/both-channels-active/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Iota`.",
  "declaration_id": "TauLib.BookI.Boundary.Iota::both_channels_active",
  "declaration_slug": "both-channels-active",
  "kind": "def",
  "name": "both_channels_active",
  "module_name": "TauLib.BookI.Boundary.Iota",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota/",
  "source_line_start": 113,
  "source_line_end": 115,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L113-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Iota",
        "url": "/verify/taulib/docs/book-i-boundary-iota/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L113-L115",
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

- Module: [TauLib.BookI.Boundary.Iota](/verify/taulib/docs/book-i-boundary-iota/)
- Source path: [`TauLib/BookI/Boundary/Iota.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L113-L115)
- Source range: L113-L115
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check that both B and C counts are positive at bound n, N. -/
```

## Source Excerpt

```lean
def both_channels_active (n N : TauIdx) : Bool :=
  let (b, c) := bc_ratio_pair n N
  b > 0 && c > 0
```
