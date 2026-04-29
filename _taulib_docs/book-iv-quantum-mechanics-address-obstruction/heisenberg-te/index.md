---
{
  "projection_kind": "taulib_declaration",
  "title": "HeisenbergTE",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-te/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::HeisenbergTE",
  "declaration_slug": "heisenberg-te",
  "kind": "structure",
  "name": "HeisenbergTE",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 315,
  "source_line_end": 325,
  "registry_ids": [
    "IV.T26"
  ],
  "related_registry_items": [
    {
      "id": "IV.T26",
      "title": "Heisenberg Uncertainty (Time-Energy)",
      "url": "/registry/object/IV.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L315-L325",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L315-L325",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L315-L325)
- Source range: L315-L325
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T26` — Heisenberg Uncertainty (Time-Energy)

## Immediate Comment / Docstring

```lean
/-- [IV.T26] Heisenberg uncertainty (time-energy):
    Delta_t * Delta_E >= hbar_tau/2.

    The time-energy version follows from the same CR-structure
    but applied to the base tau^1 instead of the fiber T^2.
    The bound is the same hbar_tau/2 = 1/8. -/
```

## Source Excerpt

```lean
structure HeisenbergTE where
  /-- Lower bound = hbar_tau/2: numerator. -/
  bound_numer : Nat
  bound_numer_eq : bound_numer = 1
  /-- Lower bound denominator. -/
  bound_denom : Nat
  bound_denom_eq : bound_denom = 8
  /-- Same bound as position-momentum. -/
  same_bound : bound_numer = heisenberg_xp.bound_numer ∧
               bound_denom = heisenberg_xp.bound_denom
  deriving Repr
```
