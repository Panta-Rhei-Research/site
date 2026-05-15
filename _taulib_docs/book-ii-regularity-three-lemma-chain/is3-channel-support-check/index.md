---
{
  "projection_kind": "taulib_declaration",
  "title": "is3_channel_support_check",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-three-lemma-chain/is3-channel-support-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::is3_channel_support_check",
  "declaration_slug": "is3-channel-support-check",
  "kind": "def",
  "name": "is3_channel_support_check",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 290,
  "source_line_end": 291,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L290-L291",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.ThreeLemmaChain",
        "url": "/corpus/taulib/docs/book-ii-regularity-three-lemma-chain/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L290-L291",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/corpus/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L290-L291)
- Source range: L290-L291
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T33, IS3] Channel support: B on B-sector, C on C-sector. -/
```

## Source Excerpt

```lean
def is3_channel_support_check (bound : TauIdx) : Bool :=
  prime_split_support_check bound
```
