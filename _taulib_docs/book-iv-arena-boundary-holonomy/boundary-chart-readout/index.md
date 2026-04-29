---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryChartReadout",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/boundary-chart-readout/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::BoundaryChartReadout",
  "declaration_slug": "boundary-chart-readout",
  "kind": "structure",
  "name": "BoundaryChartReadout",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 187,
  "source_line_end": 194,
  "registry_ids": [
    "IV.D263"
  ],
  "related_registry_items": [
    {
      "id": "IV.D263",
      "title": "Chart readout homomorphism",
      "url": "/registry/object/IV.D263/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L187-L194",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L187-L194",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L187-L194)
- Source range: L187-L194
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D263` — Chart readout homomorphism

## Immediate Comment / Docstring

```lean
/-- [IV.D263] Chart readout from boundary data: assembles sector lifts
    into a coherent 4D readout. -/
```

## Source Excerpt

```lean
structure BoundaryChartReadout where
  /-- Number of sector lifts used. -/
  lift_count : Nat
  lift_count_eq : lift_count = 5
  /-- Output dimension. -/
  output_dim : Nat
  output_eq : output_dim = 4
  deriving Repr
```
