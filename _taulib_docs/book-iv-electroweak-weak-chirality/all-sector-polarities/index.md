---
{
  "projection_kind": "taulib_declaration",
  "title": "all_sector_polarities",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/all-sector-polarities/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::all_sector_polarities",
  "declaration_slug": "all-sector-polarities",
  "kind": "def",
  "name": "all_sector_polarities",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 72,
  "source_line_end": 73,
  "registry_ids": [
    "IV.P52"
  ],
  "related_registry_items": [
    {
      "id": "IV.P52",
      "title": "Polarity Assignments",
      "url": "/registry/object/IV.P52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L72-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L72-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L72-L73)
- Source range: L72-L73
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P52` — Polarity Assignments

## Immediate Comment / Docstring

```lean
/-- [IV.P52] Polarity signatures of all 5 sectors at E1. -/
```

## Source Excerpt

```lean
def all_sector_polarities : List PolarityIndex :=
  [pol_D, pol_A, pol_B, pol_C, pol_Omega]
```
