---
{
  "projection_kind": "taulib_declaration",
  "title": "FusionConvergence",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/fusion-convergence/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.CrossLimit::FusionConvergence",
  "declaration_slug": "fusion-convergence",
  "kind": "structure",
  "name": "FusionConvergence",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "source_line_start": 117,
  "source_line_end": 126,
  "registry_ids": [
    "VI.T31"
  ],
  "related_registry_items": [
    {
      "id": "VI.T31",
      "title": "BH ω-Representative: Fusion Convergence",
      "url": "/registry/object/VI.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L117-L126",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L117-L126",
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
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L117-L126)
- Source range: L117-L126
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T31` — BH ω-Representative: Fusion Convergence

## Immediate Comment / Docstring

```lean
/-- [VI.T31] Fusion Convergence: BH merger monotonically converges codes.
    (i) Monotone: d_k(code_f) ≤ max{d_k(code_1), d_k(code_2)}
    (ii) Strict improvement for distinct codes at ∞-many levels
    (iii) Limit: merger net → ι_τ
    Authority: V.D171 (Blueprint Fusion), V.T112 (Monoid Closure). -/
```

## Source Excerpt

```lean
structure FusionConvergence where
  /-- Fusion never increases ι_τ-distance. -/
  monotone : Bool := true
  /-- Distinct codes yield strict improvement. -/
  strict_improvement : Bool := true
  /-- Net converges to ι_τ. -/
  converges_to_iota : Bool := true
  /-- Blueprint monoid has no inverses (irreversibility). -/
  no_inverses : Bool := true
  deriving Repr
```
