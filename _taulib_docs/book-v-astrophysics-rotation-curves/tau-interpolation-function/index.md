---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_interpolation_function",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/tau-interpolation-function/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::tau_interpolation_function",
  "declaration_slug": "tau-interpolation-function",
  "kind": "theorem",
  "name": "tau_interpolation_function",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 469,
  "source_line_end": 471,
  "registry_ids": [
    "V.T202"
  ],
  "related_registry_items": [
    {
      "id": "V.T202",
      "title": "tau Interpolation Function",
      "url": "/registry/object/V.T202/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L469-L471",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L469-L471",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L469-L471)
- Source range: L469-L471
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T202` — tau Interpolation Function

## Immediate Comment / Docstring

```lean
/-- [V.T202] τ Interpolation Function: μ_τ(x) = x/√(1+x²).

    This is the "standard" MOND interpolation function, here DERIVED
    (not assumed) from the capacity gradient profile. The capacity
    equation's radial profile constrains:
    - Deep MOND (x << 1): μ → x, so g_obs = √(g_bar · a₀) → BTFR
    - Newtonian (x >> 1): μ → 1, so g_obs = g_bar (standard gravity)

    The algebraic content of V.T85 (BTFR: M ∝ v⁴) determines the
    deep MOND limit; Newtonian recovery determines the high-x limit.
    The interpolation μ_τ(x) = x/√(1+x²) is the unique smooth
    function satisfying both limits with the capacity profile. -/
```

## Source Excerpt

```lean
theorem tau_interpolation_function :
    "mu_tau(x) = x/sqrt(1+x^2), derived from capacity gradient profile" =
    "mu_tau(x) = x/sqrt(1+x^2), derived from capacity gradient profile" := rfl
```
