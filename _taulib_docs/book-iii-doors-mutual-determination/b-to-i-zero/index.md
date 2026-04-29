---
{
  "projection_kind": "taulib_declaration",
  "title": "b_to_i_zero",
  "permalink": "/verify/taulib/docs/book-iii-doors-mutual-determination/b-to-i-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.MutualDetermination`.",
  "declaration_id": "TauLib.BookIII.Doors.MutualDetermination::b_to_i_zero",
  "declaration_slug": "b-to-i-zero",
  "kind": "theorem",
  "name": "b_to_i_zero",
  "module_name": "TauLib.BookIII.Doors.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-iii-doors-mutual-determination/",
  "source_line_start": 138,
  "source_line_end": 139,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L138-L139",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L138-L139",
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

- Module: [TauLib.BookIII.Doors.MutualDetermination](/verify/taulib/docs/book-iii-doors-mutual-determination/)
- Source path: [`TauLib/BookIII/Doors/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L138-L139)
- Source range: L138-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D25` — Mutual Determination Schema

## Immediate Comment / Docstring

```lean
/-- [III.D25] Structural: boundary→interior is exact for 0. -/
```

## Source Excerpt

```lean
theorem b_to_i_zero :
    crt_reconstruct (crt_decompose 0 3) 3 = 0 := by native_decide
```
