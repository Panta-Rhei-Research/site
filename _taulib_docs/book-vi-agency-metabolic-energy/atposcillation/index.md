---
{
  "projection_kind": "taulib_declaration",
  "title": "ATPOscillation",
  "permalink": "/verify/taulib/docs/book-vi-agency-metabolic-energy/atposcillation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.MetabolicEnergy`.",
  "declaration_id": "TauLib.BookVI.Agency.MetabolicEnergy::ATPOscillation",
  "declaration_slug": "atposcillation",
  "kind": "structure",
  "name": "ATPOscillation",
  "module_name": "TauLib.BookVI.Agency.MetabolicEnergy",
  "module_url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/",
  "source_line_start": 39,
  "source_line_end": 50,
  "registry_ids": [
    "VI.D32"
  ],
  "related_registry_items": [
    {
      "id": "VI.D32",
      "title": "ATP/ADP Oscillation",
      "url": "/registry/object/VI.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L39-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.MetabolicEnergy",
        "url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L39-L50",
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

- Module: [TauLib.BookVI.Agency.MetabolicEnergy](/verify/taulib/docs/book-vi-agency-metabolic-energy/)
- Source path: [`TauLib/BookVI/Agency/MetabolicEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L39-L50)
- Source range: L39-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D32` — ATP/ADP Oscillation

## Immediate Comment / Docstring

```lean
/-- [VI.D32] ATP/ADP Oscillation: discrete energy currency.
    ΔG ≈ 30.5 kJ/mol. Set by Riemann force at E₂
    (Book III, Part III: energy quantization).
    Calibrated by ι_τ (Book I, Part IX). -/
```

## Source Excerpt

```lean
structure ATPOscillation where
  /-- Free energy in kJ/mol (×10 for integer representation). -/
  delta_g_x10 : Nat
  /-- ΔG ≈ 30.5 kJ/mol → 305 in ×10 representation. -/
  delta_g_eq : delta_g_x10 = 305
  /-- Governed by Riemann force (Book III, Part III). -/
  riemann_governed : Bool := true
  /-- Calibrated by ι_τ (Book I, Part IX). -/
  iota_tau_calibrated : Bool := true
  /-- Universal across all terrestrial life. -/
  universal : Bool := true
  deriving Repr
```
