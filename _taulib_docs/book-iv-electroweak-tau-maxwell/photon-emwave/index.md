---
{
  "projection_kind": "taulib_declaration",
  "title": "PhotonEMWave",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/photon-emwave/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::PhotonEMWave",
  "declaration_slug": "photon-emwave",
  "kind": "structure",
  "name": "PhotonEMWave",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 412,
  "source_line_end": 419,
  "registry_ids": [
    "IV.P47"
  ],
  "related_registry_items": [
    {
      "id": "IV.P47",
      "title": "Photon-Wave Identity",
      "url": "/registry/object/IV.P47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L412-L419",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L412-L419",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L412-L419)
- Source range: L412-L419
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P47` — Photon-Wave Identity

## Immediate Comment / Docstring

```lean
/-- [IV.P47] The photon (τ-transport mode) and the EM wave (Maxwell
    solution) are the SAME object at different descriptive levels.
    Photon = quantum level, EM wave = classical limit. -/
```

## Source Excerpt

```lean
structure PhotonEMWave where
  /-- Same object at two levels. -/
  same_object : Bool := true
  /-- Photon = quantum (discrete). -/
  quantum_level : Bool := true
  /-- EM wave = classical (continuous). -/
  classical_level : Bool := true
  deriving Repr
```
