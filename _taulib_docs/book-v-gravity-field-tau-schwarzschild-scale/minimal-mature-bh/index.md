---
{
  "projection_kind": "taulib_declaration",
  "title": "MinimalMatureBH",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/minimal-mature-bh/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauSchwarzschildScale`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschildScale::MinimalMatureBH",
  "declaration_slug": "minimal-mature-bh",
  "kind": "structure",
  "name": "MinimalMatureBH",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschildScale",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/",
  "source_line_start": 104,
  "source_line_end": 115,
  "registry_ids": [
    "V.L5"
  ],
  "related_registry_items": [
    {
      "id": "V.L5",
      "title": "Minimal Mature Black Hole",
      "url": "/registry/object/V.L5/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L104-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschildScale",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L104-L115",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschildScale](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschildScale.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L104-L115)
- Source range: L104-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.L5` — Minimal Mature Black Hole

## Immediate Comment / Docstring

```lean
/-- [V.L5] Minimal mature black hole: below M_min, geometric relaxation
    completes before torus vacuum stabilizes. M_min is the lower boundary
    of the mature BH population.

    - Below M_min: linking topology relaxes → no stable T² vacuum
    - Above M_min: torus vacuum stabilizes → mature BH with r/R = ι_τ
    - M_min sets the Chandrasekhar-scale threshold for τ-BH formation

    The existence of M_min ensures the mature BH population is bounded
    below. No τ-BH can be arbitrarily light. -/
```

## Source Excerpt

```lean
structure MinimalMatureBH where
  /-- M_min exists as a threshold. -/
  threshold_exists : Bool := true
  /-- Below M_min: no stable torus vacuum. -/
  below_unstable : Bool := true
  /-- Above M_min: stable mature BH. -/
  above_stable : Bool := true
  /-- Population is bounded below. -/
  population_bounded : Bool := true
  /-- Relaxation modes (geometric + topological). -/
  relaxation_modes : Nat := 2
  deriving Repr
```
