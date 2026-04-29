---
{
  "projection_kind": "taulib_declaration",
  "title": "structural_arrow",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/structural-arrow/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::structural_arrow",
  "declaration_slug": "structural-arrow",
  "kind": "theorem",
  "name": "structural_arrow",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 129,
  "source_line_end": 130,
  "registry_ids": [
    "IV.T95"
  ],
  "related_registry_items": [
    {
      "id": "IV.T95",
      "title": "Structural Arrow of Time",
      "url": "/registry/object/IV.T95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L129-L130",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.RefinementTower",
        "url": "/verify/taulib/docs/book-iv-arena-refinement-tower/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L129-L130",
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

- Module: [TauLib.BookIV.Arena.RefinementTower](/verify/taulib/docs/book-iv-arena-refinement-tower/)
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L129-L130)
- Source range: L129-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T95` — Structural Arrow of Time

## Immediate Comment / Docstring

```lean
/-- [IV.T95] Structural arrow of time: the refinement tower is directed,
    meaning deeper levels always refine shallower ones. This gives an
    irreversible arrow: once at depth n, you cannot "un-refine" to n-1. -/
```

## Source Excerpt

```lean
theorem structural_arrow (t1 t2 : ProtoTime) (h : t1 < t2) :
    t2.tick > t1.tick := h
```
