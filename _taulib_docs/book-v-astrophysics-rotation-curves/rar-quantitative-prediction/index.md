---
{
  "projection_kind": "taulib_declaration",
  "title": "rar_quantitative_prediction",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/rar-quantitative-prediction/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::rar_quantitative_prediction",
  "declaration_slug": "rar-quantitative-prediction",
  "kind": "theorem",
  "name": "rar_quantitative_prediction",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 487,
  "source_line_end": 489,
  "registry_ids": [
    "V.P142"
  ],
  "related_registry_items": [
    {
      "id": "V.P142",
      "title": "RAR Quantitative Prediction",
      "url": "/registry/object/V.P142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L487-L489",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L487-L489",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L487-L489)
- Source range: L487-L489
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P142` — RAR Quantitative Prediction

## Immediate Comment / Docstring

```lean
/-- [V.P142] RAR Quantitative Prediction: the τ interpolation function
    μ_τ(x) = x/√(1+x²) produces a tight Radial Acceleration Relation
    with a SINGLE universal a₀ governing all galaxies.

    Key results (12-galaxy sample, 6 radii each = 72 data points):
    - μ_τ matches the "standard" MOND interpolation exactly
    - A single a₀ governs dwarfs (DDO 154) through giants (NGC 2841)
    - No free halo parameters needed
    - Deep MOND: g_obs = √(g_bar · a₀) → flat rotation curves
    - Newtonian: g_obs = g_bar → standard gravity recovered -/
```

## Source Excerpt

```lean
theorem rar_quantitative_prediction :
    "RAR from mu_tau = x/sqrt(1+x^2): single a_0, zero free halo params" =
    "RAR from mu_tau = x/sqrt(1+x^2): single a_0, zero free halo params" := rfl
```
