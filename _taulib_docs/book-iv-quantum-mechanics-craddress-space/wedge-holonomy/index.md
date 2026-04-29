---
{
  "projection_kind": "taulib_declaration",
  "title": "WedgeHolonomy",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/wedge-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::WedgeHolonomy",
  "declaration_slug": "wedge-holonomy",
  "kind": "structure",
  "name": "WedgeHolonomy",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 159,
  "source_line_end": 165,
  "registry_ids": [
    "IV.L01"
  ],
  "related_registry_items": [
    {
      "id": "IV.L01",
      "title": "Wedge Holonomy",
      "url": "/registry/object/IV.L01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L159-L165",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L159-L165",
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L159-L165)
- Source range: L159-L165
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L01` — Wedge Holonomy

## Immediate Comment / Docstring

```lean
/-- [IV.L01] Holonomy of chi_{m,n} around the wedge point of L:
    exp(2*pi*i*(m+n)*iota_tau). The holonomy phase depends on
    the sum m+n scaled by iota_tau. We record the structural fact:
    the holonomy winding factor is (m+n)*iota/iotaD. -/
```

## Source Excerpt

```lean
structure WedgeHolonomy where
  /-- The character mode. -/
  mode : CharacterMode
  /-- Holonomy winding = (m + n). -/
  winding : Int
  winding_eq : winding = mode.m + mode.n
  deriving Repr
```
