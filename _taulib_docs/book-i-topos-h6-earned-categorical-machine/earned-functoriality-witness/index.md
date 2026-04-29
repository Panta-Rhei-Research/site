---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_functoriality_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/earned-functoriality-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H6EarnedCategoricalMachine`.",
  "declaration_id": "TauLib.BookI.Topos.H6EarnedCategoricalMachine::earned_functoriality_witness",
  "declaration_slug": "earned-functoriality-witness",
  "kind": "theorem",
  "name": "earned_functoriality_witness",
  "module_name": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
  "module_url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/",
  "source_line_start": 239,
  "source_line_end": 245,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L239-L245",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L239-L245",
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
- Source path: [`TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L239-L245)
- Source range: L239-L245
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 functoriality structural witness**.

    The composition operator on `HolFun` (`holfun_comp_rf`,
    existing) is the functorial assignment.  Reduce-compatibility
    is preserved under composition (the structural shadow of
    paper §7's "probe-category functoriality" in TauLib).

    The "probe category" of paper §7 (`def:probe-category`) is
    rendered in TauLib at the meta-level: any reduce-form-compatible
    functor admits composition by `holfun_comp_rf`. -/
```

## Source Excerpt

```lean
theorem earned_functoriality_witness (f g : TauIdx → TauIdx)
    (hf : ReduceCompat f) (hg : ReduceCompat g) :
    -- Composition of reduce-compatible maps is reduce-compatible
    -- (the structural functoriality witness)
    ReduceCompat (f ∘ g) := by
  intro a b k h
  exact hf (g a) (g b) k (hg a b k h)
```
