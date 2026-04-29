---
{
  "projection_kind": "taulib_declaration",
  "title": "PolaritySwitching",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/polarity-switching/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::PolaritySwitching",
  "declaration_slug": "polarity-switching",
  "kind": "structure",
  "name": "PolaritySwitching",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 58,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D319"
  ],
  "related_registry_items": [
    {
      "id": "IV.D319",
      "title": "Polarity-switching transition",
      "url": "/registry/object/IV.D319/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L58-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L58-L69",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L58-L69)
- Source range: L58-L69
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D319` — Polarity-switching transition

## Immediate Comment / Docstring

```lean
/-- [IV.D319] A polarity-switching transition in the A-sector: a process
    that changes the chi_plus/chi_minus composition of a state.
    The W boson mediates such transitions (e.g., up-quark to down-quark).
    The transition amplitude depends on the sector polarity measure. -/
```

## Source Excerpt

```lean
structure PolaritySwitching where
  /-- Source chirality. -/
  source : ChiralityType
  /-- Target chirality. -/
  target : ChiralityType
  /-- Source must be left-handed (sigma_A-admissible). -/
  source_left : source = .Left
  /-- Target must be left-handed. -/
  target_left : target = .Left
  /-- The mediating boson name. -/
  mediator : String
  deriving Repr
```
