---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_associativity_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/earned-associativity-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H6EarnedCategoricalMachine`.",
  "declaration_id": "TauLib.BookI.Topos.H6EarnedCategoricalMachine::earned_associativity_witness",
  "declaration_slug": "earned-associativity-witness",
  "kind": "theorem",
  "name": "earned_associativity_witness",
  "module_name": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
  "module_url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/",
  "source_line_start": 191,
  "source_line_end": 195,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L191-L195",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L191-L195",
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
- Source path: [`TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L191-L195)
- Source range: L191-L195
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 Thm `earned-associativity` — KEYSTONE structural
    witness**.

    `(f₁ ∘ f₂) ∘ f₃ = f₁ ∘ (f₂ ∘ f₃)` at the StageFun level,
    direct from `stagefun_comp_assoc`.

    The DEEPER content of paper §7's associativity is that this
    holds *modulo* the equivalence relation `~` on NF codes —
    which by paper Step 4 + paper §7's Church–Rosser citation
    requires NF confluence.  In TauLib that's exactly Wave 26's
    `nf_confluence_statement` (deterministic `normalize` makes
    confluence computational).

    Wave 29 packages BOTH:
    (a) the concrete StageFun-level associativity, and
    (b) the meta-fact that confluence makes the
        equivalence-class-level associativity computational
        (via Wave 26's deterministic NF). -/
```

## Source Excerpt

```lean
theorem earned_associativity_witness (f₁ f₂ f₃ : StageFun) :
    -- (a) Concrete StageFun associativity (existing)
    StageFun.comp (StageFun.comp f₁ f₂) f₃ =
      StageFun.comp f₁ (StageFun.comp f₂ f₃) :=
  stagefun_comp_assoc f₁ f₂ f₃
```
