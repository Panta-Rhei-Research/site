---
{
  "projection_kind": "taulib_declaration",
  "title": "GeometricCharge",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/geometric-charge/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::GeometricCharge",
  "declaration_slug": "geometric-charge",
  "kind": "structure",
  "name": "GeometricCharge",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 140,
  "source_line_end": 147,
  "registry_ids": [
    "IV.D58"
  ],
  "related_registry_items": [
    {
      "id": "IV.D58",
      "title": "Geometric Charge",
      "url": "/registry/object/IV.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L140-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L140-L147",
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

- Module: [TauLib.BookIV.QuantumMechanics.QuantumCharacters](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/)
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L140-L147)
- Source range: L140-L147
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D58` — Geometric Charge

## Immediate Comment / Docstring

```lean
/-- [IV.D58] Geometric charge from relative orientation of the
    gamma-tube and eta-tube on T^2. Charge is an integer multiple
    of a minimal quantum e_tau. Represented as (charge, scale). -/
```

## Source Excerpt

```lean
structure GeometricCharge where
  /-- Charge numerator (integer winding number). -/
  charge : Int
  /-- Scale denominator (for fractional display). -/
  scale : Nat
  /-- Scale is positive. -/
  scale_pos : scale > 0
  deriving Repr
```
