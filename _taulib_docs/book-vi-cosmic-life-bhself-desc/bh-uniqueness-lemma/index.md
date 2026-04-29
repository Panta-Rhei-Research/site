---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_uniqueness_lemma",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-uniqueness-lemma/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::bh_uniqueness_lemma",
  "declaration_slug": "bh-uniqueness-lemma",
  "kind": "theorem",
  "name": "bh_uniqueness_lemma",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 72,
  "source_line_end": 74,
  "registry_ids": [
    "VI.L09"
  ],
  "related_registry_items": [
    {
      "id": "VI.L09",
      "title": "BH Uniqueness Lemma",
      "url": "/registry/object/VI.L09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L72-L74",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.BHSelfDesc",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L72-L74",
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

- Module: [TauLib.BookVI.CosmicLife.BHSelfDesc](/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/)
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L72-L74)
- Source range: L72-L74
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.L09` — BH Uniqueness Lemma

## Immediate Comment / Docstring

```lean
/-- [VI.L09] BH uniqueness: unique element at every refinement level.
    Follows from Israel-Carter-Robinson (No-Hair) theorem. -/
```

## Source Excerpt

```lean
theorem bh_uniqueness_lemma :
    bh_target.kerr_newman = true ∧
    bh_target.selects_argmin = true := ⟨rfl, rfl⟩
```
