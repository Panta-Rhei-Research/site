---
{
  "projection_kind": "taulib_declaration",
  "title": "StructureGenerationPredicate",
  "permalink": "/verify/taulib/docs/book-vi-source-source-sector/structure-generation-predicate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.SourceSector`.",
  "declaration_id": "TauLib.BookVI.Source.SourceSector::StructureGenerationPredicate",
  "declaration_slug": "structure-generation-predicate",
  "kind": "structure",
  "name": "StructureGenerationPredicate",
  "module_name": "TauLib.BookVI.Source.SourceSector",
  "module_url": "/verify/taulib/docs/book-vi-source-source-sector/",
  "source_line_start": 70,
  "source_line_end": 81,
  "registry_ids": [
    "VI.D37"
  ],
  "related_registry_items": [
    {
      "id": "VI.D37",
      "title": "Structure Generation Predicate",
      "url": "/registry/object/VI.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L70-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.SourceSector",
        "url": "/verify/taulib/docs/book-vi-source-source-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L70-L81",
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

- Module: [TauLib.BookVI.Source.SourceSector](/verify/taulib/docs/book-vi-source-source-sector/)
- Source path: [`TauLib/BookVI/Source/SourceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L70-L81)
- Source range: L70-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D37` — Structure Generation Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D37] Structure Generation Predicate: 3 conditions.
    (i) Net production of structural complexity on T² fiber
    (ii) Hodge capacity gradient positive (Book III, Part IV)
    (iii) Energy input from base τ¹ (photon capture or equivalent) -/
```

## Source Excerpt

```lean
structure StructureGenerationPredicate where
  /-- Number of conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  count_eq : condition_count = 3
  /-- (i) Net production on fiber. -/
  net_production : Bool := true
  /-- (ii) Hodge capacity gradient positive. -/
  hodge_gradient_positive : Bool := true
  /-- (iii) Energy input from base. -/
  base_energy_input : Bool := true
  deriving Repr
```
