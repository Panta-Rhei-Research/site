---
{
  "projection_kind": "taulib_declaration",
  "title": "aqual_as_projection",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/aqual-as-projection/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::aqual_as_projection",
  "declaration_slug": "aqual-as-projection",
  "kind": "theorem",
  "name": "aqual_as_projection",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 925,
  "source_line_end": 929,
  "registry_ids": [
    "V.P146"
  ],
  "related_registry_items": [
    {
      "id": "V.P146",
      "title": "AQUAL as Projection",
      "url": "/registry/object/V.P146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L925-L929",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L925-L929",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L925-L929)
- Source range: L925-L929
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P146` — AQUAL as Projection

## Immediate Comment / Docstring

```lean
/-- [V.P146] AQUAL as Projection (τ-effective, circular orbits).

    From two-channel g² = g_N² + g_N·a₀, define μ = g_N/g:
      μ² = g_N²/(g_N²+g_N·a₀) = x/(1+x), x = g_N/a₀
      μ_2ch(x) = √(x/(1+x))

    For spherical symmetry, AQUAL PDE ∇·[μ·∇Φ] = 4πGρ is
    algebraically equivalent (∇·[g_N/g · g · r̂] = ∇·[g_N · r̂] = 4πGρ).
    Nonlinearity appears only upon projecting out fiber T².
    General non-spherical PDE form remains open. -/
```

## Source Excerpt

```lean
theorem aqual_as_projection :
    "AQUAL = projection of linear tau^3 geodesic to base tau^1. " ++
    "Circular/spherical: mu_2ch(x) = sqrt(x/(1+x)) from two-channel." =
    "AQUAL = projection of linear tau^3 geodesic to base tau^1. " ++
    "Circular/spherical: mu_2ch(x) = sqrt(x/(1+x)) from two-channel." := rfl
```
