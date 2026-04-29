---
{
  "projection_kind": "taulib_declaration",
  "title": "HermeticTruthComplete",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/hermetic-truth-complete/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::HermeticTruthComplete",
  "declaration_slug": "hermetic-truth-complete",
  "kind": "structure",
  "name": "HermeticTruthComplete",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 201,
  "source_line_end": 214,
  "registry_ids": [
    "V.T162"
  ],
  "related_registry_items": [
    {
      "id": "V.T162",
      "title": "The Hermetic Truth",
      "url": "/registry/object/V.T162/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L201-L214",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L201-L214",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L201-L214)
- Source range: L201-L214
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T162` — The Hermetic Truth

## Immediate Comment / Docstring

```lean
/-- [V.T162] The Hermetic Truth (Complete): τ³ is a single object
    producing all microphysics, all macrophysics, and conditions for
    observers. Fiber and base are two projections of one structure.

    This is the capstone: it combines the Hermetic Identity (V.T159),
    self-description (V.T160), and Hermetic Closure (V.T161).

    Note: distinct from V.T143 `HermeticTruth` in BridgeToLife.lean,
    which states the tensor product is exact. V.T162 is the full synthesis. -/
```

## Source Excerpt

```lean
structure HermeticTruthComplete where
  /-- All microphysics from fiber T². -/
  microphysics_complete : Bool := true
  /-- All macrophysics from base τ¹. -/
  macrophysics_complete : Bool := true
  /-- Observer conditions from sector structure. -/
  observer_conditions : Bool := true
  /-- Single object (τ³). -/
  single_object : Bool := true
  /-- Fiber + base = two projections. -/
  two_projections : Bool := true
  /-- Number of projections (fiber + base). -/
  projection_count : Nat := 2
  deriving Repr
```
