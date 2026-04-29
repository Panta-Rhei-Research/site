---
{
  "projection_kind": "taulib_declaration",
  "title": "AddressResolution",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/address-resolution/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::AddressResolution",
  "declaration_slug": "address-resolution",
  "kind": "structure",
  "name": "AddressResolution",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 72,
  "source_line_end": 85,
  "registry_ids": [
    "IV.D74"
  ],
  "related_registry_items": [
    {
      "id": "IV.D74",
      "title": "Address Resolution",
      "url": "/registry/object/IV.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L72-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Measurement",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L72-L85",
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L72-L85)
- Source range: L72-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D74` — Address Resolution

## Immediate Comment / Docstring

```lean
/-- [IV.D74] Measurement = address resolution.

    A measurement event is the coupling of a quantum state ψ (holomorphic
    field on T²) to a macroscopic detector, forcing resolution of the
    CR-address to a definite lattice site (m₀, n₀).

    The detector's own CR-address structure acts as a "selector":
    it projects ψ onto the eigenmode at (m₀, n₀) with probability
    given by the squared coefficient |c_{m₀,n₀}|². -/
```

## Source Excerpt

```lean
structure AddressResolution where
  /-- Resolved fiber mode index. -/
  outcome_m : Int
  /-- Resolved base mode index. -/
  outcome_n : Int
  /-- Probability numerator |c_{m₀,n₀}|² (scaled). -/
  probability_numer : Nat
  /-- Probability denominator. -/
  probability_denom : Nat
  /-- Denominator positive. -/
  denom_pos : probability_denom > 0
  /-- Probability ≤ 1 (numer ≤ denom). -/
  prob_le_one : probability_numer ≤ probability_denom
  deriving Repr
```
