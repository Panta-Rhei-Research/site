---
{
  "projection_kind": "taulib_declaration",
  "title": "macro_tau_ns_regularity",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-ns-regularity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::macro_tau_ns_regularity",
  "declaration_slug": "macro-tau-ns-regularity",
  "kind": "theorem",
  "name": "macro_tau_ns_regularity",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 189,
  "source_line_end": 195,
  "registry_ids": [
    "V.T71"
  ],
  "related_registry_items": [
    {
      "id": "V.T71",
      "title": "Macro tau-NS regularity",
      "url": "/registry/object/V.T71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L189-L195",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L189-L195",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L189-L195)
- Source range: L189-L195
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T71` — Macro tau-NS regularity

## Immediate Comment / Docstring

```lean
/-- [V.T71] Macro tau-NS regularity: for every τ-admissible initial datum
    on τ³, the macro tau-NS evolution produces a bounded velocity readout
    at every base point and fiber point.

    No macro-scale singularity forms. Follows from three-condition
    sufficiency and compactness. -/
```

## Source Excerpt

```lean
theorem macro_tau_ns_regularity (flow : MacroTauNSFlow) (c : Tau3Compactness)
    (conds : MacroThreeConditions)
    (_h1 : conds.c1_clopen_locality = true)
    (_h2 : conds.c2_bounded_extraction = true)
    (_h3 : conds.c3_defect_contractivity = true)
    (hbd : flow.initial.mobility_n ≤ c.mobility_bound) :
    flow.initial.mobility_n ≤ c.mobility_bound := hbd
```
