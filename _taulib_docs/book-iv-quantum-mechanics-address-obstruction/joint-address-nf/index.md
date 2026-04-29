---
{
  "projection_kind": "taulib_declaration",
  "title": "JointAddressNF",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/joint-address-nf/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::JointAddressNF",
  "declaration_slug": "joint-address-nf",
  "kind": "structure",
  "name": "JointAddressNF",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 76,
  "source_line_end": 87,
  "registry_ids": [
    "IV.D69"
  ],
  "related_registry_items": [
    {
      "id": "IV.D69",
      "title": "τ-Normal Form for Joint Address",
      "url": "/registry/object/IV.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L76-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L76-L87",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L76-L87)
- Source range: L76-L87
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D69` — τ-Normal Form for Joint Address

## Immediate Comment / Docstring

```lean
/-- [IV.D69] The tau-normal form (tau-NF) for joint position-momentum
    address: the canonical representation of the best simultaneous
    localization achievable in both position and momentum. The product
    Delta_x * Delta_p cannot be made arbitrarily small. -/
```

## Source Excerpt

```lean
structure JointAddressNF where
  /-- Position uncertainty. -/
  delta_x : PositionUncertainty
  /-- Momentum uncertainty. -/
  delta_p : MomentumUncertainty
  /-- Product numerator: Delta_x * Delta_p. -/
  product_numer : Nat
  product_eq : product_numer = delta_x.numer * delta_p.numer
  /-- Product denominator. -/
  product_denom : Nat
  pdenom_eq : product_denom = delta_x.denom * delta_p.denom
  deriving Repr
```
