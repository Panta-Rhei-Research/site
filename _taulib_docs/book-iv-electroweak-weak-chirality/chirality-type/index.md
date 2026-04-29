---
{
  "projection_kind": "taulib_declaration",
  "title": "ChiralityType",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/chirality-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::ChiralityType",
  "declaration_slug": "chirality-type",
  "kind": "inductive",
  "name": "ChiralityType",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 109,
  "source_line_end": 114,
  "registry_ids": [
    "IV.D111"
  ],
  "related_registry_items": [
    {
      "id": "IV.D111",
      "title": "Z0 Defect Bundle",
      "url": "/registry/object/IV.D111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L109-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L109-L114",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L109-L114)
- Source range: L109-L114
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D111` — Z0 Defect Bundle

## Immediate Comment / Docstring

```lean
/-- [IV.D111] Chirality: left- or right-handedness of a fermion state.
    In the tau-framework, chirality is a boundary-character property:
    left-handed = sigma_A-admissible, right-handed = sigma_A-inadmissible. -/
```

## Source Excerpt

```lean
inductive ChiralityType where
  /-- Left-handed: participates in weak interaction. -/
  | Left
  /-- Right-handed: invisible to weak force. -/
  | Right
  deriving Repr, DecidableEq, BEq
```
