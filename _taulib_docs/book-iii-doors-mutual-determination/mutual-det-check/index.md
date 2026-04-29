---
{
  "projection_kind": "taulib_declaration",
  "title": "mutual_det_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-mutual-determination/mutual-det-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.MutualDetermination`.",
  "declaration_id": "TauLib.BookIII.Doors.MutualDetermination::mutual_det_check",
  "declaration_slug": "mutual-det-check",
  "kind": "def",
  "name": "mutual_det_check",
  "module_name": "TauLib.BookIII.Doors.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-iii-doors-mutual-determination/",
  "source_line_start": 103,
  "source_line_end": 106,
  "registry_ids": [
    "III.D25"
  ],
  "related_registry_items": [
    {
      "id": "III.D25",
      "title": "Mutual Determination Schema",
      "url": "/registry/object/III.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L103-L106",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MutualDetermination",
        "url": "/verify/taulib/docs/book-iii-doors-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L103-L106",
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

- Module: [TauLib.BookIII.Doors.MutualDetermination](/verify/taulib/docs/book-iii-doors-mutual-determination/)
- Source path: [`TauLib/BookIII/Doors/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L103-L106)
- Source range: L103-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D25` — Mutual Determination Schema

## Immediate Comment / Docstring

```lean
/-- [III.D25] Full mutual determination: all three descriptions equivalent. -/
```

## Source Excerpt

```lean
def mutual_det_check (bound db : TauIdx) : Bool :=
  boundary_to_interior_check bound db &&
  interior_to_spectral_check bound db &&
  spectral_to_boundary_check bound db
```
