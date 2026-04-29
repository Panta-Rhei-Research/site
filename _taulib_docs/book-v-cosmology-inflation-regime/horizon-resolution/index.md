---
{
  "projection_kind": "taulib_declaration",
  "title": "horizon_resolution",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/horizon-resolution/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::horizon_resolution",
  "declaration_slug": "horizon-resolution",
  "kind": "theorem",
  "name": "horizon_resolution",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 203,
  "source_line_end": 205,
  "registry_ids": [
    "V.P91"
  ],
  "related_registry_items": [
    {
      "id": "V.P91",
      "title": "Horizon Resolution",
      "url": "/registry/object/V.P91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L203-L205",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L203-L205",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L203-L205)
- Source range: L203-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P91` — Horizon Resolution

## Immediate Comment / Docstring

```lean
/-- [V.P91] Horizon resolution: the horizon problem does not arise
    in τ because the base circle τ¹ is compact.

    All points on τ¹ are at finite distance from α₁. There is no
    horizon — the entire τ¹ is always in causal contact. The CMB
    uniformity is expected, not surprising. -/
```

## Source Excerpt

```lean
theorem horizon_resolution :
    "tau^1 compact => no horizon problem, all points in causal contact" =
    "tau^1 compact => no horizon problem, all points in causal contact" := rfl
```
