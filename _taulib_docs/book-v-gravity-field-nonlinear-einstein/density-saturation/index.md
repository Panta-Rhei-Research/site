---
{
  "projection_kind": "taulib_declaration",
  "title": "DensitySaturation",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/density-saturation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::DensitySaturation",
  "declaration_slug": "density-saturation",
  "kind": "structure",
  "name": "DensitySaturation",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 178,
  "source_line_end": 191,
  "registry_ids": [
    "V.D57"
  ],
  "related_registry_items": [
    {
      "id": "V.D57",
      "title": "Density-saturated character",
      "url": "/registry/object/V.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L178-L191",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L178-L191",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L178-L191)
- Source range: L178-L191
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D57` — Density-saturated character

## Immediate Comment / Docstring

```lean
/-- [V.D57] Density saturation: maximum density at finite depth.

    The τ-framework has a density bound at every refinement depth n.
    No physical configuration can exceed the saturation density:

        ρ(n) ≤ ρ_sat(n)

    This replaces orthodox GR singularities with finite-density cores.
    The saturation density increases with depth but remains finite
    at every finite n.

    Numerically: ρ_sat is proportional to κ_τ / gap³. -/
```

## Source Excerpt

```lean
structure DensitySaturation where
  /-- Saturation density numerator. -/
  max_density_numer : Nat
  /-- Saturation density denominator. -/
  max_density_denom : Nat
  /-- Denominator positive. -/
  denom_pos : max_density_denom > 0
  /-- Saturation density is positive. -/
  density_positive : max_density_numer > 0
  /-- Refinement depth at which saturation is computed. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  deriving Repr
```
