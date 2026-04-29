---
{
  "projection_kind": "taulib_declaration",
  "title": "bug_hiding_reason_count",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::bug_hiding_reason_count",
  "declaration_slug": "bug-hiding-reason-count",
  "kind": "theorem",
  "name": "bug_hiding_reason_count",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 157,
  "source_line_end": 157,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L157-L157",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.DiagonalResonance",
        "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L157-L157",
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

- Module: [TauLib.BookI.MetaLogic.DiagonalResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/)
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L157-L157)
- Source range: L157-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- There are exactly 5 bug hiding reasons. -/
```

## Source Excerpt

```lean
theorem bug_hiding_reason_count : allBugHidingReasons.length = 5 := by rfl
```
