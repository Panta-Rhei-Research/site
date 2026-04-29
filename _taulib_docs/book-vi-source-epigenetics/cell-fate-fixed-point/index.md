---
{
  "projection_kind": "taulib_declaration",
  "title": "CellFateFixedPoint",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/cell-fate-fixed-point/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::CellFateFixedPoint",
  "declaration_slug": "cell-fate-fixed-point",
  "kind": "structure",
  "name": "CellFateFixedPoint",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 305,
  "source_line_end": 314,
  "registry_ids": [
    "VI.P22"
  ],
  "related_registry_items": [
    {
      "id": "VI.P22",
      "title": "Cell Fate as Fixed Point",
      "url": "/registry/object/VI.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L305-L314",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L305-L314",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L305-L314)
- Source range: L305-L314
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P22` — Cell Fate as Fixed Point

## Immediate Comment / Docstring

```lean
/-- [VI.P22] Cell Fate as Fixed Point.
    At terminal differentiation, the SelfDesc evaluator maintains the
    fully restricted chromatin partition. Perturbations within the basin
    of attraction are absorbed by SelfDesc closure (VI.T03).
    Terminal differentiation is a fixed point of the evaluator dynamics.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure CellFateFixedPoint where
  /-- Terminal state is self-maintaining. -/
  self_maintaining : Bool := true
  /-- Perturbations absorbed by SelfDesc closure (VI.T03). -/
  basin_absorbing : Bool := true
  /-- Fixed point of evaluator dynamics. -/
  is_fixed_point : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
