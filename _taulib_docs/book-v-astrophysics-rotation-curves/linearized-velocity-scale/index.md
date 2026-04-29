---
{
  "projection_kind": "taulib_declaration",
  "title": "linearizedVelocityScale",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/linearized-velocity-scale/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::linearizedVelocityScale",
  "declaration_slug": "linearized-velocity-scale",
  "kind": "def",
  "name": "linearizedVelocityScale",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 623,
  "source_line_end": 625,
  "registry_ids": [
    "V.D262"
  ],
  "related_registry_items": [
    {
      "id": "V.D262",
      "title": "Linearized Velocity Scale",
      "url": "/registry/object/V.D262/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L623-L625",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L623-L625",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L623-L625)
- Source range: L623-L625
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D262` — Linearized Velocity Scale

## Immediate Comment / Docstring

```lean
/-- [V.D262] Linearized Velocity Scale: the characteristic velocity
    from the linearized capacity equation.

    v_lin = √(GM_b/(2ℓ_τ))

    For NGC 3198: v_lin ≈ 0.074 km/s (4 OOM below observed ~150 km/s).
    The gap factor v_T85/v_lin ≈ 2011 (velocity), or
    (v_T85/v_lin)⁴ = c²ℓ_τ/(2GM) ≈ 4×10¹² (v⁴).

    This gap is the c² cancellation theorem in action:
    linearization strips out the metric coupling a₀ = c²/(2ℓ_τ). -/
```

## Source Excerpt

```lean
def linearizedVelocityScale : String :=
  "v_lin = sqrt(GM/(2*ell_tau)) ~ 0.074 km/s for NGC 3198. " ++
  "Gap: v_T85/v_lin ~ 2011 (velocity), (v_T85/v_lin)^4 = c^2*ell/(2GM) ~ 4e12."
```
