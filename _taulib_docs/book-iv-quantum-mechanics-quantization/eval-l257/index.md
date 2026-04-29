---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L257",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l257/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::#eval:257",
  "declaration_slug": "eval-l257",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 257,
  "source_line_end": 257,
  "registry_ids": [
    "IV.R305",
    "IV.R310",
    "IV.R312",
    "IV.R314"
  ],
  "related_registry_items": [
    {
      "id": "IV.R305",
      "title": "Comparison with geometric quantization",
      "url": "/registry/object/IV.R305/"
    },
    {
      "id": "IV.R310",
      "title": "Connection to Book~II spectral gap",
      "url": "/registry/object/IV.R310/"
    },
    {
      "id": "IV.R312",
      "title": "Born rule derived, not postulated",
      "url": "/registry/object/IV.R312/"
    },
    {
      "id": "IV.R314",
      "title": "Why standard QM works",
      "url": "/registry/object/IV.R314/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L257-L257",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L257-L257",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L257-L257)
- Source range: L257-L257
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R305` — Comparison with geometric quantization
- `IV.R310` — Connection to Book~II spectral gap
- `IV.R312` — Born rule derived, not postulated
- `IV.R314` — Why standard QM works

## Immediate Comment / Docstring

```lean
-- [IV.R305] Holomorphic flow: the Schrodinger equation is the
-- holomorphic flow of the energy operator on tau^3.
-- (Structural remark)

-- [IV.R310] Discrete spectra follow inevitably from compact T^2.
-- No additional "quantization condition" is needed.
-- (Structural remark — verified by topological_quantization)

-- [IV.R312] The commutation relation [X, P] = i*hbar is DERIVED,
-- not postulated. It follows from the CR-structure on tau^3.
-- (Structural remark — verified by canonical_commutation)

-- [IV.R314] Observables in tau are more restrictive than in orthodox QM:
-- only holomorphic-flow-generated operators qualify.
-- (Structural remark)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval field_position.label               -- X
```
