---
{
  "projection_kind": "taulib_declaration",
  "title": "ClosureReturn",
  "permalink": "/verify/taulib/docs/book-vi-closure-closure-sector/closure-return/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.ClosureSector`.",
  "declaration_id": "TauLib.BookVI.Closure.ClosureSector::ClosureReturn",
  "declaration_slug": "closure-return",
  "kind": "structure",
  "name": "ClosureReturn",
  "module_name": "TauLib.BookVI.Closure.ClosureSector",
  "module_url": "/verify/taulib/docs/book-vi-closure-closure-sector/",
  "source_line_start": 106,
  "source_line_end": 113,
  "registry_ids": [
    "VI.T23"
  ],
  "related_registry_items": [
    {
      "id": "VI.T23",
      "title": "Closure as η-Fiber Return",
      "url": "/registry/object/VI.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L106-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L106-L113",
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
- Source path: [`TauLib/BookVI/Closure/ClosureSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/ClosureSector.lean#L106-L113)
- Source range: L106-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T23` — Closure as η-Fiber Return

## Immediate Comment / Docstring

```lean
/-- [VI.T23] Closure = π''-Fiber Return Theorem.
    A closure Life loop has nontrivial π''-winding on the fiber
    with net structure recycling (returning complexity to base). -/
```

## Source Excerpt

```lean
structure ClosureReturn where
  /-- Winding on π'' (fiber). -/
  winding_pi_double : Nat
  /-- Winding is nontrivial (≥ 1). -/
  pi_double_nontrivial : winding_pi_double ≥ 1
  /-- Net structure recycling. -/
  net_recycling : Bool := true
  deriving Repr
```
