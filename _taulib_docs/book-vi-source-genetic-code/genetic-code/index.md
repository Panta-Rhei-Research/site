---
{
  "projection_kind": "taulib_declaration",
  "title": "genetic_code",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/genetic-code/",
  "summary_short": "`def` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::genetic_code",
  "declaration_slug": "genetic-code",
  "kind": "def",
  "name": "genetic_code",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 55,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L55-L61",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L55-L61",
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

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L55-L61)
- Source range: L55-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
def genetic_code : BSDGeneticCode where
  amino_acids := 20
  aa_eq := rfl
  codons := 64
  codons_eq := rfl
  stop_codons := 3
  stop_eq := rfl
```
