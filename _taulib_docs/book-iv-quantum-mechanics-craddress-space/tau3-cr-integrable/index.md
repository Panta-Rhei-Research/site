---
{
  "projection_kind": "taulib_declaration",
  "title": "tau3_cr_integrable",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/tau3-cr-integrable/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::tau3_cr_integrable",
  "declaration_slug": "tau3-cr-integrable",
  "kind": "theorem",
  "name": "tau3_cr_integrable",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 103,
  "source_line_end": 103,
  "registry_ids": [
    "IV.P09"
  ],
  "related_registry_items": [
    {
      "id": "IV.P09",
      "title": "Integrability of τ³ CR-Structure",
      "url": "/registry/object/IV.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L103-L103",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L103-L103",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L103-L103)
- Source range: L103-L103
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P09` — Integrability of τ³ CR-Structure

## Immediate Comment / Docstring

```lean
/-- [IV.P09] The CR-structure on tau^3 is integrable:
    Nijenhuis tensor vanishes because T^2 is flat and the
    fibration projection is holomorphic. -/
```

## Source Excerpt

```lean
theorem tau3_cr_integrable : cr_structure_tau3.nijenhuis_vanishes = true := rfl
```
