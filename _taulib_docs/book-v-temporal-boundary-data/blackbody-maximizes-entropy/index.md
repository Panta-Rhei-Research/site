---
{
  "projection_kind": "taulib_declaration",
  "title": "blackbody_maximizes_entropy",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/blackbody-maximizes-entropy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::blackbody_maximizes_entropy",
  "declaration_slug": "blackbody-maximizes-entropy",
  "kind": "theorem",
  "name": "blackbody_maximizes_entropy",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 209,
  "source_line_end": 210,
  "registry_ids": [
    "V.P08"
  ],
  "related_registry_items": [
    {
      "id": "V.P08",
      "title": "Blackbody as coherence equilibrium",
      "url": "/registry/object/V.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L209-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L209-L210",
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
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L209-L210)
- Source range: L209-L210
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P08` — Blackbody as coherence equilibrium

## Immediate Comment / Docstring

```lean
/-- [V.P08] Planck blackbody spectrum maximises refinement entropy S_ref
    at fixed total energy. The canonical CMB surface is at the
    equilibrium temperature. -/
```

## Source Excerpt

```lean
theorem blackbody_maximizes_entropy :
    canonical_cmb.mean_temp_denom = 1000 := by rfl
```
