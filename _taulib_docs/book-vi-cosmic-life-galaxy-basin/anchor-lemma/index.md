---
{
  "projection_kind": "taulib_declaration",
  "title": "AnchorLemma",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/anchor-lemma/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.GalaxyBasin`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.GalaxyBasin::AnchorLemma",
  "declaration_slug": "anchor-lemma",
  "kind": "structure",
  "name": "AnchorLemma",
  "module_name": "TauLib.BookVI.CosmicLife.GalaxyBasin",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/",
  "source_line_start": 107,
  "source_line_end": 116,
  "registry_ids": [
    "VI.T33"
  ],
  "related_registry_items": [
    {
      "id": "VI.T33",
      "title": "Galaxy-SMBH Anchor Lemma",
      "url": "/registry/object/VI.T33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L107-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.GalaxyBasin",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L107-L116",
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

- Module: [TauLib.BookVI.CosmicLife.GalaxyBasin](/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/)
- Source path: [`TauLib/BookVI/CosmicLife/GalaxyBasin.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L107-L116)
- Source range: L107-L116
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T33` — Galaxy-SMBH Anchor Lemma

## Immediate Comment / Docstring

```lean
/-- [VI.T33] Galaxy–SMBH Anchor Lemma: galactic ω-germ code
    factors through SMBH's ω-code.
    code(D^gal)[ω] = Φ_bas ∘ code(D^SMBH)[ω]
    Empirical grounding: M–σ relation. -/
```

## Source Excerpt

```lean
structure AnchorLemma where
  /-- Code factors through anchor. -/
  code_factorizes : Bool := true
  /-- Same SMBH → same galactic code (up to Φ_bas). -/
  code_determines_basin : Bool := true
  /-- Evaluator decomposes through anchor. -/
  eval_decomposes : Bool := true
  /-- Φ_bas grounded by M–σ relation. -/
  m_sigma_grounding : Bool := true
  deriving Repr
```
