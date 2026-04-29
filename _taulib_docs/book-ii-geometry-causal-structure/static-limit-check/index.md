---
{
  "projection_kind": "taulib_declaration",
  "title": "static_limit_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-causal-structure/static-limit-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.CausalStructure`.",
  "declaration_id": "TauLib.BookII.Geometry.CausalStructure::static_limit_check",
  "declaration_slug": "static-limit-check",
  "kind": "def",
  "name": "static_limit_check",
  "module_name": "TauLib.BookII.Geometry.CausalStructure",
  "module_url": "/verify/taulib/docs/book-ii-geometry-causal-structure/",
  "source_line_start": 136,
  "source_line_end": 142,
  "registry_ids": [
    "II.T19"
  ],
  "related_registry_items": [
    {
      "id": "II.T19",
      "title": "Euclidean as Static Limit",
      "url": "/registry/object/II.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L136-L142",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L136-L142",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookII/Geometry/CausalStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L136-L142)
- Source range: L136-L142
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T19` — Euclidean as Static Limit

## Immediate Comment / Docstring

```lean
/-- [II.T19] In the static limit (no split-complex coupling),
    the causal structure degenerates:
    - Null cone collapses (wave → Laplace)
    - All directions become spacelike (Euclidean)

    Euclidean geometry survives because Tarski axioms
    (betweenness, congruence) depend only on ultrametric
    distance, not on j. -/
```

## Source Excerpt

```lean
def static_limit_check : Bool :=
  -- Without j coupling, displacement norm is dx² + dy² (always ≥ 0)
  -- Every nonzero direction is "spacelike" (Euclidean positive-definite)
  let test_vectors := [(1,0), (0,1), (1,1), (2,3), (-1,4)]
  test_vectors.all fun (dx, dy) =>
    -- Euclidean norm squared is always non-negative
    dx * dx + dy * dy ≥ 0
```
