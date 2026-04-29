---
{
  "projection_kind": "taulib_declaration",
  "title": "comp_reduce_coherent",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/comp-reduce-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::comp_reduce_coherent",
  "declaration_slug": "comp-reduce-coherent",
  "kind": "theorem",
  "name": "comp_reduce_coherent",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 134,
  "source_line_end": 160,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L134-L160",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L134-L160",
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L134-L160)
- Source range: L134-L160
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Composition of reduce-form functions preserves tower coherence,
    provided the outer function's underlying maps preserve residue classes. -/
```

## Source Excerpt

```lean
theorem comp_reduce_coherent (f₁ f₂ : StageFun)
    (rf₁ : ReduceForm f₁) (rf₂ : ReduceForm f₂)
    (h₁ : TowerCoherent f₁) (h₂ : TowerCoherent f₂)
    (hrc_b : ReduceCompat rf₁.b_map) (hrc_c : ReduceCompat rf₁.c_map) :
    TowerCoherent (f₁.comp f₂) := by
  obtain ⟨h₁b, h₁c⟩ := h₁
  obtain ⟨h₂b, h₂c⟩ := h₂
  constructor
  · intro n k l hkl
    simp only [StageFun.comp]
    -- Goal: reduce(f₁.b(f₂.b(n,l), l), k) = f₁.b(f₂.b(n,k), k)
    -- Step 1: tower coherence of f₁
    rw [h₁b (f₂.b_fun n l) k l hkl]
    -- Goal: f₁.b(f₂.b(n,l), k) = f₁.b(f₂.b(n,k), k)
    rw [rf₁.b_eq, rf₁.b_eq]
    -- Goal: reduce(rf₁.b_map(f₂.b(n,l)), k) = reduce(rf₁.b_map(f₂.b(n,k)), k)
    apply hrc_b
    -- Goal: reduce(f₂.b(n,l), k) = reduce(f₂.b(n,k), k)
    rw [h₂b n k l hkl, rf₂.b_eq n k]
    exact (reduction_compat (rf₂.b_map n) (le_refl k)).symm
  · intro n k l hkl
    simp only [StageFun.comp]
    rw [h₁c (f₂.c_fun n l) k l hkl]
    rw [rf₁.c_eq, rf₁.c_eq]
    apply hrc_c
    rw [h₂c n k l hkl, rf₂.c_eq n k]
    exact (reduction_compat (rf₂.c_map n) (le_refl k)).symm
```
