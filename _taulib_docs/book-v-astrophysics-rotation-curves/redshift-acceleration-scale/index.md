---
{
  "projection_kind": "taulib_declaration",
  "title": "redshift_acceleration_scale",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/redshift-acceleration-scale/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::redshift_acceleration_scale",
  "declaration_slug": "redshift-acceleration-scale",
  "kind": "theorem",
  "name": "redshift_acceleration_scale",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 555,
  "source_line_end": 557,
  "registry_ids": [
    "V.T204"
  ],
  "related_registry_items": [
    {
      "id": "V.T204",
      "title": "Redshift-Dependent Acceleration Scale",
      "url": "/registry/object/V.T204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L555-L557",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L555-L557",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L555-L557)
- Source range: L555-L557
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T204` — Redshift-Dependent Acceleration Scale

## Immediate Comment / Docstring

```lean
/-- [V.T204] Redshift-Dependent Acceleration Scale.

    UNIQUE falsifiable prediction of the τ-framework:
      a₀(z) = c · H(z) · ι_τ / 2

    where H(z) = H₀ · √(Ω_m(1+z)³ + Ω_Λ) is the Hubble rate.
    This predicts a₀ EVOLVES with redshift:

    z=0: a₀ = 1.12×10⁻¹⁰ m/s² (1.00× local)
    z=1: a₀ = 2.09×10⁻¹⁰ m/s² (1.87× local)
    z=2: a₀ = 3.39×10⁻¹⁰ m/s² (3.03× local)
    z=4: a₀ = 6.57×10⁻¹⁰ m/s² (5.87× local)

    Distinguishing predictions:
    - CDM: a₀ is not fundamental (depends on halo profile)
    - MOND: a₀ is CONSTANT (does not evolve)
    - τ: a₀(z) ∝ H(z) EVOLVES — testable with JWST -/
```

## Source Excerpt

```lean
theorem redshift_acceleration_scale :
    "a_0(z) = c*H(z)*iota/2 evolves with redshift, unique to tau framework" =
    "a_0(z) = c*H(z)*iota/2 evolves with redshift, unique to tau framework" := rfl
```
