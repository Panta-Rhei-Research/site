---
{
  "projection_kind": "taulib_declaration",
  "title": "gen_sector_injective",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/gen-sector-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::gen_sector_injective",
  "declaration_slug": "gen-sector-injective",
  "kind": "theorem",
  "name": "gen_sector_injective",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 216,
  "source_line_end": 220,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L216-L220",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SectorParameters",
        "url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L216-L220",
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

- Module: [TauLib.BookIV.Sectors.SectorParameters](/verify/taulib/docs/book-iv-sectors-sector-parameters/)
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L216-L220)
- Source range: L216-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Generator-sector correspondence is injective on primitive sectors. -/
```

## Source Excerpt

```lean
theorem gen_sector_injective :
    gravity_sector.generator ≠ weak_sector.generator ∧
    weak_sector.generator ≠ em_sector.generator ∧
    em_sector.generator ≠ strong_sector.generator := by
  exact ⟨by decide, by decide, by decide⟩
```
