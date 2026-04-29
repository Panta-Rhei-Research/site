---
{
  "projection_kind": "taulib_declaration",
  "title": "stagefun_id_comp_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/stagefun-id-comp-check/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::stagefun_id_comp_check",
  "declaration_slug": "stagefun-id-comp-check",
  "kind": "theorem",
  "name": "stagefun_id_comp_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 266,
  "source_line_end": 269,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L266-L269",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/verify/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L266-L269",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L266-L269)
- Source range: L266-L269
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- StageFun identity unit laws: id_stage composed with itself yields
    tower-coherent result equal to id_stage evaluation. -/
```

## Source Excerpt

```lean
theorem stagefun_id_comp_check (n k : TauIdx) :
    (StageFun.comp id_stage id_stage).b_fun n k = id_stage.b_fun n k := by
  simp only [StageFun.comp, id_stage]
  exact reduction_compat n (Nat.le_refl k)
```
