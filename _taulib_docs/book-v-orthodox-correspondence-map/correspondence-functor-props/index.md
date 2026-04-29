---
{
  "projection_kind": "taulib_declaration",
  "title": "correspondence_functor_props",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-props/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::correspondence_functor_props",
  "declaration_slug": "correspondence-functor-props",
  "kind": "theorem",
  "name": "correspondence_functor_props",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 247,
  "source_line_end": 252,
  "registry_ids": [
    "V.T121"
  ],
  "related_registry_items": [
    {
      "id": "V.T121",
      "title": "Properties of the correspondence functor",
      "url": "/registry/object/V.T121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L247-L252",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L247-L252",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L247-L252)
- Source range: L247-L252
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T121` — Properties of the correspondence functor

## Immediate Comment / Docstring

```lean
/-- [V.T121] Combined properties of the correspondence functor. -/
```

## Source Excerpt

```lean
theorem correspondence_functor_props :
    correspondence_functor.well_defined = true ∧
    correspondence_functor.functorial = true ∧
    correspondence_functor.surjective = false ∧
    correspondence_functor.injective = false :=
  ⟨rfl, rfl, rfl, rfl⟩
```
