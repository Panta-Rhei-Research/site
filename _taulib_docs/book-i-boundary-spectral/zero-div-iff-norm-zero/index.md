---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_div_iff_norm_zero",
  "permalink": "/verify/taulib/docs/book-i-boundary-spectral/zero-div-iff-norm-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Spectral`.",
  "declaration_id": "TauLib.BookI.Boundary.Spectral::zero_div_iff_norm_zero",
  "declaration_slug": "zero-div-iff-norm-zero",
  "kind": "theorem",
  "name": "zero_div_iff_norm_zero",
  "module_name": "TauLib.BookI.Boundary.Spectral",
  "module_url": "/verify/taulib/docs/book-i-boundary-spectral/",
  "source_line_start": 199,
  "source_line_end": 202,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L199-L202",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L199-L202",
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
- Source path: [`TauLib/BookI/Boundary/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L199-L202)
- Source range: L199-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Zero divisors have zero spectral norm. -/
```

## Source Excerpt

```lean
theorem zero_div_iff_norm_zero (z : SplitComplex) :
    spectral_norm z = 0 ↔ (z.re + z.im = 0 ∨ z.re - z.im = 0) := by
  simp only [spectral_norm, spectral, to_sectors]
  exact mul_eq_zero
```
