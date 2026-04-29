---
{
  "projection_kind": "taulib_declaration",
  "title": "BHDecodeHorizon",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/bhdecode-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::BHDecodeHorizon",
  "declaration_slug": "bhdecode-horizon",
  "kind": "structure",
  "name": "BHDecodeHorizon",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 55,
  "source_line_end": 62,
  "registry_ids": [
    "VI.D59"
  ],
  "related_registry_items": [
    {
      "id": "VI.D59",
      "title": "BH DecodeHorizon",
      "url": "/registry/object/VI.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L55-L62",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L55-L62",
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

- Module: [TauLib.BookVI.CosmicLife.BHSelfDesc](/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/)
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L55-L62)
- Source range: L55-L62
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D59` — BH DecodeHorizon

## Immediate Comment / Docstring

```lean
/-- [VI.D59] BH DecodeHorizon: constant ω-germ code from (M,J,Q).
    The code is finitely determined (profinite limit stabilizes at step 1). -/
```

## Source Excerpt

```lean
structure BHDecodeHorizon where
  /-- Code is constant across blueprint ball. -/
  constant_code : Bool := true
  /-- Three conserved charges encode the genotype. -/
  charge_count : Nat := 3
  /-- Profinite limit stabilizes after 1 step (No-Hair). -/
  stabilization_depth : Nat := 1
  deriving Repr
```
