---
{
  "projection_kind": "taulib_declaration",
  "title": "right_handed_no_weak",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/right-handed-no-weak/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::right_handed_no_weak",
  "declaration_slug": "right-handed-no-weak",
  "kind": "theorem",
  "name": "right_handed_no_weak",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 45,
  "source_line_end": 48,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L45-L48",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L45-L48",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L45-L48)
- Source range: L45-L48
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Right-handed states have zero weak coupling. -/
```

## Source Excerpt

```lean
theorem right_handed_no_weak :
    sigma_a_admissible .Right = false ∧
    sigma_a_admissible .Left = true := by
  exact ⟨rfl, rfl⟩
```
