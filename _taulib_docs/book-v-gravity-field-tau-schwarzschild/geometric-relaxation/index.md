---
{
  "projection_kind": "taulib_declaration",
  "title": "GeometricRelaxation",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/geometric-relaxation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::GeometricRelaxation",
  "declaration_slug": "geometric-relaxation",
  "kind": "structure",
  "name": "GeometricRelaxation",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 107,
  "source_line_end": 120,
  "registry_ids": [
    "V.D63"
  ],
  "related_registry_items": [
    {
      "id": "V.D63",
      "title": "Geometric relaxation",
      "url": "/registry/object/V.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L107-L120",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L107-L120",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L107-L120)
- Source range: L107-L120
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D63` — Geometric relaxation

## Immediate Comment / Docstring

```lean
/-- [V.D63] Geometric relaxation: the process by which a collapsing
    object loses mass to gravitational binding energy.

    The mass index decreases from M_initial to M_stable.
    This is NOT Hawking evaporation -- it occurs BEFORE maturity. -/
```

## Source Excerpt

```lean
structure GeometricRelaxation where
  /-- Initial mass index numerator. -/
  initial_mass_numer : Nat
  /-- Stable mass index numerator. -/
  stable_mass_numer : Nat
  /-- Common denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Binding energy fraction: initial >= stable. -/
  mass_decrease : initial_mass_numer ≥ stable_mass_numer
  /-- This occurs before maturity horizon. -/
  pre_maturity : Bool := true
  deriving Repr
```
