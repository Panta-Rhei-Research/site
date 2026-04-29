---
{
  "projection_kind": "taulib_declaration",
  "title": "crossing_iff_real",
  "permalink": "/verify/taulib/docs/book-i-boundary-fourier/crossing-iff-real/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::crossing_iff_real",
  "declaration_slug": "crossing-iff-real",
  "kind": "theorem",
  "name": "crossing_iff_real",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/verify/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 51,
  "source_line_end": 56,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L51-L56",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L51-L56",
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

- Module: [TauLib.BookI.Boundary.Fourier](/verify/taulib/docs/book-i-boundary-fourier/)
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L51-L56)
- Source range: L51-L56
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D39` — Crossing Point

## Immediate Comment / Docstring

```lean
/-- [I.D39] Crossing characterization: a split-complex element z is at the crossing
    iff z is real (im = 0). Proof: b_sector = c_sector iff re+im = re-im iff im = 0. -/
```

## Source Excerpt

```lean
theorem crossing_iff_real (z : SplitComplex) :
    is_crossing (spectral z) ↔ z.im = 0 := by
  simp only [is_crossing, spectral, to_sectors]
  constructor
  · intro h; omega
  · intro h; omega
```
