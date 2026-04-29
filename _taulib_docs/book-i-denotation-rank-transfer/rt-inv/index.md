---
{
  "projection_kind": "taulib_declaration",
  "title": "RT_inv",
  "permalink": "/verify/taulib/docs/book-i-denotation-rank-transfer/rt-inv/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.RankTransfer`.",
  "declaration_id": "TauLib.BookI.Denotation.RankTransfer::RT_inv",
  "declaration_slug": "rt-inv",
  "kind": "def",
  "name": "RT_inv",
  "module_name": "TauLib.BookI.Denotation.RankTransfer",
  "module_url": "/verify/taulib/docs/book-i-denotation-rank-transfer/",
  "source_line_start": 34,
  "source_line_end": 34,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L34-L34",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L34-L34",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookI/Denotation/RankTransfer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L34-L34)
- Source range: L34-L34
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Rank transfer inverse: orbit ray element → TauIdx (extracts depth). -/
```

## Source Excerpt

```lean
def RT_inv (x : TauObj) : TauIdx := x.depth
```
