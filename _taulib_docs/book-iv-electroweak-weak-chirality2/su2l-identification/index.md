---
{
  "projection_kind": "taulib_declaration",
  "title": "su2l_identification",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/su2l-identification/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::su2l_identification",
  "declaration_slug": "su2l-identification",
  "kind": "def",
  "name": "su2l_identification",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 171,
  "source_line_end": 177,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L171-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L171-L177",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L171-L177)
- Source range: L171-L177
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical SU(2)_L identification. -/
```

## Source Excerpt

```lean
def su2l_identification : SU2LIdentification where
  gauge_dim := 3
  gauge_dim_eq := rfl
  num_generators := 3
  num_gen_eq := rfl
  chirality := .Left
  chirality_left := rfl
```
