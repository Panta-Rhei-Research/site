---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorVacuum",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/sector-vacuum/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::SectorVacuum",
  "declaration_slug": "sector-vacuum",
  "kind": "structure",
  "name": "SectorVacuum",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 371,
  "source_line_end": 377,
  "registry_ids": [
    "VII.D13"
  ],
  "related_registry_items": [
    {
      "id": "VII.D13",
      "title": "Sector Vacuum",
      "url": "/registry/object/VII.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L371-L377",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L371-L377",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L371-L377)
- Source range: L371-L377
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D13` — Sector Vacuum

## Immediate Comment / Docstring

```lean
/-- [VII.D13] Sector Vacuum: ground state minimizing defect functional.
    Δ_X : S_X → [0,∞), v_X = argmin Δ_X. -/
```

## Source Excerpt

```lean
structure SectorVacuum where
  sector : SectorId
  /-- Defect is minimized (zero defect at vacuum). -/
  defect_minimized : Bool := true
  /-- Canonical minimizer. -/
  canonical : Bool := true
  deriving Repr
```
