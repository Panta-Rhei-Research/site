---
{
  "projection_kind": "taulib_declaration",
  "title": "photon_spin",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/photon-spin/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::photon_spin",
  "declaration_slug": "photon-spin",
  "kind": "theorem",
  "name": "photon_spin",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 246,
  "source_line_end": 247,
  "registry_ids": [
    "IV.P33"
  ],
  "related_registry_items": [
    {
      "id": "IV.P33",
      "title": "Photon Spin and Polarization",
      "url": "/registry/object/IV.P33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L246-L247",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.PhotonMode",
        "url": "/corpus/taulib/docs/book-iv-electroweak-photon-mode/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L246-L247",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Electroweak.PhotonMode](/corpus/taulib/docs/book-iv-electroweak-photon-mode/)
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L246-L247)
- Source range: L246-L247
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P33` — Photon Spin and Polarization

## Immediate Comment / Docstring

```lean
/-- [IV.P33] Photon has spin s=1, with exactly 2 polarization
    states (not 2s+1=3) due to masslessness removing longitudinal. -/
```

## Source Excerpt

```lean
theorem photon_spin : photon.spin = 1 ∧ photon.polarizations = 2 :=
  ⟨rfl, rfl⟩
```
