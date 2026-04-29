---
{
  "projection_kind": "taulib_declaration",
  "title": "R_tau_countable_irrefutable",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/r-tau-countable-irrefutable/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::R_tau_countable_irrefutable",
  "declaration_slug": "r-tau-countable-irrefutable",
  "kind": "theorem",
  "name": "R_tau_countable_irrefutable",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 203,
  "source_line_end": 212,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L203-L212",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.CantorRefutation",
        "url": "/verify/taulib/docs/book-i-sets-cantor-refutation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L203-L212",
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

- Module: [TauLib.BookI.Sets.CantorRefutation](/verify/taulib/docs/book-i-sets-cantor-refutation/)
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L203-L212)
- Source range: L203-L212
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The irrefutability of countability: since the three prerequisites
    for Cantor's argument are absent, no function within tau can
    witness |R_tau| > aleph_0. Combined with R_tau_countable,
    the cardinality of the tau-reals is exactly aleph_0. -/
```

## Source Excerpt

```lean
theorem R_tau_countable_irrefutable :
    -- Forward: R_tau embeds into Nat
    (exists (f : TauIdx -> Nat), Function.Injective f) /\
    -- Backward: Nat embeds into R_tau (every natural IS a tau-index)
    (exists (g : Nat -> TauIdx), Function.Injective g) /\
    -- No diagonal apparatus exists to prove uncountability
    (¬ exists (_ : CantorDiagonalApparatus), True) :=
  ⟨⟨id, fun _ _ h => h⟩,
   ⟨id, fun _ _ h => h⟩,
   cantor_inapplicable⟩
```
