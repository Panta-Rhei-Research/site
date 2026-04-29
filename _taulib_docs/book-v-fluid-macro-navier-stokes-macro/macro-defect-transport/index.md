---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroDefectTransport",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-defect-transport/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::MacroDefectTransport",
  "declaration_slug": "macro-defect-transport",
  "kind": "structure",
  "name": "MacroDefectTransport",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 68,
  "source_line_end": 83,
  "registry_ids": [
    "V.D96"
  ],
  "related_registry_items": [
    {
      "id": "V.D96",
      "title": "Macro defect-transport equation",
      "url": "/registry/object/V.D96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L68-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L68-L83",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L68-L83)
- Source range: L68-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D96` — Macro defect-transport equation

## Immediate Comment / Docstring

```lean
/-- [V.D96] Macro defect-transport equation: base-projected evolution
    of the 4-component defect tuple (μ, ν, κ, θ), where fiber
    contributions from B, C, ω sectors are averaged and enter
    only through cross-couplings. -/
```

## Source Excerpt

```lean
structure MacroDefectTransport where
  /-- Mobility component at primorial level n. -/
  mobility_n : Nat
  /-- Vorticity component at primorial level n. -/
  vorticity_n : Nat
  /-- Compression component at primorial level n. -/
  compression_n : Nat
  /-- Topological component at primorial level n. -/
  topological_n : Nat
  /-- Primorial level index. -/
  level : Nat
  /-- Whether base-projection has been applied. -/
  is_projected : Bool := true
  /-- Whether fiber averaging has been applied. -/
  is_averaged : Bool := true
  deriving Repr, DecidableEq, BEq
```
