---
{
  "projection_kind": "taulib_declaration",
  "title": "single_anchor_sufficiency",
  "permalink": "/corpus/taulib/docs/book-iv-physics-readout-functor/single-anchor-sufficiency/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "declaration_id": "TauLib.BookIV.Physics.ReadoutFunctor::single_anchor_sufficiency",
  "declaration_slug": "single-anchor-sufficiency",
  "kind": "theorem",
  "name": "single_anchor_sufficiency",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_url": "/corpus/taulib/docs/book-iv-physics-readout-functor/",
  "source_line_start": 224,
  "source_line_end": 226,
  "registry_ids": [
    "IV.T129"
  ],
  "related_registry_items": [
    {
      "id": "IV.T129",
      "title": "Single-Anchor Sufficiency",
      "url": "/registry/object/IV.T129/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L224-L226",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.ReadoutFunctor",
        "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L224-L226",
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

- Module: [TauLib.BookIV.Physics.ReadoutFunctor](/corpus/taulib/docs/book-iv-physics-readout-functor/)
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L224-L226)
- Source range: L224-L226
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.T129` — Single-Anchor Sufficiency

## Immediate Comment / Docstring

```lean
/-- [IV.T129] Single-anchor sufficiency: the readout functor requires
    exactly 1 empirical input (m_n) and 4 exact SI constants. -/
```

## Source Excerpt

```lean
theorem single_anchor_sufficiency :
    readout.num_anchors = 1 ∧ readout.num_exact_si = 4 := by
  exact ⟨rfl, rfl⟩
```
