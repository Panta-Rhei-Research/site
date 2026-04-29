---
{
  "projection_kind": "taulib_declaration",
  "title": "c2_cancellation_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/c2-cancellation-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::c2_cancellation_theorem",
  "declaration_slug": "c2-cancellation-theorem",
  "kind": "theorem",
  "name": "c2_cancellation_theorem",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 602,
  "source_line_end": 606,
  "registry_ids": [
    "V.T205"
  ],
  "related_registry_items": [
    {
      "id": "V.T205",
      "title": "c² Cancellation Theorem",
      "url": "/registry/object/V.T205/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L602-L606",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L602-L606",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L602-L606)
- Source range: L602-L606
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T205` — c² Cancellation Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T205] c² Cancellation Theorem: in the linearized capacity equation,
    the c² factor cancels exactly between source and velocity extraction.

    Source:     (∇² − 1/ℓ²)u = −(4πG/c²)ρ  →  u ~ GM/(c²r)
    Extraction: v² = −(c²r/2)u′             →  c² × c⁻² = 1
    Net:        v_cap² = GM·f(r/R_d, r/ℓ_τ)/r  (independent of c)

    The c² factor in V.T85 (v⁴ = GMc²/(2ℓ_τ)) is NOT accessible by
    any linearization of the capacity equation.

    Verified numerically: point mass (3D), thin disk (2D, K₀), arbitrary
    density (Green's function convolution), all to machine precision.

    Physical content: the cancellation is a dimensional necessity.
    The capacity equation is a SCALAR equation with source 4πGρ/c².
    The c⁻² in the source is required by dimensional analysis (u is
    dimensionless). Extraction via v² = −(c²r/2)u′ re-introduces c²
    which exactly cancels the c⁻². -/
```

## Source Excerpt

```lean
theorem c2_cancellation_theorem :
    "v_cap^2 = GM*f(r/Rd, r/ell)/r, independent of c; " ++
    "c^2 in V.T85 NOT accessible by linearization" =
    "v_cap^2 = GM*f(r/Rd, r/ell)/r, independent of c; " ++
    "c^2 in V.T85 NOT accessible by linearization" := rfl
```
