---
{
  "projection_kind": "taulib_declaration",
  "title": "cnub_mass_constraint",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/cnub-mass-constraint/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::cnub_mass_constraint",
  "declaration_slug": "cnub-mass-constraint",
  "kind": "theorem",
  "name": "cnub_mass_constraint",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 225,
  "source_line_end": 227,
  "registry_ids": [
    "V.P09"
  ],
  "related_registry_items": [
    {
      "id": "V.P09",
      "title": "CnuB mass constraint",
      "url": "/registry/object/V.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L225-L227",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L225-L227",
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
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L225-L227)
- Source range: L225-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P09` — CnuB mass constraint

## Immediate Comment / Docstring

```lean
/-- [V.P09] CnuB constrains total neutrino mass:
    sum m_nu ~ 58 meV (from m_nu ~ m_e * iota_tau^15), consistent with
    cosmological bounds (< 120 meV). -/
```

## Source Excerpt

```lean
theorem cnub_mass_constraint :
    canonical_cnub.total_mass_meV < 120 := by
  simp [canonical_cnub]
```
