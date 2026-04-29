---
{
  "projection_kind": "taulib_declaration",
  "title": "chirality_selection",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/chirality-selection/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::chirality_selection",
  "declaration_slug": "chirality-selection",
  "kind": "theorem",
  "name": "chirality_selection",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 114,
  "source_line_end": 116,
  "registry_ids": [
    "IV.T123"
  ],
  "related_registry_items": [
    {
      "id": "IV.T123",
      "title": "Chirality Selection",
      "url": "/registry/object/IV.T123/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L114-L116",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L114-L116",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L114-L116)
- Source range: L114-L116
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T123` — Chirality Selection

## Immediate Comment / Docstring

```lean
/-- [IV.T123] Chirality Selection Theorem: the weak interaction selects
    exactly the left-handed projection. This follows from:
    (1) A-sector has balanced polarity (Parity Bridge),
    (2) sigma_A acts non-trivially (flips chirality),
    (3) only sigma_A-admissible states couple to W/Z.

    Formally: for all chirality types c, c couples to weak iff c = Left. -/
```

## Source Excerpt

```lean
theorem chirality_selection (c : ChiralityType) :
    sigma_a_admissible c = true ↔ c = .Left := by
  cases c <;> simp [sigma_a_admissible]
```
