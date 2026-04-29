---
{
  "projection_kind": "taulib_declaration",
  "title": "PhotonBoundaryChar",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/photon-boundary-char/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::PhotonBoundaryChar",
  "declaration_slug": "photon-boundary-char",
  "kind": "structure",
  "name": "PhotonBoundaryChar",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 266,
  "source_line_end": 270,
  "registry_ids": [
    "IV.P35"
  ],
  "related_registry_items": [
    {
      "id": "IV.P35",
      "title": "Photon as Boundary Character",
      "url": "/registry/object/IV.P35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L266-L270",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L266-L270",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L266-L270)
- Source range: L266-L270
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P35` — Photon as Boundary Character

## Immediate Comment / Docstring

```lean
/-- [IV.P35] Photon as boundary character under the Central Theorem:
    the photon field is the (0,0) character in A_spec(L). -/
```

## Source Excerpt

```lean
structure PhotonBoundaryChar where
  m_index : Int
  n_index : Int
  is_trivial : m_index = 0 ∧ n_index = 0
  deriving Repr
```
