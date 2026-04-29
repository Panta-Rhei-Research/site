---
{
  "projection_kind": "taulib_declaration",
  "title": "NoSingularity",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/no-singularity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::NoSingularity",
  "declaration_slug": "no-singularity",
  "kind": "structure",
  "name": "NoSingularity",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 155,
  "source_line_end": 164,
  "registry_ids": [
    "V.T127"
  ],
  "related_registry_items": [
    {
      "id": "V.T127",
      "title": "No singularity theorem",
      "url": "/registry/object/V.T127/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L155-L164",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L155-L164",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L155-L164)
- Source range: L155-L164
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T127` — No singularity theorem

## Immediate Comment / Docstring

```lean
/-- [V.T127] No singularity theorem.

    The tau-Einstein equation admits no singular solutions because:
    1. R^H is in H_partial[omega] (profinite, finite at every depth)
    2. kappa_tau = 1 - iota_tau is finite and nonzero
    3. T is bounded by the defect budget at each refinement level

    Singular solutions of GR (black hole interiors, big bang) are
    chart artifacts: the chart projection pr_chart can produce
    singularities even from non-singular boundary data. -/
```

## Source Excerpt

```lean
structure NoSingularity where
  /-- Profinite algebra is finite at every depth. -/
  finite_at_depth : Bool := true
  /-- Coupling kappa_tau is finite and nonzero. -/
  coupling_finite : Bool := true
  /-- Stress-energy bounded by defect budget. -/
  stress_bounded : Bool := true
  /-- All three conditions hold. -/
  all_conditions : Bool := true
  deriving Repr
```
