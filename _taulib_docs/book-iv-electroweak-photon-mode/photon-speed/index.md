---
{
  "projection_kind": "taulib_declaration",
  "title": "PhotonSpeed",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/photon-speed/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::PhotonSpeed",
  "declaration_slug": "photon-speed",
  "kind": "structure",
  "name": "PhotonSpeed",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 178,
  "source_line_end": 182,
  "registry_ids": [
    "IV.T34"
  ],
  "related_registry_items": [
    {
      "id": "IV.T34",
      "title": "Photon Propagation Speed",
      "url": "/registry/object/IV.T34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L178-L182",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L178-L182",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L178-L182)
- Source range: L178-L182
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T34` — Photon Propagation Speed

## Immediate Comment / Docstring

```lean
/-- [IV.T34] Photon propagates at limiting speed c.
    Zero mass implies zero fiber obstruction implies base-only
    propagation at c. -/
```

## Source Excerpt

```lean
structure PhotonSpeed where
  mass_zero : Bool := true
  speed_is_c : Bool := true
  fiber_obstruction_zero : Bool := true
  deriving Repr
```
