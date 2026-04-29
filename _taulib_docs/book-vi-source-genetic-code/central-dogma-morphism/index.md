---
{
  "projection_kind": "taulib_declaration",
  "title": "CentralDogmaMorphism",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/central-dogma-morphism/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::CentralDogmaMorphism",
  "declaration_slug": "central-dogma-morphism",
  "kind": "structure",
  "name": "CentralDogmaMorphism",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 109,
  "source_line_end": 120,
  "registry_ids": [
    "VI.P15"
  ],
  "related_registry_items": [
    {
      "id": "VI.P15",
      "title": "Central Dogma as Morphism Composition",
      "url": "/registry/object/VI.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L109-L120",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L109-L120",
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

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L109-L120)
- Source range: L109-L120
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P15` — Central Dogma as Morphism Composition

## Immediate Comment / Docstring

```lean
/-- [VI.P15] Central Dogma as Morphism Composition.
    DNA → mRNA → Protein maps between τ³ factors:
    τ¹_DNA → (τ¹ × T²)_mRNA → T²_Protein.
    Authority: Book II, Part II (τ³ = τ¹ ×_f T² factor structure). -/
```

## Source Excerpt

```lean
structure CentralDogmaMorphism where
  /-- Number of morphism steps. -/
  steps : Nat
  /-- Exactly 2 steps (transcription + translation). -/
  steps_eq : steps = 2
  /-- Source factor: τ¹ (DNA, temporal/base). -/
  source_factor : String := "tau1_DNA"
  /-- Intermediate: τ¹ × T² (mRNA, mixed). -/
  intermediate : String := "tau1_x_T2_mRNA"
  /-- Target factor: T² (Protein, fiber/spatial). -/
  target_factor : String := "T2_Protein"
  deriving Repr
```
