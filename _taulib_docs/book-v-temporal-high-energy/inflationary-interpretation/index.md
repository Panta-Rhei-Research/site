---
{
  "projection_kind": "taulib_declaration",
  "title": "InflationaryInterpretation",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/inflationary-interpretation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::InflationaryInterpretation",
  "declaration_slug": "inflationary-interpretation",
  "kind": "structure",
  "name": "InflationaryInterpretation",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 217,
  "source_line_end": 226,
  "registry_ids": [
    "V.R33"
  ],
  "related_registry_items": [
    {
      "id": "V.R33",
      "title": "Inflation as Progression",
      "url": "/registry/object/V.R33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L217-L226",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.HighEnergy",
        "url": "/verify/taulib/docs/book-v-temporal-high-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L217-L226",
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

- Module: [TauLib.BookV.Temporal.HighEnergy](/verify/taulib/docs/book-v-temporal-high-energy/)
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L217-L226)
- Source range: L217-L226
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R33` — Inflation as Progression

## Immediate Comment / Docstring

```lean
/-- [V.R33] The inflationary epoch corresponds to rapid early progression.

    In the opening regime, H(n) is exponentially large (ι_τ^(-n) with
    small n). This maps to the inflationary epoch in orthodox cosmology:
    - Rapid spatial expansion = rapid refinement progression
    - Sector coupling near-maximal = GUT unification
    - Inflation ends when sectors differentiate = coupling split

    The τ-framework does NOT postulate an inflaton field: inflation
    is simply the high H(n) at early depths of the refinement tower. -/
```

## Source Excerpt

```lean
structure InflationaryInterpretation where
  /-- The opening regime. -/
  regime : OpeningRegime
  /-- Rate at start of regime. -/
  initial_rate : RefinementRate
  /-- Rate at end of regime. -/
  final_rate : RefinementRate
  /-- Rate decreases (early H > late H). -/
  rate_decreases : initial_rate.depth < final_rate.depth
  deriving Repr
```
