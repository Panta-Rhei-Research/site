---
{
  "projection_kind": "taulib_declaration",
  "title": "CRManifold",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/crmanifold/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::CRManifold",
  "declaration_slug": "crmanifold",
  "kind": "structure",
  "name": "CRManifold",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 45,
  "source_line_end": 54,
  "registry_ids": [
    "IV.D49"
  ],
  "related_registry_items": [
    {
      "id": "IV.D49",
      "title": "CR-Manifold",
      "url": "/registry/object/IV.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L45-L54",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L45-L54",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L45-L54)
- Source range: L45-L54
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D49` — CR-Manifold

## Immediate Comment / Docstring

```lean
/-- [IV.D49] CR-manifold of type (k, l): a real smooth manifold of
    dimension 2k + l carrying a CR-structure. The tau^3 arena is
    CR of type (1, 1), giving real dimension 2*1 + 1 = 3. -/
```

## Source Excerpt

```lean
structure CRManifold where
  /-- Complex tangent dimension k (number of holomorphic directions). -/
  k : Nat
  /-- Totally real dimension l. -/
  l : Nat
  /-- Total real dimension = 2k + l. -/
  real_dim : Nat
  /-- Dimension consistency. -/
  dim_eq : real_dim = 2 * k + l
  deriving Repr
```
