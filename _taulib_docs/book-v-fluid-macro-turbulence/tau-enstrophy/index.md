---
{
  "projection_kind": "taulib_declaration",
  "title": "TauEnstrophy",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/tau-enstrophy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::TauEnstrophy",
  "declaration_slug": "tau-enstrophy",
  "kind": "structure",
  "name": "TauEnstrophy",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 157,
  "source_line_end": 162,
  "registry_ids": [
    "V.D100"
  ],
  "related_registry_items": [
    {
      "id": "V.D100",
      "title": "tau-enstrophy",
      "url": "/registry/object/V.D100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L157-L162",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L157-L162",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L157-L162)
- Source range: L157-L162
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D100` — tau-enstrophy

## Immediate Comment / Docstring

```lean
/-- [V.D100] Tau-enstrophy: Ω_n = (1/2)(ν_n^macro)², the squared
    vorticity component of the macro defect tuple at primorial level n.

    Governs vorticity budget evolution across the refinement tower. -/
```

## Source Excerpt

```lean
structure TauEnstrophy where
  /-- Vorticity component (squared/2, encoded as Nat). -/
  vorticity_sq_half : Nat
  /-- Primorial level. -/
  level : Nat
  deriving Repr, DecidableEq, BEq
```
