---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_a_iff_left",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/sigma-a-iff-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::sigma_a_iff_left",
  "declaration_slug": "sigma-a-iff-left",
  "kind": "theorem",
  "name": "sigma_a_iff_left",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 129,
  "source_line_end": 131,
  "registry_ids": [
    "IV.L05"
  ],
  "related_registry_items": [
    {
      "id": "IV.L05",
      "title": "Sigma_A-Admissibility Selects Chirality",
      "url": "/registry/object/IV.L05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L129-L131",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L129-L131",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L129-L131)
- Source range: L129-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.L05` — Sigma_A-Admissibility Selects Chirality

## Immediate Comment / Docstring

```lean
/-- [IV.L05] sigma_A-admissible if and only if left-handed. -/
```

## Source Excerpt

```lean
theorem sigma_a_iff_left (c : ChiralityType) :
    sigma_a_admissible c = true ↔ c = .Left := by
  cases c <;> simp [sigma_a_admissible]
```
