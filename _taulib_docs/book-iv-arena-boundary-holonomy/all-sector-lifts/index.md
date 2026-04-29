---
{
  "projection_kind": "taulib_declaration",
  "title": "all_sector_lifts",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/all-sector-lifts/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::all_sector_lifts",
  "declaration_slug": "all-sector-lifts",
  "kind": "def",
  "name": "all_sector_lifts",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 175,
  "source_line_end": 177,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L175-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L175-L177",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L175-L177)
- Source range: L175-L177
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All 5 canonical sector lifts. -/
```

## Source Excerpt

```lean
def all_sector_lifts : List SectorLift :=
  [⟨.D, true, rfl⟩, ⟨.A, true, rfl⟩, ⟨.B, true, rfl⟩,
   ⟨.C, true, rfl⟩, ⟨.Omega, true, rfl⟩]
```
