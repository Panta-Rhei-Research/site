---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_fixed_iff_real",
  "permalink": "/corpus/taulib/docs/book-i-boundary-fourier/sigma-fixed-iff-real/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::sigma_fixed_iff_real",
  "declaration_slug": "sigma-fixed-iff-real",
  "kind": "theorem",
  "name": "sigma_fixed_iff_real",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/corpus/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 196,
  "source_line_end": 206,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L196-L206",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Fourier",
        "url": "/corpus/taulib/docs/book-i-boundary-fourier/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L196-L206",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.Fourier](/corpus/taulib/docs/book-i-boundary-fourier/)
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L196-L206)
- Source range: L196-L206
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Fourier-space characterization of fixed points of σ: z is σ-fixed iff z is real. -/
```

## Source Excerpt

```lean
theorem sigma_fixed_iff_real (z : SplitComplex) :
    polarity_inv z = z ↔ z.im = 0 := by
  constructor
  · intro h
    have := congrArg SplitComplex.im h
    simp [polarity_inv] at this
    omega
  · intro h
    ext
    · simp [polarity_inv]
    · simp [polarity_inv, h]
```
