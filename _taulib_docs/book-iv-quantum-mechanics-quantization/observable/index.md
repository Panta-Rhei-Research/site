---
{
  "projection_kind": "taulib_declaration",
  "title": "Observable",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/observable/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::Observable",
  "declaration_slug": "observable",
  "kind": "structure",
  "name": "Observable",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 192,
  "source_line_end": 201,
  "registry_ids": [
    "IV.D67"
  ],
  "related_registry_items": [
    {
      "id": "IV.D67",
      "title": "Observable",
      "url": "/registry/object/IV.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L192-L201",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L192-L201",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L192-L201)
- Source range: L192-L201
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D67` — Observable

## Immediate Comment / Docstring

```lean
/-- [IV.D67] Observable: a self-adjoint quantum operator on H_tau.
    Observables are the physically measurable quantities.
    Self-adjointness ensures real eigenvalues (measurement outcomes). -/
```

## Source Excerpt

```lean
structure Observable where
  /-- The underlying quantum operator. -/
  op : QuantumOperator
  /-- Self-adjoint: A_hat^dagger = A_hat. -/
  is_self_adjoint : Bool
  sa_true : is_self_adjoint = true
  /-- Eigenvalues are real (consequence of self-adjointness). -/
  real_eigenvalues : Bool
  real_true : real_eigenvalues = true
  deriving Repr
```
