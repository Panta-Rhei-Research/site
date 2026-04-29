---
{
  "projection_kind": "taulib_declaration",
  "title": "KolmogorovConstant",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::KolmogorovConstant",
  "declaration_slug": "kolmogorov-constant",
  "kind": "structure",
  "name": "KolmogorovConstant",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 137,
  "source_line_end": 142,
  "registry_ids": [
    "V.R146"
  ],
  "related_registry_items": [
    {
      "id": "V.R146",
      "title": "The Kolmogorov constant C_K",
      "url": "/registry/object/V.R146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L137-L142",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L137-L142",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L137-L142)
- Source range: L137-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R146` — The Kolmogorov constant C_K

## Immediate Comment / Docstring

```lean
/-- [V.R146] The Kolmogorov constant C_K ≈ 1.5-1.7, determined by
    defect-tuple geometry of the 4-component budget space (μ, ν, κ, θ).

    Encoded as range: 15/10 ≤ C_K ≤ 17/10. -/
```

## Source Excerpt

```lean
structure KolmogorovConstant where
  /-- C_K numerator (scaled by 10). -/
  ck_scaled : Nat
  /-- In range [15, 17] (i.e. C_K ∈ [1.5, 1.7]). -/
  in_range : 15 ≤ ck_scaled ∧ ck_scaled ≤ 17
  deriving Repr
```
