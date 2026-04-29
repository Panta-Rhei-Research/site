---
{
  "projection_kind": "taulib_declaration",
  "title": "BookIExport",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/book-iexport/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.BoundaryInterior`.",
  "declaration_id": "TauLib.BookI.Holomorphy.BoundaryInterior::BookIExport",
  "declaration_slug": "book-iexport",
  "kind": "structure",
  "name": "BookIExport",
  "module_name": "TauLib.BookI.Holomorphy.BoundaryInterior",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/",
  "source_line_start": 103,
  "source_line_end": 118,
  "registry_ids": [
    "I.P29"
  ],
  "related_registry_items": [
    {
      "id": "I.P29",
      "title": "Passage to Book II",
      "url": "/registry/object/I.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L103-L118",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.BoundaryInterior",
        "url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L103-L118",
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

- Module: [TauLib.BookI.Holomorphy.BoundaryInterior](/verify/taulib/docs/book-i-holomorphy-boundary-interior/)
- Source path: [`TauLib/BookI/Holomorphy/BoundaryInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L103-L118)
- Source range: L103-L118
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.P29` — Passage to Book II

## Immediate Comment / Docstring

```lean
/-- [I.P29] Passage to Book II: the earned import list.
    Book I has earned all the tools needed for the Central Theorem.

    The canonical data structure that Book II receives: -/
```

## Source Excerpt

```lean
structure BookIExport where
  -- The earned category
  category : Tau.Topos.CatTau
  -- The earned topos
  topos : Tau.Topos.EarnedTopos
  -- The holomorphic function space Hol(L)
  hol_space : Type := HolFun
  -- The identity theorem provides uniqueness
  identity : ∀ f₁ f₂ : StageFun,
    TowerCoherent f₁ → TowerCoherent f₂ →
    ∀ d₀, (∀ n, agree_at f₁ f₂ n d₀) →
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k
  -- The subobject classifier is Truth4
  classifier_four : ∀ v : Tau.Logic.Omega_tau,
    v = Tau.Logic.Truth4.T ∨ v = Tau.Logic.Truth4.F ∨
    v = Tau.Logic.Truth4.B ∨ v = Tau.Logic.Truth4.N
```
