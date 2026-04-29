---
{
  "projection_kind": "taulib_declaration",
  "title": "U1Holonomy",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/u1-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::U1Holonomy",
  "declaration_slug": "u1-holonomy",
  "kind": "structure",
  "name": "U1Holonomy",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 110,
  "source_line_end": 118,
  "registry_ids": [
    "IV.D83"
  ],
  "related_registry_items": [
    {
      "id": "IV.D83",
      "title": "U(1) Holonomy on T^2",
      "url": "/registry/object/IV.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L110-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L110-L118",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L110-L118)
- Source range: L110-L118
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D83` — U(1) Holonomy on T^2

## Immediate Comment / Docstring

```lean
/-- [IV.D83] U(1) holonomy of the B-sector connection around a closed
    loop on T². The holonomy is exp(i·2π·(flux/Φ₀)) where flux is
    the EM flux through the loop and Φ₀ is the flux quantum. -/
```

## Source Excerpt

```lean
structure U1Holonomy where
  /-- Sector (must be B). -/
  sector : Sector
  sector_eq : sector = .B
  /-- Winding number (integer from compactness of T²). -/
  winding : Int
  /-- Phase is 2π times winding number (modulo 2π). -/
  phase_is_periodic : Bool := true
  deriving Repr
```
