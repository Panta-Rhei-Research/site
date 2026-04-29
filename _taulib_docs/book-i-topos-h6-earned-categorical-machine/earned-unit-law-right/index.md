---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_unit_law_right",
  "permalink": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/earned-unit-law-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H6EarnedCategoricalMachine`.",
  "declaration_id": "TauLib.BookI.Topos.H6EarnedCategoricalMachine::earned_unit_law_right",
  "declaration_slug": "earned-unit-law-right",
  "kind": "theorem",
  "name": "earned_unit_law_right",
  "module_name": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
  "module_url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/",
  "source_line_start": 156,
  "source_line_end": 158,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L156-L158",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L156-L158",
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
- Source path: [`TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L156-L158)
- Source range: L156-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 Prop `unit-laws` — right identity witness**.

    Direct from `cat_tau_id_right_stage` (paper §7
    `f ∘ id_X = f`). -/
```

## Source Excerpt

```lean
theorem earned_unit_law_right (f : StageFun) (n k : TauIdx) :
    (StageFun.comp f id_stage).b_fun n k = f.b_fun (reduce n k) k :=
  cat_tau_id_right_stage f n k
```
