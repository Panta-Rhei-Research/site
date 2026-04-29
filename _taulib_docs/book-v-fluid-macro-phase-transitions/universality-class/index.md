---
{
  "projection_kind": "taulib_declaration",
  "title": "UniversalityClass",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/universality-class/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::UniversalityClass",
  "declaration_slug": "universality-class",
  "kind": "structure",
  "name": "UniversalityClass",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 193,
  "source_line_end": 202,
  "registry_ids": [
    "V.D116"
  ],
  "related_registry_items": [
    {
      "id": "V.D116",
      "title": "Second-order macro transition",
      "url": "/registry/object/V.D116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L193-L202",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
        "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L193-L202",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L193-L202)
- Source range: L193-L202
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D116` — Second-order macro transition

## Immediate Comment / Docstring

```lean
/-- [V.D116] Universality class: systems with the same (d, n) share
    the same critical exponents.

    d = spatial dimension, n = order-parameter dimension.
    Microscopic details are irrelevant. -/
```

## Source Excerpt

```lean
structure UniversalityClass where
  /-- Spatial dimension. -/
  spatial_dim : Nat
  /-- Order-parameter dimension. -/
  op_dim : Nat
  /-- Name of the class. -/
  name : String
  /-- Representative critical exponents. -/
  exponents : CriticalExponentSet
  deriving Repr
```
