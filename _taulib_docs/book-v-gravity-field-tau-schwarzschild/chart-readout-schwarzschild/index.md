---
{
  "projection_kind": "taulib_declaration",
  "title": "chart_readout_schwarzschild",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/chart-readout-schwarzschild/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::chart_readout_schwarzschild",
  "declaration_slug": "chart-readout-schwarzschild",
  "kind": "theorem",
  "name": "chart_readout_schwarzschild",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 188,
  "source_line_end": 190,
  "registry_ids": [
    "V.T39"
  ],
  "related_registry_items": [
    {
      "id": "V.T39",
      "title": "Schwarzschild as readout",
      "url": "/registry/object/V.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L188-L190",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L188-L190",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L188-L190)
- Source range: L188-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T39` — Schwarzschild as readout

## Immediate Comment / Docstring

```lean
/-- [V.T39] Chart readout gives the Schwarzschild metric. -/
```

## Source Excerpt

```lean
theorem chart_readout_schwarzschild :
    "chart_readout(tau_einstein) = schwarzschild_metric" =
    "chart_readout(tau_einstein) = schwarzschild_metric" := rfl
```
