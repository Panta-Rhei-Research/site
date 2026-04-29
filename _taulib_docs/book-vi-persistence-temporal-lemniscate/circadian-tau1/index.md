---
{
  "projection_kind": "taulib_declaration",
  "title": "CircadianTau1",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/circadian-tau1/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::CircadianTau1",
  "declaration_slug": "circadian-tau1",
  "kind": "structure",
  "name": "CircadianTau1",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 102,
  "source_line_end": 107,
  "registry_ids": [
    "VI.P09"
  ],
  "related_registry_items": [
    {
      "id": "VI.P09",
      "title": "24-Hour Cycle as τ¹ Rotation",
      "url": "/registry/object/VI.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L102-L107",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L102-L107",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L102-L107)
- Source range: L102-L107
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P09` — 24-Hour Cycle as τ¹ Rotation

## Immediate Comment / Docstring

```lean
/-- [VI.P09] 24-Hour Cycle as τ¹ Rotation (conjectural).
    Molecular clock intrinsic period near 24h across all terrestrial life
    suggests a τ¹-derived timescale constraint. -/
```

## Source Excerpt

```lean
structure CircadianTau1 where
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  /-- Period locked to τ¹ rotation. -/
  tau1_locked : Bool := true
  deriving Repr
```
