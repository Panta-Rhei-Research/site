---
{
  "projection_kind": "taulib_declaration",
  "title": "RT",
  "permalink": "/verify/taulib/docs/book-i-denotation-rank-transfer/rt/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.RankTransfer`.",
  "declaration_id": "TauLib.BookI.Denotation.RankTransfer::RT",
  "declaration_slug": "rt",
  "kind": "def",
  "name": "RT",
  "module_name": "TauLib.BookI.Denotation.RankTransfer",
  "module_url": "/verify/taulib/docs/book-i-denotation-rank-transfer/",
  "source_line_start": 31,
  "source_line_end": 31,
  "registry_ids": [
    "I.D08"
  ],
  "related_registry_items": [
    {
      "id": "I.D08",
      "title": "Rank Transfer Maps",
      "url": "/registry/object/I.D08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L31-L31",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L31-L31",
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
- Source path: [`TauLib/BookI/Denotation/RankTransfer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L31-L31)
- Source range: L31-L31
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D08` — Rank Transfer Maps

## Immediate Comment / Docstring

```lean
/-- [I.D08] Rank transfer: TauIdx → orbit ray O_g, mapping n ↦ ⟨g, n⟩. -/
```

## Source Excerpt

```lean
def RT (g : Generator) (n : TauIdx) : TauObj := ⟨g, n⟩
```
