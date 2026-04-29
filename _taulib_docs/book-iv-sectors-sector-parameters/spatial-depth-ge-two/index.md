---
{
  "projection_kind": "taulib_declaration",
  "title": "spatial_depth_ge_two",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/spatial-depth-ge-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::spatial_depth_ge_two",
  "declaration_slug": "spatial-depth-ge-two",
  "kind": "theorem",
  "name": "spatial_depth_ge_two",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 237,
  "source_line_end": 239,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L237-L239",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L237-L239",
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
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L237-L239)
- Source range: L237-L239
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem spatial_depth_ge_two :
    em_sector.depth ≥ 2 ∧ strong_sector.depth ≥ 2 ∧ higgs_sector.depth ≥ 2 := by
  exact ⟨by decide, by decide, by decide⟩
```
