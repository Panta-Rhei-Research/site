---
{
  "projection_kind": "taulib_declaration",
  "title": "StoneWitness",
  "permalink": "/verify/taulib/docs/book-ii-topology-stone-space/stone-witness/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Topology.StoneSpace`.",
  "declaration_id": "TauLib.BookII.Topology.StoneSpace::StoneWitness",
  "declaration_slug": "stone-witness",
  "kind": "structure",
  "name": "StoneWitness",
  "module_name": "TauLib.BookII.Topology.StoneSpace",
  "module_url": "/verify/taulib/docs/book-ii-topology-stone-space/",
  "source_line_start": 122,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L122-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.StoneSpace",
        "url": "/verify/taulib/docs/book-ii-topology-stone-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L122-L126",
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

- Module: [TauLib.BookII.Topology.StoneSpace](/verify/taulib/docs/book-ii-topology-stone-space/)
- Source path: [`TauLib/BookII/Topology/StoneSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L122-L126)
- Source range: L122-L126
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Stone space witness structure: for each pair (x,y) with x ≠ y,
    records the separating stage. -/
```

## Source Excerpt

```lean
structure StoneWitness where
  x : TauIdx
  y : TauIdx
  sep_stage : TauIdx  -- stage at which x,y are separated
  deriving Repr
```
