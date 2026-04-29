---
{
  "projection_kind": "taulib_declaration",
  "title": "separating_stage",
  "permalink": "/verify/taulib/docs/book-ii-topology-stone-space/separating-stage/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.StoneSpace`.",
  "declaration_id": "TauLib.BookII.Topology.StoneSpace::separating_stage",
  "declaration_slug": "separating-stage",
  "kind": "def",
  "name": "separating_stage",
  "module_name": "TauLib.BookII.Topology.StoneSpace",
  "module_url": "/verify/taulib/docs/book-ii-topology-stone-space/",
  "source_line_start": 58,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L58-L60",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L58-L60",
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

- Module: [TauLib.BookII.Topology.StoneSpace](/verify/taulib/docs/book-ii-topology-stone-space/)
- Source path: [`TauLib/BookII/Topology/StoneSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L58-L60)
- Source range: L58-L60
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Constructive witness: return the separating stage for x ≠ y. -/
```

## Source Excerpt

```lean
def separating_stage (x y db : TauIdx) : TauIdx :=
  if x == y then db + 1
  else disagree_depth x y db + 1
```
