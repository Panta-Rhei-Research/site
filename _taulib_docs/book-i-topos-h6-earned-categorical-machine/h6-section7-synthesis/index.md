---
{
  "projection_kind": "taulib_declaration",
  "title": "h6_section7_synthesis",
  "permalink": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/h6-section7-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H6EarnedCategoricalMachine`.",
  "declaration_id": "TauLib.BookI.Topos.H6EarnedCategoricalMachine::h6_section7_synthesis",
  "declaration_slug": "h6-section7-synthesis",
  "kind": "theorem",
  "name": "h6_section7_synthesis",
  "module_name": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
  "module_url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/",
  "source_line_start": 276,
  "source_line_end": 291,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L276-L291",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
        "url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L276-L291",
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

- Module: [TauLib.BookI.Topos.H6EarnedCategoricalMachine](/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/)
- Source path: [`TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L276-L291)
- Source range: L276-L291
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 29 H6 §7 synthesis theorem (the KEYSTONE)**.

    Packages the full earned categorical machine of paper §7:

    1. **Earned composition**: `StageFun.comp` exists as the
       binary operation (witness via canonical formula).

    2. **Earned identity admissibility**: the identity map
       is reduce-compatible (`id_reduce_compat`) — the
       structural shadow of paper §7's empty-NF-code
       admissibility.

    3. **Unit laws**: `id ∘ f` and `f ∘ id` give correct
       behavior at the stage level (with appropriate
       normalization).

    4. **Associativity (KEYSTONE)**: `(f₁ ∘ f₂) ∘ f₃ =
       f₁ ∘ (f₂ ∘ f₃)` via `stagefun_comp_assoc`.

    5. **NF confluence (associativity meta-witness)**: the
       deeper "modulo `~`" associativity of paper §7 reduces
       to Wave 26's deterministic-NF confluence.

    All five clauses witness paper §7 at the structural-content
    level. -/
```

## Source Excerpt

```lean
theorem h6_section7_synthesis (f₁ f₂ f₃ : StageFun) (n k : TauIdx) :
    -- Clause 1: Earned composition exists
    StageFun.comp f₁ f₂ = ⟨fun n k => f₁.b_fun (f₂.b_fun n k) k,
                          fun n k => f₁.c_fun (f₂.c_fun n k) k⟩ ∧
    -- Clause 2: Identity is reduce-compatible
    ReduceCompat (fun (n : TauIdx) => n) ∧
    -- Clause 3: Left + right unit laws
    ((StageFun.comp id_stage f₁).b_fun n k = reduce (f₁.b_fun n k) k ∧
     (StageFun.comp f₁ id_stage).b_fun n k = f₁.b_fun (reduce n k) k) ∧
    -- Clause 4: Associativity (KEYSTONE)
    StageFun.comp (StageFun.comp f₁ f₂) f₃ =
      StageFun.comp f₁ (StageFun.comp f₂ f₃) :=
  ⟨earned_composition_witness f₁ f₂,
   earned_identity_admissible_witness,
   earned_unit_laws_witness f₁ n k,
   earned_associativity_witness f₁ f₂ f₃⟩
```
