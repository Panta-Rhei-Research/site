---
{
  "projection_kind": "taulib_declaration",
  "title": "density_halving",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/density-halving/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::density_halving",
  "declaration_slug": "density-halving",
  "kind": "theorem",
  "name": "density_halving",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 220,
  "source_line_end": 223,
  "registry_ids": [
    "IV.P10"
  ],
  "related_registry_items": [
    {
      "id": "IV.P10",
      "title": "Density Halving",
      "url": "/registry/object/IV.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L220-L223",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L220-L223",
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L220-L223)
- Source range: L220-L223
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P10` — Density Halving

## Immediate Comment / Docstring

```lean
/-- [IV.P10] Lambda_CR has density 1/2 in Z^2: for every admissible
    address (m,n), its neighbor (m+1,n) is inadmissible.
    This proves the sublattice has index 2. -/
```

## Source Excerpt

```lean
theorem density_halving (addr : CRAddress) (h : cr_admissible addr) :
    ¬ cr_admissible ⟨addr.m + 1, addr.n⟩ := by
  simp only [cr_admissible] at h ⊢
  omega
```
