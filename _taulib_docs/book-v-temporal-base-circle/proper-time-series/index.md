---
{
  "projection_kind": "taulib_declaration",
  "title": "ProperTimeSeries",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/proper-time-series/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::ProperTimeSeries",
  "declaration_slug": "proper-time-series",
  "kind": "structure",
  "name": "ProperTimeSeries",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 135,
  "source_line_end": 146,
  "registry_ids": [
    "V.D17"
  ],
  "related_registry_items": [
    {
      "id": "V.D17",
      "title": "Proper Time (Arc Length)",
      "url": "/registry/object/V.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L135-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BaseCircle",
        "url": "/verify/taulib/docs/book-v-temporal-base-circle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L135-L146",
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

- Module: [TauLib.BookV.Temporal.BaseCircle](/verify/taulib/docs/book-v-temporal-base-circle/)
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L135-L146)
- Source range: L135-L146
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D17` — Proper Time (Arc Length)

## Immediate Comment / Docstring

```lean
/-- [V.D17] Proper time series: accumulated arc length along the α-orbit.

    Each tick contributes a decrement proportional to the depth:
    the deeper the tick, the shorter the time increment. At the
    rational-approximation level, tick n contributes ι_τ^n.

    The total proper time is finite: Σ ι_τ^n = ι_τ/(1−ι_τ) < ∞.

    We store the accumulated time as a Nat pair (numer, denom). -/
```

## Source Excerpt

```lean
structure ProperTimeSeries where
  /-- Current depth (how many ticks accumulated). -/
  depth : Nat
  /-- Depth is positive (at least one tick). -/
  depth_pos : depth > 0
  /-- Accumulated proper time numerator. -/
  time_numer : Nat
  /-- Accumulated proper time denominator. -/
  time_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : time_denom > 0
  deriving Repr
```
