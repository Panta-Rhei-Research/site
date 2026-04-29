---
{
  "projection_kind": "taulib_declaration",
  "title": "DistinctionThreshold",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/distinction-threshold/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::DistinctionThreshold",
  "declaration_slug": "distinction-threshold",
  "kind": "structure",
  "name": "DistinctionThreshold",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 263,
  "source_line_end": 274,
  "registry_ids": [
    "VI.D76"
  ],
  "related_registry_items": [
    {
      "id": "VI.D76",
      "title": "Distinction Threshold",
      "url": "/registry/object/VI.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L263-L274",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L263-L274",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L263-L274)
- Source range: L263-L274
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D76` — Distinction Threshold

## Immediate Comment / Docstring

```lean
/-- [VI.D76] Distinction Threshold: minimum complexity for life.
    Distinction requires 5 conditions, SelfDesc requires 3 conditions,
    giving threshold = 8. When C(n) ≥ 8, the system has sufficient
    freed capacity to instantiate Distinction + SelfDesc simultaneously. -/
```

## Source Excerpt

```lean
structure DistinctionThreshold where
  /-- Total threshold conditions. -/
  threshold_conditions : Nat
  /-- Threshold is exactly 8. -/
  threshold_eq : threshold_conditions = 8
  /-- Distinction contributes 5 conditions. -/
  distinction_count : Nat := 5
  /-- SelfDesc contributes 3 conditions. -/
  selfdesc_count : Nat := 3
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
