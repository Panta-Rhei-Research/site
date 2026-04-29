---
{
  "projection_kind": "taulib_declaration",
  "title": "StructureRecyclingPredicate",
  "permalink": "/verify/taulib/docs/book-vi-closure-closure-sector/structure-recycling-predicate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.ClosureSector`.",
  "declaration_id": "TauLib.BookVI.Closure.ClosureSector::StructureRecyclingPredicate",
  "declaration_slug": "structure-recycling-predicate",
  "kind": "structure",
  "name": "StructureRecyclingPredicate",
  "module_name": "TauLib.BookVI.Closure.ClosureSector",
  "module_url": "/verify/taulib/docs/book-vi-closure-closure-sector/",
  "source_line_start": 72,
  "source_line_end": 83,
  "registry_ids": [
    "VI.D42"
  ],
  "related_registry_items": [
    {
      "id": "VI.D42",
      "title": "Structure Recycling Predicate",
      "url": "/registry/object/VI.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L72-L83",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.ClosureSector",
        "url": "/verify/taulib/docs/book-vi-closure-closure-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L72-L83",
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

- Module: [TauLib.BookVI.Closure.ClosureSector](/verify/taulib/docs/book-vi-closure-closure-sector/)
- Source path: [`TauLib/BookVI/Closure/ClosureSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L72-L83)
- Source range: L72-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D42` — Structure Recycling Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D42] Structure Recycling Predicate: 3 conditions.
    (i) Net reduction of structural complexity on T² fiber
    (ii) Hodge capacity gradient negative (reverse of source)
    (iii) Energy release returned to base τ¹
    Dual to Structure Generation Predicate (VI.D37). -/
```

## Source Excerpt

```lean
structure StructureRecyclingPredicate where
  /-- Number of conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  count_eq : condition_count = 3
  /-- (i) Net reduction on fiber. -/
  net_reduction : Bool := true
  /-- (ii) Hodge capacity gradient negative. -/
  hodge_gradient_negative : Bool := true
  /-- (iii) Energy returned to base. -/
  energy_to_base : Bool := true
  deriving Repr
```
