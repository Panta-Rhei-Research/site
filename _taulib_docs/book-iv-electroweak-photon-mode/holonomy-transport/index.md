---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyTransport",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/holonomy-transport/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::HolonomyTransport",
  "declaration_slug": "holonomy-transport",
  "kind": "structure",
  "name": "HolonomyTransport",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 195,
  "source_line_end": 202,
  "registry_ids": [
    "IV.T35"
  ],
  "related_registry_items": [
    {
      "id": "IV.T35",
      "title": "Dissolution of Wave-Particle Duality",
      "url": "/registry/object/IV.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L195-L202",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L195-L202",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L195-L202)
- Source range: L195-L202
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T35` — Dissolution of Wave-Particle Duality

## Immediate Comment / Docstring

```lean
/-- [IV.T35] Photon as holonomy transport mode: the photon IS the
    parallel transport of the U(1) connection. Wave/particle duality
    is structural: wave = boundary character, particle = defect bundle. -/
```

## Source Excerpt

```lean
structure HolonomyTransport where
  /-- The photon mode. -/
  mode : PhotonMode
  /-- Wave aspect = boundary character on L. -/
  wave_is_character : Bool := true
  /-- Particle aspect = defect bundle on T². -/
  particle_is_defect : Bool := true
  deriving Repr
```
