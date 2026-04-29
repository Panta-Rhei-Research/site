---
{
  "projection_kind": "taulib_declaration",
  "title": "QuantumOperator",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/quantum-operator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::QuantumOperator",
  "declaration_slug": "quantum-operator",
  "kind": "structure",
  "name": "QuantumOperator",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 73,
  "source_line_end": 81,
  "registry_ids": [
    "IV.D66"
  ],
  "related_registry_items": [
    {
      "id": "IV.D66",
      "title": "Quantum Operator",
      "url": "/registry/object/IV.D66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L73-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Quantization",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L73-L81",
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

- Module: [TauLib.BookIV.QuantumMechanics.Quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L73-L81)
- Source range: L73-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D66` — Quantum Operator

## Immediate Comment / Docstring

```lean
/-- [IV.D66] Quantum operator: the quantization map X_hat f(p) =
    d/dt f(phi_t(p)) where phi_t is the holomorphic flow of X.
    Each holomorphic vector field X yields a quantum operator X_hat
    acting on CR(tau^3). -/
```

## Source Excerpt

```lean
structure QuantumOperator where
  /-- The underlying classical holomorphic field. -/
  classical_field : HolomorphicField
  /-- Whether the operator is bounded. -/
  is_bounded : Bool
  /-- Whether the operator is linear. -/
  is_linear : Bool
  linear_true : is_linear = true
  deriving Repr
```
