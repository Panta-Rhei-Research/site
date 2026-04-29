---
{
  "projection_kind": "taulib_declaration",
  "title": "IonosphericReflection",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/ionospheric-reflection/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::IonosphericReflection",
  "declaration_slug": "ionospheric-reflection",
  "kind": "structure",
  "name": "IonosphericReflection",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 201,
  "source_line_end": 206,
  "registry_ids": [
    "V.R152"
  ],
  "related_registry_items": [
    {
      "id": "V.R152",
      "title": "Ionospheric reflection",
      "url": "/registry/object/V.R152/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L201-L206",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L201-L206",
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
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L201-L206)
- Source range: L201-L206
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R152` — Ionospheric reflection

## Immediate Comment / Docstring

```lean
/-- [V.R152] Ionospheric reflection: Earth's ionosphere reflects radio
    waves below ω_p ~ 2π × 10 MHz as a direct consequence of the
    B-sector cutoff. EM modes below the plasma frequency cannot sustain
    propagating B-sector boundary obstructions. -/
```

## Source Excerpt

```lean
structure IonosphericReflection where
  /-- Ionospheric plasma frequency in MHz (approximate). -/
  plasma_freq_mhz : Nat := 10
  /-- Reflected waves are below cutoff. -/
  is_reflected : Bool := true
  deriving Repr
```
