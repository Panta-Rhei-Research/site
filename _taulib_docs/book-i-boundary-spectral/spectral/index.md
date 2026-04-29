---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral",
  "permalink": "/verify/taulib/docs/book-i-boundary-spectral/spectral/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Spectral`.",
  "declaration_id": "TauLib.BookI.Boundary.Spectral::spectral",
  "declaration_slug": "spectral",
  "kind": "def",
  "name": "spectral",
  "module_name": "TauLib.BookI.Boundary.Spectral",
  "module_url": "/verify/taulib/docs/book-i-boundary-spectral/",
  "source_line_start": 44,
  "source_line_end": 44,
  "registry_ids": [
    "I.T12"
  ],
  "related_registry_items": [
    {
      "id": "I.T12",
      "title": "Spectral Decomposition",
      "url": "/registry/object/I.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L44-L44",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L44-L44",
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

- Module: [TauLib.BookI.Boundary.Spectral](/verify/taulib/docs/book-i-boundary-spectral/)
- Source path: [`TauLib/BookI/Boundary/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L44-L44)
- Source range: L44-L44
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.T12` — Spectral Decomposition

## Immediate Comment / Docstring

```lean
/-- [I.T12] The spectral transform: maps z to its (B-sector, C-sector) pair.
    This is to_sectors repackaged in spectral/character language. -/
```

## Source Excerpt

```lean
def spectral (z : SplitComplex) : SectorPair := to_sectors z
```
