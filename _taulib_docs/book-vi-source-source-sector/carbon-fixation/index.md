---
{
  "projection_kind": "taulib_declaration",
  "title": "CarbonFixation",
  "permalink": "/verify/taulib/docs/book-vi-source-source-sector/carbon-fixation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.SourceSector`.",
  "declaration_id": "TauLib.BookVI.Source.SourceSector::CarbonFixation",
  "declaration_slug": "carbon-fixation",
  "kind": "structure",
  "name": "CarbonFixation",
  "module_name": "TauLib.BookVI.Source.SourceSector",
  "module_url": "/verify/taulib/docs/book-vi-source-source-sector/",
  "source_line_start": 129,
  "source_line_end": 138,
  "registry_ids": [
    "VI.D38"
  ],
  "related_registry_items": [
    {
      "id": "VI.D38",
      "title": "Carbon Fixation as Canonical Production",
      "url": "/registry/object/VI.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L129-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.SourceSector",
        "url": "/verify/taulib/docs/book-vi-source-source-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L129-L138",
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

- Module: [TauLib.BookVI.Source.SourceSector](/verify/taulib/docs/book-vi-source-source-sector/)
- Source path: [`TauLib/BookVI/Source/SourceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L129-L138)
- Source range: L129-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D38` — Carbon Fixation as Canonical Production

## Immediate Comment / Docstring

```lean
/-- [VI.D38] Carbon Fixation as Canonical Source Production.
    Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.
    The archetypal structure generation process. -/
```

## Source Excerpt

```lean
structure CarbonFixation where
  /-- CO₂ molecules fixed per glucose. -/
  co2_per_glucose : Nat
  /-- Exactly 6. -/
  co2_eq : co2_per_glucose = 6
  /-- Driven by Hodge capacity gradient. -/
  hodge_driven : Bool := true
  /-- Global rate: ~120 Gt C/yr. -/
  global_fixation_gt : Nat := 120
  deriving Repr
```
