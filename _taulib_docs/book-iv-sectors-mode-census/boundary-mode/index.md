---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryMode",
  "permalink": "/verify/taulib/docs/book-iv-sectors-mode-census/boundary-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Sectors.ModeCensus`.",
  "declaration_id": "TauLib.BookIV.Sectors.ModeCensus::BoundaryMode",
  "declaration_slug": "boundary-mode",
  "kind": "structure",
  "name": "BoundaryMode",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_url": "/verify/taulib/docs/book-iv-sectors-mode-census/",
  "source_line_start": 62,
  "source_line_end": 65,
  "registry_ids": [
    "IV.D49"
  ],
  "related_registry_items": [
    {
      "id": "IV.D49",
      "title": "CR-Manifold",
      "url": "/registry/object/IV.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L62-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.ModeCensus",
        "url": "/verify/taulib/docs/book-iv-sectors-mode-census/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L62-L65",
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

- Module: [TauLib.BookIV.Sectors.ModeCensus](/verify/taulib/docs/book-iv-sectors-mode-census/)
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L62-L65)
- Source range: L62-L65
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D49` — CR-Manifold

## Immediate Comment / Docstring

```lean
/-- [IV.D49] A boundary mode is a (generator, lobe configuration) pair.
    There are 5 × 3 = 15 such modes. -/
```

## Source Excerpt

```lean
structure BoundaryMode where
  gen : Gen5
  config : LobeConfig
  deriving Repr, DecidableEq, BEq
```
