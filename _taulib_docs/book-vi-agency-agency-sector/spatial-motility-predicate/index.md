---
{
  "projection_kind": "taulib_declaration",
  "title": "SpatialMotilityPredicate",
  "permalink": "/verify/taulib/docs/book-vi-agency-agency-sector/spatial-motility-predicate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.AgencySector`.",
  "declaration_id": "TauLib.BookVI.Agency.AgencySector::SpatialMotilityPredicate",
  "declaration_slug": "spatial-motility-predicate",
  "kind": "structure",
  "name": "SpatialMotilityPredicate",
  "module_name": "TauLib.BookVI.Agency.AgencySector",
  "module_url": "/verify/taulib/docs/book-vi-agency-agency-sector/",
  "source_line_start": 67,
  "source_line_end": 78,
  "registry_ids": [
    "VI.D30"
  ],
  "related_registry_items": [
    {
      "id": "VI.D30",
      "title": "Spatial Motility Predicate",
      "url": "/registry/object/VI.D30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L67-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.AgencySector",
        "url": "/verify/taulib/docs/book-vi-agency-agency-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L67-L78",
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

- Module: [TauLib.BookVI.Agency.AgencySector](/verify/taulib/docs/book-vi-agency-agency-sector/)
- Source path: [`TauLib/BookVI/Agency/AgencySector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L67-L78)
- Source range: L67-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D30` — Spatial Motility Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D30] Spatial Motility Predicate: 3 conditions for agency.
    (i) Displacement on base τ¹ within one Life Loop cycle
    (ii) Displacement is distinction-preserving (carrier boundary intact)
    (iii) Energy cost bounded by metabolic budget -/
```

## Source Excerpt

```lean
structure SpatialMotilityPredicate where
  /-- Number of conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  count_eq : condition_count = 3
  /-- (i) Displacement on base. -/
  base_displacement : Bool := true
  /-- (ii) Distinction-preserving. -/
  distinction_preserving : Bool := true
  /-- (iii) Energy-bounded. -/
  energy_bounded : Bool := true
  deriving Repr
```
