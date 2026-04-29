---
{
  "projection_kind": "taulib_declaration",
  "title": "OneConstantOneAnchor",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/one-constant-one-anchor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::OneConstantOneAnchor",
  "declaration_slug": "one-constant-one-anchor",
  "kind": "structure",
  "name": "OneConstantOneAnchor",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 432,
  "source_line_end": 441,
  "registry_ids": [
    "IV.R120"
  ],
  "related_registry_items": [
    {
      "id": "IV.R120",
      "title": "One constant one anchor zero parameters",
      "url": "/registry/object/IV.R120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L432-L441",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L432-L441",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L432-L441)
- Source range: L432-L441
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R120` — One constant one anchor zero parameters

## Immediate Comment / Docstring

```lean
/-- [IV.R120] Every fundamental particle mass is determined by:
    - 1 dimensionless constant: ι_τ = 2/(π+e)
    - 1 dimensional anchor: m_n = 939.565421 MeV
    - 0 free dimensionless parameters

    The SM's ~25 free parameters reduce to this single input. -/
```

## Source Excerpt

```lean
structure OneConstantOneAnchor where
  /-- Number of dimensionless constants. -/
  num_constants : Nat := 1
  /-- Number of dimensional anchors. -/
  num_anchors : Nat := 1
  /-- Number of free parameters. -/
  num_free : Nat := 0
  /-- SM free parameters replaced. -/
  sm_replaced : Nat := 25
  deriving Repr
```
