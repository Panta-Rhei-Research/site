---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossingMediator",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/crossing-mediator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::CrossingMediator",
  "declaration_slug": "crossing-mediator",
  "kind": "structure",
  "name": "CrossingMediator",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 183,
  "source_line_end": 196,
  "registry_ids": [
    "IV.D72"
  ],
  "related_registry_items": [
    {
      "id": "IV.D72",
      "title": "σ-Equivariant Crossing-Point Mediator",
      "url": "/registry/object/IV.D72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L183-L196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L183-L196",
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

- Module: [TauLib.BookIV.QuantumMechanics.AddressObstruction](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/)
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L183-L196)
- Source range: L183-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D72` — σ-Equivariant Crossing-Point Mediator

## Immediate Comment / Docstring

```lean
/-- [IV.D72] sigma-equivariant crossing-point mediator: the unique
    element of H_fix[omega] that mediates between position and
    momentum resolutions. This is hbar_tau = 1/4. -/
```

## Source Excerpt

```lean
structure CrossingMediator where
  /-- Mediator numerator. -/
  numer : Nat
  /-- Mediator denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- sigma-equivariant (at crossing point). -/
  is_sigma_equivariant : Bool
  sigma_true : is_sigma_equivariant = true
  /-- Unique (only crossing-point mediator). -/
  is_unique : Bool
  unique_true : is_unique = true
  deriving Repr
```
