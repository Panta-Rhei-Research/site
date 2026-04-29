---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_identity_nat",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-nat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::tau_identity_nat",
  "declaration_slug": "tau-identity-nat",
  "kind": "theorem",
  "name": "tau_identity_nat",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 134,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L134-L138",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L134-L138",
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/verify/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L134-L138)
- Source range: L134-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The τ-Identity Theorem (for natural-number inputs):
    If two tower-coherent stagewise functions agree at stage d₀ for ALL inputs,
    they agree at all stages ≤ d₀.

    Combined with the principle that a HolFun is determined by its action
    on reduce(n, k) (CRT coherence), this gives: agreement at any single
    primorial stage forces global agreement. -/
```

## Source Excerpt

```lean
theorem tau_identity_nat (f₁ f₂ : StageFun)
    (h₁ : TowerCoherent f₁) (h₂ : TowerCoherent f₂)
    (d₀ : TauIdx) (hagree : ∀ n, agree_at f₁ f₂ n d₀) :
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k :=
  tail_agree_propagation f₁ f₂ h₁ h₂ d₀ hagree
```
