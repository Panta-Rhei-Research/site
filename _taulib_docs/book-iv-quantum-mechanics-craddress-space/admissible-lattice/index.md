---
{
  "projection_kind": "taulib_declaration",
  "title": "AdmissibleLattice",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/admissible-lattice/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::AdmissibleLattice",
  "declaration_slug": "admissible-lattice",
  "kind": "structure",
  "name": "AdmissibleLattice",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 207,
  "source_line_end": 211,
  "registry_ids": [
    "IV.D54"
  ],
  "related_registry_items": [
    {
      "id": "IV.D54",
      "title": "CR-Admissible Sublattice",
      "url": "/registry/object/IV.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L207-L211",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L207-L211",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L207-L211)
- Source range: L207-L211
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D54` — CR-Admissible Sublattice

## Immediate Comment / Docstring

```lean
/-- [IV.D54] The CR-admissible sublattice Lambda_CR = {(m,n) in Z^2 : m+n even}.
    This is a sublattice of Z^2 of index 2. -/
```

## Source Excerpt

```lean
structure AdmissibleLattice where
  /-- Address in the lattice. -/
  addr : CRAddress
  /-- CR-admissibility proof. -/
  admissible : cr_admissible addr
```
