---
{
  "projection_kind": "taulib_declaration",
  "title": "SaturationState",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-state/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::SaturationState",
  "declaration_slug": "saturation-state",
  "kind": "structure",
  "name": "SaturationState",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 231,
  "source_line_end": 243,
  "registry_ids": [
    "IV.D73"
  ],
  "related_registry_items": [
    {
      "id": "IV.D73",
      "title": "Canonical Saturation State",
      "url": "/registry/object/IV.D73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L231-L243",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L231-L243",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L231-L243)
- Source range: L231-L243
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D73` — Canonical Saturation State

## Immediate Comment / Docstring

```lean
/-- [IV.D73] Canonical saturation state psi_sat: the unique state in H_tau
    that achieves exact equality Delta_x * Delta_p = hbar_tau/2.
    This is the Gaussian coherent state on T^2 (the tau-analog of the
    ground-state harmonic oscillator wavefunction). -/
```

## Source Excerpt

```lean
structure SaturationState where
  /-- The product Delta_x * Delta_p numerator (= hbar_tau/2 = 1/8). -/
  product_numer : Nat
  /-- Product denominator. -/
  product_denom : Nat
  /-- Denominator positive. -/
  denom_pos : product_denom > 0
  /-- Achieves exact equality: product = hbar_tau/2 = 1/8. -/
  saturates : product_numer * 8 = product_denom
  /-- The saturation state is unique. -/
  is_unique : Bool
  unique_true : is_unique = true
  deriving Repr
```
