---
{
  "projection_kind": "taulib_declaration",
  "title": "DecompactificationBound",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompactification-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::DecompactificationBound",
  "declaration_slug": "decompactification-bound",
  "kind": "structure",
  "name": "DecompactificationBound",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 298,
  "source_line_end": 311,
  "registry_ids": [
    "V.D314"
  ],
  "related_registry_items": [
    {
      "id": "V.D314",
      "title": "Decompactification Bound",
      "url": "/registry/object/V.D314/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L298-L311",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L298-L311",
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
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L298-L311)
- Source range: L298-L311
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D314` — Decompactification Bound

## Immediate Comment / Docstring

```lean
/-- [V.D314] Decompactification bound.

    At primorial depth n, the ABCD regularity bound gives:
    ||u||_∞ ≤ C_n · (ν/L²)^{1 - 1/p_n#}

    where p_n# is the nth primorial. The regularity exponent
    α_n = 1 - 1/p_n# converges super-exponentially to the Leray
    exponent α = 1. -/
```

## Source Excerpt

```lean
structure DecompactificationBound where
  /-- Primorial depth. -/
  depth : Nat
  /-- nth primorial (encoded). -/
  primorial : Nat
  /-- Primorial is positive. -/
  primorial_pos : primorial > 0
  /-- α_n numerator: primorial - 1. -/
  alpha_numer : Nat
  /-- α_n denominator: primorial. -/
  alpha_denom : Nat
  /-- α = (p# - 1) / p#. -/
  alpha_eq : alpha_numer + 1 = alpha_denom
  deriving Repr
```
