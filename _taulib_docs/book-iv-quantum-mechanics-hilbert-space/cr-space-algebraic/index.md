---
{
  "projection_kind": "taulib_declaration",
  "title": "cr_space_algebraic",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-hilbert-space/cr-space-algebraic/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::cr_space_algebraic",
  "declaration_slug": "cr-space-algebraic",
  "kind": "theorem",
  "name": "cr_space_algebraic",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 75,
  "source_line_end": 79,
  "registry_ids": [
    "IV.P16"
  ],
  "related_registry_items": [
    {
      "id": "IV.P16",
      "title": "Algebraic Properties of CR(τ³)",
      "url": "/registry/object/IV.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L75-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L75-L79",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L75-L79)
- Source range: L75-L79
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P16` — Algebraic Properties of CR(τ³)

## Immediate Comment / Docstring

```lean
/-- [IV.P16] CR(tau^3) is a complex vector space, commutative algebra,
    and infinite-dimensional. -/
```

## Source Excerpt

```lean
theorem cr_space_algebraic :
    cr_function_space.is_vector_space = true ∧
    cr_function_space.is_algebra = true ∧
    cr_function_space.is_infinite_dim = true :=
  ⟨rfl, rfl, rfl⟩
```
