---
{
  "projection_kind": "taulib_declaration",
  "title": "SpinHalfEmergence",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/spin-half-emergence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::SpinHalfEmergence",
  "declaration_slug": "spin-half-emergence",
  "kind": "structure",
  "name": "SpinHalfEmergence",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 242,
  "source_line_end": 251,
  "registry_ids": [
    "IV.T17"
  ],
  "related_registry_items": [
    {
      "id": "IV.T17",
      "title": "Emergence of Spin-1/2",
      "url": "/registry/object/IV.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L242-L251",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L242-L251",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L242-L251)
- Source range: L242-L251
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T17` — Emergence of Spin-1/2

## Immediate Comment / Docstring

```lean
/-- [IV.T17] Emergence of spin-1/2: the bi-rotation on T^2 constrained
    by CR-parity (m+n even) produces a double cover, which is the
    SU(2) structure responsible for spin-1/2 in quantum mechanics.

    Structural: the sublattice index (= 2) equals the double cover
    degree, which is the denominator of the minimal spin quantum number.
    spin_half_denom = sublattice_index = 2. -/
```

## Source Excerpt

```lean
structure SpinHalfEmergence where
  /-- Sublattice index in Z^2. -/
  sublattice_index : Nat
  index_eq : sublattice_index = 2
  /-- Double cover degree. -/
  double_cover_degree : Nat
  cover_eq : double_cover_degree = 2
  /-- They agree. -/
  spin_from_index : sublattice_index = double_cover_degree
  deriving Repr
```
