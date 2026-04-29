---
{
  "projection_kind": "taulib_declaration",
  "title": "TemporalStabilityPredicate",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/temporal-stability-predicate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::TemporalStabilityPredicate",
  "declaration_slug": "temporal-stability-predicate",
  "kind": "structure",
  "name": "TemporalStabilityPredicate",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 79,
  "source_line_end": 90,
  "registry_ids": [
    "VI.D25"
  ],
  "related_registry_items": [
    {
      "id": "VI.D25",
      "title": "Temporal Stability Predicate",
      "url": "/registry/object/VI.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L79-L90",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L79-L90",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L79-L90)
- Source range: L79-L90
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D25` — Temporal Stability Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D25] Temporal Stability Predicate: 3 conditions for persistence.
    (i) Defect-functional norm bounded over τ¹ period
    (ii) α-flow orbit returns to ε-neighborhood
    (iii) Refinement tower eventually constant on base -/
```

## Source Excerpt

```lean
structure TemporalStabilityPredicate where
  /-- Number of conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  count_eq : condition_count = 3
  /-- (i) Defect-norm bounded. -/
  defect_bounded : Bool := true
  /-- (ii) α-flow returns (Poincaré recurrence on τ¹). -/
  alpha_flow_returns : Bool := true
  /-- (iii) Refinement eventually constant. -/
  refinement_constant : Bool := true
  deriving Repr
```
