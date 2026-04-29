---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_neg",
  "permalink": "/verify/taulib/docs/book-i-boundary-spectral/spectral-neg/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Spectral`.",
  "declaration_id": "TauLib.BookI.Boundary.Spectral::spectral_neg",
  "declaration_slug": "spectral-neg",
  "kind": "theorem",
  "name": "spectral_neg",
  "module_name": "TauLib.BookI.Boundary.Spectral",
  "module_url": "/verify/taulib/docs/book-i-boundary-spectral/",
  "source_line_start": 118,
  "source_line_end": 120,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L118-L120",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Spectral",
        "url": "/verify/taulib/docs/book-i-boundary-spectral/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L118-L120",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.Spectral](/verify/taulib/docs/book-i-boundary-spectral/)
- Source path: [`TauLib/BookI/Boundary/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L118-L120)
- Source range: L118-L120
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The spectral transform preserves negation. -/
```

## Source Excerpt

```lean
theorem spectral_neg (z : SplitComplex) :
    spectral (SplitComplex.neg z) = SectorPair.neg (spectral z) :=
  to_sectors_neg z
```
