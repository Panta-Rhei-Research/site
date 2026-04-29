---
{
  "projection_kind": "taulib_declaration",
  "title": "capacity_equation_solution",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/capacity-equation-solution/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::capacity_equation_solution",
  "declaration_slug": "capacity-equation-solution",
  "kind": "theorem",
  "name": "capacity_equation_solution",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 434,
  "source_line_end": 436,
  "registry_ids": [
    "V.T201"
  ],
  "related_registry_items": [
    {
      "id": "V.T201",
      "title": "Capacity Equation Numerical Solution",
      "url": "/registry/object/V.T201/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L434-L436",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L434-L436",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L434-L436)
- Source range: L434-L436
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T201` — Capacity Equation Numerical Solution

## Immediate Comment / Docstring

```lean
/-- [V.T201] Capacity equation numerical solution (first-ever).

    The linearized capacity equation (screened Poisson) produces:
    v_screen = √(G·M_b/(2·ℓ_τ)) at large r — CONSTANT, correct
    qualitative behavior. But amplitude is 4 orders of magnitude
    below observed (~0.07 km/s vs ~150 km/s for NGC 3198).

    The c² factor in V.T85 (v⁴ = G·M·c²/(2·ℓ_τ)) requires the
    full nonlinear τ-Einstein equation, not the linearized
    capacity perturbation. The point-mass solution confirms:
    u(r) = (GM/(c²r))·exp(−r/ℓ_τ), giving v_cap = v_N/√2 (Keplerian). -/
```

## Source Excerpt

```lean
theorem capacity_equation_solution :
    "Linearized: v_screen = sqrt(GM/(2*ell_tau)) ~ 0.07 km/s, 4 OOM below obs" =
    "Linearized: v_screen = sqrt(GM/(2*ell_tau)) ~ 0.07 km/s, 4 OOM below obs" := rfl
```
