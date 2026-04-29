---
{
  "projection_kind": "taulib_declaration",
  "title": "HolomorphicField",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/holomorphic-field/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::HolomorphicField",
  "declaration_slug": "holomorphic-field",
  "kind": "structure",
  "name": "HolomorphicField",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 41,
  "source_line_end": 49,
  "registry_ids": [
    "IV.D65"
  ],
  "related_registry_items": [
    {
      "id": "IV.D65",
      "title": "Holomorphic Vector Field",
      "url": "/registry/object/IV.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L41-L49",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L41-L49",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L41-L49)
- Source range: L41-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D65` — Holomorphic Vector Field

## Immediate Comment / Docstring

```lean
/-- [IV.D65] Holomorphic vector field on tau^3: a smooth vector field X
    satisfying [X, dbar_b] = 0. These are the symmetries of the
    CR-structure, and they generate the classical dynamics. -/
```

## Source Excerpt

```lean
structure HolomorphicField where
  /-- Name/label of the field. -/
  label : String
  /-- Commutes with dbar_b. -/
  commutes_with_dbar : Bool
  comm_true : commutes_with_dbar = true
  /-- Carrier type (where it acts). -/
  carrier : String
  deriving Repr
```
