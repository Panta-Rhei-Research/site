---
{
  "projection_kind": "taulib_declaration",
  "title": "EntropyBoundData",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::EntropyBoundData",
  "declaration_slug": "entropy-bound-data",
  "kind": "structure",
  "name": "EntropyBoundData",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 157,
  "source_line_end": 161,
  "registry_ids": [
    "IV.P30"
  ],
  "related_registry_items": [
    {
      "id": "IV.P30",
      "title": "Entropy-Mode-Count Bound",
      "url": "/registry/object/IV.P30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L157-L161",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L157-L161",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.QuantumMechanics.EnergyEntropy](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/)
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L157-L161)
- Source range: L157-L161
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.P30` — Entropy-Mode-Count Bound

## Immediate Comment / Docstring

```lean
/-- [IV.P30] S[ψ] ≤ ln|A| where A = support of ψ. -/
```

## Source Excerpt

```lean
structure EntropyBoundData where
  entropy : CREntropy
  support_size : Nat
  support_pos : support_size > 0
  deriving Repr
```
