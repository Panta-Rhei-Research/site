---
{
  "projection_kind": "taulib_declaration",
  "title": "xp_self_adjoint",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/xp-self-adjoint/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::xp_self_adjoint",
  "declaration_slug": "xp-self-adjoint",
  "kind": "theorem",
  "name": "xp_self_adjoint",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 226,
  "source_line_end": 229,
  "registry_ids": [
    "IV.P24"
  ],
  "related_registry_items": [
    {
      "id": "IV.P24",
      "title": "X and P Are Self-Adjoint",
      "url": "/registry/object/IV.P24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L226-L229",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L226-L229",
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

- Module: [TauLib.BookIV.QuantumMechanics.Quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L226-L229)
- Source range: L226-L229
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P24` — X and P Are Self-Adjoint

## Immediate Comment / Docstring

```lean
/-- [IV.P24] Both position X_hat and momentum P_hat are self-adjoint
    operators on H_tau. This is a structural consequence of the
    fact that holomorphic flows on tau^3 preserve the inner product. -/
```

## Source Excerpt

```lean
theorem xp_self_adjoint :
    obs_position.is_self_adjoint = true ∧
    obs_momentum.is_self_adjoint = true :=
  ⟨rfl, rfl⟩
```
