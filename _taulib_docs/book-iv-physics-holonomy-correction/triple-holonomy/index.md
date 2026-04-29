---
{
  "projection_kind": "taulib_declaration",
  "title": "TripleHolonomy",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/triple-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::TripleHolonomy",
  "declaration_slug": "triple-holonomy",
  "kind": "structure",
  "name": "TripleHolonomy",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 77,
  "source_line_end": 88,
  "registry_ids": [
    "IV.D44"
  ],
  "related_registry_items": [
    {
      "id": "IV.D44",
      "title": "Triple Holonomy",
      "url": "/registry/object/IV.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L77-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L77-L88",
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L77-L88)
- Source range: L77-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D44` — Triple Holonomy

## Immediate Comment / Docstring

```lean
/-- [IV.D44] The three independent U(1) circles in τ³ = τ¹ ×_f T².

    Each circle contributes one factor of π through holonomy integration.
    The product gives π³ ≈ 31.006. -/
```

## Source Excerpt

```lean
structure TripleHolonomy where
  /-- Number of independent U(1) circles. -/
  circle_count : Nat
  /-- Each is in a different component of the fibration. -/
  components : List String
  /-- Circle count matches component count. -/
  count_match : circle_count = components.length
  /-- π exponent = circle count. -/
  pi_exponent : Nat
  /-- The exponent equals the circle count. -/
  exp_match : pi_exponent = circle_count
  deriving Repr
```
