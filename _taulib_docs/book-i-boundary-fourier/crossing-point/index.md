---
{
  "projection_kind": "taulib_declaration",
  "title": "crossing_point",
  "permalink": "/verify/taulib/docs/book-i-boundary-fourier/crossing-point/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::crossing_point",
  "declaration_slug": "crossing-point",
  "kind": "def",
  "name": "crossing_point",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/verify/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 41,
  "source_line_end": 41,
  "registry_ids": [
    "I.D39"
  ],
  "related_registry_items": [
    {
      "id": "I.D39",
      "title": "Crossing Point",
      "url": "/registry/object/I.D39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L41-L41",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L41-L41",
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
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L41-L41)
- Source range: L41-L41
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D39` — Crossing Point

## Immediate Comment / Docstring

```lean
/-- [I.D39] The crossing point in sector coordinates: both sectors equal.
    This is the algebraic locus where the two lobes of the lemniscate meet. -/
```

## Source Excerpt

```lean
def crossing_point : SectorPair := ⟨1, 1⟩
```
