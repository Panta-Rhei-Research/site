---
{
  "projection_kind": "taulib_declaration",
  "title": "approach_count",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/approach-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::approach_count",
  "declaration_slug": "approach-count",
  "kind": "theorem",
  "name": "approach_count",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 135,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L135-L136",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L135-L136",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L135-L136)
- Source range: L135-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Total number of approaches compared. -/
```

## Source Excerpt

```lean
theorem approach_count :
    ([string_comparison, lqg_comparison, cdt_comparison, causal_set_comparison].length : Nat) = 4 := rfl
```
