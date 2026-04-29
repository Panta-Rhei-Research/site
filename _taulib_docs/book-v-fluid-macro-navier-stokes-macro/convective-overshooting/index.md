---
{
  "projection_kind": "taulib_declaration",
  "title": "convective_overshooting",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::convective_overshooting",
  "declaration_slug": "convective-overshooting",
  "kind": "def",
  "name": "convective_overshooting",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 263,
  "source_line_end": 265,
  "registry_ids": [
    "V.R141"
  ],
  "related_registry_items": [
    {
      "id": "V.R141",
      "title": "Convective overshooting",
      "url": "/registry/object/V.R141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L263-L265",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L263-L265",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L263-L265)
- Source range: L263-L265
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R141` — Convective overshooting

## Immediate Comment / Docstring

```lean
/-- [V.R141] Convective overshooting: penetration of convective motions
    into the radiative zone is a bounded violation of the convective-
    radiative inequality, governed by the macro regularity theorem. -/
```

## Source Excerpt

```lean
def convective_overshooting : Prop :=
  ∀ (d : MacroDefectTransport) (bound : Nat),
    d.mobility_n ≤ bound → d.mobility_n ≤ bound
```
