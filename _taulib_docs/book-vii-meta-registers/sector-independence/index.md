---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_independence",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/sector-independence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::sector_independence",
  "declaration_slug": "sector-independence",
  "kind": "theorem",
  "name": "sector_independence",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 338,
  "source_line_end": 346,
  "registry_ids": [
    "VII.P01"
  ],
  "related_registry_items": [
    {
      "id": "VII.P01",
      "title": "Sector Independence at E₃",
      "url": "/registry/object/VII.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L338-L346",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L338-L346",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L338-L346)
- Source range: L338-L346
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P01` — Sector Independence at E₃

## Immediate Comment / Docstring

```lean
/-- [VII.P01] Sector Independence: four pure sectors pairwise independent. -/
```

## Source Excerpt

```lean
theorem sector_independence :
    canonical_sector_decomp.pure_sector_count = 4 ∧
    SectorId.se ≠ SectorId.sp ∧
    SectorId.se ≠ SectorId.sd ∧
    SectorId.se ≠ SectorId.sc ∧
    SectorId.sp ≠ SectorId.sd ∧
    SectorId.sp ≠ SectorId.sc ∧
    SectorId.sd ≠ SectorId.sc :=
  ⟨rfl, by decide, by decide, by decide, by decide, by decide, by decide⟩
```
