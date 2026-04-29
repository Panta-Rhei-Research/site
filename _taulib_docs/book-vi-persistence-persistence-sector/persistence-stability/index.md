---
{
  "projection_kind": "taulib_declaration",
  "title": "PersistenceStability",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/persistence-stability/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::PersistenceStability",
  "declaration_slug": "persistence-stability",
  "kind": "structure",
  "name": "PersistenceStability",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 114,
  "source_line_end": 123,
  "registry_ids": [
    "VI.T16"
  ],
  "related_registry_items": [
    {
      "id": "VI.T16",
      "title": "Persistence as α-Base Stability",
      "url": "/registry/object/VI.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L114-L123",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L114-L123",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L114-L123)
- Source range: L114-L123
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T16` — Persistence as α-Base Stability

## Immediate Comment / Docstring

```lean
/-- [VI.T16] Persistence = α-Base Stability Theorem.
    A Life loop restricted to τ¹ base with winding number w_α = 1
    satisfies the Temporal Stability Predicate iff it is a
    persistence-sector Life loop. -/
```

## Source Excerpt

```lean
structure PersistenceStability where
  /-- Winding number on base. -/
  winding_alpha : Nat
  /-- Winding is exactly 1. -/
  winding_eq : winding_alpha = 1
  /-- Temporal stability holds. -/
  temporal_stable : Bool := true
  /-- Sector assignment is persistence. -/
  sector_persistence : Bool := true
  deriving Repr
```
