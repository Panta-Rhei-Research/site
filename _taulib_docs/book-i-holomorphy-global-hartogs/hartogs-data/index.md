---
{
  "projection_kind": "taulib_declaration",
  "title": "HartogsData",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/hartogs-data/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.GlobalHartogs`.",
  "declaration_id": "TauLib.BookI.Holomorphy.GlobalHartogs::HartogsData",
  "declaration_slug": "hartogs-data",
  "kind": "structure",
  "name": "HartogsData",
  "module_name": "TauLib.BookI.Holomorphy.GlobalHartogs",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/",
  "source_line_start": 42,
  "source_line_end": 54,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L42-L54",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.GlobalHartogs",
        "url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L42-L54",
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

- Module: [TauLib.BookI.Holomorphy.GlobalHartogs](/verify/taulib/docs/book-i-holomorphy-global-hartogs/)
- Source path: [`TauLib/BookI/Holomorphy/GlobalHartogs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L42-L54)
- Source range: L42-L54
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A Hartogs extension pair: two tower-coherent functions that agree
    outside a thin set K at some reference depth. -/
```

## Source Excerpt

```lean
structure HartogsData where
  -- The first function
  f₁ : StageFun
  -- The second function
  f₂ : StageFun
  -- Tower coherence of f₁
  coh₁ : TowerCoherent f₁
  -- Tower coherence of f₂
  coh₂ : TowerCoherent f₂
  -- Reference depth where agreement is checked
  depth : TauIdx
  -- Agreement at reference depth for all inputs
  agree_ref : ∀ n, agree_at f₁ f₂ n depth
```
