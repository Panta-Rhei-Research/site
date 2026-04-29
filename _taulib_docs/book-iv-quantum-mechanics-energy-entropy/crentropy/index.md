---
{
  "projection_kind": "taulib_declaration",
  "title": "CREntropy",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/crentropy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::CREntropy",
  "declaration_slug": "crentropy",
  "kind": "structure",
  "name": "CREntropy",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 142,
  "source_line_end": 147,
  "registry_ids": [
    "IV.D80"
  ],
  "related_registry_items": [
    {
      "id": "IV.D80",
      "title": "Holomorphic Entropy",
      "url": "/registry/object/IV.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L142-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L142-L147",
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

- Module: [TauLib.BookIV.QuantumMechanics.EnergyEntropy](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/)
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L142-L147)
- Source range: L142-L147
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D80` — Holomorphic Entropy

## Immediate Comment / Docstring

```lean
/-- [IV.D80] CR-Entropy S(n) = log(# admissible CR-addresses at depth n).
    Combinatorial entropy on the finite lattice; grows monotonically. -/
```

## Source Excerpt

```lean
structure CREntropy where
  entropy_numer : Nat
  entropy_denom : Nat
  denom_pos : entropy_denom > 0
  depth : Nat
  deriving Repr
```
