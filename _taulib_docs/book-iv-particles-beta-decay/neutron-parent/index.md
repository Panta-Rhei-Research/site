---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronParent",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/neutron-parent/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::NeutronParent",
  "declaration_slug": "neutron-parent",
  "kind": "structure",
  "name": "NeutronParent",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 57,
  "source_line_end": 66,
  "registry_ids": [
    "IV.R121"
  ],
  "related_registry_items": [
    {
      "id": "IV.R121",
      "title": "Neutron as parent of atomic matter",
      "url": "/registry/object/IV.R121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L57-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L57-L66",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L57-L66)
- Source range: L57-L66
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R121` — Neutron as parent of atomic matter

## Immediate Comment / Docstring

```lean
/-- [IV.R121] In the τ-picture, beta decay is differentiation of the
    calibration anchor into component spectral modes:
    - Proton: weak-polarized neutron (p = n + δ_A)
    - Electron: spectral residual (m_e = m_n/R)
    - Antineutrino: base-mode time-eigenstate

    The neutron is the PARENT of all atomic matter. -/
```

## Source Excerpt

```lean
structure NeutronParent where
  /-- Products of differentiation. -/
  products : List String := ["proton", "electron", "antineutrino"]
  /-- Proton is weak-polarized neutron. -/
  proton_is_polarized : Bool := true
  /-- Electron is spectral residual. -/
  electron_is_residual : Bool := true
  /-- Neutron is ontological parent. -/
  parent : Bool := true
  deriving Repr
```
