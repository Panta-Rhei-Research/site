---
{
  "projection_kind": "taulib_declaration",
  "title": "distinction_well_defined",
  "permalink": "/verify/taulib/docs/book-vi-life-core-distinction/distinction-well-defined-l74/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.Distinction`.",
  "declaration_id": "TauLib.BookVI.LifeCore.Distinction::distinction_well_defined",
  "declaration_slug": "distinction-well-defined-l74",
  "kind": "theorem",
  "name": "distinction_well_defined",
  "module_name": "TauLib.BookVI.LifeCore.Distinction",
  "module_url": "/verify/taulib/docs/book-vi-life-core-distinction/",
  "source_line_start": 74,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L74-L78",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.Distinction",
        "url": "/verify/taulib/docs/book-vi-life-core-distinction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L74-L78",
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

- Module: [TauLib.BookVI.LifeCore.Distinction](/verify/taulib/docs/book-vi-life-core-distinction/)
- Source path: [`TauLib/BookVI/LifeCore/Distinction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L74-L78)
- Source range: L74-L78
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
theorem distinction_well_defined :
    distinction_wd.bounded_stabilization = true ∧
    distinction_wd.terminates = true ∧
    distinction_wd.unique_given_chi = true :=
  ⟨rfl, rfl, rfl⟩
```
