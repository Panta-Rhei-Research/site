---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossingLimitTheorem",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/crossing-limit-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.CrossLimit::CrossingLimitTheorem",
  "declaration_slug": "crossing-limit-theorem",
  "kind": "structure",
  "name": "CrossingLimitTheorem",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "source_line_start": 144,
  "source_line_end": 155,
  "registry_ids": [
    "VI.T35"
  ],
  "related_registry_items": [
    {
      "id": "VI.T35",
      "title": "Crossing-Limit Theorem",
      "url": "/registry/object/VI.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L144-L155",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.CrossLimit",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L144-L155",
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

- Module: [TauLib.BookVI.CosmicLife.CrossLimit](/verify/taulib/docs/book-vi-cosmic-life-cross-limit/)
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L144-L155)
- Source range: L144-L155
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T35` — Crossing-Limit Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T35] Crossing-Limit Theorem: merger-directed net → ι_τ.
    Three-step proof: (1) monotonicity from VI.T31, (2) strict improvement
    from primorial ladder, (3) standard net convergence.
    Cofinal sequence authority: V.T116 (Finite Motif), V.T117 (Saturation Radius). -/
```

## Source Excerpt

```lean
structure CrossingLimitTheorem where
  /-- Target value is ι_τ = 2/(π+e). -/
  target : String := "iota_tau"
  /-- Monotone fusion (from VI.T31). -/
  monotone_fusion : Bool := true
  /-- Strictly contracting along primorial ladder. -/
  strictly_contracting : Bool := true
  /-- Convergence to maximal aliveness. -/
  maximal_aliveness : Bool := true
  /-- Cofinal sequence via V.T116 + V.T117. -/
  cofinal_from_bookV : Bool := true
  deriving Repr
```
