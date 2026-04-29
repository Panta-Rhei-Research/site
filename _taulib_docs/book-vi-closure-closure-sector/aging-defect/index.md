---
{
  "projection_kind": "taulib_declaration",
  "title": "AgingDefect",
  "permalink": "/verify/taulib/docs/book-vi-closure-closure-sector/aging-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.ClosureSector`.",
  "declaration_id": "TauLib.BookVI.Closure.ClosureSector::AgingDefect",
  "declaration_slug": "aging-defect",
  "kind": "structure",
  "name": "AgingDefect",
  "module_name": "TauLib.BookVI.Closure.ClosureSector",
  "module_url": "/verify/taulib/docs/book-vi-closure-closure-sector/",
  "source_line_start": 132,
  "source_line_end": 139,
  "registry_ids": [
    "VI.D43"
  ],
  "related_registry_items": [
    {
      "id": "VI.D43",
      "title": "Aging as Defect Accumulation",
      "url": "/registry/object/VI.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L132-L139",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L132-L139",
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
- Source path: [`TauLib/BookVI/Closure/ClosureSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L132-L139)
- Source range: L132-L139
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D43` — Aging as Defect Accumulation

## Immediate Comment / Docstring

```lean
/-- [VI.D43] Aging as Defect Accumulation.
    Defect functional Δ(n) increases monotonically with refinement level n.
    For finite-lineage carriers, the repair budget R_max is finite,
    so defect eventually exceeds repair capacity. -/
```

## Source Excerpt

```lean
structure AgingDefect where
  /-- Defect increases monotonically. -/
  monotone_increase : Bool := true
  /-- Repair budget is finite. -/
  finite_repair : Bool := true
  /-- Applies to finite-lineage carriers only. -/
  finite_lineage_only : Bool := true
  deriving Repr
```
