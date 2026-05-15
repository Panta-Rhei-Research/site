---
{
  "projection_kind": "taulib_declaration",
  "title": "char_add_15_3",
  "permalink": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/char-add-15-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::char_add_15_3",
  "declaration_slug": "char-add-15-3",
  "kind": "theorem",
  "name": "char_add_15_3",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 398,
  "source_line_end": 399,
  "registry_ids": [
    "II.P14"
  ],
  "related_registry_items": [
    {
      "id": "II.P14",
      "title": "Character Algebra Ring Structure",
      "url": "/registry/object/II.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L398-L399",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
        "url": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L398-L399",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L398-L399)
- Source range: L398-L399
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.P14` — Character Algebra Ring Structure

## Immediate Comment / Docstring

```lean
-- Character addition [II.P14]
```

## Source Excerpt

```lean
theorem char_add_15_3 :
    character_add_check 15 3 = true := by native_decide
```
