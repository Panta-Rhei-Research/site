---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticParticleExport",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/ontic-particle-export/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::OnticParticleExport",
  "declaration_slug": "ontic-particle-export",
  "kind": "structure",
  "name": "OnticParticleExport",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 117,
  "source_line_end": 122,
  "registry_ids": [
    "V.D13"
  ],
  "related_registry_items": [
    {
      "id": "V.D13",
      "title": "OnticParticle --- IV.D22",
      "url": "/registry/object/V.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L117-L122",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L117-L122",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L117-L122)
- Source range: L117-L122
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D13` — OnticParticle --- IV.D22

## Immediate Comment / Docstring

```lean
/-- [V.D13] Ontic particle export: a persistent defect bundle with
    fiber carrier and positive mass. This wraps OnticParticle from
    Book IV MassEnergy with the Book V export interpretation.

    An ontic particle satisfies:
    1. Persistence (stable T² fiber)
    2. ρ-invariance (survives refinement iteration)
    3. Positive fiber stiffness (mass > 0) -/
```

## Source Excerpt

```lean
structure OnticParticleExport where
  /-- The underlying ontic particle from Book IV. -/
  particle : OnticParticle
  /-- Mass is positive. -/
  mass_positive : particle.mass.numer > 0
  deriving Repr
```
