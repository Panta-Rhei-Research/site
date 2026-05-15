---
{
  "projection_kind": "taulib_declaration",
  "title": "Sequent",
  "permalink": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/sequent/",
  "summary_short": "`structure` declaration in `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding::Sequent",
  "declaration_slug": "sequent",
  "kind": "structure",
  "name": "Sequent",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "source_line_start": 124,
  "source_line_end": 127,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L124-L127",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
        "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L124-L127",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.KernelFoundation.GirardLinearEmbedding](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/)
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L124-L127)
- Source range: L124-L127
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A `Sequent Γ ⊢ Δ` is a pair of formula lists. -/
```

## Source Excerpt

```lean
structure Sequent where
  antecedent : List Formula
  succedent  : List Formula
  deriving DecidableEq
```
