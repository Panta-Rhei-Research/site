---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticReadoutLayers",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/ontic-readout-layers/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::OnticReadoutLayers",
  "declaration_slug": "ontic-readout-layers",
  "kind": "structure",
  "name": "OnticReadoutLayers",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 153,
  "source_line_end": 162,
  "registry_ids": [
    "V.D186"
  ],
  "related_registry_items": [
    {
      "id": "V.D186",
      "title": "Ontic and readout layers",
      "url": "/registry/object/V.D186/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L153-L162",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L153-L162",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L153-L162)
- Source range: L153-L162
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D186` — Ontic and readout layers

## Immediate Comment / Docstring

```lean
/-- [V.D186] The two layers of physical description.

    Ontic layer: boundary holonomy algebra H_partial[omega] and
    the enrichment functor E₀→E₁. Entities are structural.

    Readout layer: the orthodox VM (QFT Hilbert space, GR metric,
    thermodynamic potentials) obtained by chart projection. -/
```

## Source Excerpt

```lean
structure OnticReadoutLayers where
  /-- Number of layers (always 2). -/
  layer_count : Nat
  /-- Exactly 2 layers. -/
  count_eq : layer_count = 2
  /-- Ontic layer is observer-independent. -/
  ontic_independent : Bool := true
  /-- Readout layer is chart-dependent. -/
  readout_chart_dependent : Bool := true
  deriving Repr
```
