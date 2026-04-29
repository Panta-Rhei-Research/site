---
{
  "projection_kind": "taulib_declaration",
  "title": "WithinBetweenLevels",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-between-levels/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.EnergyEntropy::WithinBetweenLevels",
  "declaration_slug": "within-between-levels",
  "kind": "structure",
  "name": "WithinBetweenLevels",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "source_line_start": 210,
  "source_line_end": 213,
  "registry_ids": [
    "IV.P31"
  ],
  "related_registry_items": [
    {
      "id": "IV.P31",
      "title": "Reversibility-Irreversibility Resolution",
      "url": "/registry/object/IV.P31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L210-L213",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L210-L213",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L210-L213)
- Source range: L210-L213
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P31` — Reversibility-Irreversibility Resolution

## Immediate Comment / Docstring

```lean
/-- [IV.P31] Schrodinger reversible within level; thermodynamics
    irreversible between levels. Resolves the paradox of irreversibility. -/
```

## Source Excerpt

```lean
structure WithinBetweenLevels where
  within_reversible : Bool := true
  between_irreversible : Bool := true
  deriving Repr
```
