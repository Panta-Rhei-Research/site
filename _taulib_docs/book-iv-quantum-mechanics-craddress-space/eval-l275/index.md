---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L275",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l275/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::#eval:275",
  "declaration_slug": "eval-l275",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 275,
  "source_line_end": 275,
  "registry_ids": [
    "IV.R292",
    "IV.R294",
    "IV.R295"
  ],
  "related_registry_items": [
    {
      "id": "IV.R292",
      "title": "CR-type (1,1) and three-dimensionality",
      "url": "/registry/object/IV.R292/"
    },
    {
      "id": "IV.R294",
      "title": "Spin-frac1",
      "url": "/registry/object/IV.R294/"
    },
    {
      "id": "IV.R295",
      "title": "Bosons and fermions",
      "url": "/registry/object/IV.R295/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L275-L275",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L275-L275",
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L275-L275)
- Source range: L275-L275
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R292` — CR-type (1,1) and three-dimensionality
- `IV.R294` — Spin-frac1
- `IV.R295` — Bosons and fermions

## Immediate Comment / Docstring

```lean
-- [IV.R292] CR-geometry on tau^3 is the unique CR-structure compatible
-- with the fibration pi: tau^3 -> tau^1.
-- (Structural remark — verified by tau3_cr_integrable above)

-- [IV.R294] The address space Z^2 is the Pontryagin dual of T^2.
-- (Structural remark)

-- [IV.R295] CR-parity halves the address space, earning spin-1/2.
-- (Structural remark — verified by density_halving + spin_half_emergence)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval cr_structure_tau3.k             -- 1
```
