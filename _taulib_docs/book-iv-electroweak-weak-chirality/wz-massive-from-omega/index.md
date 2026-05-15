---
{
  "projection_kind": "taulib_declaration",
  "title": "wz_massive_from_omega",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/wz-massive-from-omega/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::wz_massive_from_omega",
  "declaration_slug": "wz-massive-from-omega",
  "kind": "theorem",
  "name": "wz_massive_from_omega",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 261,
  "source_line_end": 265,
  "registry_ids": [
    "IV.P53"
  ],
  "related_registry_items": [
    {
      "id": "IV.P53",
      "title": "Mass of Channel-Switching Defect Bundles",
      "url": "/registry/object/IV.P53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L261-L265",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality",
        "url": "/corpus/taulib/docs/book-iv-electroweak-weak-chirality/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L261-L265",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/corpus/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L261-L265)
- Source range: L261-L265
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P53` — Mass of Channel-Switching Defect Bundles

## Immediate Comment / Docstring

```lean
/-- [IV.P53] W and Z bosons are massive because omega is the conical
    singularity of L (lemniscate crossing point). The crossing fixes
    a coherence scale, breaking the would-be massless gauge symmetry.
    Structural: massive = true for both W and Z. -/
```

## Source Excerpt

```lean
theorem wz_massive_from_omega :
    w_plus.massive = true ∧
    w_minus.massive = true ∧
    z_zero.massive = true := by
  exact ⟨rfl, rfl, rfl⟩
```
