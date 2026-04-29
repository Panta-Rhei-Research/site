---
{
  "projection_kind": "taulib_declaration",
  "title": "total_proper_time_bounded",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/total-proper-time-bounded/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::total_proper_time_bounded",
  "declaration_slug": "total-proper-time-bounded",
  "kind": "theorem",
  "name": "total_proper_time_bounded",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 265,
  "source_line_end": 272,
  "registry_ids": [
    "V.T10"
  ],
  "related_registry_items": [
    {
      "id": "V.T10",
      "title": "Bounded Time Theorem",
      "url": "/registry/object/V.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L265-L272",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L265-L272",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L265-L272)
- Source range: L265-L272
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T10` — Bounded Time Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T10] Total proper time t_∞ is finite.

    The proper time series is a geometric sum:
    t_∞ = Σ_{n≥1} ι_τ^n = ι_τ/(1−ι_τ) < ∞

    Since ι_τ ≈ 0.341304 < 1, the series converges.
    Limit = ι_τ/(1−ι_τ) ≈ 0.518441.

    We prove the bound: iota < iotaD (i.e. ι_τ < 1), which is
    the convergence condition for the geometric series. -/
```

## Source Excerpt

```lean
theorem total_proper_time_bounded :
    -- ι_τ < 1 (convergence condition)
    iota < iotaD ∧
    -- ι_τ/(1−ι_τ) numerator < denominator (total < 1)
    iota < iotaD - iota := by
  constructor
  · simp [iota, iotaD, iota_tau_numer, iota_tau_denom]
  · simp [iota, iotaD, iota_tau_numer, iota_tau_denom]
```
