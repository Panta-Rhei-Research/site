---
{
  "projection_kind": "taulib_declaration",
  "title": "pol_at",
  "permalink": "/verify/taulib/docs/book-i-polarity-spectral/pol-at/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Spectral`.",
  "declaration_id": "TauLib.BookI.Polarity.Spectral::pol_at",
  "declaration_slug": "pol-at",
  "kind": "def",
  "name": "pol_at",
  "module_name": "TauLib.BookI.Polarity.Spectral",
  "module_url": "/verify/taulib/docs/book-i-polarity-spectral/",
  "source_line_start": 65,
  "source_line_end": 65,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L65-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Spectral",
        "url": "/verify/taulib/docs/book-i-polarity-spectral/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L65-L65",
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

- Module: [TauLib.BookI.Polarity.Spectral](/verify/taulib/docs/book-i-polarity-spectral/)
- Source path: [`TauLib/BookI/Polarity/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L65-L65)
- Source range: L65-L65
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Polarity at bound N: true = B-dominant, false = C-dominant. -/
```

## Source Excerpt

```lean
def pol_at (p N : TauIdx) : Bool := b_max p N > c_max p N
```
