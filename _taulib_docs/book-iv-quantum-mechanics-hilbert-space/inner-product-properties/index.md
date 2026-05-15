---
{
  "projection_kind": "taulib_declaration",
  "title": "inner_product_properties",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-properties/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::inner_product_properties",
  "declaration_slug": "inner-product-properties",
  "kind": "theorem",
  "name": "inner_product_properties",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 116,
  "source_line_end": 120,
  "registry_ids": [
    "IV.P17"
  ],
  "related_registry_items": [
    {
      "id": "IV.P17",
      "title": "Inner Product Properties",
      "url": "/registry/object/IV.P17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L116-L120",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-hilbert-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L116-L120",
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

- Module: [TauLib.BookIV.QuantumMechanics.HilbertSpace](/corpus/taulib/docs/book-iv-quantum-mechanics-hilbert-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L116-L120)
- Source range: L116-L120
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P17` — Inner Product Properties

## Immediate Comment / Docstring

```lean
/-- [IV.P17] The inner product is sesquilinear, Hermitian,
    and positive definite. -/
```

## Source Excerpt

```lean
theorem inner_product_properties :
    tau_inner_product.is_sesquilinear = true ∧
    tau_inner_product.is_hermitian = true ∧
    tau_inner_product.is_positive_definite = true :=
  ⟨rfl, rfl, rfl⟩
```
