---
{
  "projection_kind": "taulib_declaration",
  "title": "GeneExpressionProfile",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/gene-expression-profile/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::GeneExpressionProfile",
  "declaration_slug": "gene-expression-profile",
  "kind": "structure",
  "name": "GeneExpressionProfile",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 107,
  "source_line_end": 116,
  "registry_ids": [
    "VI.D80"
  ],
  "related_registry_items": [
    {
      "id": "VI.D80",
      "title": "Gene Expression Profile",
      "url": "/registry/object/VI.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L107-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L107-L116",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L107-L116)
- Source range: L107-L116
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D80` — Gene Expression Profile

## Immediate Comment / Docstring

```lean
/-- [VI.D80] Gene Expression Profile.
    The subset of the genetic code (VI.D40) that the Central Dogma (VI.P15)
    actually reads at a given epigenetic state. Only genes in D⁻¹(+)
    (euchromatin) are transcribed.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure GeneExpressionProfile where
  /-- Total genes in genome. -/
  total_genes : Nat
  /-- Genes expressed (in euchromatin). -/
  expressed_genes : Nat
  /-- Expressed ≤ total (chromatin restricts). -/
  expressed_leq_total : expressed_genes ≤ total_genes
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
