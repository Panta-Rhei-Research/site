---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_physics",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/sector-physics-l203/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::sector_physics",
  "declaration_slug": "sector-physics-l203",
  "kind": "def",
  "name": "sector_physics",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 203,
  "source_line_end": 209,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L203-L209",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SectorParameters",
        "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L203-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIV.Sectors.SectorParameters](/corpus/taulib/docs/book-iv-sectors-sector-parameters/)
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L203-L209)
- Source range: L203-L209
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Lookup sector physics by abstract sector. -/
```

## Source Excerpt

```lean
def sector_physics (s : Sector) : SectorPhysics :=
  match s with
  | .D => gravity_sector
  | .A => weak_sector
  | .B => em_sector
  | .C => strong_sector
  | .Omega => higgs_sector
```
