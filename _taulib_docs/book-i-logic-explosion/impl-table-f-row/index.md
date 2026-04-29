---
{
  "projection_kind": "taulib_declaration",
  "title": "impl_table_F_row",
  "permalink": "/verify/taulib/docs/book-i-logic-explosion/impl-table-f-row/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.Explosion`.",
  "declaration_id": "TauLib.BookI.Logic.Explosion::impl_table_F_row",
  "declaration_slug": "impl-table-f-row",
  "kind": "theorem",
  "name": "impl_table_F_row",
  "module_name": "TauLib.BookI.Logic.Explosion",
  "module_url": "/verify/taulib/docs/book-i-logic-explosion/",
  "source_line_start": 134,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L134-L136",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Explosion",
        "url": "/verify/taulib/docs/book-i-logic-explosion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L134-L136",
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

- Module: [TauLib.BookI.Logic.Explosion](/verify/taulib/docs/book-i-logic-explosion/)
- Source path: [`TauLib/BookI/Logic/Explosion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L134-L136)
- Source range: L134-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem impl_table_F_row : Truth4.impl F T = T ∧ Truth4.impl F F = T ∧
    Truth4.impl F B = T ∧ Truth4.impl F N = T := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> rfl
```
