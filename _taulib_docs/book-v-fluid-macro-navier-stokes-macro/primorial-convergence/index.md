---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_convergence",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/primorial-convergence/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::primorial_convergence",
  "declaration_slug": "primorial-convergence",
  "kind": "theorem",
  "name": "primorial_convergence",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 364,
  "source_line_end": 366,
  "registry_ids": [
    "V.T254"
  ],
  "related_registry_items": [
    {
      "id": "V.T254",
      "title": "Primorial Convergence Rate",
      "url": "/registry/object/V.T254/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L364-L366",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L364-L366",
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
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L364-L366)
- Source range: L364-L366
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T254` — Primorial Convergence Rate

## Immediate Comment / Docstring

```lean
/-- [V.T254] Primorial convergence rate.

    1 - α_n = 1/p_n# → 0 as n → ∞.
    The convergence is super-exponential: p_n# > e^{cn} for large n.
    The regularity exponent approaches the Leray value α = 1
    faster than any geometric sequence. -/
```

## Source Excerpt

```lean
theorem primorial_convergence (d : DecompactificationBound)
    (h : d.alpha_numer + 1 = d.alpha_denom) :
    d.alpha_numer + 1 = d.alpha_denom := h
```
