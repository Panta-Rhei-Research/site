---
{
  "projection_kind": "taulib_declaration",
  "title": "FirstOrderCh53",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/first-order-ch53/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::FirstOrderCh53",
  "declaration_slug": "first-order-ch53",
  "kind": "structure",
  "name": "FirstOrderCh53",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 325,
  "source_line_end": 334,
  "registry_ids": [
    "IV.D238"
  ],
  "related_registry_items": [
    {
      "id": "IV.D238",
      "title": "First-order phase transition",
      "url": "/registry/object/IV.D238/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L325-L334",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L325-L334",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L325-L334)
- Source range: L325-L334
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D238` — First-order phase transition

## Immediate Comment / Docstring

```lean
/-- [IV.D238] First-order phase transition (ch53 formulation): one or more
    defect-tuple components undergo a discontinuous jump as a control
    parameter (e.g., tau-temperature) crosses a threshold.
    Examples: melting, boiling, Bose-Einstein condensation. -/
```

## Source Excerpt

```lean
structure FirstOrderCh53 where
  /-- Transition order (1 = first-order, discontinuous). -/
  transition_order : Nat := 1
  /-- Number of discontinuous thermodynamic quantities (1 = latent heat). -/
  n_discontinuous_quantities : Nat := 1
  /-- Examples. -/
  examples : List String := ["melting", "boiling", "BEC"]
  /-- This is first order. -/
  is_first_order : transition_order = 1
  deriving Repr
```
