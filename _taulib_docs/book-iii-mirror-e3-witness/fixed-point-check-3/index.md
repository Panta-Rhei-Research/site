---
{
  "projection_kind": "taulib_declaration",
  "title": "fixed_point_check_3",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/fixed-point-check-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::fixed_point_check_3",
  "declaration_slug": "fixed-point-check-3",
  "kind": "theorem",
  "name": "fixed_point_check_3",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 234,
  "source_line_end": 235,
  "registry_ids": [
    "III.D85"
  ],
  "related_registry_items": [
    {
      "id": "III.D85",
      "title": "Self-Referential Fixed Point",
      "url": "/registry/object/III.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L234-L235",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L234-L235",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L234-L235)
- Source range: L234-L235
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D85` — Self-Referential Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D85] E₃ fixed points exist at stages 1-3. -/
```

## Source Excerpt

```lean
theorem fixed_point_check_3 :
    fixed_point_check 3 = true := by native_decide
```
