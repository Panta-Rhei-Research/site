---
{
  "projection_kind": "taulib_declaration",
  "title": "cat_tau_thin",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-thin/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedArrows`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedArrows::cat_tau_thin",
  "declaration_slug": "cat-tau-thin",
  "kind": "theorem",
  "name": "cat_tau_thin",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-arrows/",
  "source_line_start": 117,
  "source_line_end": 121,
  "registry_ids": [
    "I.P25"
  ],
  "related_registry_items": [
    {
      "id": "I.P25",
      "title": "Thin Category",
      "url": "/registry/object/I.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L117-L121",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedArrows",
        "url": "/verify/taulib/docs/book-i-topos-earned-arrows/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L117-L121",
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

- Module: [TauLib.BookI.Topos.EarnedArrows](/verify/taulib/docs/book-i-topos-earned-arrows/)
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L117-L121)
- Source range: L117-L121
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P25` — Thin Category

## Immediate Comment / Docstring

```lean
/-- [I.P25] Cat_τ is thin: if two tower-coherent stagewise functions
    agree at stage d₀ for all inputs, they agree at all stages ≤ d₀.
    This is a direct corollary of the τ-Identity Theorem (I.T21). -/
```

## Source Excerpt

```lean
theorem cat_tau_thin (f₁ f₂ : StageFun)
    (h₁ : TowerCoherent f₁) (h₂ : TowerCoherent f₂)
    (d₀ : TauIdx) (hagree : ∀ n, agree_at f₁ f₂ n d₀) :
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k :=
  tau_identity_nat f₁ f₂ h₁ h₂ d₀ hagree
```
