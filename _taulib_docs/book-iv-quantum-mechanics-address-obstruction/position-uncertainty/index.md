---
{
  "projection_kind": "taulib_declaration",
  "title": "PositionUncertainty",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/position-uncertainty/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::PositionUncertainty",
  "declaration_slug": "position-uncertainty",
  "kind": "structure",
  "name": "PositionUncertainty",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 44,
  "source_line_end": 53,
  "registry_ids": [
    "IV.D68"
  ],
  "related_registry_items": [
    {
      "id": "IV.D68",
      "title": "Address Uncertainty",
      "url": "/registry/object/IV.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L44-L53",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L44-L53",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L44-L53)
- Source range: L44-L53
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D68` — Address Uncertainty

## Immediate Comment / Docstring

```lean
/-- [IV.D68] Position uncertainty Delta_x: the spread of address precision
    in the position (real-space) direction on T^2.
    Represented as a scaled rational (numer, denom). -/
```

## Source Excerpt

```lean
structure PositionUncertainty where
  /-- Uncertainty numerator (scaled). -/
  numer : Nat
  /-- Uncertainty denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Uncertainty is positive: numer > 0. -/
  numer_pos : numer > 0
  deriving Repr
```
