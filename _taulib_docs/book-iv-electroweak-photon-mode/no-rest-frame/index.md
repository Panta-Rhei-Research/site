---
{
  "projection_kind": "taulib_declaration",
  "title": "NoRestFrame",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/no-rest-frame/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::NoRestFrame",
  "declaration_slug": "no-rest-frame",
  "kind": "structure",
  "name": "NoRestFrame",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 232,
  "source_line_end": 235,
  "registry_ids": [
    "IV.P32"
  ],
  "related_registry_items": [
    {
      "id": "IV.P32",
      "title": "No Rest Frame",
      "url": "/registry/object/IV.P32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L232-L235",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L232-L235",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L232-L235)
- Source range: L232-L235
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P32` — No Rest Frame

## Immediate Comment / Docstring

```lean
/-- [IV.P32] Photon has no rest frame: zero mass implies no
    Lorentz frame where momentum vanishes. -/
```

## Source Excerpt

```lean
structure NoRestFrame where
  mass_zero : Bool := true
  no_rest_frame : Bool := true
  deriving Repr
```
