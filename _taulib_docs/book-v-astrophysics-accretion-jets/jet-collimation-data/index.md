---
{
  "projection_kind": "taulib_declaration",
  "title": "JetCollimationData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-collimation-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::JetCollimationData",
  "declaration_slug": "jet-collimation-data",
  "kind": "structure",
  "name": "JetCollimationData",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 188,
  "source_line_end": 199,
  "registry_ids": [
    "V.D131"
  ],
  "related_registry_items": [
    {
      "id": "V.D131",
      "title": "Synchrotron Readout",
      "url": "/registry/object/V.D131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L188-L199",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.AccretionJets",
        "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L188-L199",
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

- Module: [TauLib.BookV.Astrophysics.AccretionJets](/verify/taulib/docs/book-v-astrophysics-accretion-jets/)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L188-L199)
- Source range: L188-L199
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D131` — Synchrotron Readout

## Immediate Comment / Docstring

```lean
/-- [V.D131] Jet collimation data: the opening angle and extent of
    a relativistic jet, determined by the lemniscate boundary
    geometry and the ambient pressure profile. -/
```

## Source Excerpt

```lean
structure JetCollimationData where
  /-- Opening half-angle (degrees × 10). -/
  half_angle : Nat
  /-- Jet extent (kpc, scaled × 10). -/
  extent_kpc : Nat
  /-- Lorentz factor (bulk). -/
  lorentz_factor : Nat
  /-- Lorentz factor at least 1. -/
  lorentz_ge_one : lorentz_factor ≥ 1
  /-- Whether the jet is relativistic (Γ > 2). -/
  is_relativistic : Bool
  deriving Repr
```
