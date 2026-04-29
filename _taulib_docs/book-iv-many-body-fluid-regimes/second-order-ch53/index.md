---
{
  "projection_kind": "taulib_declaration",
  "title": "SecondOrderCh53",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/second-order-ch53/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::SecondOrderCh53",
  "declaration_slug": "second-order-ch53",
  "kind": "structure",
  "name": "SecondOrderCh53",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 343,
  "source_line_end": 352,
  "registry_ids": [
    "IV.D239"
  ],
  "related_registry_items": [
    {
      "id": "IV.D239",
      "title": "Second-order phase transition",
      "url": "/registry/object/IV.D239/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L343-L352",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L343-L352",
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L343-L352)
- Source range: L343-L352
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D239` — Second-order phase transition

## Immediate Comment / Docstring

```lean
/-- [IV.D239] Second-order (continuous) phase transition (ch53 formulation):
    all defect-tuple components are continuous but one or more derivatives
    are discontinuous at the transition point.
    Examples: ferromagnetic transition, superfluid lambda-point. -/
```

## Source Excerpt

```lean
structure SecondOrderCh53 where
  /-- Transition order (2 = second-order, continuous). -/
  transition_order : Nat := 2
  /-- Order of first discontinuous derivative (1 = 1st derivative). -/
  discontinuous_derivative_order : Nat := 1
  /-- Examples. -/
  examples : List String := ["ferromagnetic", "superfluid lambda-point"]
  /-- This is second order. -/
  is_second_order : transition_order = 2
  deriving Repr
```
