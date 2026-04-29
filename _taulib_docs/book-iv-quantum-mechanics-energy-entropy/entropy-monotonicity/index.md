---
{
  "projection_kind": "taulib_declaration",
  "title": "EntropyMonotonicity",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-monotonicity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::EntropyMonotonicity",
  "declaration_slug": "entropy-monotonicity",
  "kind": "structure",
  "name": "EntropyMonotonicity",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 178,
  "source_line_end": 184,
  "registry_ids": [
    "IV.T31"
  ],
  "related_registry_items": [
    {
      "id": "IV.T31",
      "title": "Second Law of Thermodynamics",
      "url": "/registry/object/IV.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L178-L184",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L178-L184",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L178-L184)
- Source range: L178-L184
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T31` — Second Law of Thermodynamics

## Immediate Comment / Docstring

```lean
/-- [IV.T31] Entropy non-decreasing along the α-orbit. -/
```

## Source Excerpt

```lean
structure EntropyMonotonicity where
  s_before : CREntropy
  s_after : CREntropy
  depth_order : s_after.depth > s_before.depth
  nondecreasing : s_after.entropy_numer * s_before.entropy_denom ≥
                  s_before.entropy_numer * s_after.entropy_denom
  deriving Repr
```
