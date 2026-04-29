---
{
  "projection_kind": "taulib_declaration",
  "title": "ReactionDiffusionTau3",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/reaction-diffusion-tau3/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::ReactionDiffusionTau3",
  "declaration_slug": "reaction-diffusion-tau3",
  "kind": "structure",
  "name": "ReactionDiffusionTau3",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 167,
  "source_line_end": 174,
  "registry_ids": [
    "VI.P14"
  ],
  "related_registry_items": [
    {
      "id": "VI.P14",
      "title": "Reaction-Diffusion from τ³ Structure",
      "url": "/registry/object/VI.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L167-L174",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.GeneticCode",
        "url": "/verify/taulib/docs/book-vi-source-genetic-code/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L167-L174",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L167-L174)
- Source range: L167-L174
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P14` — Reaction-Diffusion from τ³ Structure

## Immediate Comment / Docstring

```lean
/-- [VI.P14] Reaction-Diffusion from τ³ Structure.
    The fibered product τ³ = τ¹ ×_f T² naturally separates
    reaction (temporal, base) from diffusion (spatial, fiber).
    Authority: Book II, Part II (τ³ fibration). -/
```

## Source Excerpt

```lean
structure ReactionDiffusionTau3 where
  /-- Reaction = base dynamics. -/
  reaction_is_base : Bool := true
  /-- Diffusion = fiber dynamics. -/
  diffusion_is_fiber : Bool := true
  /-- Natural separation from τ³ structure. -/
  tau3_separated : Bool := true
  deriving Repr
```
