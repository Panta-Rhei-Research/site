---
{
  "projection_kind": "taulib_declaration",
  "title": "PhotonMode",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/photon-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::PhotonMode",
  "declaration_slug": "photon-mode",
  "kind": "structure",
  "name": "PhotonMode",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 62,
  "source_line_end": 84,
  "registry_ids": [
    "IV.D82"
  ],
  "related_registry_items": [
    {
      "id": "IV.D82",
      "title": "Photon Mode",
      "url": "/registry/object/IV.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L62-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.PhotonMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L62-L84",
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

- Module: [TauLib.BookIV.Electroweak.PhotonMode](/verify/taulib/docs/book-iv-electroweak-photon-mode/)
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L62-L84)
- Source range: L62-L84
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D82` — Photon Mode

## Immediate Comment / Docstring

```lean
/-- [IV.D82] The photon as B-sector transport mode with degenerate
    fiber character (m,n) = (0,0). The unique massless EM mode. -/
```

## Source Excerpt

```lean
structure PhotonMode where
  /-- The sector: must be B (EM). -/
  sector : Sector
  sector_eq : sector = .B
  /-- The generator: must be γ. -/
  generator : Generator
  gen_eq : generator = .gamma
  /-- Fiber character m-index = 0 (degenerate). -/
  m_index : Int
  m_zero : m_index = 0
  /-- Fiber character n-index = 0 (degenerate). -/
  n_index : Int
  n_zero : n_index = 0
  /-- Mass = 0 (from constant character in ker(Δ_Hodge)). -/
  mass_numer : Nat
  mass_zero : mass_numer = 0
  /-- Spin quantum number (s = 1). -/
  spin : Nat
  spin_eq : spin = 1
  /-- Number of polarization states. -/
  polarizations : Nat
  pol_eq : polarizations = 2
  deriving Repr
```
