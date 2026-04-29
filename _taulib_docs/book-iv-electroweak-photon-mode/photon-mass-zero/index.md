---
{
  "projection_kind": "taulib_declaration",
  "title": "photon_mass_zero",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/photon-mass-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::photon_mass_zero",
  "declaration_slug": "photon-mass-zero",
  "kind": "theorem",
  "name": "photon_mass_zero",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 169,
  "source_line_end": 169,
  "registry_ids": [
    "IV.T33"
  ],
  "related_registry_items": [
    {
      "id": "IV.T33",
      "title": "Photon Masslessness",
      "url": "/registry/object/IV.T33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L169-L169",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L169-L169",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L169-L169)
- Source range: L169-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T33` — Photon Masslessness

## Immediate Comment / Docstring

```lean
/-- [IV.T33] Photon mass is exactly zero: constant fiber character
    (0,0) lies in ker(Δ_Hodge), so no mass eigenvalue arises. -/
```

## Source Excerpt

```lean
theorem photon_mass_zero : photon.mass_numer = 0 := rfl
```
