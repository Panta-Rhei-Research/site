---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L320",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-photon-mode/eval-l320/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Electroweak.PhotonMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.PhotonMode::#eval:320",
  "declaration_slug": "eval-l320",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Electroweak.PhotonMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-photon-mode/",
  "source_line_start": 320,
  "source_line_end": 320,
  "registry_ids": [
    "IV.R347",
    "IV.R348",
    "IV.R349",
    "IV.R350",
    "IV.R351"
  ],
  "related_registry_items": [
    {
      "id": "IV.R347",
      "title": "Masslessness is geometric, not postulated",
      "url": "/registry/object/IV.R347/"
    },
    {
      "id": "IV.R348",
      "title": "Experimental limits on photon mass",
      "url": "/registry/object/IV.R348/"
    },
    {
      "id": "IV.R349",
      "title": "The Planck--Einstein relation in tau^3",
      "url": "/registry/object/IV.R349/"
    },
    {
      "id": "IV.R350",
      "title": "Massless spin-1: two, not three",
      "url": "/registry/object/IV.R350/"
    },
    {
      "id": "IV.R351",
      "title": "Double slit in tau^3",
      "url": "/registry/object/IV.R351/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L320-L320",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L320-L320",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookIV/Electroweak/PhotonMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/PhotonMode.lean#L320-L320)
- Source range: L320-L320
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R347` — Masslessness is geometric, not postulated
- `IV.R348` — Experimental limits on photon mass
- `IV.R349` — The Planck--Einstein relation in tau^3
- `IV.R350` — Massless spin-1: two, not three
- `IV.R351` — Double slit in tau^3

## Immediate Comment / Docstring

```lean
-- [IV.R347] The photon is not postulated — it is the unique B-sector
-- transport mode with degenerate fiber character. (Structural remark)

-- [IV.R348] Wave/particle duality is not mysterious: wave = boundary
-- character, particle = defect bundle. Same object, two readings.

-- [IV.R349] Zero mass is not fine-tuned: the constant character (0,0)
-- necessarily lies in ker(Δ_Hodge) by the spectral theorem.

-- [IV.R350] The speed c is the base propagation speed on τ¹; it is
-- not separately postulated but follows from zero fiber obstruction.

-- [IV.R351] Charge quantization is AUTOMATIC from compactness of T²,
-- not imposed by hand as in orthodox QED.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval photon.sector                    -- Sector.B
```
