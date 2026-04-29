---
{
  "projection_kind": "taulib_declaration",
  "title": "kolmogorov_53_from_tau",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-53-from-tau/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::kolmogorov_53_from_tau",
  "declaration_slug": "kolmogorov-53-from-tau",
  "kind": "theorem",
  "name": "kolmogorov_53_from_tau",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 410,
  "source_line_end": 414,
  "registry_ids": [
    "V.T250"
  ],
  "related_registry_items": [
    {
      "id": "V.T250",
      "title": "-5/3 from τ Dimensions",
      "url": "/registry/object/V.T250/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L410-L414",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L410-L414",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L410-L414)
- Source range: L410-L414
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T250` — -5/3 from τ Dimensions

## Immediate Comment / Docstring

```lean
/-- [V.T250] The -5/3 exponent from τ dimensions.

    The energy spectrum exponent -5/3 arises because the cascade
    operates on dim(τ³) = 3 spatial dimensions while dissipating
    through |gen| + dim(T²) = 3 + 2 = 5 channels. -/
```

## Source Excerpt

```lean
theorem kolmogorov_53_from_tau :
    kolmogorov_decomposition.numer = kolmogorov_decomposition.n_gen + kolmogorov_decomposition.fiber_dim ∧
    kolmogorov_decomposition.denom = kolmogorov_decomposition.tau3_dim ∧
    kolmogorov_decomposition.free_params = 0 := by
  exact ⟨by native_decide, by native_decide, by native_decide⟩
```
