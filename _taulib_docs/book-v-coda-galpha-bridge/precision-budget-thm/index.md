---
{
  "projection_kind": "taulib_declaration",
  "title": "precision_budget_thm",
  "permalink": "/verify/taulib/docs/book-v-coda-galpha-bridge/precision-budget-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.GAlphaBridge`.",
  "declaration_id": "TauLib.BookV.Coda.GAlphaBridge::precision_budget_thm",
  "declaration_slug": "precision-budget-thm",
  "kind": "theorem",
  "name": "precision_budget_thm",
  "module_name": "TauLib.BookV.Coda.GAlphaBridge",
  "module_url": "/verify/taulib/docs/book-v-coda-galpha-bridge/",
  "source_line_start": 213,
  "source_line_end": 217,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L213-L217",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.GAlphaBridge",
        "url": "/verify/taulib/docs/book-v-coda-galpha-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L213-L217",
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

- Module: [TauLib.BookV.Coda.GAlphaBridge](/verify/taulib/docs/book-v-coda-galpha-bridge/)
- Source path: [`TauLib/BookV/Coda/GAlphaBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L213-L217)
- Source range: L213-L217
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Precision budget: 3 sources, c₁ dominant, α negligible. -/
```

## Source Excerpt

```lean
theorem precision_budget_thm :
    precision_budget.n_sources = 3 ∧
    precision_budget.dominant_is_c1 = true ∧
    precision_budget.alpha_negligible = true :=
  ⟨rfl, rfl, rfl⟩
```
