---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_completeness",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/spectral-completeness/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::spectral_completeness",
  "declaration_slug": "spectral-completeness",
  "kind": "theorem",
  "name": "spectral_completeness",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 262,
  "source_line_end": 263,
  "registry_ids": [
    "IV.P20"
  ],
  "related_registry_items": [
    {
      "id": "IV.P20",
      "title": "Spectral Completeness",
      "url": "/registry/object/IV.P20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L262-L263",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L262-L263",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L262-L263)
- Source range: L262-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P20` — Spectral Completeness

## Immediate Comment / Docstring

```lean
/-- [IV.P20] Unique decomposition: every f in H_tau admits a unique
    expansion f = sum c_{m,n} chi_{m,n} over Lambda_CR.
    The convergence is in L^2 norm. -/
```

## Source Excerpt

```lean
theorem spectral_completeness :
    onb_admissible.is_complete = true := rfl
```
