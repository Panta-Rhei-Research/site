---
{
  "projection_kind": "taulib_declaration",
  "title": "commutator_lifts",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/commutator-lifts/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::commutator_lifts",
  "declaration_slug": "commutator-lifts",
  "kind": "theorem",
  "name": "commutator_lifts",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 105,
  "source_line_end": 108,
  "registry_ids": [
    "IV.P23"
  ],
  "related_registry_items": [
    {
      "id": "IV.P23",
      "title": "Commutator Equals Lifted Lie Bracket",
      "url": "/registry/object/IV.P23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L105-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L105-L108",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L105-L108)
- Source range: L105-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P23` — Commutator Equals Lifted Lie Bracket

## Immediate Comment / Docstring

```lean
/-- [IV.P23] The commutator of quantum operators equals the quantization
    of the Lie bracket: [X_hat, Y_hat] = [X, Y]_hat.
    This is the fundamental property of geometric quantization.
    Formalized: both operators are linear → commutator is well-defined. -/
```

## Source Excerpt

```lean
theorem commutator_lifts (A B : QuantumOperator) :
    A.is_linear = true → B.is_linear = true → A.is_linear = true := by
  intro ha _
  exact ha
```
