---
{
  "projection_kind": "taulib_declaration",
  "title": "ComplexityBudget",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-budget/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::ComplexityBudget",
  "declaration_slug": "complexity-budget",
  "kind": "structure",
  "name": "ComplexityBudget",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 220,
  "source_line_end": 227,
  "registry_ids": [
    "VI.D75"
  ],
  "related_registry_items": [
    {
      "id": "VI.D75",
      "title": "Complexity Budget",
      "url": "/registry/object/VI.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L220-L227",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L220-L227",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L220-L227)
- Source range: L220-L227
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D75` — Complexity Budget

## Immediate Comment / Docstring

```lean
/-- [VI.D75] Complexity Budget: C(n) = N − |D_n|, dual of defect count.
    As defects decay geometrically (V.T62), freed capacity increases
    monotonically, providing structural resources for complex configurations.
    Cross-ref: V.T60 (finite budget), V.T62 (geometric decay). -/
```

## Source Excerpt

```lean
structure ComplexityBudget where
  /-- Initial defect count N (finite by V.T60). -/
  initial_defects : Nat
  /-- Freed capacity increases monotonically as defects decay. -/
  freed_capacity_monotone : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
