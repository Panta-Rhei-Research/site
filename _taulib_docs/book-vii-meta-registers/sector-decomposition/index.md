---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorDecomposition",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/sector-decomposition/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::SectorDecomposition",
  "declaration_slug": "sector-decomposition",
  "kind": "structure",
  "name": "SectorDecomposition",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 308,
  "source_line_end": 320,
  "registry_ids": [
    "VII.T03"
  ],
  "related_registry_items": [
    {
      "id": "VII.T03",
      "title": "Sector Decomposition at E₃",
      "url": "/registry/object/VII.T03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L308-L320",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L308-L320",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L308-L320)
- Source range: L308-L320
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T03` — Sector Decomposition at E₃

## Immediate Comment / Docstring

```lean
/-- [VII.T03] Sector Decomposition: Adm_{E₃} = S_E ⊔ S_P ⊔ (S_D\S_L) ⊔ (S_C\S_L) ⊔ S_L.
    Every E₃-admissible content belongs to exactly one of five sectors. -/
```

## Source Excerpt

```lean
structure SectorDecomposition where
  sector_count : Nat
  count_eq : sector_count = 5
  pure_sector_count : Nat
  pure_eq : pure_sector_count = 4
  mixed_sector_count : Nat
  mixed_eq : mixed_sector_count = 1
  sum_eq : pure_sector_count + mixed_sector_count = sector_count
  /-- Exhaustive: MetaDecode projects to four registers covering all content. -/
  exhaustive : Bool := true
  /-- Disjoint: codomain categories structurally distinct. -/
  disjoint : Bool := true
  deriving Repr
```
