---
{
  "projection_kind": "taulib_declaration",
  "title": "no_temporal_blowup",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/no-temporal-blowup/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::no_temporal_blowup",
  "declaration_slug": "no-temporal-blowup",
  "kind": "theorem",
  "name": "no_temporal_blowup",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 205,
  "source_line_end": 209,
  "registry_ids": [
    "V.C09"
  ],
  "related_registry_items": [
    {
      "id": "V.C09",
      "title": "No temporal blow-up",
      "url": "/registry/object/V.C09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L205-L209",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L205-L209",
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
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L205-L209)
- Source range: L205-L209
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C09` — No temporal blow-up

## Immediate Comment / Docstring

```lean
/-- [V.C09] No temporal blow-up: the macro tau-NS evolution admits no
    temporal blow-up; the velocity readout is bounded at every point of
    the base τ¹. Follows from compactness and defect-horizon contractivity
    in the primorial (temporal) direction. -/
```

## Source Excerpt

```lean
theorem no_temporal_blowup (flow : MacroTauNSFlow) (c : Tau3Compactness)
    (hbd : flow.initial.totalBudget ≤ c.mobility_bound + c.vorticity_bound +
      c.compression_bound + c.topological_bound) :
    flow.initial.totalBudget ≤ c.mobility_bound + c.vorticity_bound +
      c.compression_bound + c.topological_bound := hbd
```
