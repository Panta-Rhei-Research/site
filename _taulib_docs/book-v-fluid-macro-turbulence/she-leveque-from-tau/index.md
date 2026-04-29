---
{
  "projection_kind": "taulib_declaration",
  "title": "she_leveque_from_tau",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-from-tau/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::she_leveque_from_tau",
  "declaration_slug": "she-leveque-from-tau",
  "kind": "theorem",
  "name": "she_leveque_from_tau",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 317,
  "source_line_end": 322,
  "registry_ids": [
    "V.T248"
  ],
  "related_registry_items": [
    {
      "id": "V.T248",
      "title": "She-Lévêque from τ³ Dimensions",
      "url": "/registry/object/V.T248/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L317-L322",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L317-L322",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L317-L322)
- Source range: L317-L322
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T248` — She-Lévêque from τ³ Dimensions

## Immediate Comment / Docstring

```lean
/-- [V.T248] She-Leveque formula from τ³ dimensional structure.

    ζ_p = p/9 + 2[1-(2/3)^{p/3}] is exactly derivable from:
    - 1/9 = 1/dim(τ³)²
    - 2 = dim(T²) (fiber dimension)
    - 2/3 = dim(T²)/dim(τ³) (fiber-to-total ratio)
    - p/3 = p/dim(τ³)

    Zero free parameters. -/
```

## Source Excerpt

```lean
theorem she_leveque_from_tau (d : SheLevequeDecomposition)
    (h0 : d.free_params = 0) :
    d.free_params = 0 ∧
    d.linear_denom = d.tau3_dim * d.tau3_dim ∧
    d.nonlinear_prefactor = d.fiber_dim :=
  ⟨h0, d.linear_check, d.prefactor_check⟩
```
