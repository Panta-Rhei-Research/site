---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_selfdesc_theorem",
  "permalink": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-selfdesc-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::bh_selfdesc_theorem",
  "declaration_slug": "bh-selfdesc-theorem",
  "kind": "theorem",
  "name": "bh_selfdesc_theorem",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 130,
  "source_line_end": 136,
  "registry_ids": [
    "VI.T30"
  ],
  "related_registry_items": [
    {
      "id": "VI.T30",
      "title": "BH SelfDesc Theorem",
      "url": "/registry/object/VI.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L130-L136",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.BHSelfDesc",
        "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L130-L136",
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

- Module: [TauLib.BookVI.CosmicLife.BHSelfDesc](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/)
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L130-L136)
- Source range: L130-L136
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `VI.T30` — BH SelfDesc Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T30] BH SelfDesc Theorem: all conditions, BH is alive. -/
```

## Source Excerpt

```lean
theorem bh_selfdesc_theorem :
    bh_sd.conditions_satisfied = 3 ∧
    bh_sd.completeness = true ∧
    bh_sd.internality = true ∧
    bh_sd.refinement_coherence = true ∧
    bh_sd.bh_alive = true :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
