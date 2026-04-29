---
{
  "projection_kind": "taulib_declaration",
  "title": "code_reconstruction",
  "permalink": "/verify/taulib/docs/book-vi-life-core-self-desc/code-reconstruction/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.SelfDesc`.",
  "declaration_id": "TauLib.BookVI.LifeCore.SelfDesc::code_reconstruction",
  "declaration_slug": "code-reconstruction",
  "kind": "theorem",
  "name": "code_reconstruction",
  "module_name": "TauLib.BookVI.LifeCore.SelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-life-core-self-desc/",
  "source_line_start": 47,
  "source_line_end": 48,
  "registry_ids": [
    "VI.P02"
  ],
  "related_registry_items": [
    {
      "id": "VI.P02",
      "title": "Code Reconstruction",
      "url": "/registry/object/VI.P02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L47-L48",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.SelfDesc",
        "url": "/verify/taulib/docs/book-vi-life-core-self-desc/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L47-L48",
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

- Module: [TauLib.BookVI.LifeCore.SelfDesc](/verify/taulib/docs/book-vi-life-core-self-desc/)
- Source path: [`TauLib/BookVI/LifeCore/SelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L47-L48)
- Source range: L47-L48
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.P02` — Code Reconstruction

## Immediate Comment / Docstring

```lean
/-- [VI.P02] Code reconstruction: ω-germ code encodes distinction. -/
```

## Source Excerpt

```lean
theorem code_reconstruction :
    internal_eval.no_oracle = true := rfl
```
