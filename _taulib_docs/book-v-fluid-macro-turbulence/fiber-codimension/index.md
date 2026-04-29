---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberCodimension",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/fiber-codimension/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::FiberCodimension",
  "declaration_slug": "fiber-codimension",
  "kind": "structure",
  "name": "FiberCodimension",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 248,
  "source_line_end": 257,
  "registry_ids": [
    "V.D308"
  ],
  "related_registry_items": [
    {
      "id": "V.D308",
      "title": "Fiber Co-dimension of Dissipative Structures",
      "url": "/registry/object/V.D308/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L248-L257",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L248-L257",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L248-L257)
- Source range: L248-L257
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D308` — Fiber Co-dimension of Dissipative Structures

## Immediate Comment / Docstring

```lean
/-- [V.D308] Fiber co-dimension of dissipative structures.

    The most intense dissipative structures (vortex filaments) have
    co-dimension C₀ = dim(T²) = 2 in the fibered product τ³.
    They are loci where the fiber T² degenerates. -/
```

## Source Excerpt

```lean
structure FiberCodimension where
  /-- Total dimension of τ³. -/
  tau3_dim : Nat := 3
  /-- Fiber dimension (T²). -/
  fiber_dim : Nat := 2
  /-- Co-dimension = fiber dimension. -/
  codim : Nat := 2
  /-- Co-dimension equals fiber dimension. -/
  codim_eq : codim = fiber_dim := by omega
  deriving Repr
```
