---
{
  "projection_kind": "taulib_declaration",
  "title": "ElectricCharge",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/electric-charge/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::ElectricCharge",
  "declaration_slug": "electric-charge",
  "kind": "structure",
  "name": "ElectricCharge",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 145,
  "source_line_end": 148,
  "registry_ids": [
    "IV.D84"
  ],
  "related_registry_items": [
    {
      "id": "IV.D84",
      "title": "Electric Charge",
      "url": "/registry/object/IV.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L145-L148",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L145-L148",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L145-L148)
- Source range: L145-L148
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D84` — Electric Charge

## Immediate Comment / Docstring

```lean
/-- [IV.D84] Electric charge as winding number of U(1) holonomy.
    Charge is quantized in units of e (from T² compactness).
    The value is an integer: q/e ∈ ℤ. -/
```

## Source Excerpt

```lean
structure ElectricCharge where
  /-- Charge in units of e. -/
  charge_units : Int
  deriving Repr, DecidableEq, BEq
```
