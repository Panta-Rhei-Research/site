---
{
  "projection_kind": "taulib_declaration",
  "title": "charge_conservation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/charge-conservation/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::charge_conservation",
  "declaration_slug": "charge-conservation",
  "kind": "theorem",
  "name": "charge_conservation",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 214,
  "source_line_end": 215,
  "registry_ids": [
    "IV.T36"
  ],
  "related_registry_items": [
    {
      "id": "IV.T36",
      "title": "Charge Conservation",
      "url": "/registry/object/IV.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L214-L215",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L214-L215",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L214-L215)
- Source range: L214-L215
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T36` — Charge Conservation

## Immediate Comment / Docstring

```lean
/-- [IV.T36] Total electric charge is conserved: winding numbers
    are additive under composition of holonomy loops. -/
```

## Source Excerpt

```lean
theorem charge_conservation (q₁ q₂ : ElectricCharge) :
    (q₁.add q₂).charge_units = q₁.charge_units + q₂.charge_units := rfl
```
