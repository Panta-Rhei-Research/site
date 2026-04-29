---
{
  "projection_kind": "taulib_declaration",
  "title": "AbiogenesisTimescaleBound",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-timescale-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::AbiogenesisTimescaleBound",
  "declaration_slug": "abiogenesis-timescale-bound",
  "kind": "structure",
  "name": "AbiogenesisTimescaleBound",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 361,
  "source_line_end": 370,
  "registry_ids": [
    "VI.D77"
  ],
  "related_registry_items": [
    {
      "id": "VI.D77",
      "title": "Abiogenesis Timescale Bound",
      "url": "/registry/object/VI.D77/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L361-L370",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L361-L370",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L361-L370)
- Source range: L361-L370
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D77` — Abiogenesis Timescale Bound

## Immediate Comment / Docstring

```lean
/-- [VI.D77] Abiogenesis Timescale Bound: upper bound in orbit steps.
    T_abio ≤ n₁/₂ · ⌈ln(N/threshold)⌉ where n₁/₂ ≈ 1.66 (V.D90).
    Geometric decay with half-life n₁/₂ gives time to reach threshold
    from initial N defects.
    Cross-ref: V.D90 (defect half-life n₁/₂ ≈ 1.66). -/
```

## Source Excerpt

```lean
structure AbiogenesisTimescaleBound where
  /-- Half-life in orbit steps (scaled: 166 = 1.66 × 100). -/
  half_life_steps : Nat := 166
  /-- Threshold conditions to cross. -/
  threshold : Nat := 8
  /-- Bound is derived from half-life. -/
  derived_from_half_life : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
