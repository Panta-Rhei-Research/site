---
{
  "projection_kind": "taulib_declaration",
  "title": "fourier",
  "permalink": "/verify/taulib/docs/book-i-boundary-fourier/fourier/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::fourier",
  "declaration_slug": "fourier",
  "kind": "def",
  "name": "fourier",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/verify/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 149,
  "source_line_end": 149,
  "registry_ids": [
    "I.D40"
  ],
  "related_registry_items": [
    {
      "id": "I.D40",
      "title": "Bipolar Fourier Transform",
      "url": "/registry/object/I.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L149-L149",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Fourier",
        "url": "/verify/taulib/docs/book-i-boundary-fourier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L149-L149",
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

- Module: [TauLib.BookI.Boundary.Fourier](/verify/taulib/docs/book-i-boundary-fourier/)
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L149-L149)
- Source range: L149-L149
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D40` — Bipolar Fourier Transform

## Immediate Comment / Docstring

```lean
/-- [I.D40] The bipolar Fourier transform: maps z to its spectral decomposition.
    This is the spectral transform repackaged as harmonic analysis. -/
```

## Source Excerpt

```lean
def fourier (z : SplitComplex) : SectorPair := spectral z
```
