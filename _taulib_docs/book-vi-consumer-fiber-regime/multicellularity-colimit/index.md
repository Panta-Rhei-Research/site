---
{
  "projection_kind": "taulib_declaration",
  "title": "MulticellularityColimit",
  "permalink": "/verify/taulib/docs/book-vi-consumer-fiber-regime/multicellularity-colimit/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.FiberRegime`.",
  "declaration_id": "TauLib.BookVI.Consumer.FiberRegime::MulticellularityColimit",
  "declaration_slug": "multicellularity-colimit",
  "kind": "structure",
  "name": "MulticellularityColimit",
  "module_name": "TauLib.BookVI.Consumer.FiberRegime",
  "module_url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/",
  "source_line_start": 93,
  "source_line_end": 102,
  "registry_ids": [
    "VI.D48"
  ],
  "related_registry_items": [
    {
      "id": "VI.D48",
      "title": "Multicellularity as Colimit",
      "url": "/registry/object/VI.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L93-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.FiberRegime",
        "url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L93-L102",
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

- Module: [TauLib.BookVI.Consumer.FiberRegime](/verify/taulib/docs/book-vi-consumer-fiber-regime/)
- Source path: [`TauLib/BookVI/Consumer/FiberRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L93-L102)
- Source range: L93-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D48` — Multicellularity as Colimit

## Immediate Comment / Docstring

```lean
/-- [VI.D48] Multicellularity as Colimit (Book I, Part VII).
    A multicellular organism is a colimit over a diagram of
    cooperating cell types. The colimit construction ensures
    universal properties: any compatible morphism factors through it. -/
```

## Source Excerpt

```lean
structure MulticellularityColimit where
  /-- Minimum cell count for multicellularity. -/
  cell_count : Nat
  /-- At least 2 cells. -/
  multi : cell_count ≥ 2
  /-- Cells are cooperative (not parasitic). -/
  cooperative : Bool := true
  /-- Construction is a categorical colimit. -/
  colimit_construction : Bool := true
  deriving Repr
```
