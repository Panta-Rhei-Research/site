---
{
  "projection_kind": "taulib_declaration",
  "title": "density_halving_converse",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/density-halving-converse/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::density_halving_converse",
  "declaration_slug": "density-halving-converse",
  "kind": "theorem",
  "name": "density_halving_converse",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 226,
  "source_line_end": 229,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L226-L229",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L226-L229",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L226-L229)
- Source range: L226-L229
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Conversely, if (m,n) is inadmissible, (m+1,n) is admissible. -/
```

## Source Excerpt

```lean
theorem density_halving_converse (addr : CRAddress) (h : ¬ cr_admissible addr) :
    cr_admissible ⟨addr.m + 1, addr.n⟩ := by
  simp only [cr_admissible] at h ⊢
  omega
```
