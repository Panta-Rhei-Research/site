---
{
  "projection_kind": "taulib_declaration",
  "title": "TauHorizon",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/tau-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::TauHorizon",
  "declaration_slug": "tau-horizon",
  "kind": "structure",
  "name": "TauHorizon",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 257,
  "source_line_end": 274,
  "registry_ids": [
    "V.D60"
  ],
  "related_registry_items": [
    {
      "id": "V.D60",
      "title": "tau-Horizon",
      "url": "/registry/object/V.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L257-L274",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L257-L274",
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
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L257-L274)
- Source range: L257-L274
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D60` — tau-Horizon

## Immediate Comment / Docstring

```lean
/-- [V.D60] τ-Horizon: surface of causal disconnection.

    Beyond the τ-horizon, no null intertwiner can escape to
    asymptotic observers. Unlike the orthodox event horizon:
    - Defined locally (not globally)
    - Resolution-dependent (sharpens with depth)
    - No singularity inside (density saturation instead)

    The τ-horizon radius is determined by the Schwarzschild-like
    condition at the given depth: R_h(n) ≈ 2G_τ M at depth n. -/
```

## Source Excerpt

```lean
structure TauHorizon where
  /-- Horizon radius numerator (in τ-units). -/
  radius_numer : Nat
  /-- Horizon radius denominator. -/
  radius_denom : Nat
  /-- Denominator positive. -/
  denom_pos : radius_denom > 0
  /-- Radius is positive. -/
  radius_positive : radius_numer > 0
  /-- Causal disconnection flag. -/
  causal_disconnect : Bool
  /-- Horizon is causally disconnecting. -/
  causal_proof : causal_disconnect = true
  /-- Refinement depth at which horizon is resolved. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  deriving Repr
```
