---
{
  "projection_kind": "taulib_declaration",
  "title": "z_reion_pos",
  "permalink": "/verify/taulib/docs/book-v-cosmology-reionization/z-reion-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.Reionization`.",
  "declaration_id": "TauLib.BookV.Cosmology.Reionization::z_reion_pos",
  "declaration_slug": "z-reion-pos",
  "kind": "theorem",
  "name": "z_reion_pos",
  "module_name": "TauLib.BookV.Cosmology.Reionization",
  "module_url": "/verify/taulib/docs/book-v-cosmology-reionization/",
  "source_line_start": 84,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L84-L84",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.Reionization",
        "url": "/verify/taulib/docs/book-v-cosmology-reionization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L84-L84",
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

- Module: [TauLib.BookV.Cosmology.Reionization](/verify/taulib/docs/book-v-cosmology-reionization/)
- Source path: [`TauLib/BookV/Cosmology/Reionization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L84-L84)
- Source range: L84-L84
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- z_reion = 8 is positive. -/
```

## Source Excerpt

```lean
theorem z_reion_pos : z_reion > 0 := by decide
```
