---
{
  "projection_kind": "taulib_declaration",
  "title": "TowerNaturalTransformation",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/tower-natural-transformation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::TowerNaturalTransformation",
  "declaration_slug": "tower-natural-transformation",
  "kind": "structure",
  "name": "TowerNaturalTransformation",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 63,
  "source_line_end": 74,
  "registry_ids": [
    "IV.D241"
  ],
  "related_registry_items": [
    {
      "id": "IV.D241",
      "title": "Tower-natural transformation",
      "url": "/registry/object/IV.D241/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L63-L74",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.LawsAsStructure",
        "url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L63-L74",
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

- Module: [TauLib.BookIV.Coda.LawsAsStructure](/verify/taulib/docs/book-iv-coda-laws-as-structure/)
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L63-L74)
- Source range: L63-L74
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D241` — Tower-natural transformation

## Immediate Comment / Docstring

```lean
/-- [IV.D241] A tower-natural transformation eta: F => G between sector
    functors F, G: tau^1 -> tau^3|_{T^2} is a family {eta_n: F[n] -> G[n]}
    in the boundary holonomy algebra that commutes with the refinement
    tower maps:

    eta_{n+1} composed phi_{n,n+1}^G = phi_{n,n+1}^F composed eta_n

    for all primorial stages n. Every conservation law in the tau-framework
    corresponds to such a transformation. -/
```

## Source Excerpt

```lean
structure TowerNaturalTransformation where
  /-- Family indexed by primorial stages. -/
  indexed_by_stages : Bool := true
  /-- Commutes with refinement tower maps. -/
  commutes_with_tower : Bool := true
  /-- Source functor. -/
  source : String := "F: tau^1 -> tau^3|_{T^2}"
  /-- Target functor. -/
  target : String := "G: tau^1 -> tau^3|_{T^2}"
  /-- Conservation law correspondence. -/
  conservation_law : Bool := true
  deriving Repr
```
