---
{
  "projection_kind": "taulib_declaration",
  "title": "turing_hodge_eigenmodes",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/turing-hodge-eigenmodes-l153/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::turing_hodge_eigenmodes",
  "declaration_slug": "turing-hodge-eigenmodes-l153",
  "kind": "theorem",
  "name": "turing_hodge_eigenmodes",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 153,
  "source_line_end": 157,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L153-L157",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.GeneticCode",
        "url": "/verify/taulib/docs/book-vi-source-genetic-code/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L153-L157",
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

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L153-L157)
- Source range: L153-L157
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
theorem turing_hodge_eigenmodes :
    turing_hodge.hodge_laplacian = true ∧
    turing_hodge.reaction_source = "tau1_base" ∧
    turing_hodge.diffusion_domain = "T2_fiber" :=
  ⟨rfl, rfl, rfl⟩
```
