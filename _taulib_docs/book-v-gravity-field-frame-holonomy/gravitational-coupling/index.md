---
{
  "projection_kind": "taulib_declaration",
  "title": "GravitationalCoupling",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gravitational-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::GravitationalCoupling",
  "declaration_slug": "gravitational-coupling",
  "kind": "structure",
  "name": "GravitationalCoupling",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 226,
  "source_line_end": 238,
  "registry_ids": [
    "V.D46"
  ],
  "related_registry_items": [
    {
      "id": "V.D46",
      "title": "Gravitational coupling kappa_tau",
      "url": "/registry/object/V.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L226-L238",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L226-L238",
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L226-L238)
- Source range: L226-L238
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D46` — Gravitational coupling kappa_tau

## Immediate Comment / Docstring

```lean
/-- [V.D46] Gravitational coupling κ_τ = 1 − ι_τ.

    The D-sector self-coupling at primorial depth 1.
    Numerically: κ_τ = 658541/1000000 ≈ 0.658541.

    Properties:
    - σ-fixed (unpolarized, invariant under polarity swap)
    - Unique unpolarized coupling on the base circle
    - Temporal complement: κ_τ + κ_A = 1 (with weak sector) -/
```

## Source Excerpt

```lean
structure GravitationalCoupling where
  /-- κ_τ numerator = iotaD − iota. -/
  kappa_numer : Nat
  /-- κ_τ denominator = iotaD. -/
  kappa_denom : Nat
  /-- Denominator positive. -/
  denom_pos : kappa_denom > 0
  /-- The value equals 1 − ι_τ. -/
  is_one_minus_iota : kappa_numer = iotaD - iota ∧
                      kappa_denom = iotaD
  /-- σ-fixed (unpolarized). -/
  sigma_fixed : Bool := true
  deriving Repr
```
