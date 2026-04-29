---
{
  "projection_kind": "taulib_declaration",
  "title": "obs_position",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/obs-position/",
  "summary_short": "`def` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::obs_position",
  "declaration_slug": "obs-position",
  "kind": "def",
  "name": "obs_position",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 204,
  "source_line_end": 209,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L204-L209",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Quantization",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L204-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.QuantumMechanics.Quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L204-L209)
- Source range: L204-L209
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Position as observable. -/
```

## Source Excerpt

```lean
def obs_position : Observable where
  op := op_position
  is_self_adjoint := true
  sa_true := rfl
  real_eigenvalues := true
  real_true := rfl
```
