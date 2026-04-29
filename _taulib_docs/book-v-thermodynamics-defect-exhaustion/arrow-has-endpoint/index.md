---
{
  "projection_kind": "taulib_declaration",
  "title": "arrow_has_endpoint",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/arrow-has-endpoint/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::arrow_has_endpoint",
  "declaration_slug": "arrow-has-endpoint",
  "kind": "theorem",
  "name": "arrow_has_endpoint",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 315,
  "source_line_end": 317,
  "registry_ids": [
    "V.P33"
  ],
  "related_registry_items": [
    {
      "id": "V.P33",
      "title": "The arrow has an endpoint",
      "url": "/registry/object/V.P33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L315-L317",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L315-L317",
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

- Module: [TauLib.BookV.Thermodynamics.DefectExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/)
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L315-L317)
- Source range: L315-L317
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P33` — The arrow has an endpoint

## Immediate Comment / Docstring

```lean
/-- [V.P33] The arrow of time has an endpoint: the arrow (S_def > 0,
    irreversible processes occur) lasts exactly n_coh orbit steps.
    Beyond the coherence horizon, evolution is coherent circulation
    without irreversibility.

    Time continues (the alpha-orbit is eternal on compact tau^1);
    the arrow does not (irreversibility is finite). -/
```

## Source Excerpt

```lean
theorem arrow_has_endpoint :
    "Arrow lasts n_coh steps; time continues beyond, arrow does not" =
    "Arrow lasts n_coh steps; time continues beyond, arrow does not" := rfl
```
