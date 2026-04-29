---
{
  "projection_kind": "taulib_declaration",
  "title": "Homochirality",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/homochirality/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::Homochirality",
  "declaration_slug": "homochirality",
  "kind": "structure",
  "name": "Homochirality",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 122,
  "source_line_end": 131,
  "registry_ids": [
    "VI.D28"
  ],
  "related_registry_items": [
    {
      "id": "VI.D28",
      "title": "Homochirality",
      "url": "/registry/object/VI.D28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L122-L131",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L122-L131",
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
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L122-L131)
- Source range: L122-L131
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D28` — Homochirality

## Immediate Comment / Docstring

```lean
/-- [VI.D28] Homochirality: L-amino acids / D-sugars.
    Phenomenological shadow of the Parity Bridge (conjectural).
    The weak sector's parity violation (IV.T146, IV.T160) seeds
    the biological chirality preference. -/
```

## Source Excerpt

```lean
structure Homochirality where
  /-- L-amino acids preferred. -/
  l_amino_acids : Bool := true
  /-- D-sugars preferred. -/
  d_sugars : Bool := true
  /-- Connected to Parity Bridge. -/
  parity_bridge_shadow : Bool := true
  /-- Scope: τ-effective (upgraded from conjectural via VI.R26 derivation chain). -/
  scope : String := "tau_effective"
  deriving Repr
```
