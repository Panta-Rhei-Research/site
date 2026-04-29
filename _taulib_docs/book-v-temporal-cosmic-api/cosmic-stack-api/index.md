---
{
  "projection_kind": "taulib_declaration",
  "title": "cosmic_stack_api",
  "permalink": "/verify/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-api/",
  "summary_short": "`def` declaration in `TauLib.BookV.Temporal.CosmicAPI`.",
  "declaration_id": "TauLib.BookV.Temporal.CosmicAPI::cosmic_stack_api",
  "declaration_slug": "cosmic-stack-api",
  "kind": "def",
  "name": "cosmic_stack_api",
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_url": "/verify/taulib/docs/book-v-temporal-cosmic-api/",
  "source_line_start": 91,
  "source_line_end": 118,
  "registry_ids": [
    "V.D40"
  ],
  "related_registry_items": [
    {
      "id": "V.D40",
      "title": "Cosmic Stack API",
      "url": "/registry/object/V.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L91-L118",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.CosmicAPI",
        "url": "/verify/taulib/docs/book-v-temporal-cosmic-api/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L91-L118",
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

- Module: [TauLib.BookV.Temporal.CosmicAPI](/verify/taulib/docs/book-v-temporal-cosmic-api/)
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L91-L118)
- Source range: L91-L118
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D40` — Cosmic Stack API

## Immediate Comment / Docstring

```lean
/-- [V.D40] The Cosmic Stack API: all 21 Part I outputs listed
    as the formal interface for Parts II–VIII.

    Categories:
    - Temporal base (6 items): base circle, alpha-tick, proper time,
      causal ordering, geodesic duration, three epochs
    - Photon & readout (5 items): null intertwiner, operational distance,
      refinement drift, readout expansion, Hubble readout
    - Distance ladder (5 items): readout functor, Cepheid calibrator,
      BAO ruler, readout curvature, dark energy artifact
    - Boundary data (3 items): recombination, CMB surface, CνB surface
    - Sector interface (2 items): 5-sector coupling table, opening regime -/
```

## Source Excerpt

```lean
def cosmic_stack_api : List APIItem := [
  -- Temporal base (6)
  ⟨"V.D15", "Base circle τ¹", .TauEffective⟩,
  ⟨"V.D16", "Alpha-tick", .TauEffective⟩,
  ⟨"V.D17", "Proper time (arc length)", .TauEffective⟩,
  ⟨"V.D18", "Causal ordering", .TauEffective⟩,
  ⟨"V.D19", "Geodesic duration", .TauEffective⟩,
  ⟨"V.D20", "Three temporal epochs", .TauEffective⟩,
  -- Photon & readout (5)
  ⟨"V.D27", "Null intertwiner (photon)", .TauEffective⟩,
  ⟨"V.D28", "Operational distance", .TauEffective⟩,
  ⟨"V.D29", "Refinement drift (redshift)", .TauEffective⟩,
  ⟨"V.D30", "Readout expansion", .TauEffective⟩,
  ⟨"V.D31", "Hubble readout parameter", .TauEffective⟩,
  -- Distance ladder (5)
  ⟨"V.D32", "Distance readout functor", .TauEffective⟩,
  ⟨"V.D33", "Cepheid readout calibrator", .TauEffective⟩,
  ⟨"V.D34", "BAO standard ruler", .TauEffective⟩,
  ⟨"V.D35", "Readout curvature", .Conjectural⟩,
  ⟨"V.T19", "Dark energy artifact", .Conjectural⟩,
  -- Boundary data (3)
  ⟨"V.D36", "Recombination orbit depth", .TauEffective⟩,
  ⟨"V.D37", "CMB constraint surface", .TauEffective⟩,
  ⟨"V.D39", "CνB echo surface", .TauEffective⟩,
  -- Sector interface (2)
  ⟨"V.T10", "5-sector coupling table", .TauEffective⟩,
  ⟨"V.D24", "Opening regime", .TauEffective⟩
]
```
