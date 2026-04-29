---
{
  "projection_kind": "taulib_declaration",
  "title": "PlasmaOscillation",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-oscillation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::PlasmaOscillation",
  "declaration_slug": "plasma-oscillation",
  "kind": "structure",
  "name": "PlasmaOscillation",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 146,
  "source_line_end": 153,
  "registry_ids": [
    "V.P46"
  ],
  "related_registry_items": [
    {
      "id": "V.P46",
      "title": "Plasma oscillations",
      "url": "/registry/object/V.P46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L146-L153",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauPlasma",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L146-L153",
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

- Module: [TauLib.BookV.FluidMacro.TauPlasma](/verify/taulib/docs/book-v-fluid-macro-tau-plasma/)
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L146-L153)
- Source range: L146-L153
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P46` — Plasma oscillations

## Immediate Comment / Docstring

```lean
/-- [V.P46] Plasma oscillations: a small charge perturbation oscillates
    at the plasma frequency ω_p.

    The oscillations are longitudinal (compression-rarefaction in electron
    density) and do not propagate below ω_p. -/
```

## Source Excerpt

```lean
structure PlasmaOscillation where
  /-- The plasma frequency. -/
  frequency : PlasmaFrequency
  /-- Oscillations are longitudinal. -/
  is_longitudinal : Bool := true
  /-- No propagation below ω_p. -/
  cutoff_below : Bool := true
  deriving Repr
```
