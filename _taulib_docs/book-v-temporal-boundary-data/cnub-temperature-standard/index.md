---
{
  "projection_kind": "taulib_declaration",
  "title": "cnub_temperature_standard",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/cnub-temperature-standard/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::cnub_temperature_standard",
  "declaration_slug": "cnub-temperature-standard",
  "kind": "theorem",
  "name": "cnub_temperature_standard",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 213,
  "source_line_end": 216,
  "registry_ids": [
    "V.R48"
  ],
  "related_registry_items": [
    {
      "id": "V.R48",
      "title": "No new prediction for T_mathrmC",
      "url": "/registry/object/V.R48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L213-L216",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BoundaryData",
        "url": "/verify/taulib/docs/book-v-temporal-boundary-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L213-L216",
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

- Module: [TauLib.BookV.Temporal.BoundaryData](/verify/taulib/docs/book-v-temporal-boundary-data/)
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L213-L216)
- Source range: L213-L216
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R48` — No new prediction for T_mathrmC

## Immediate Comment / Docstring

```lean
/-- [V.R48] tau-framework predicts standard CnuB temperature T ~ 1.95 K. -/
```

## Source Excerpt

```lean
theorem cnub_temperature_standard :
    canonical_cnub.temp_numer = 1950 ∧
    canonical_cnub.temp_denom = 1000 := by
  exact ⟨rfl, rfl⟩
```
