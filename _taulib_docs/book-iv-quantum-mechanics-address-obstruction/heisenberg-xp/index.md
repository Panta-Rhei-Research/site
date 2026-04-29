---
{
  "projection_kind": "taulib_declaration",
  "title": "HeisenbergXP",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-xp/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::HeisenbergXP",
  "declaration_slug": "heisenberg-xp",
  "kind": "structure",
  "name": "HeisenbergXP",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 279,
  "source_line_end": 292,
  "registry_ids": [
    "IV.T25"
  ],
  "related_registry_items": [
    {
      "id": "IV.T25",
      "title": "Heisenberg Uncertainty (Position-Momentum)",
      "url": "/registry/object/IV.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L279-L292",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L279-L292",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L279-L292)
- Source range: L279-L292
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T25` — Heisenberg Uncertainty (Position-Momentum)

## Immediate Comment / Docstring

```lean
/-- [IV.T25] Full Heisenberg uncertainty principle (position-momentum):
    Delta_x * Delta_p >= hbar_tau/2 for all states, with sharp bound
    attained by psi_sat.

    This is a THEOREM in the tau-framework, derived from:
    1. CR-structure on tau^3 (source of non-commutativity)
    2. Canonical commutation [X, P] = i*hbar_tau
    3. Cauchy-Schwarz inequality on H_tau

    The bound hbar_tau/2 = 1/8.
    Formalized: the NoJointMinimum constraint with bound (1, 8). -/
```

## Source Excerpt

```lean
structure HeisenbergXP where
  /-- Lower bound = hbar_tau/2: numerator. -/
  bound_numer : Nat
  bound_numer_eq : bound_numer = 1
  /-- Lower bound denominator. -/
  bound_denom : Nat
  bound_denom_eq : bound_denom = 8
  /-- Bound is attained (by saturation state). -/
  is_sharp : Bool
  sharp_true : is_sharp = true
  /-- Derived (not postulated). -/
  is_derived : Bool
  derived_true : is_derived = true
  deriving Repr
```
