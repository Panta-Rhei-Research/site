---
{
  "projection_kind": "taulib_declaration",
  "title": "face_conflict_is_1_3",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/face-conflict-is-1-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::face_conflict_is_1_3",
  "declaration_slug": "face-conflict-is-1-3",
  "kind": "theorem",
  "name": "face_conflict_is_1_3",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [
    "V.T147"
  ],
  "related_registry_items": [
    {
      "id": "V.T147",
      "title": "Face-Conflict Theorem",
      "url": "/registry/object/V.T147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L120-L122",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L120-L122",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L120-L122)
- Source range: L120-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T147` — Face-Conflict Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T147] P(face conflict) = 1/3, i.e. 3 out of 9 pairs. -/
```

## Source Excerpt

```lean
theorem face_conflict_is_1_3 :
    face_conflict.conflict_count * 3 = face_conflict.total_pairs :=
  by native_decide
```
