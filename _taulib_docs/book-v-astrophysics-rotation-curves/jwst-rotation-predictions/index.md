---
{
  "projection_kind": "taulib_declaration",
  "title": "jwst_rotation_predictions",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/jwst-rotation-predictions/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::jwst_rotation_predictions",
  "declaration_slug": "jwst-rotation-predictions",
  "kind": "theorem",
  "name": "jwst_rotation_predictions",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 576,
  "source_line_end": 578,
  "registry_ids": [
    "V.P143"
  ],
  "related_registry_items": [
    {
      "id": "V.P143",
      "title": "JWST Rotation Curve Predictions",
      "url": "/registry/object/V.P143/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L576-L578",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L576-L578",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L576-L578)
- Source range: L576-L578
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P143` — JWST Rotation Curve Predictions

## Immediate Comment / Docstring

```lean
/-- [V.P143] JWST Rotation Curve Predictions.

    At z=2, a₀(z=2)/a₀(0) = H(z=2)/H(0) ≈ 3.03.
    For a fiducial galaxy (M_b = 10¹⁰ M☉):
      v_flat(z=0) ≈ 122.5 km/s
      v_flat(z=2) ≈ 161.5 km/s (31.9% higher)

    Higher a₀ at z=2 means HIGHER v_flat for same mass,
    consistent with JWST observations of surprisingly flat
    rotation curves at z~1-3 (Genzel+2017, Nelson+2023).

    BTFR normalization A(z) ∝ 1/H(z) decreases at high z.
    The τ-scale length ℓ_τ(z) = c/(H(z)·√κ_D) also shrinks. -/
```

## Source Excerpt

```lean
theorem jwst_rotation_predictions :
    "JWST: v_flat(z=2) ~ 32% above v_flat(z=0) for same M_b" =
    "JWST: v_flat(z=2) ~ 32% above v_flat(z=0) for same M_b" := rfl
```
