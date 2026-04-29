---
{
  "projection_kind": "taulib_declaration",
  "title": "EpigeneticState",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-state/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::EpigeneticState",
  "declaration_slug": "epigenetic-state",
  "kind": "structure",
  "name": "EpigeneticState",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 79,
  "source_line_end": 88,
  "registry_ids": [
    "VI.D79"
  ],
  "related_registry_items": [
    {
      "id": "VI.D79",
      "title": "Epigenetic State",
      "url": "/registry/object/VI.D79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L79-L88",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L79-L88",
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
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L79-L88)
- Source range: L79-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D79` — Epigenetic State

## Immediate Comment / Docstring

```lean
/-- [VI.D79] Epigenetic State.
    Evaluator-modulated code reading at refinement level n.
    Combines chromatin partition (VI.D78) with refinement level (VI.P18).
    The evaluator (VI.D08, SelfDesc) reads the same ω-germ code differently
    at each level by restricting which genes are accessible.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure EpigeneticState where
  /-- Refinement level in the differentiation tower (0 = totipotent). -/
  refinement_level : Nat
  /-- Associated chromatin partition determines accessible genes. -/
  has_chromatin_partition : Bool := true
  /-- Number of genes in euchromatin (active) at this level. -/
  active_gene_count : Nat
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
