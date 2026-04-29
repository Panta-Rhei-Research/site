---
{
  "projection_kind": "taulib_declaration",
  "title": "b_times_c_zero",
  "permalink": "/verify/taulib/docs/book-i-boundary-fourier/b-times-c-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::b_times_c_zero",
  "declaration_slug": "b-times-c-zero",
  "kind": "theorem",
  "name": "b_times_c_zero",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/verify/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 106,
  "source_line_end": 113,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L106-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L106-L113",
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
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L106-L113)
- Source range: L106-L113
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The B-ideal and C-ideal are orthogonal: their product is zero.
    If z ∈ ker(χ₋) and w ∈ ker(χ₊), then z·w = 0 in sector coordinates. -/
```

## Source Excerpt

```lean
theorem b_times_c_zero (z w : SplitComplex)
    (hz : in_b_ideal z) (hw : in_c_ideal w) :
    spectral (SplitComplex.mul z w) = SectorPair.zero := by
  rw [spectral_mul]
  unfold in_b_ideal at hz
  unfold in_c_ideal at hw
  simp only [SectorPair.mul, SectorPair.zero, SectorPair.mk.injEq]
  exact ⟨by rw [hw]; ring, by rw [hz]; ring⟩
```
