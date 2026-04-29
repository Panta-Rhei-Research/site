---
{
  "projection_kind": "taulib_declaration",
  "title": "charge_quantized",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/charge-quantized/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::charge_quantized",
  "declaration_slug": "charge-quantized",
  "kind": "theorem",
  "name": "charge_quantized",
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 223,
  "source_line_end": 224,
  "registry_ids": [
    "IV.T120"
  ],
  "related_registry_items": [
    {
      "id": "IV.T120",
      "title": "Charge quantization",
      "url": "/registry/object/IV.T120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L223-L224",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L223-L224",
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L223-L224)
- Source range: L223-L224
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T120` — Charge quantization

## Immediate Comment / Docstring

```lean
/-- [IV.T120] Electric charge is quantized in units of e.
    From compactness of T²: holonomy exp(i·2π·n) requires n ∈ ℤ. -/
```

## Source Excerpt

```lean
theorem charge_quantized (q : ElectricCharge) :
    ∃ n : Int, q.charge_units = n := ⟨q.charge_units, rfl⟩
```
