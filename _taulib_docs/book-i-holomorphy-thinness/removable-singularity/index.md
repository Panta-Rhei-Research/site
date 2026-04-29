---
{
  "projection_kind": "taulib_declaration",
  "title": "removable_singularity",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-thinness/removable-singularity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.Thinness`.",
  "declaration_id": "TauLib.BookI.Holomorphy.Thinness::removable_singularity",
  "declaration_slug": "removable-singularity",
  "kind": "theorem",
  "name": "removable_singularity",
  "module_name": "TauLib.BookI.Holomorphy.Thinness",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-thinness/",
  "source_line_start": 115,
  "source_line_end": 119,
  "registry_ids": [
    "I.T30"
  ],
  "related_registry_items": [
    {
      "id": "I.T30",
      "title": "Removable Singularity",
      "url": "/registry/object/I.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L115-L119",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.Thinness",
        "url": "/verify/taulib/docs/book-i-holomorphy-thinness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L115-L119",
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

- Module: [TauLib.BookI.Holomorphy.Thinness](/verify/taulib/docs/book-i-holomorphy-thinness/)
- Source path: [`TauLib/BookI/Holomorphy/Thinness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L115-L119)
- Source range: L115-L119
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T30` — Removable Singularity

## Immediate Comment / Docstring

```lean
/-- [I.T30] Removable Singularity: if two tower-coherent functions
    agree at depth d₀ for all inputs, they agree at all depths ≤ d₀.

    This is a repackaging of the Identity Theorem (I.T21)
    in the language of extensions. The "removable singularity" interpretation:
    knowing f on a dense set of inputs at stage d₀ determines f everywhere
    (because reduced inputs form a finite set at each stage). -/
```

## Source Excerpt

```lean
theorem removable_singularity (f₁ f₂ : StageFun)
    (hcoh1 : TowerCoherent f₁) (hcoh2 : TowerCoherent f₂)
    (d₀ : TauIdx) (hagree : ∀ n, agree_at f₁ f₂ n d₀) :
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k :=
  tau_identity_nat f₁ f₂ hcoh1 hcoh2 d₀ hagree
```
