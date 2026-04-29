---
{
  "projection_kind": "taulib_declaration",
  "title": "TauEinsteinField",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/tau-einstein-field/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::TauEinsteinField",
  "declaration_slug": "tau-einstein-field",
  "kind": "structure",
  "name": "TauEinsteinField",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 161,
  "source_line_end": 174,
  "registry_ids": [
    "V.D51"
  ],
  "related_registry_items": [
    {
      "id": "V.D51",
      "title": "tau-Einstein equation --- V.D06",
      "url": "/registry/object/V.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L161-L174",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauEinsteinEq",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L161-L174",
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L161-L174)
- Source range: L161-L174
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D51` — tau-Einstein equation --- V.D06

## Immediate Comment / Docstring

```lean
/-- [V.D51] τ-Einstein equation in the gravitational field context:
    R^H = κ_τ · T^mat.

    This is a boundary-character identity in H_∂[n]:
    - LHS: curvature character (D-sector holonomy defect)
    - RHS: κ_τ times matter character (3 spatial sectors)

    Cross-multiplied identity:
    defect_numer · kappa_denom · matter_denom =
    kappa_numer · matter_total · defect_denom

    Key distinctions from orthodox GR:
    1. Algebraic identity, not differential equation
    2. Boundary determines interior (Hartogs)
    3. Unique by τ-NF minimization (no gauge freedom)
    4. Backreaction automatic (τ-Bianchi corollary) -/
```

## Source Excerpt

```lean
structure TauEinsteinField where
  /-- The curvature character R^H. -/
  curvature : CurvatureCharH
  /-- The matter character T^mat. -/
  matter : MatterCharField
  /-- The gravitational coupling κ_τ. -/
  kappa : GravitationalCoupling
  /-- Depths must match. -/
  depth_match : curvature.depth = matter.depth
  /-- The Einstein identity (cross-multiplied). -/
  einstein_identity :
    curvature.defect_numer * kappa.kappa_denom * matter.denom =
    kappa.kappa_numer * matter.total_numer * curvature.defect_denom
  deriving Repr
```
