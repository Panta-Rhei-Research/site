---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L196",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l196/",
  "summary_short": "`example` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::#eval:196",
  "declaration_slug": "example-l196",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 196,
  "source_line_end": 196,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L196-L196",
  "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L196-L196",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L196-L196)
- Source range: L196-L196
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Example: (1, 0) is NOT admissible (1+0 = 1, odd). -/
```

## Source Excerpt

```lean
example : ¬ cr_admissible ⟨1, 0⟩ := by decide
```
