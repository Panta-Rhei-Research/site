---
{
  "projection_kind": "taulib_declaration",
  "title": "RegimeInvariance",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/regime-invariance/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::RegimeInvariance",
  "declaration_slug": "regime-invariance",
  "kind": "structure",
  "name": "RegimeInvariance",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 72,
  "source_line_end": 83,
  "registry_ids": [
    "V.D155"
  ],
  "related_registry_items": [
    {
      "id": "V.D155",
      "title": "Regime Invariance",
      "url": "/registry/object/V.D155/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L72-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L72-L83",
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
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L72-L83)
- Source range: L72-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D155` — Regime Invariance

## Immediate Comment / Docstring

```lean
/-- [V.D155] Regime invariance: a dynamical equation on τ¹ is
    regime-invariant if its algebraic form is unchanged across
    all refinement depths.

    The τ-Einstein equation R^H[χ_{n+1}] = κ_τ · T[χ_n] is
    regime-invariant: κ_τ = 1 − ι_τ is fixed, only χ_n varies. -/
```

## Source Excerpt

```lean
structure RegimeInvariance where
  /-- Coupling depth-independence (1 = fixed across all depths). -/
  coupling_fixed : Nat := 1
  /-- Equation depth-independence (1 = structural form unchanged). -/
  equation_fixed : Nat := 1
  /-- Coupling value numerator (κ_τ = 1 − ι_τ ≈ 0.6585). -/
  coupling_numer : Nat := 658541
  /-- Coupling value denominator. -/
  coupling_denom : Nat := 1000000
  /-- Denominator positive. -/
  coupling_denom_pos : coupling_denom > 0 := by omega
  deriving Repr
```
