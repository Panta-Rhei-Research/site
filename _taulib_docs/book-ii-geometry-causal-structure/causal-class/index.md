---
{
  "projection_kind": "taulib_declaration",
  "title": "CausalClass",
  "permalink": "/verify/taulib/docs/book-ii-geometry-causal-structure/causal-class/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Geometry.CausalStructure`.",
  "declaration_id": "TauLib.BookII.Geometry.CausalStructure::CausalClass",
  "declaration_slug": "causal-class",
  "kind": "inductive",
  "name": "CausalClass",
  "module_name": "TauLib.BookII.Geometry.CausalStructure",
  "module_url": "/verify/taulib/docs/book-ii-geometry-causal-structure/",
  "source_line_start": 94,
  "source_line_end": 98,
  "registry_ids": [
    "II.D22"
  ],
  "related_registry_items": [
    {
      "id": "II.D22",
      "title": "Causal Structure",
      "url": "/registry/object/II.D22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L94-L98",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.CausalStructure",
        "url": "/verify/taulib/docs/book-ii-geometry-causal-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L94-L98",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookII.Geometry.CausalStructure](/verify/taulib/docs/book-ii-geometry-causal-structure/)
- Source path: [`TauLib/BookII/Geometry/CausalStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L94-L98)
- Source range: L94-L98
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.D22` — Causal Structure

## Immediate Comment / Docstring

```lean
/-- [II.D22] Causal classification of displacement vectors.
    A vector (Δx, Δy) is classified by the sign of Δx² - Δy²:
    - Timelike: |Δx| > |Δy| (inside null cone)
    - Spacelike: |Δx| < |Δy| (outside null cone)
    - Null: |Δx| = |Δy| (on null cone boundary) -/
```

## Source Excerpt

```lean
inductive CausalClass where
  | timelike   : CausalClass
  | spacelike  : CausalClass
  | null       : CausalClass
  deriving Repr, DecidableEq
```
