---
{
  "projection_kind": "taulib_declaration",
  "title": "EeMonotoneConvergence",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/ee-monotone-convergence/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::EeMonotoneConvergence",
  "declaration_slug": "ee-monotone-convergence",
  "kind": "structure",
  "name": "EeMonotoneConvergence",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 209,
  "source_line_end": 218,
  "registry_ids": [
    "VI.P21"
  ],
  "related_registry_items": [
    {
      "id": "VI.P21",
      "title": "Monotone Convergence of Enantiomeric Excess",
      "url": "/registry/object/VI.P21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L209-L218",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L209-L218",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L209-L218)
- Source range: L209-L218
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P21` — Monotone Convergence of Enantiomeric Excess

## Immediate Comment / Docstring

```lean
/-- [VI.P21] ee(n) → 1 monotonically: enantiomeric excess increases
    at every refinement level and converges to 1.
    The double-well potential (Hodge stabilization) prevents regression,
    and Poincaré topological lock-in on L = S¹ ∨ S¹ provides
    additional protection beyond energetic barriers. -/
```

## Source Excerpt

```lean
structure EeMonotoneConvergence where
  /-- Monotone increasing. -/
  monotone_increasing : Bool := true
  /-- Converges to ee = 1. -/
  limit_is_one : Bool := true
  /-- Double-well barrier prevents regression. -/
  hodge_stabilization : Bool := true
  /-- Topological lock-in on L. -/
  poincare_lockin : Bool := true
  deriving Repr
```
