---
{
  "projection_kind": "taulib_declaration",
  "title": "cmb_standard_temperature",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/cmb-standard-temperature/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::cmb_standard_temperature",
  "declaration_slug": "cmb-standard-temperature",
  "kind": "theorem",
  "name": "cmb_standard_temperature",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 203,
  "source_line_end": 204,
  "registry_ids": [
    "V.R47"
  ],
  "related_registry_items": [
    {
      "id": "V.R47",
      "title": "No new information, new interpretation",
      "url": "/registry/object/V.R47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L203-L204",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L203-L204",
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
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L203-L204)
- Source range: L203-L204
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R47` — No new information, new interpretation

## Immediate Comment / Docstring

```lean
/-- [V.R47] CMB data don't change; what changes is the ontological reading.
    The canonical mean temperature is 2725 (representing 2.725 K). -/
```

## Source Excerpt

```lean
theorem cmb_standard_temperature :
    canonical_cmb.mean_temp_numer = 2725 := by rfl
```
