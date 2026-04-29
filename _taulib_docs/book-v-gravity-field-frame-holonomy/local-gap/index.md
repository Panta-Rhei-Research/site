---
{
  "projection_kind": "taulib_declaration",
  "title": "LocalGap",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/local-gap/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::LocalGap",
  "declaration_slug": "local-gap",
  "kind": "structure",
  "name": "LocalGap",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 133,
  "source_line_end": 146,
  "registry_ids": [
    "V.D43"
  ],
  "related_registry_items": [
    {
      "id": "V.D43",
      "title": "Holonomy gap element",
      "url": "/registry/object/V.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L133-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L133-L146",
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L133-L146)
- Source range: L133-L146
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D43` — Holonomy gap element

## Immediate Comment / Docstring

```lean
/-- [V.D43] Local gap element: smallest addressable gravitational
    quantum at depth n.

    The local gap is the minimal holonomy element that can be
    resolved at the given refinement depth. It decreases as depth
    increases (finer resolution), converging to zero in the
    ω-germ limit.

    gap(n) = κ_τ / refinement_scale(n) -/
```

## Source Excerpt

```lean
structure LocalGap where
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- Gap numerator (κ_τ numerator at this scale). -/
  gap_numer : Nat
  /-- Gap denominator (refinement scale). -/
  gap_denom : Nat
  /-- Denominator positive. -/
  denom_pos : gap_denom > 0
  /-- Gap is positive at any finite depth. -/
  gap_positive : gap_numer > 0
  deriving Repr
```
