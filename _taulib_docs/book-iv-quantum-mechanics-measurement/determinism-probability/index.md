---
{
  "projection_kind": "taulib_declaration",
  "title": "determinism_probability",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/determinism-probability/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::determinism_probability",
  "declaration_slug": "determinism-probability",
  "kind": "theorem",
  "name": "determinism_probability",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 248,
  "source_line_end": 255,
  "registry_ids": [
    "IV.P28"
  ],
  "related_registry_items": [
    {
      "id": "IV.P28",
      "title": "Determinism-Probability Reconciliation",
      "url": "/registry/object/IV.P28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L248-L255",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Measurement",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L248-L255",
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L248-L255)
- Source range: L248-L255
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P28` — Determinism-Probability Reconciliation

## Immediate Comment / Docstring

```lean
/-- [IV.P28] Both determinism and probability are simultaneously true. -/
```

## Source Excerpt

```lean
theorem determinism_probability (d : DualTrackCompatibility)
    (h1 : d.substrate_deterministic = true)
    (h2 : d.readout_probabilistic = true)
    (h3 : d.compatible = true) :
    d.substrate_deterministic = true ∧
    d.readout_probabilistic = true ∧
    d.compatible = true :=
  ⟨h1, h2, h3⟩
```
