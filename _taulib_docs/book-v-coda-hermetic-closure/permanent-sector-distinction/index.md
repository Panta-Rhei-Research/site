---
{
  "projection_kind": "taulib_declaration",
  "title": "PermanentSectorDistinction",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/permanent-sector-distinction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::PermanentSectorDistinction",
  "declaration_slug": "permanent-sector-distinction",
  "kind": "structure",
  "name": "PermanentSectorDistinction",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 330,
  "source_line_end": 343,
  "registry_ids": [
    "V.P121"
  ],
  "related_registry_items": [
    {
      "id": "V.P121",
      "title": "Permanent sector distinction",
      "url": "/registry/object/V.P121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L330-L343",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L330-L343",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L330-L343)
- Source range: L330-L343
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P121` — Permanent sector distinction

## Immediate Comment / Docstring

```lean
/-- [V.P121] Permanent sector distinction: the five sectors are
    topologically distinct characters on L. No deformation can merge
    two sectors. Sector Exhaustion proves no sixth exists.

    - 5 sectors = 5 distinct characters on L = S¹ ∨ S¹
    - Topological distinction: cannot be continuously deformed into each other
    - Exhaustion: no 6th character exists (sector budget = 5)
    - Permanence: structure is rigid (V.P120) and cannot change -/
```

## Source Excerpt

```lean
structure PermanentSectorDistinction where
  /-- Number of distinct sectors. -/
  n_sectors : Nat
  /-- Five sectors. -/
  sectors_eq : n_sectors = 5
  /-- Topologically distinct. -/
  topologically_distinct : Bool := true
  /-- No sixth exists. -/
  no_sixth : Bool := true
  /-- Structure is permanent. -/
  permanent : Bool := true
  /-- Maximum sector budget. -/
  max_sectors : Nat := 5
  deriving Repr
```
