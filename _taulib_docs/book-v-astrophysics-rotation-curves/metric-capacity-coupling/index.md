---
{
  "projection_kind": "taulib_declaration",
  "title": "metric_capacity_coupling",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/metric-capacity-coupling/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::metric_capacity_coupling",
  "declaration_slug": "metric-capacity-coupling",
  "kind": "theorem",
  "name": "metric_capacity_coupling",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 649,
  "source_line_end": 653,
  "registry_ids": [
    "V.T206"
  ],
  "related_registry_items": [
    {
      "id": "V.T206",
      "title": "Metric-Capacity Coupling Source Theorem",
      "url": "/registry/object/V.T206/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L649-L653",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L649-L653",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L649-L653)
- Source range: L649-L653
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T206` — Metric-Capacity Coupling Source Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T206] Metric-Capacity Coupling Source Theorem.

    The linearized capacity equation sources scalar field u with:
      S_cap = 4πGρ/c²  (scalar source, c⁻² suppressed)

    The full τ-Einstein equation sources metric perturbation h₀₀
    through the connection to the Newtonian potential Φ:
      h₀₀ = 2Φ/c²  where ∇²Φ = 4πGρ  (metric source)

    In both cases, the perturbation scales as GM/(c²r). But the
    FLATTENING mechanism (K₀ profile → logarithmic potential) requires
    an amplitude set by the metric coupling a₀ = c²/(2ℓ_τ), which
    the scalar capacity equation cannot access.

    The c² in V.T85 enters through a₀ = c²/(2ℓ_τ), a metric quantity
    that links the screening length ℓ_τ to the acceleration scale.
    It is NOT a PDE output but a structural consequence of the
    relativistic connection between c, ℓ_τ, and gravitational dynamics. -/
```

## Source Excerpt

```lean
theorem metric_capacity_coupling :
    "a_0 = c^2/(2*ell_tau) = c*H0*sqrt(kD)/2 is METRIC coupling, " ++
    "not accessible from scalar capacity PDE (V.T205)" =
    "a_0 = c^2/(2*ell_tau) = c*H0*sqrt(kD)/2 is METRIC coupling, " ++
    "not accessible from scalar capacity PDE (V.T205)" := rfl
```
