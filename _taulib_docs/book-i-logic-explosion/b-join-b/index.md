---
{
  "projection_kind": "taulib_declaration",
  "title": "B_join_B",
  "permalink": "/corpus/taulib/docs/book-i-logic-explosion/b-join-b/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.Explosion`.",
  "declaration_id": "TauLib.BookI.Logic.Explosion::B_join_B",
  "declaration_slug": "b-join-b",
  "kind": "theorem",
  "name": "B_join_B",
  "module_name": "TauLib.BookI.Logic.Explosion",
  "module_url": "/corpus/taulib/docs/book-i-logic-explosion/",
  "source_line_start": 91,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L91-L91",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Explosion",
        "url": "/corpus/taulib/docs/book-i-logic-explosion/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L91-L91",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Logic.Explosion](/corpus/taulib/docs/book-i-logic-explosion/)
- Source path: [`TauLib/BookI/Logic/Explosion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L91-L91)
- Source range: L91-L91
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- B is idempotent under join. -/
```

## Source Excerpt

```lean
theorem B_join_B : Truth4.join B B = B := rfl
```
