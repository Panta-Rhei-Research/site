---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_a_admissible",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/sigma-a-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::sigma_a_admissible",
  "declaration_slug": "sigma-a-admissible",
  "kind": "def",
  "name": "sigma_a_admissible",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 123,
  "source_line_end": 126,
  "registry_ids": [
    "IV.D112"
  ],
  "related_registry_items": [
    {
      "id": "IV.D112",
      "title": "Chirality",
      "url": "/registry/object/IV.D112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L123-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L123-L126",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L123-L126)
- Source range: L123-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D112` — Chirality

## Immediate Comment / Docstring

```lean
/-- [IV.D112] sigma_A-admissibility: a fermion state is sigma_A-admissible iff
    it is left-handed. The weak sector involution sigma_A acts only on
    the left-handed projection. -/
```

## Source Excerpt

```lean
def sigma_a_admissible (c : ChiralityType) : Bool :=
  match c with
  | .Left => true
  | .Right => false
```
