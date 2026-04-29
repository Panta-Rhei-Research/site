---
{
  "projection_kind": "taulib_declaration",
  "title": "AbiogenesisNotContingent",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-not-contingent/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::AbiogenesisNotContingent",
  "declaration_slug": "abiogenesis-not-contingent",
  "kind": "structure",
  "name": "AbiogenesisNotContingent",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 469,
  "source_line_end": 480,
  "registry_ids": [
    "VI.R28"
  ],
  "related_registry_items": [
    {
      "id": "VI.R28",
      "title": "Abiogenesis is not contingent",
      "url": "/registry/object/VI.R28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L469-L480",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L469-L480",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L469-L480)
- Source range: L469-L480
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R28` — Abiogenesis is not contingent

## Immediate Comment / Docstring

```lean
/-- [VI.R28] Abiogenesis Not Contingent: philosophical consequence.
    Life is not an accident requiring explanation but an inevitable
    structural feature of any τ-governed universe with sustained energy
    gradient. The derivation chain (VI.T46) shows that from K0–K6 alone,
    given dissipative conditions, persistence-sector entry is forced. -/
```

## Source Excerpt

```lean
structure AbiogenesisNotContingent where
  /-- Life is structurally necessary, not contingent. -/
  not_contingent : Bool := true
  /-- Requires sustained energy gradient. -/
  requires_energy_gradient : Bool := true
  /-- Follows from VI.T46. -/
  derived_from_inevitability : Bool := true
  /-- Scope: τ-effective (remark). -/
  scope : String := "tau_effective"
  deriving Repr

end Tau.BookVI.Persistence
```
