---
{
  "projection_kind": "taulib_declaration",
  "title": "RT_alpha_eq",
  "permalink": "/verify/taulib/docs/book-i-denotation-rank-transfer/rt-alpha-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.RankTransfer`.",
  "declaration_id": "TauLib.BookI.Denotation.RankTransfer::RT_alpha_eq",
  "declaration_slug": "rt-alpha-eq",
  "kind": "theorem",
  "name": "RT_alpha_eq",
  "module_name": "TauLib.BookI.Denotation.RankTransfer",
  "module_url": "/verify/taulib/docs/book-i-denotation-rank-transfer/",
  "source_line_start": 72,
  "source_line_end": 74,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L72-L74",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.RankTransfer",
        "url": "/verify/taulib/docs/book-i-denotation-rank-transfer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L72-L74",
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

- Module: [TauLib.BookI.Denotation.RankTransfer](/verify/taulib/docs/book-i-denotation-rank-transfer/)
- Source path: [`TauLib/BookI/Denotation/RankTransfer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L72-L74)
- Source range: L72-L74
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- RT for alpha is the same as toAlphaOrbit. -/
```

## Source Excerpt

```lean
theorem RT_alpha_eq (n : TauIdx) :
    RT alpha n = toAlphaOrbit n := by
  rfl
```
