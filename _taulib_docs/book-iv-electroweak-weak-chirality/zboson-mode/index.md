---
{
  "projection_kind": "taulib_declaration",
  "title": "ZBosonMode",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/zboson-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::ZBosonMode",
  "declaration_slug": "zboson-mode",
  "kind": "structure",
  "name": "ZBosonMode",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 163,
  "source_line_end": 172,
  "registry_ids": [
    "IV.D110"
  ],
  "related_registry_items": [
    {
      "id": "IV.D110",
      "title": "W-pm Defect Bundles",
      "url": "/registry/object/IV.D110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L163-L172",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L163-L172",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L163-L172)
- Source range: L163-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D110` — W-pm Defect Bundles

## Immediate Comment / Docstring

```lean
/-- [IV.D110] Z boson: the neutral weak transport mode. Mediates
    neutral-current weak interactions. Also massive via omega-coupling. -/
```

## Source Excerpt

```lean
structure ZBosonMode where
  /-- Name identifier. -/
  name : String
  /-- Electric charge: always 0. -/
  charge : Int
  charge_zero : charge = 0
  /-- Massive. -/
  massive : Bool
  massive_true : massive = true
  deriving Repr
```
