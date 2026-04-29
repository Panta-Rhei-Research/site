---
{
  "projection_kind": "taulib_declaration",
  "title": "right_handed_invisible",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/right-handed-invisible/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::right_handed_invisible",
  "declaration_slug": "right-handed-invisible",
  "kind": "theorem",
  "name": "right_handed_invisible",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 41,
  "source_line_end": 42,
  "registry_ids": [
    "IV.C01"
  ],
  "related_registry_items": [
    {
      "id": "IV.C01",
      "title": "Right-handed decoupling",
      "url": "/registry/object/IV.C01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L41-L42",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L41-L42",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L41-L42)
- Source range: L41-L42
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.C01` — Right-handed decoupling

## Immediate Comment / Docstring

```lean
/-- [IV.C01] Right-handed fermion configurations are invisible to the
    weak force. This is a structural consequence: sigma_A-inadmissible
    states do not couple to A-sector transport modes.
    Formalized as: sigma_a_admissible Right = false. -/
```

## Source Excerpt

```lean
theorem right_handed_invisible :
    sigma_a_admissible .Right = false := by rfl
```
