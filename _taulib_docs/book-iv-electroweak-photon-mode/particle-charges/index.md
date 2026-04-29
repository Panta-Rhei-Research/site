---
{
  "projection_kind": "taulib_declaration",
  "title": "particle_charges",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/particle-charges/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::particle_charges",
  "declaration_slug": "particle-charges",
  "kind": "theorem",
  "name": "particle_charges",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 254,
  "source_line_end": 258,
  "registry_ids": [
    "IV.P34"
  ],
  "related_registry_items": [
    {
      "id": "IV.P34",
      "title": "Charge of Fundamental Modes",
      "url": "/registry/object/IV.P34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L254-L258",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L254-L258",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L254-L258)
- Source range: L254-L258
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P34` — Charge of Fundamental Modes

## Immediate Comment / Docstring

```lean
/-- [IV.P34] Electron charge -e, proton +e, neutron 0. -/
```

## Source Excerpt

```lean
theorem particle_charges :
    charge_electron.charge_units = -1 ∧
    charge_proton.charge_units = 1 ∧
    charge_neutron.charge_units = 0 :=
  ⟨rfl, rfl, rfl⟩
```
