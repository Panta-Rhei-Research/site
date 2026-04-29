---
{
  "projection_kind": "taulib_declaration",
  "title": "cr_parity_constraint",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-parity-constraint/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::cr_parity_constraint",
  "declaration_slug": "cr-parity-constraint",
  "kind": "theorem",
  "name": "cr_parity_constraint",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 188,
  "source_line_end": 190,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L188-L190",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L188-L190",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L188-L190)
- Source range: L188-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CR parity constraint: m+n even iff admissible. -/
```

## Source Excerpt

```lean
theorem cr_parity_constraint (addr : CRAddress) :
    cr_admissible addr ↔ (addr.m + addr.n) % 2 = 0 :=
  Iff.rfl
```
