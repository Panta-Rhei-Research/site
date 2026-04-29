---
{
  "projection_kind": "taulib_declaration",
  "title": "pol_label",
  "permalink": "/verify/taulib/docs/book-i-polarity-spectral/pol-label/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Spectral`.",
  "declaration_id": "TauLib.BookI.Polarity.Spectral::pol_label",
  "declaration_slug": "pol-label",
  "kind": "def",
  "name": "pol_label",
  "module_name": "TauLib.BookI.Polarity.Spectral",
  "module_url": "/verify/taulib/docs/book-i-polarity-spectral/",
  "source_line_start": 68,
  "source_line_end": 69,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L68-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L68-L69",
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
- Source path: [`TauLib/BookI/Polarity/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L68-L69)
- Source range: L68-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- String polarity label. -/
```

## Source Excerpt

```lean
def pol_label (p N : TauIdx) : String :=
  if pol_at p N then "B" else "C"
```
