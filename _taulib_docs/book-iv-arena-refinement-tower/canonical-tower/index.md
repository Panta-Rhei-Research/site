---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_tower",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/canonical-tower/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::canonical_tower",
  "declaration_slug": "canonical-tower",
  "kind": "def",
  "name": "canonical_tower",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 54,
  "source_line_end": 57,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L54-L57",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L54-L57",
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

- Module: [TauLib.BookIV.Arena.RefinementTower](/verify/taulib/docs/book-iv-arena-refinement-tower/)
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L54-L57)
- Source range: L54-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Canonical refinement tower: level n has depth n. -/
```

## Source Excerpt

```lean
def canonical_tower : RefinementTower where
  level := fun n => ⟨if n > 0 then n else 1, by split <;> omega⟩
  level_depth := by
    intro n hn; simp [show n > 0 from hn]
```
