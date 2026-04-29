---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_iff_is_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/hol-iff-is-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::hol_iff_is_check",
  "declaration_slug": "hol-iff-is-check",
  "kind": "def",
  "name": "hol_iff_is_check",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 299,
  "source_line_end": 303,
  "registry_ids": [
    "II.T33"
  ],
  "related_registry_items": [
    {
      "id": "II.T33",
      "title": "Holomorphic iff Idempotent-Supported",
      "url": "/registry/object/II.T33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L299-L303",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.ThreeLemmaChain",
        "url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L299-L303",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L299-L303)
- Source range: L299-L303
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T33` — Holomorphic iff Idempotent-Supported

## Immediate Comment / Docstring

```lean
/-- [II.T33] Holomorphic iff Idempotent-Supported: the full characterization.
    A stagewise function is holomorphic iff it satisfies IS1-IS4. -/
```

## Source Excerpt

```lean
def hol_iff_is_check (bound db : TauIdx) : Bool :=
  is1_decomposition_check bound db &&
  is2_naturality_check bound db &&
  is3_channel_support_check bound &&
  is4_polarity_check bound
```
