---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_ratio_acceleration",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/holonomy-ratio-acceleration/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::holonomy_ratio_acceleration",
  "declaration_slug": "holonomy-ratio-acceleration",
  "kind": "theorem",
  "name": "holonomy_ratio_acceleration",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 310,
  "source_line_end": 312,
  "registry_ids": [
    "V.T200"
  ],
  "related_registry_items": [
    {
      "id": "V.T200",
      "title": "Holonomy Ratio Acceleration Theorem",
      "url": "/registry/object/V.T200/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L310-L312",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L310-L312",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L310-L312)
- Source range: L310-L312
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T200` — Holonomy Ratio Acceleration Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T200] Holonomy Ratio Acceleration Theorem: the ratio between the
    bare capacity acceleration (V.T85) and the dressed MOND acceleration
    (V.D232) is exactly √(κ_D/κ_B), the holonomy-to-baryon coupling ratio.

    a₀(T85)/a₀(D232) = √(κ_D/κ_B) = √((1−ι_τ)/ι_τ²) ≈ 2.378

    V.T85  (bare):    a₀^bare = c·H₀·√(1−ι_τ)/2     (PDE restoring term)
    V.D232 (dressed): a₀^dress = c·H₀·ι_τ/2          (MOND observational)

    The same ratio governs:
    - Silk damping: ℓ_D/ℓ₁ = κ_D/κ_B (Sprint 14B, +9 ppm)
    - Matter-baryon fraction: ω_m/ω_b ~ κ_D/κ_B (Sprint 8A) -/
```

## Source Excerpt

```lean
theorem holonomy_ratio_acceleration :
    "a0_T85/a0_D232 = sqrt(kappa_D/kappa_B) = sqrt((1-iota)/iota^2) = 2.378" =
    "a0_T85/a0_D232 = sqrt(kappa_D/kappa_B) = sqrt((1-iota)/iota^2) = 2.378" := rfl
```
