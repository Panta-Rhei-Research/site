---
{
  "projection_kind": "taulib_declaration",
  "title": "DualTrackCompatibility",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/dual-track-compatibility/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::DualTrackCompatibility",
  "declaration_slug": "dual-track-compatibility",
  "kind": "structure",
  "name": "DualTrackCompatibility",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 238,
  "source_line_end": 245,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L238-L245",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L238-L245",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L238-L245)
- Source range: L238-L245
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P28` — Determinism-Probability Reconciliation

## Immediate Comment / Docstring

```lean
/-- [IV.P28] Substrate determinism + outcome probability coexist.

    - **Substrate level**: The τ-orbit evolution α ↦ ρ(α) is fully
      deterministic (unique successor at each refinement step).
    - **Readout level**: Measurement outcomes are probabilistic
      (Born rule gives |c_{m₀,n₀}|²).

    These are NOT contradictory because they operate at different
    levels of the dual-track architecture:
    - Determinism: ontic (the orbit IS definite at each step)
    - Probability: epistemic (the readout projects multi-mode state) -/
```

## Source Excerpt

```lean
structure DualTrackCompatibility where
  /-- Substrate is deterministic. -/
  substrate_deterministic : Bool := true
  /-- Readout is probabilistic. -/
  readout_probabilistic : Bool := true
  /-- Both are simultaneously true. -/
  compatible : Bool := true
  deriving Repr
```
