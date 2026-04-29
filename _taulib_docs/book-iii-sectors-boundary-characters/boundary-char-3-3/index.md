---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_char_3_3",
  "permalink": "/verify/taulib/docs/book-iii-sectors-boundary-characters/boundary-char-3-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::boundary_char_3_3",
  "declaration_slug": "boundary-char-3-3",
  "kind": "theorem",
  "name": "boundary_char_3_3",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 179,
  "source_line_end": 180,
  "registry_ids": [
    "III.D11"
  ],
  "related_registry_items": [
    {
      "id": "III.D11",
      "title": "Boundary Character Space",
      "url": "/registry/object/III.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L179-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.BoundaryCharacters",
        "url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L179-L180",
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

- Module: [TauLib.BookIII.Sectors.BoundaryCharacters](/verify/taulib/docs/book-iii-sectors-boundary-characters/)
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L179-L180)
- Source range: L179-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D11` — Boundary Character Space

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Boundary character group [III.D11]
```

## Source Excerpt

```lean
theorem boundary_char_3_3 :
    boundary_char_check 3 3 = true := by native_decide
```
