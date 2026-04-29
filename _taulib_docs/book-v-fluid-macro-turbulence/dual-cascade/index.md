---
{
  "projection_kind": "taulib_declaration",
  "title": "DualCascade",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/dual-cascade/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::DualCascade",
  "declaration_slug": "dual-cascade",
  "kind": "structure",
  "name": "DualCascade",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 185,
  "source_line_end": 192,
  "registry_ids": [
    "V.P44"
  ],
  "related_registry_items": [
    {
      "id": "V.P44",
      "title": "Dual cascade decomposition",
      "url": "/registry/object/V.P44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L185-L192",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L185-L192",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L185-L192)
- Source range: L185-L192
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P44` — Dual cascade decomposition

## Immediate Comment / Docstring

```lean
/-- [V.P44] Dual cascade decomposition (2D):
    - Inverse energy cascade: μ² from high to low levels
    - Forward enstrophy cascade: ν² from low to high levels
    K5 sector isolation prevents μ-ν cross-transfer. -/
```

## Source Excerpt

```lean
structure DualCascade where
  /-- Energy cascade direction. -/
  energy_direction : CascadeDirection := .Inverse
  /-- Enstrophy cascade direction. -/
  enstrophy_direction : CascadeDirection := .Forward
  /-- No μ-ν cross-transfer in inertial range. -/
  no_cross_transfer : Bool := true
  deriving Repr
```
