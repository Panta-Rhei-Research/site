---
{
  "projection_kind": "taulib_declaration",
  "title": "NoJointMinimum",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/no-joint-minimum/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::NoJointMinimum",
  "declaration_slug": "no-joint-minimum",
  "kind": "structure",
  "name": "NoJointMinimum",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 156,
  "source_line_end": 168,
  "registry_ids": [
    "IV.T23"
  ],
  "related_registry_items": [
    {
      "id": "IV.T23",
      "title": "No-Joint-Minimum Theorem",
      "url": "/registry/object/IV.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L156-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L156-L168",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L156-L168)
- Source range: L156-L168
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T23` — No-Joint-Minimum Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T23] No-Joint-Minimum (NoJointMin): Delta_x * Delta_p >= hbar_tau/2
    for ALL states in H_tau. No state can have both Delta_x and Delta_p
    arbitrarily small simultaneously. This is an ADDRESS OBSTRUCTION,
    not a measurement disturbance.

    hbar_tau/2 = 1/8 in tau-units (since hbar_tau = 1/4).
    Cross-multiplied: product_numer * 8 >= product_denom. -/
```

## Source Excerpt

```lean
structure NoJointMinimum where
  /-- The joint address normal form. -/
  joint : JointAddressNF
  /-- Lower bound numerator: hbar_tau/2 = 1/8. -/
  bound_numer : Nat
  bound_eq : bound_numer = 1
  /-- Lower bound denominator. -/
  bound_denom : Nat
  bdenom_eq : bound_denom = 8
  /-- The inequality: product >= bound (cross-multiplied). -/
  inequality : joint.product_numer * bound_denom ≥
               bound_numer * joint.product_denom
  deriving Repr
```
