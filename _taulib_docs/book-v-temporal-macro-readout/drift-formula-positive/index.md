---
{
  "projection_kind": "taulib_declaration",
  "title": "drift_formula_positive",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/drift-formula-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::drift_formula_positive",
  "declaration_slug": "drift-formula-positive",
  "kind": "theorem",
  "name": "drift_formula_positive",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 154,
  "source_line_end": 157,
  "registry_ids": [
    "V.T16"
  ],
  "related_registry_items": [
    {
      "id": "V.T16",
      "title": "Redshift-Depth Relation",
      "url": "/registry/object/V.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L154-L157",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/verify/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L154-L157",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L154-L157)
- Source range: L154-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T16` — Redshift-Depth Relation

## Immediate Comment / Docstring

```lean
/-- [V.T16] Drift depth difference is positive for cosmological
    observations (source earlier than receiver). -/
```

## Source Excerpt

```lean
theorem drift_formula_positive (d : RefinementDrift) :
    d.depth_diff > 0 := by
  simp only [RefinementDrift.depth_diff]
  exact Nat.sub_pos_of_lt d.source_earlier
```
