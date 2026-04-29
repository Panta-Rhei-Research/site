---
{
  "projection_kind": "taulib_declaration",
  "title": "von_neumann_axioms",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/von-neumann-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::von_neumann_axioms",
  "declaration_slug": "von-neumann-axioms",
  "kind": "theorem",
  "name": "von_neumann_axioms",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 181,
  "source_line_end": 185,
  "registry_ids": [
    "IV.T18"
  ],
  "related_registry_items": [
    {
      "id": "IV.T18",
      "title": "Hilbert Space Properties",
      "url": "/registry/object/IV.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L181-L185",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L181-L185",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L181-L185)
- Source range: L181-L185
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T18` — Hilbert Space Properties

## Immediate Comment / Docstring

```lean
/-- [IV.T18] The three von Neumann axioms for quantum mechanics:
    H_tau is (1) complete, (2) separable, and (3) infinite-dimensional.
    These are exactly the axioms required for quantum mechanical state spaces. -/
```

## Source Excerpt

```lean
theorem von_neumann_axioms :
    hilbert_tau.is_complete = true ∧
    hilbert_tau.is_separable = true ∧
    hilbert_tau.is_infinite_dim = true :=
  ⟨rfl, rfl, rfl⟩
```
