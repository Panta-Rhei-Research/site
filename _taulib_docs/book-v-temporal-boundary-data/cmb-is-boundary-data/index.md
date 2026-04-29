---
{
  "projection_kind": "taulib_declaration",
  "title": "cmb_is_boundary_data",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/cmb-is-boundary-data/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::cmb_is_boundary_data",
  "declaration_slug": "cmb-is-boundary-data",
  "kind": "theorem",
  "name": "cmb_is_boundary_data",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 198,
  "source_line_end": 199,
  "registry_ids": [
    "V.P07"
  ],
  "related_registry_items": [
    {
      "id": "V.P07",
      "title": "CMB multipoles as boundary characters",
      "url": "/registry/object/V.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L198-L199",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L198-L199",
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
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L198-L199)
- Source range: L198-L199
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P07` — CMB multipoles as boundary characters

## Immediate Comment / Docstring

```lean
/-- [V.P07] CMB multipoles are boundary data: the CMBSurface structure
    carries a positive multipole count, confirming the angular character
    decomposition contains information. -/
```

## Source Excerpt

```lean
theorem cmb_is_boundary_data (s : CMBSurface) :
    s.multipole_count > 0 := s.has_modes
```
