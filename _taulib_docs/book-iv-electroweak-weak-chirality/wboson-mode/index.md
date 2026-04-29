---
{
  "projection_kind": "taulib_declaration",
  "title": "WBosonMode",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/wboson-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::WBosonMode",
  "declaration_slug": "wboson-mode",
  "kind": "structure",
  "name": "WBosonMode",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 141,
  "source_line_end": 150,
  "registry_ids": [
    "IV.D109"
  ],
  "related_registry_items": [
    {
      "id": "IV.D109",
      "title": "Channel-Switching Defect Bundle",
      "url": "/registry/object/IV.D109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L141-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L141-L150",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L141-L150)
- Source range: L141-L150
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D109` — Channel-Switching Defect Bundle

## Immediate Comment / Docstring

```lean
/-- [IV.D109] W boson: the polarity-switching transport mode in the
    A-sector. Carries charge and mediates charged-current weak
    interactions. W is massive because omega (lemniscate crossing)
    provides a conical singularity that fixes the coherence scale. -/
```

## Source Excerpt

```lean
structure WBosonMode where
  /-- Name identifier. -/
  name : String
  /-- Electric charge (in units of e): +1, -1, or 0. -/
  charge : Int
  /-- Massive (true) or massless (false). -/
  massive : Bool
  /-- Chirality coupling: left-only. -/
  left_only : Bool
  deriving Repr
```
