---
{
  "projection_kind": "taulib_declaration",
  "title": "hbar_tau_quarter",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-quantization/hbar-tau-quarter/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::hbar_tau_quarter",
  "declaration_slug": "hbar-tau-quarter",
  "kind": "theorem",
  "name": "hbar_tau_quarter",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 180,
  "source_line_end": 183,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L180-L183",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Quantization",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-quantization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L180-L183",
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

- Module: [TauLib.BookIV.QuantumMechanics.Quantization](/corpus/taulib/docs/book-iv-quantum-mechanics-quantization/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L180-L183)
- Source range: L180-L183
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- hbar_tau = 1/4 in tau-units. -/
```

## Source Excerpt

```lean
theorem hbar_tau_quarter :
    canonical_commutation.hbar_numer = 1 ∧
    canonical_commutation.hbar_denom = 4 :=
  canonical_commutation.is_quarter
```
