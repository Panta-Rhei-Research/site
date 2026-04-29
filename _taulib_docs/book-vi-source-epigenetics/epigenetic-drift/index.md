---
{
  "projection_kind": "taulib_declaration",
  "title": "EpigeneticDrift",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-drift/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::EpigeneticDrift",
  "declaration_slug": "epigenetic-drift",
  "kind": "structure",
  "name": "EpigeneticDrift",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 334,
  "source_line_end": 343,
  "registry_ids": [
    "VI.D85"
  ],
  "related_registry_items": [
    {
      "id": "VI.D85",
      "title": "Epigenetic Drift",
      "url": "/registry/object/VI.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L334-L343",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L334-L343",
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
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L334-L343)
- Source range: L334-L343
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D85` — Epigenetic Drift

## Immediate Comment / Docstring

```lean
/-- [VI.D85] Epigenetic Drift.
    Age-related loss of epigenetic fidelity: methylation patterns erode,
    histone marks become noisy. An instance of the aging defect (VI.D43)
    at the chromatin level. The Horvath methylation clock correlates
    epigenetic drift with chronological age.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure EpigeneticDrift where
  /-- Primary mechanism: methylation loss + histone mark erosion. -/
  drift_source : String := "methylation_loss_and_histone_erosion"
  /-- Fidelity decreases monotonically with age. -/
  monotone_fidelity_loss : Bool := true
  /-- Instance of aging defect (VI.D43). -/
  instance_of_aging_defect : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
