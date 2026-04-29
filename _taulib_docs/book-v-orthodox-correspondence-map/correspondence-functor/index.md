---
{
  "projection_kind": "taulib_declaration",
  "title": "CorrespondenceFunctor",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::CorrespondenceFunctor",
  "declaration_slug": "correspondence-functor",
  "kind": "structure",
  "name": "CorrespondenceFunctor",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 216,
  "source_line_end": 225,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L216-L225",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L216-L225",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L216-L225)
- Source range: L216-L225
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T121` — Properties of the correspondence functor

## Immediate Comment / Docstring

```lean
/-- [V.T121] The correspondence functor Phi maps tau-observables
    (boundary characters on H_partial[omega]) to orthodox observables
    (Hermitian operators on Hilbert space / metric tensors on manifolds).

    Properties:
    1. Well-defined: every boundary character maps to an observable
    2. Functorial: composition preserved
    3. NOT surjective: artifacts have no preimage
    4. NOT injective on objects: distinct boundary data can project
       to same readout

    The failure of surjectivity is precisely the set of artifacts.
    The failure of injectivity reflects information loss in chart
    projection. -/
```

## Source Excerpt

```lean
structure CorrespondenceFunctor where
  /-- Well-defined: every source has an image. -/
  well_defined : Bool := true
  /-- Functorial: preserves composition. -/
  functorial : Bool := true
  /-- NOT surjective: artifacts exist. -/
  surjective : Bool := false
  /-- NOT injective on objects: chart projection loses info. -/
  injective : Bool := false
  deriving Repr
```
