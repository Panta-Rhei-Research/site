---
{
  "projection_kind": "taulib_declaration",
  "title": "stone_space_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-stone-space/stone-space-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.StoneSpace`.",
  "declaration_id": "TauLib.BookII.Topology.StoneSpace::stone_space_check",
  "declaration_slug": "stone-space-check",
  "kind": "def",
  "name": "stone_space_check",
  "module_name": "TauLib.BookII.Topology.StoneSpace",
  "module_url": "/verify/taulib/docs/book-ii-topology-stone-space/",
  "source_line_start": 113,
  "source_line_end": 118,
  "registry_ids": [
    "II.D14"
  ],
  "related_registry_items": [
    {
      "id": "II.D14",
      "title": "Stone Space",
      "url": "/registry/object/II.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L113-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L113-L118",
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
- Source path: [`TauLib/BookII/Topology/StoneSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L113-L118)
- Source range: L113-L118
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D14` — Stone Space

## Immediate Comment / Docstring

```lean
/-- [II.D14] Stone space: compact + Hausdorff + totally disconnected.
    Combined verification. -/
```

## Source Excerpt

```lean
def stone_space_check (bound db : TauIdx) : Bool :=
  hausdorff_check bound db &&
  totally_disconnected_check bound db &&
  finite_subcover_check 1 bound &&
  finite_subcover_check 2 bound &&
  finite_subcover_check 3 bound
```
