---
{
  "projection_kind": "taulib_declaration",
  "title": "onb_is_admissible_characters",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onb-is-admissible-characters/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::onb_is_admissible_characters",
  "declaration_slug": "onb-is-admissible-characters",
  "kind": "theorem",
  "name": "onb_is_admissible_characters",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 248,
  "source_line_end": 253,
  "registry_ids": [
    "IV.T19"
  ],
  "related_registry_items": [
    {
      "id": "IV.T19",
      "title": "Orthonormal Basis",
      "url": "/registry/object/IV.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L248-L253",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L248-L253",
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

- Module: [TauLib.BookIV.QuantumMechanics.HilbertSpace](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L248-L253)
- Source range: L248-L253
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T19` — Orthonormal Basis

## Immediate Comment / Docstring

```lean
/-- [IV.T19] ONB is indexed by admissible characters. -/
```

## Source Excerpt

```lean
theorem onb_is_admissible_characters :
    onb_admissible.index_type = "Lambda_CR" ∧
    onb_admissible.is_orthogonal = true ∧
    onb_admissible.is_normalized = true ∧
    onb_admissible.is_complete = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
