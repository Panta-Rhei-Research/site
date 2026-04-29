---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_composition_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/earned-composition-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H6EarnedCategoricalMachine`.",
  "declaration_id": "TauLib.BookI.Topos.H6EarnedCategoricalMachine::earned_composition_witness",
  "declaration_slug": "earned-composition-witness",
  "kind": "theorem",
  "name": "earned_composition_witness",
  "module_name": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
  "module_url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/",
  "source_line_start": 114,
  "source_line_end": 118,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L114-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L114-L118",
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
- Source path: [`TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L114-L118)
- Source range: L114-L118
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 Thm `earned-composition` — structural witness**.

    Composition exists at the StageFun level via
    `StageFun.comp` (existing).  The keystone fact is that
    composition preserves the structural-coherence predicate
    `TowerCoherent` (Wave 5-era `comp_reduce_coherent`), which
    is the algebraic shadow of paper §7's three admissibility
    predicates (Typed, Stable, tail-independence) at the
    TauLib stage-function level.

    Concretely: composition on `StageFun` is associative
    (`stagefun_comp_assoc`), satisfies left-identity
    (`cat_tau_id_left_stage`), and satisfies right-identity
    (`cat_tau_id_right_stage`).  The "earned" character of
    paper §7 is captured by these being theorems in TauLib,
    not axioms. -/
```

## Source Excerpt

```lean
theorem earned_composition_witness (f₁ f₂ : StageFun) :
    -- Composition exists as a binary operation
    StageFun.comp f₁ f₂ = ⟨fun n k => f₁.b_fun (f₂.b_fun n k) k,
                          fun n k => f₁.c_fun (f₂.c_fun n k) k⟩ :=
  rfl
```
