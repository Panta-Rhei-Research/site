---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_identity_finite_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-finite-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::tau_identity_finite_witness",
  "declaration_slug": "tau-identity-finite-witness",
  "kind": "theorem",
  "name": "tau_identity_finite_witness",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 147,
  "source_line_end": 183,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L147-L183",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L147-L183",
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
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L147-L183)
- Source range: L147-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Special case: if two tower-coherent functions agree at all stages for all
    reduce(n, d₀) inputs (a finite set!), they agree at all stages ≤ d₀
    for ALL inputs.

    This captures the "finite witness" property: checking finitely many
    inputs (all residue classes mod M_{d₀}) suffices to determine
    the function at all coarser stages. -/
```

## Source Excerpt

```lean
theorem tau_identity_finite_witness (f₁ f₂ : StageFun)
    (h₁ : TowerCoherent f₁) (h₂ : TowerCoherent f₂)
    (d₀ : TauIdx)
    -- Agreement on all residue classes mod M_{d₀}
    (hagree : ∀ n, n < primorial d₀ → agree_at f₁ f₂ n d₀)
    -- f₁ and f₂ depend only on residue class at each stage
    (hf₁ : ∀ n k, f₁.b_fun n k = f₁.b_fun (reduce n k) k)
    (hf₂ : ∀ n k, f₂.b_fun n k = f₂.b_fun (reduce n k) k)
    (hg₁ : ∀ n k, f₁.c_fun n k = f₁.c_fun (reduce n k) k)
    (hg₂ : ∀ n k, f₂.c_fun n k = f₂.c_fun (reduce n k) k) :
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k := by
  intro n k hk
  -- reduce(n, d₀) < primorial d₀
  have hred : reduce n d₀ < primorial d₀ := Nat.mod_lt n (primorial_pos d₀)
  -- f₁ and f₂ agree at d₀ for reduce(n, d₀)
  have h_agree_red := hagree (reduce n d₀) hred
  -- By downward propagation, they agree at k ≤ d₀
  have h_at_k := tail_agree_downward f₁ f₂ h₁ h₂ (reduce n d₀) d₀ h_agree_red k hk
  -- Now lift to n using the residue-class dependence
  obtain ⟨hb_k, hc_k⟩ := h_at_k
  constructor
  · calc f₁.b_fun n k = f₁.b_fun (reduce n k) k := hf₁ n k
      _ = f₂.b_fun (reduce n k) k := by
          -- reduce(n, k) = reduce(reduce(n, d₀), k)
          -- since reduce(n, d₀) < primorial d₀ and k ≤ d₀
          rw [hf₁ (reduce n d₀) k] at hb_k
          rw [hf₂ (reduce n d₀) k] at hb_k
          have : reduce n k = reduce (reduce n d₀) k := (reduction_compat n hk).symm
          rw [this]; exact hb_k
      _ = f₂.b_fun n k := (hf₂ n k).symm
  · calc f₁.c_fun n k = f₁.c_fun (reduce n k) k := hg₁ n k
      _ = f₂.c_fun (reduce n k) k := by
          rw [hg₁ (reduce n d₀) k] at hc_k
          rw [hg₂ (reduce n d₀) k] at hc_k
          have : reduce n k = reduce (reduce n d₀) k := (reduction_compat n hk).symm
          rw [this]; exact hc_k
      _ = f₂.c_fun n k := (hg₂ n k).symm
```
