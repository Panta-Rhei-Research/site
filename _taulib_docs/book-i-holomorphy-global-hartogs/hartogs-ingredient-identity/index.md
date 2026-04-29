---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_ingredient_identity",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/hartogs-ingredient-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.GlobalHartogs`.",
  "declaration_id": "TauLib.BookI.Holomorphy.GlobalHartogs::hartogs_ingredient_identity",
  "declaration_slug": "hartogs-ingredient-identity",
  "kind": "theorem",
  "name": "hartogs_ingredient_identity",
  "module_name": "TauLib.BookI.Holomorphy.GlobalHartogs",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/",
  "source_line_start": 105,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L105-L110",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L105-L110",
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

- Module: [TauLib.BookI.Holomorphy.GlobalHartogs](/verify/taulib/docs/book-i-holomorphy-global-hartogs/)
- Source path: [`TauLib/BookI/Holomorphy/GlobalHartogs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L105-L110)
- Source range: L105-L110
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ingredient 4: Identity Theorem provides uniqueness (I.T21). -/
```

## Source Excerpt

```lean
theorem hartogs_ingredient_identity :
    ∀ f₁ f₂ : StageFun,
    TowerCoherent f₁ → TowerCoherent f₂ →
    ∀ d₀, (∀ n, agree_at f₁ f₂ n d₀) →
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k :=
  tau_identity_nat
```
