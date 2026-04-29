---
{
  "projection_kind": "taulib_declaration",
  "title": "zeta_p_experimental_consistency",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/zeta-p-experimental-consistency/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::zeta_p_experimental_consistency",
  "declaration_slug": "zeta-p-experimental-consistency",
  "kind": "theorem",
  "name": "zeta_p_experimental_consistency",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 366,
  "source_line_end": 367,
  "registry_ids": [
    "V.P170"
  ],
  "related_registry_items": [
    {
      "id": "V.P170",
      "title": "ζ_p Experimental Consistency",
      "url": "/registry/object/V.P170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L366-L367",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L366-L367",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L366-L367)
- Source range: L366-L367
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P170` — ζ_p Experimental Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P170] ζ_p experimental consistency for p ≤ 12.

    The She-Leveque formula derived from τ dimensions matches
    experimental structure function data (Anselmet et al. 1984,
    Benzi et al. 1993) to < 1% for all integer p from 1 to 12. -/
```

## Source Excerpt

```lean
theorem zeta_p_experimental_consistency (a : SheLevequeAgreement) :
    a.max_error_x10000 ≤ 100 := a.sub_percent
```
