---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_commutation",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/canonical-commutation-l173/",
  "summary_short": "`def` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::canonical_commutation",
  "declaration_slug": "canonical-commutation-l173",
  "kind": "def",
  "name": "canonical_commutation",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 173,
  "source_line_end": 177,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L173-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L173-L177",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L173-L177)
- Source range: L173-L177
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical commutation structure with hbar_tau = 1/4. -/
```

## Source Excerpt

```lean
def canonical_commutation : CanonicalCommutation where
  hbar_numer := 1
  hbar_denom := 4
  denom_pos := by omega
  is_quarter := ⟨rfl, rfl⟩
```
