---
{
  "projection_kind": "taulib_declaration",
  "title": "charge_quantized",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/charge-quantized/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::charge_quantized",
  "declaration_slug": "charge-quantized",
  "kind": "theorem",
  "name": "charge_quantized",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 163,
  "source_line_end": 165,
  "registry_ids": [
    "IV.P13"
  ],
  "related_registry_items": [
    {
      "id": "IV.P13",
      "title": "Charge Quantization from Winding",
      "url": "/registry/object/IV.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L163-L165",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L163-L165",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L163-L165)
- Source range: L163-L165
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P13` — Charge Quantization from Winding

## Immediate Comment / Docstring

```lean
/-- [IV.P13] Charge quantization from winding: electric charge is an
    integer multiple of the minimal charge e_tau. The integer is the
    winding number of the gamma-tube around the eta-tube.
    Formalized: charge is always an integer multiple of unit. -/
```

## Source Excerpt

```lean
theorem charge_quantized (gc : GeometricCharge) (_ : gc.scale = 1) :
    ∃ k : Int, gc.charge = k * 1 :=
  ⟨gc.charge, by ring⟩
```
