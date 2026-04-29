---
{
  "projection_kind": "taulib_declaration",
  "title": "InfinityTradeOff",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/infinity-trade-off/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::InfinityTradeOff",
  "declaration_slug": "infinity-trade-off",
  "kind": "structure",
  "name": "InfinityTradeOff",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 146,
  "source_line_end": 151,
  "registry_ids": [
    "II.D69"
  ],
  "related_registry_items": [
    {
      "id": "II.D69",
      "title": "The Infinity Trade-Off",
      "url": "/registry/object/II.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L146-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.SignClassification",
        "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L146-L151",
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

- Module: [TauLib.BookII.Mirror.SignClassification](/verify/taulib/docs/book-ii-mirror-sign-classification/)
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L146-L151)
- Source range: L146-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D69` — The Infinity Trade-Off

## Immediate Comment / Docstring

```lean
/-- [II.D69] The infinity trade-off: four boolean witnesses
    encoding the structural choices at the infinity level.

    - has_unique_omega: tau's single countable infinity
    - has_archimedean_density: orthodox Archimedean property of R
    - has_epsilon_delta: orthodox epsilon-delta continuity
    - has_finite_witnesses: tau's finite-stage witnesses -/
```

## Source Excerpt

```lean
structure InfinityTradeOff where
  has_unique_omega : Bool
  has_archimedean_density : Bool
  has_epsilon_delta : Bool
  has_finite_witnesses : Bool
  deriving DecidableEq, Repr
```
