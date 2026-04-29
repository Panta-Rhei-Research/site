---
{
  "projection_kind": "taulib_declaration",
  "title": "BreathingSpectrum",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::BreathingSpectrum",
  "declaration_slug": "breathing-spectrum",
  "kind": "structure",
  "name": "BreathingSpectrum",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 81,
  "source_line_end": 87,
  "registry_ids": [
    "IV.P171"
  ],
  "related_registry_items": [
    {
      "id": "IV.P171",
      "title": "Breathing spectrum",
      "url": "/registry/object/IV.P171/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L81-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.BreathingModes",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L81-L87",
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

- Module: [TauLib.BookIV.MassDerivation.BreathingModes](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/)
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L81-L87)
- Source range: L81-L87
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P171` — Breathing spectrum

## Immediate Comment / Docstring

```lean
/-- [IV.P171] Breathing spectrum on T²: discrete positive eigenvalues. -/
```

## Source Excerpt

```lean
structure BreathingSpectrum where
  is_discrete : Bool := true
  all_positive : Bool := true
  shape_numer : Nat
  shape_denom : Nat
  denom_pos : shape_denom > 0
  deriving Repr
```
