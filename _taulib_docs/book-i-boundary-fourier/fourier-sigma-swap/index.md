---
{
  "projection_kind": "taulib_declaration",
  "title": "fourier_sigma_swap",
  "permalink": "/verify/taulib/docs/book-i-boundary-fourier/fourier-sigma-swap/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::fourier_sigma_swap",
  "declaration_slug": "fourier-sigma-swap",
  "kind": "theorem",
  "name": "fourier_sigma_swap",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/verify/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 190,
  "source_line_end": 193,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L190-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L190-L193",
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
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L190-L193)
- Source range: L190-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D40` — Bipolar Fourier Transform

## Immediate Comment / Docstring

```lean
/-- [I.D40] σ = component swap in Fourier coordinates: σ exchanges B ↔ C harmonics. -/
```

## Source Excerpt

```lean
theorem fourier_sigma_swap (z : SplitComplex) :
    fourier (polarity_inv z) =
    ⟨(fourier z).c_sector, (fourier z).b_sector⟩ :=
  spectral_sigma z
```
