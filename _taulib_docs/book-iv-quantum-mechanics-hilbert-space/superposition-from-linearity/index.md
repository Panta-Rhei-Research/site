---
{
  "projection_kind": "taulib_declaration",
  "title": "superposition_from_linearity",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/superposition-from-linearity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::superposition_from_linearity",
  "declaration_slug": "superposition-from-linearity",
  "kind": "theorem",
  "name": "superposition_from_linearity",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 324,
  "source_line_end": 325,
  "registry_ids": [
    "IV.P22"
  ],
  "related_registry_items": [
    {
      "id": "IV.P22",
      "title": "Superposition from Linearity",
      "url": "/registry/object/IV.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L324-L325",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L324-L325",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L324-L325)
- Source range: L324-L325
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P22` — Superposition from Linearity

## Immediate Comment / Docstring

```lean
/-- [IV.P22] Superposition is a theorem (linearity of H_tau), not a
    postulate. Since CR(tau^3) is a complex vector space, any linear
    combination of physical states is again a state.
    Formalized: vector space implies superposition. -/
```

## Source Excerpt

```lean
theorem superposition_from_linearity :
    cr_function_space.is_vector_space = true := rfl
```
