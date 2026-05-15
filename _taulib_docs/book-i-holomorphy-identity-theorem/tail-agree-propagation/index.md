---
{
  "projection_kind": "taulib_declaration",
  "title": "tail_agree_propagation",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-identity-theorem/tail-agree-propagation/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::tail_agree_propagation",
  "declaration_slug": "tail-agree-propagation",
  "kind": "theorem",
  "name": "tail_agree_propagation",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 100,
  "source_line_end": 105,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L100-L105",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/corpus/taulib/docs/book-i-holomorphy-identity-theorem/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L100-L105",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/corpus/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L100-L105)
- Source range: L100-L105
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tail agreement propagation (universal over inputs):
    If two tower-coherent stagewise functions agree at stage d₀ for ALL inputs n,
    then they agree at all stages k ≤ d₀ for all inputs. -/
```

## Source Excerpt

```lean
theorem tail_agree_propagation (f₁ f₂ : StageFun)
    (h₁ : TowerCoherent f₁) (h₂ : TowerCoherent f₂)
    (d₀ : TauIdx) (hagree : ∀ n, agree_at f₁ f₂ n d₀) :
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k := by
  intro n k hk
  exact tail_agree_downward f₁ f₂ h₁ h₂ n d₀ (hagree n) k hk
```
