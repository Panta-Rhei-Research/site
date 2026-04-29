---
{
  "projection_kind": "taulib_declaration",
  "title": "ParityPreserving",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/parity-preserving/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::ParityPreserving",
  "declaration_slug": "parity-preserving",
  "kind": "structure",
  "name": "ParityPreserving",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 84,
  "source_line_end": 89,
  "registry_ids": [
    "IV.D108"
  ],
  "related_registry_items": [
    {
      "id": "IV.D108",
      "title": "Polarity-Preserving Interaction",
      "url": "/registry/object/IV.D108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L84-L89",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L84-L89",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L84-L89)
- Source range: L84-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D108` — Polarity-Preserving Interaction

## Immediate Comment / Docstring

```lean
/-- [IV.D108] An interaction is parity-preserving if it does not
    distinguish left from right chirality. EM, Strong, and Gravity
    are parity-preserving; Weak is not. -/
```

## Source Excerpt

```lean
structure ParityPreserving where
  /-- The sector. -/
  sector : Sector
  /-- Whether the sector preserves parity. -/
  preserves : Bool
  deriving Repr
```
