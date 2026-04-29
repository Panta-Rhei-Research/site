---
{
  "projection_kind": "taulib_declaration",
  "title": "tail_agree_downward",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tail-agree-downward/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::tail_agree_downward",
  "declaration_slug": "tail-agree-downward",
  "kind": "theorem",
  "name": "tail_agree_downward",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 77,
  "source_line_end": 95,
  "registry_ids": [
    "I.L07"
  ],
  "related_registry_items": [
    {
      "id": "I.L07",
      "title": "Tail Agreement Propagation",
      "url": "/registry/object/I.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L77-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L77-L95",
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
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L77-L95)
- Source range: L77-L95
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.L07` — Tail Agreement Propagation

## Immediate Comment / Docstring

```lean
/-- [I.L07] Tail Agreement Propagation (single input):
    If two tower-coherent stagewise functions agree at stage d₀ for input n,
    then they agree at ALL stages k ≤ d₀ for input n.

    This is the "downward" direction: agreement at a fine stage implies
    agreement at all coarser stages.

    Proof: By tower coherence, f₁(n, d₀) reduced to stage k equals f₁(n, k).
    If f₁(n, d₀) = f₂(n, d₀), then reducing both sides gives f₁(n, k) = f₂(n, k). -/
```

## Source Excerpt

```lean
theorem tail_agree_downward (f₁ f₂ : StageFun)
    (h₁ : TowerCoherent f₁) (h₂ : TowerCoherent f₂)
    (n d₀ : TauIdx) (hagree : agree_at f₁ f₂ n d₀) :
    ∀ k, k ≤ d₀ → agree_at f₁ f₂ n k := by
  intro k hk
  obtain ⟨hb, hc⟩ := hagree
  obtain ⟨h₁b, h₁c⟩ := h₁
  obtain ⟨h₂b, h₂c⟩ := h₂
  constructor
  · -- B-sector: f₁.b(n, k) = reduce(f₁.b(n, d₀), k) = reduce(f₂.b(n, d₀), k) = f₂.b(n, k)
    calc f₁.b_fun n k
        = reduce (f₁.b_fun n d₀) k := (h₁b n k d₀ hk).symm
      _ = reduce (f₂.b_fun n d₀) k := by rw [hb]
      _ = f₂.b_fun n k := h₂b n k d₀ hk
  · -- C-sector: analogous
    calc f₁.c_fun n k
        = reduce (f₁.c_fun n d₀) k := (h₁c n k d₀ hk).symm
      _ = reduce (f₂.c_fun n d₀) k := by rw [hc]
      _ = f₂.c_fun n k := h₂c n k d₀ hk
```
