---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_triad",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/boundary-triad/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::boundary_triad",
  "declaration_slug": "boundary-triad",
  "kind": "theorem",
  "name": "boundary_triad",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 217,
  "source_line_end": 226,
  "registry_ids": [
    "IV.T97"
  ],
  "related_registry_items": [
    {
      "id": "IV.T97",
      "title": "Boundary Triad Theorem",
      "url": "/registry/object/IV.T97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L217-L226",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L217-L226",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L217-L226)
- Source range: L217-L226
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T97` — Boundary Triad Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T97] Boundary Triad Theorem: the boundary L carries exactly 3
    canonical structures: (1) bipolar characters, (2) sector lifts,
    (3) chart readouts. These are the complete set of observable data. -/
```

## Source Excerpt

```lean
theorem boundary_triad :
    -- 3 canonical structures
    (1 + 1 + 1 : Nat) = 3 ∧
    -- Characters decompose bipolarly
    CharacterType.ChiPlus ≠ CharacterType.ChiMinus ∧
    -- 5 sector lifts
    all_sector_lifts.length = 5 ∧
    -- 4D chart readout
    chart_readout.target_dim = 4 := by
  simp [all_sector_lifts, chart_readout]
```
