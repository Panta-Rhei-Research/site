---
{
  "projection_kind": "taulib_declaration",
  "title": "MagnetoacousticMode",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::MagnetoacousticMode",
  "declaration_slug": "magnetoacoustic-mode",
  "kind": "structure",
  "name": "MagnetoacousticMode",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 149,
  "source_line_end": 168,
  "registry_ids": [
    "V.D112"
  ],
  "related_registry_items": [
    {
      "id": "V.D112",
      "title": "Alfv'en orbit",
      "url": "/registry/object/V.D112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L149-L168",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L149-L168",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L149-L168)
- Source range: L149-L168
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D112` — Alfv'en orbit

## Immediate Comment / Docstring

```lean
/-- [V.D112] Magnetoacoustic mode: compressional MHD wave involving
    both magnetic pressure and gas pressure.

    Fast mode: compressions of B and ρ are in phase
    Slow mode: compressions of B and ρ are out of phase -/
```

## Source Excerpt

```lean
structure MagnetoacousticMode where
  /-- Whether fast or slow. -/
  is_fast : Bool
  /-- Sound speed numerator (scaled). -/
  sound_speed_numer : Nat
  /-- Sound speed denominator. -/
  sound_speed_denom : Nat
  /-- Denominator positive. -/
  sound_denom_pos : sound_speed_denom > 0
  /-- Alfven speed numerator (scaled). -/
  alfven_speed_numer : Nat
  /-- Alfven speed denominator. -/
  alfven_speed_denom : Nat
  /-- Denominator positive. -/
  alfven_denom_pos : alfven_speed_denom > 0
  /-- In-phase (fast) or out-of-phase (slow). -/
  compressions_in_phase : Bool
  /-- Phase matches fast/slow classification. -/
  phase_correct : compressions_in_phase = is_fast
  deriving Repr
```
