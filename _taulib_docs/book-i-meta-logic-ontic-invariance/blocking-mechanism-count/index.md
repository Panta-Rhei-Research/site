---
{
  "projection_kind": "taulib_declaration",
  "title": "blocking_mechanism_count",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-mechanism-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::blocking_mechanism_count",
  "declaration_slug": "blocking-mechanism-count",
  "kind": "theorem",
  "name": "blocking_mechanism_count",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 60,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L60-L60",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.OnticInvariance",
        "url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L60-L60",
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

- Module: [TauLib.BookI.MetaLogic.OnticInvariance](/verify/taulib/docs/book-i-meta-logic-ontic-invariance/)
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L60-L60)
- Source range: L60-L60
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- There are exactly 3 blocking mechanisms. -/
```

## Source Excerpt

```lean
theorem blocking_mechanism_count : allBlockingMechanisms.length = 3 := by rfl
```
