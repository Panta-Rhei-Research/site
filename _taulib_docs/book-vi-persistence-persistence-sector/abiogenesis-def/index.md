---
{
  "projection_kind": "taulib_declaration",
  "title": "AbiogenesisDef",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-def/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::AbiogenesisDef",
  "declaration_slug": "abiogenesis-def",
  "kind": "structure",
  "name": "AbiogenesisDef",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 141,
  "source_line_end": 148,
  "registry_ids": [
    "VI.D26"
  ],
  "related_registry_items": [
    {
      "id": "VI.D26",
      "title": "Abiogenesis as First Persistence Event",
      "url": "/registry/object/VI.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L141-L148",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L141-L148",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L141-L148)
- Source range: L141-L148
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D26` — Abiogenesis as First Persistence Event

## Immediate Comment / Docstring

```lean
/-- [VI.D26] Abiogenesis: first entry into the persistence sector.
    The transition from non-Life to Life (E₁ → E₂). -/
```

## Source Excerpt

```lean
structure AbiogenesisDef where
  /-- First sector entered. -/
  first_sector : String := "persistence"
  /-- Transition type: E₁ → E₂. -/
  transition_type : String := "E1_to_E2"
  /-- Scope: τ-effective (upgraded from conjectural via VI.T46 derivation chain). -/
  scope : String := "tau_effective"
  deriving Repr
```
