---
{
  "projection_kind": "taulib_declaration",
  "title": "PhysicalState",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/physical-state/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::PhysicalState",
  "declaration_slug": "physical-state",
  "kind": "structure",
  "name": "PhysicalState",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 271,
  "source_line_end": 278,
  "registry_ids": [
    "IV.D63"
  ],
  "related_registry_items": [
    {
      "id": "IV.D63",
      "title": "Physical State Space",
      "url": "/registry/object/IV.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L271-L278",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L271-L278",
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

- Module: [TauLib.BookIV.QuantumMechanics.HilbertSpace](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L271-L278)
- Source range: L271-L278
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D63` — Physical State Space

## Immediate Comment / Docstring

```lean
/-- [IV.D63] Physical states = normalized + stable elements of H_tau.
    Normalized: ||psi||^2 = 1. Stable: preserved under tau-admissible evolution. -/
```

## Source Excerpt

```lean
structure PhysicalState where
  /-- The state is normalized (||psi||^2 = 1). -/
  is_normalized : Bool
  norm_true : is_normalized = true
  /-- The state is stable (preserved under admissible evolution). -/
  is_stable : Bool
  stable_true : is_stable = true
  deriving Repr
```
