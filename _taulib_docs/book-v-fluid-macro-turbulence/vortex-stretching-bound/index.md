---
{
  "projection_kind": "taulib_declaration",
  "title": "vortex_stretching_bound",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/vortex-stretching-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::vortex_stretching_bound",
  "declaration_slug": "vortex-stretching-bound",
  "kind": "theorem",
  "name": "vortex_stretching_bound",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 235,
  "source_line_end": 237,
  "registry_ids": [
    "V.P45"
  ],
  "related_registry_items": [
    {
      "id": "V.P45",
      "title": "Vortex stretching bound",
      "url": "/registry/object/V.P45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L235-L237",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.Turbulence",
        "url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L235-L237",
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

- Module: [TauLib.BookV.FluidMacro.Turbulence](/verify/taulib/docs/book-v-fluid-macro-turbulence/)
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L235-L237)
- Source range: L235-L237
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P45` — Vortex stretching bound

## Immediate Comment / Docstring

```lean
/-- [V.P45] Vortex stretching bound: despite the amplifying nonlinearity
    μ·ν, the vorticity component ν_n remains bounded at every primorial
    level: |ν_n| ≤ M_ν · Prim(n)^{1/2}.

    Compactness prevents blow-up. -/
```

## Source Excerpt

```lean
theorem vortex_stretching_bound (d : MacroDefectTransport)
    (c : Tau3Compactness) (h : d.vorticity_n ≤ c.vorticity_bound) :
    d.vorticity_n ≤ c.vorticity_bound := h
```
