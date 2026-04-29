---
{
  "projection_kind": "taulib_declaration",
  "title": "TensionProfile",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/tension-profile/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::TensionProfile",
  "declaration_slug": "tension-profile",
  "kind": "structure",
  "name": "TensionProfile",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 133,
  "source_line_end": 144,
  "registry_ids": [
    "V.D69"
  ],
  "related_registry_items": [
    {
      "id": "V.D69",
      "title": "Tension profile",
      "url": "/registry/object/V.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L133-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L133-L144",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L133-L144)
- Source range: L133-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D69` — Tension profile

## Immediate Comment / Docstring

```lean
/-- [V.D69] Tension profile: radial density rho(r) and pressure P(r)
    satisfying the TOV equation at each shell. -/
```

## Source Excerpt

```lean
structure TensionProfile where
  /-- Number of radial shells. -/
  shell_count : Nat
  /-- Central density numerator. -/
  rho_center_numer : Nat
  /-- Central density denominator. -/
  rho_center_denom : Nat
  /-- Denominator positive. -/
  denom_pos : rho_center_denom > 0
  /-- Surface pressure is zero (boundary condition). -/
  surface_pressure_zero : Bool := true
  deriving Repr
```
