---
{
  "projection_kind": "taulib_declaration",
  "title": "saturation_achieves_equality",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-achieves-equality/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::saturation_achieves_equality",
  "declaration_slug": "saturation-achieves-equality",
  "kind": "theorem",
  "name": "saturation_achieves_equality",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 260,
  "source_line_end": 262,
  "registry_ids": [
    "IV.P25"
  ],
  "related_registry_items": [
    {
      "id": "IV.P25",
      "title": "Saturation Equality",
      "url": "/registry/object/IV.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L260-L262",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L260-L262",
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

- Module: [TauLib.BookIV.QuantumMechanics.AddressObstruction](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/)
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L260-L262)
- Source range: L260-L262
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P25` — Saturation Equality

## Immediate Comment / Docstring

```lean
/-- [IV.P25] The saturation state achieves exact equality
    Delta_x * Delta_p = hbar_tau/2 = 1/8. -/
```

## Source Excerpt

```lean
theorem saturation_achieves_equality :
    saturation_state.product_numer * 8 = saturation_state.product_denom :=
  saturation_state.saturates
```
