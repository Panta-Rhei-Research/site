---
{
  "projection_kind": "taulib_declaration",
  "title": "PostResolutionState",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/post-resolution-state/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::PostResolutionState",
  "declaration_slug": "post-resolution-state",
  "kind": "structure",
  "name": "PostResolutionState",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 128,
  "source_line_end": 135,
  "registry_ids": [
    "IV.P26"
  ],
  "related_registry_items": [
    {
      "id": "IV.P26",
      "title": "Measurement Repeatability",
      "url": "/registry/object/IV.P26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L128-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L128-L135",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L128-L135)
- Source range: L128-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P26` — Measurement Repeatability

## Immediate Comment / Docstring

```lean
/-- [IV.P26] Post-resolution state: after measurement, the quantum state
    is projected onto the resolved mode.

    "Collapse" is NOT a physical process but the bookkeeping update of the
    CR-address label after resolution. The state was always a superposition
    of CR-modes; measurement resolves which mode the detector selected. -/
```

## Source Excerpt

```lean
structure PostResolutionState where
  /-- The resolved address. -/
  resolution : AddressResolution
  /-- The post-resolution state is a single eigenmode. -/
  is_eigenmode : Bool := true
  /-- The projection is idempotent (projecting again gives same state). -/
  is_idempotent : Bool := true
  deriving Repr
```
