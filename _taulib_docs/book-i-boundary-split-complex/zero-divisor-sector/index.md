---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_divisor_sector",
  "permalink": "/verify/taulib/docs/book-i-boundary-split-complex/zero-divisor-sector/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::zero_divisor_sector",
  "declaration_slug": "zero-divisor-sector",
  "kind": "theorem",
  "name": "zero_divisor_sector",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/verify/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 267,
  "source_line_end": 278,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L267-L278",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.SplitComplex",
        "url": "/verify/taulib/docs/book-i-boundary-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L267-L278",
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

- Module: [TauLib.BookI.Boundary.SplitComplex](/verify/taulib/docs/book-i-boundary-split-complex/)
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L267-L278)
- Source range: L267-L278
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A split-complex number z is a zero divisor iff one sector coordinate vanishes.
    Forward: if z * w = 0 with w nonzero, then one sector of z is zero.
    We prove: z * w = 0 implies (z.re+z.im)*(w.re+w.im) = 0 AND
    (z.re-z.im)*(w.re-w.im) = 0. So if w has both sectors nonzero,
    both sectors of z must be zero (and z = 0). Nontrivial zero divisors
    have exactly one sector vanishing. -/
```

## Source Excerpt

```lean
theorem zero_divisor_sector (z w : SplitComplex)
    (h : SplitComplex.mul z w = SplitComplex.zero) :
    (z.re + z.im) * (w.re + w.im) = 0 ∧
    (z.re - z.im) * (w.re - w.im) = 0 := by
  simp only [SplitComplex.mul, SplitComplex.zero, SplitComplex.mk.injEq] at h
  obtain ⟨hR, hI⟩ := h
  constructor
  · -- (z.re + z.im) * (w.re + w.im) = z.re*w.re + z.re*w.im + z.im*w.re + z.im*w.im
    -- = (z.re*w.re + z.im*w.im) + (z.re*w.im + z.im*w.re) = hR + hI = 0
    linear_combination hR + hI
  · -- (z.re - z.im) * (w.re - w.im) = (z.re*w.re + z.im*w.im) - (z.re*w.im + z.im*w.re) = hR - hI = 0
    linear_combination hR - hI
```
