---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryUnificationSummary",
  "permalink": "/verify/taulib/docs/book-v-cosmology-boundary-unification/boundary-unification-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BoundaryUnification`.",
  "declaration_id": "TauLib.BookV.Cosmology.BoundaryUnification::BoundaryUnificationSummary",
  "declaration_slug": "boundary-unification-summary",
  "kind": "structure",
  "name": "BoundaryUnificationSummary",
  "module_name": "TauLib.BookV.Cosmology.BoundaryUnification",
  "module_url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/",
  "source_line_start": 238,
  "source_line_end": 251,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L238-L251",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BoundaryUnification",
        "url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L238-L251",
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

- Module: [TauLib.BookV.Cosmology.BoundaryUnification](/verify/taulib/docs/book-v-cosmology-boundary-unification/)
- Source path: [`TauLib/BookV/Cosmology/BoundaryUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L238-L251)
- Source range: L238-L251
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Summary of the boundary unification principle. -/
```

## Source Excerpt

```lean
structure BoundaryUnificationSummary where
  /-- Number of primitive sectors. -/
  num_sectors : Nat := 4
  /-- Number of sector pairs. -/
  num_pairs : Nat := 6
  /-- Number of total couplings (self + cross). -/
  num_couplings : Nat := 10
  /-- Single master constant. -/
  master_constant : String := "iota_tau = 2/(pi + e)"
  /-- Whether all are determined by master constant. -/
  all_determined : Bool := true
  /-- No larger gauge group needed. -/
  no_larger_group : Bool := true
  deriving Repr
```
