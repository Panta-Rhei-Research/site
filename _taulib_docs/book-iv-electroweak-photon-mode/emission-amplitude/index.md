---
{
  "projection_kind": "taulib_declaration",
  "title": "EmissionAmplitude",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/emission-amplitude/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::EmissionAmplitude",
  "declaration_slug": "emission-amplitude",
  "kind": "structure",
  "name": "EmissionAmplitude",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 281,
  "source_line_end": 286,
  "registry_ids": [
    "IV.P36"
  ],
  "related_registry_items": [
    {
      "id": "IV.P36",
      "title": "Photon Coupling Strength",
      "url": "/registry/object/IV.P36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L281-L286",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L281-L286",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L281-L286)
- Source range: L281-L286
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P36` — Photon Coupling Strength

## Immediate Comment / Docstring

```lean
/-- [IV.P36] Emission/absorption amplitude proportional to √α.
    The coupling constant α = (8/15)·ι_τ⁴ enters as amplitude squared. -/
```

## Source Excerpt

```lean
structure EmissionAmplitude where
  /-- Amplitude squared = α (fine structure constant). -/
  amplitude_sq_numer : Nat
  amplitude_sq_denom : Nat
  denom_pos : amplitude_sq_denom > 0
  deriving Repr
```
