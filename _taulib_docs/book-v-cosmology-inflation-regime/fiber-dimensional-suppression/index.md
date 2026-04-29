---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberDimensionalSuppression",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/fiber-dimensional-suppression/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::FiberDimensionalSuppression",
  "declaration_slug": "fiber-dimensional-suppression",
  "kind": "structure",
  "name": "FiberDimensionalSuppression",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 260,
  "source_line_end": 281,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L260-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L260-L281",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L260-L281)
- Source range: L260-L281
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P136 derivation] Tensor-scalar ratio from fiber dimensional analysis.

    In the fibered product τ³ = τ¹ ×_f T²:
    - Tensor modes (GW) are D-sector frame-holonomy fluctuations on τ¹
    - Scalar modes are boundary-character fluctuations on full τ³
    - Each fiber dimension contributes breathing-fraction suppression ι_τ
    - Power spectrum is quadratic in amplitude (P ∝ |δ|²)

    Therefore: r = ι_τ^{2 · dim(T²)} = ι_τ^{2×2} = ι_τ⁴. -/
```

## Source Excerpt

```lean
structure FiberDimensionalSuppression where
  /-- Base dimension (τ¹). -/
  base_dim : Nat := 1
  /-- Fiber dimension (T²). -/
  fiber_dim : Nat := 2
  /-- Total arena dimension (τ³). -/
  arena_dim : Nat := 3
  /-- Fibration consistency: dim(τ³) = dim(τ¹) + dim(T²). -/
  fibration : arena_dim = base_dim + fiber_dim := by omega
  /-- Power spectrum order (P ∝ |δ|²). -/
  power_order : Nat := 2
  /-- Total exponent: power_order × fiber_dim = 4. -/
  total_exponent : Nat := 4
  /-- Exponent derivation. -/
  exponent_eq : total_exponent = power_order * fiber_dim := by omega
  /-- Number of tensor polarizations (GW has 2: +,×). -/
  n_tensor_pol : Nat := 2
  /-- Number of adiabatic scalar modes. -/
  n_scalar_modes : Nat := 1
  /-- Free parameters beyond ι_τ. -/
  free_params : Nat := 0
  deriving Repr
```
