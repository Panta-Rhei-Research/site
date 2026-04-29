---
{
  "projection_kind": "taulib_declaration",
  "title": "EquilibriumCarrier",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/equilibrium-carrier/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::EquilibriumCarrier",
  "declaration_slug": "equilibrium-carrier",
  "kind": "structure",
  "name": "EquilibriumCarrier",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 92,
  "source_line_end": 99,
  "registry_ids": [
    "V.D67"
  ],
  "related_registry_items": [
    {
      "id": "V.D67",
      "title": "Equilibrium carrier",
      "url": "/registry/object/V.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L92-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L92-L99",
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
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L92-L99)
- Source range: L92-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D67` — Equilibrium carrier

## Immediate Comment / Docstring

```lean
/-- [V.D67] Equilibrium carrier: a spherical carrier satisfying
    hydrostatic balance (inward gravity = outward pressure). -/
```

## Source Excerpt

```lean
structure EquilibriumCarrier where
  /-- The underlying spherical carrier. -/
  carrier : SphericalCarrier
  /-- Whether hydrostatic balance holds. -/
  is_in_equilibrium : Bool
  /-- Whether the equilibrium is stable (not just stationary). -/
  is_stable : Bool
  deriving Repr
```
