---
{
  "projection_kind": "taulib_declaration",
  "title": "BookICrownJewel",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/book-icrown-jewel/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::BookICrownJewel",
  "declaration_slug": "book-icrown-jewel",
  "kind": "structure",
  "name": "BookICrownJewel",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 234,
  "source_line_end": 252,
  "registry_ids": [
    "I.T31",
    "I.T40",
    "I.T41"
  ],
  "related_registry_items": [
    {
      "id": "I.T31",
      "title": "Global Hartogs Extension",
      "url": "/registry/object/I.T31/"
    },
    {
      "id": "I.T40",
      "title": "Presheaf Characterization",
      "url": "/registry/object/I.T40/"
    },
    {
      "id": "I.T41",
      "title": "Bi-Square Characterization",
      "url": "/registry/object/I.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L234-L252",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.PresheafEssence",
        "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L234-L252",
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L234-L252)
- Source range: L234-L252
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.T31` — Global Hartogs Extension
- `I.T40` — Presheaf Characterization
- `I.T41` — Bi-Square Characterization

## Immediate Comment / Docstring

```lean
/-- The Book I crown jewel: five generators, seven axioms, one bi-square.
    Bundles all structural theorems earned across 19 Parts into
    one record that Book II receives. -/
```

## Source Excerpt

```lean
structure BookICrownJewel where
  /-- [I.T40] Presheaf characterization: HolFun → IsNatTrans. -/
  presheaf_char : ∀ f : StageFun, TowerCoherent f → IsNatTrans f
  /-- [I.T41] Bi-square characterization: TowerCoherent ↔ both squares. -/
  bi_square_char : ∀ f : StageFun,
    TowerCoherent f ↔
    (∀ n k l : TauIdx, k ≤ l → reduce (f.b_fun n l) k = f.b_fun n k) ∧
    (∀ n k l : TauIdx, k ≤ l → reduce (f.c_fun n l) k = f.c_fun n k)
  /-- [I.T31] The limit principle: agreement at d₀ implies agreement below. -/
  limit_principle : ∀ f₁ f₂ : StageFun,
    TowerCoherent f₁ → TowerCoherent f₂ →
    ∀ d₀, (∀ n, agree_at f₁ f₂ n d₀) →
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k
  /-- Right square follows from left (structural automaticity). -/
  right_automatic : ∀ f : StageFun, TowerCoherent f →
    ∀ n k l : TauIdx, k ≤ l →
    spectral_of f n k =
    ⟨reduce (spectral_of f n l).b_coeff k,
     reduce (spectral_of f n l).c_coeff k⟩
```
