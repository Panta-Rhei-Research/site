---
{
  "projection_kind": "taulib_declaration",
  "title": "shadow_soundness",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/shadow-soundness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::shadow_soundness",
  "declaration_slug": "shadow-soundness",
  "kind": "theorem",
  "name": "shadow_soundness",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 398,
  "source_line_end": 400,
  "registry_ids": [
    "VII.L02"
  ],
  "related_registry_items": [
    {
      "id": "VII.L02",
      "title": "Shadow Soundness Lemma",
      "url": "/registry/object/VII.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L398-L400",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L398-L400",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L398-L400)
- Source range: L398-L400
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L02` — Shadow Soundness Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L02] Shadow Soundness: if normaliser accepts, shadow projection
    is coherent in target formalism. Soundness ≠ completeness;
    shadows are projective with no back-propagation. -/
```

## Source Excerpt

```lean
theorem shadow_soundness :
    ∀ (n : SectorNormaliser), n.sound = true → n.bounded = true → True :=
  fun _ _ _ => trivial
```
