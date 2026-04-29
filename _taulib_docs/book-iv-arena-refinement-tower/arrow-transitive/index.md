---
{
  "projection_kind": "taulib_declaration",
  "title": "arrow_transitive",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/arrow-transitive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::arrow_transitive",
  "declaration_slug": "arrow-transitive",
  "kind": "theorem",
  "name": "arrow_transitive",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 133,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L133-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L133-L135",
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
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L133-L135)
- Source range: L133-L135
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Transitivity of the arrow. -/
```

## Source Excerpt

```lean
theorem arrow_transitive (t1 t2 t3 : ProtoTime)
    (h12 : t1 < t2) (h23 : t2 < t3) : t1 < t3 :=
  Nat.lt_trans h12 h23
```
