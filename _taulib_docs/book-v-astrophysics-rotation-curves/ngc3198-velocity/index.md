---
{
  "projection_kind": "taulib_declaration",
  "title": "ngc3198_velocity",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/ngc3198-velocity/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::ngc3198_velocity",
  "declaration_slug": "ngc3198-velocity",
  "kind": "def",
  "name": "ngc3198_velocity",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 271,
  "source_line_end": 272,
  "registry_ids": [
    "V.T164"
  ],
  "related_registry_items": [
    {
      "id": "V.T164",
      "title": "NGC 3198 Zero-Parameter Prediction",
      "url": "/registry/object/V.T164/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L271-L272",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L271-L272",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L271-L272)
- Source range: L271-L272
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T164` — NGC 3198 Zero-Parameter Prediction

## Immediate Comment / Docstring

```lean
/-- [V.T164] NGC 3198 zero-parameter prediction from the Flat Rotation Curve Theorem.

    M_b = 1.4×10¹⁰ M_☉, H₀ = 67.4 km/s/Mpc (Planck):
      ℓ_τ = c/(H₀·√(1−ι_τ)) = 1.691×10²⁶ m
      v_∞ = (G·M_b·c²/(2·ℓ_τ))^{1/4} = 149.1 km/s

    Observed: ~150 km/s.  Accuracy: 0.6%.  Zero free parameters.

    Note: The V.D232 formula (v⁴ = G·M_b·a₀, a₀ = c·H₀·ι_τ/2) gives
    v_∞ = 122.5 km/s with local H₀=73.0 — V.T85 is the better velocity predictor
    for large spirals; V.D232 is the better a₀ formula. -/
```

## Source Excerpt

```lean
def ngc3198_velocity : String :=
  "NGC 3198: M_b=1.4e10 M_sun, H_0=67.4 (Planck) → v_inf=149.1 km/s (obs: ~150, 0.6%)"
```
