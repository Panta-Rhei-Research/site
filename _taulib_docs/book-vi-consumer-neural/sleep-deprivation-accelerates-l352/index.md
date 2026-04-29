---
{
  "projection_kind": "taulib_declaration",
  "title": "sleep_deprivation_accelerates",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/sleep-deprivation-accelerates-l352/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::sleep_deprivation_accelerates",
  "declaration_slug": "sleep-deprivation-accelerates-l352",
  "kind": "theorem",
  "name": "sleep_deprivation_accelerates",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 352,
  "source_line_end": 357,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L352-L357",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Neural",
        "url": "/verify/taulib/docs/book-vi-consumer-neural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L352-L357",
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

- Module: [TauLib.BookVI.Consumer.Neural](/verify/taulib/docs/book-vi-consumer-neural/)
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L352-L357)
- Source range: L352-L357
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem sleep_deprivation_accelerates :
    sleep_dep.budget_exhaustion_accelerated = true ∧
    sleep_dep.level_1_earlier = true ∧
    sleep_dep.cascade_earlier = true ∧
    sleep_dep.alzheimers_consistent = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
