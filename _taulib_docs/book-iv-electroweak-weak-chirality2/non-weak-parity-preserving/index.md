---
{
  "projection_kind": "taulib_declaration",
  "title": "non_weak_parity_preserving",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/non-weak-parity-preserving/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::non_weak_parity_preserving",
  "declaration_slug": "non-weak-parity-preserving",
  "kind": "theorem",
  "name": "non_weak_parity_preserving",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 133,
  "source_line_end": 137,
  "registry_ids": [
    "IV.P54"
  ],
  "related_registry_items": [
    {
      "id": "IV.P54",
      "title": "Parity in Non-Weak Sectors",
      "url": "/registry/object/IV.P54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L133-L137",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L133-L137",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L133-L137)
- Source range: L133-L137
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P54` — Parity in Non-Weak Sectors

## Immediate Comment / Docstring

```lean
/-- [IV.P54] EM, Strong, and Gravity are parity-preserving:
    they do not distinguish chirality. Their parity violation
    measure is zero. -/
```

## Source Excerpt

```lean
theorem non_weak_parity_preserving :
    parity_em.preserves = true ∧
    parity_strong.preserves = true ∧
    parity_gravity.preserves = true := by
  exact ⟨rfl, rfl, rfl⟩
```
