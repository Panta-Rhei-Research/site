---
{
  "projection_kind": "taulib_declaration",
  "title": "RepairBudget",
  "permalink": "/verify/taulib/docs/book-vi-closure-ecosystem/repair-budget/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.Ecosystem`.",
  "declaration_id": "TauLib.BookVI.Closure.Ecosystem::RepairBudget",
  "declaration_slug": "repair-budget",
  "kind": "structure",
  "name": "RepairBudget",
  "module_name": "TauLib.BookVI.Closure.Ecosystem",
  "module_url": "/verify/taulib/docs/book-vi-closure-ecosystem/",
  "source_line_start": 97,
  "source_line_end": 104,
  "registry_ids": [
    "VI.D45"
  ],
  "related_registry_items": [
    {
      "id": "VI.D45",
      "title": "Repair Budget",
      "url": "/registry/object/VI.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L97-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.Ecosystem",
        "url": "/verify/taulib/docs/book-vi-closure-ecosystem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L97-L104",
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

- Module: [TauLib.BookVI.Closure.Ecosystem](/verify/taulib/docs/book-vi-closure-ecosystem/)
- Source path: [`TauLib/BookVI/Closure/Ecosystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L97-L104)
- Source range: L97-L104
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D45` — Repair Budget

## Immediate Comment / Docstring

```lean
/-- [VI.D45] Repair Budget: finite resource for SelfDesc maintenance.
    R_max = maximum cumulative repair before defect overwhelms.
    Connects to SelfDesc Closure Theorem (VI.T03):
    perturbations within basin are corrected, but R_max bounds the basin. -/
```

## Source Excerpt

```lean
structure RepairBudget where
  /-- Budget is finite for finite-lineage carriers. -/
  finite_budget : Bool := true
  /-- Budget bounds the SelfDesc basin. -/
  bounds_basin : Bool := true
  /-- Connects to SelfDesc Closure (VI.T03). -/
  selfdesc_connection : Bool := true
  deriving Repr
```
