---
{
  "projection_kind": "taulib_declaration",
  "title": "CoulombLimit",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/coulomb-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::CoulombLimit",
  "declaration_slug": "coulomb-limit",
  "kind": "structure",
  "name": "CoulombLimit",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 308,
  "source_line_end": 315,
  "registry_ids": [
    "IV.T46"
  ],
  "related_registry_items": [
    {
      "id": "IV.T46",
      "title": "Coulomb's Law from tau-Maxwell",
      "url": "/registry/object/IV.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L308-L315",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L308-L315",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L308-L315)
- Source range: L308-L315
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T46` — Coulomb's Law from tau-Maxwell

## Immediate Comment / Docstring

```lean
/-- [IV.T46] Static limit of Maxwell gives Coulomb's law:
    F = k_e · q₁q₂ / r² where k_e = 1/(4πε₀).
    The 1/r² law follows from Gauss's law in 3 spatial dimensions. -/
```

## Source Excerpt

```lean
structure CoulombLimit where
  /-- Spatial dimension for 1/r² law. -/
  spatial_dim : Nat
  dim_eq : spatial_dim = 3
  /-- Exponent in force law = spatial_dim - 1. -/
  force_exponent : Nat
  exp_eq : force_exponent = spatial_dim - 1
  deriving Repr
```
