---
{
  "projection_kind": "taulib_declaration",
  "title": "StarBuilder",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/star-builder/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::StarBuilder",
  "declaration_slug": "star-builder",
  "kind": "structure",
  "name": "StarBuilder",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 162,
  "source_line_end": 185,
  "registry_ids": [
    "V.D70"
  ],
  "related_registry_items": [
    {
      "id": "V.D70",
      "title": "Canonical star builder",
      "url": "/registry/object/V.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L162-L185",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L162-L185",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L162-L185)
- Source range: L162-L185
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D70` — Canonical star builder

## Immediate Comment / Docstring

```lean
/-- [V.D70] Star builder: constructive existence of a stellar model
    from central density and equation of state.

    Given:
    - Central density rho_c
    - Equation of state P = P(rho)
    Returns:
    - Density profile rho(r)
    - Pressure profile P(r)
    - Total mass M
    - Total radius R
    satisfying the TOV equations. -/
```

## Source Excerpt

```lean
structure StarBuilder where
  /-- Central density numerator. -/
  rho_c_numer : Nat
  /-- Central density denominator. -/
  rho_c_denom : Nat
  /-- Denominator positive. -/
  denom_pos : rho_c_denom > 0
  /-- Total mass numerator (result). -/
  total_mass_numer : Nat
  /-- Total mass denominator. -/
  total_mass_denom : Nat
  /-- Mass denominator positive. -/
  mass_denom_pos : total_mass_denom > 0
  /-- Total radius numerator (result). -/
  total_radius_numer : Nat
  /-- Total radius denominator. -/
  total_radius_denom : Nat
  /-- Radius denominator positive. -/
  radius_denom_pos : total_radius_denom > 0
  /-- Whether the model is coherent (satisfies TOV). -/
  is_coherent : Bool
  /-- Whether the solution is unique for given rho_c. -/
  is_unique : Bool
  deriving Repr
```
