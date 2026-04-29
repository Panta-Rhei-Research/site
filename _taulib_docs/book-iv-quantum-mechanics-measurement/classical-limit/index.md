---
{
  "projection_kind": "taulib_declaration",
  "title": "ClassicalLimit",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::ClassicalLimit",
  "declaration_slug": "classical-limit",
  "kind": "structure",
  "name": "ClassicalLimit",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 210,
  "source_line_end": 217,
  "registry_ids": [
    "IV.P27"
  ],
  "related_registry_items": [
    {
      "id": "IV.P27",
      "title": "Classical Limit",
      "url": "/registry/object/IV.P27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L210-L217",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L210-L217",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L210-L217)
- Source range: L210-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P27` — Classical Limit

## Immediate Comment / Docstring

```lean
/-- [IV.P27] Classical limit: |m|, |n| → ∞ yields classical mechanics.

    When the mode indices grow large, the CR-address lattice becomes
    dense relative to the action scale. The uncertainty product
    ℏ_τ / (action scale) → 0, and quantum interference effects
    average out. Classical mechanics emerges as the continuum
    limit of the discrete CR-lattice. -/
```

## Source Excerpt

```lean
structure ClassicalLimit where
  /-- Threshold mode number above which classical approximation holds. -/
  threshold : Nat
  /-- Threshold is large (at least 100 for meaningful classical limit). -/
  threshold_large : threshold ≥ 100
  /-- Classical mechanics is the large-|m|,|n| limit. -/
  is_continuum_limit : Bool := true
  deriving Repr
```
