---
{
  "projection_kind": "taulib_declaration",
  "title": "BatchelorKraichnanSpectrum",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/batchelor-kraichnan-spectrum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::BatchelorKraichnanSpectrum",
  "declaration_slug": "batchelor-kraichnan-spectrum",
  "kind": "structure",
  "name": "BatchelorKraichnanSpectrum",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 210,
  "source_line_end": 217,
  "registry_ids": [
    "V.R147"
  ],
  "related_registry_items": [
    {
      "id": "V.R147",
      "title": "Batchelor--Kraichnan spectrum",
      "url": "/registry/object/V.R147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L210-L217",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L210-L217",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L210-L217)
- Source range: L210-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R147` — Batchelor--Kraichnan spectrum

## Immediate Comment / Docstring

```lean
/-- [V.R147] Batchelor-Kraichnan spectrum: the forward enstrophy
    cascade predicts E(k) ∝ η^{2/3} k^{-3} in the enstrophy-cascade
    range, from dimensional analysis on the vorticity budget flux. -/
```

## Source Excerpt

```lean
structure BatchelorKraichnanSpectrum where
  /-- Enstrophy cascade exponent: -3. -/
  exponent : Nat := 3
  /-- Enstrophy flux exponent: 2/3. -/
  flux_numer : Nat := 2
  flux_denom : Nat := 3
  flux_denom_pos : flux_denom > 0 := by omega
  deriving Repr
```
