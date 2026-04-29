---
{
  "projection_kind": "taulib_declaration",
  "title": "InflationaryRegime",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/inflationary-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::InflationaryRegime",
  "declaration_slug": "inflationary-regime",
  "kind": "structure",
  "name": "InflationaryRegime",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 134,
  "source_line_end": 147,
  "registry_ids": [
    "V.D156"
  ],
  "related_registry_items": [
    {
      "id": "V.D156",
      "title": "Inflationary Regime",
      "url": "/registry/object/V.D156/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L134-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L134-L147",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L134-L147)
- Source range: L134-L147
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D156` — Inflationary Regime

## Immediate Comment / Docstring

```lean
/-- [V.D156] Inflationary regime: the sub-interval of the pre-hadronic
    regime during which the chart-level readout yields approximately
    exponential expansion.

    This is NOT caused by an inflaton field. It is a regime property:
    at early α-ticks, the boundary character magnitudes are so large
    that the expansion readout appears exponential. -/
```

## Source Excerpt

```lean
structure InflationaryRegime where
  /-- Start tick of inflation. -/
  start_tick : Nat
  /-- End tick of inflation. -/
  end_tick : Nat
  /-- Start is positive. -/
  start_pos : start_tick > 0
  /-- End is after start. -/
  end_after_start : end_tick > start_tick
  /-- Number of sectors driving exponential expansion (5 = all). -/
  n_expansion_sectors : Nat := 5
  /-- Number of inflaton fields (0 = none, by V.C17). -/
  n_inflaton_fields : Nat := 0
  deriving Repr
```
