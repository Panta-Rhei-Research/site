---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_absorbed_3",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/paradox-absorbed-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::paradox_absorbed_3",
  "declaration_slug": "paradox-absorbed-3",
  "kind": "theorem",
  "name": "paradox_absorbed_3",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 242,
  "source_line_end": 243,
  "registry_ids": [
    "III.D86"
  ],
  "related_registry_items": [
    {
      "id": "III.D86",
      "title": "Paradox Absorption Map",
      "url": "/registry/object/III.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L242-L243",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L242-L243",
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
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L242-L243)
- Source range: L242-L243
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D86` — Paradox Absorption Map

## Immediate Comment / Docstring

```lean
/-- [III.D86] Paradoxes absorbed at stages 1-3. -/
```

## Source Excerpt

```lean
theorem paradox_absorbed_3 :
    paradox_absorbed_check 3 = true := by native_decide
```
