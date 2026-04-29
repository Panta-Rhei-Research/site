---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_iff_is_12_3",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/hol-iff-is-12-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::hol_iff_is_12_3",
  "declaration_slug": "hol-iff-is-12-3",
  "kind": "theorem",
  "name": "hol_iff_is_12_3",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 392,
  "source_line_end": 393,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L392-L393",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L392-L393",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L392-L393)
- Source range: L392-L393
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T33` — Holomorphic iff Idempotent-Supported

## Immediate Comment / Docstring

```lean
-- Holomorphic iff IS [II.T33]
```

## Source Excerpt

```lean
theorem hol_iff_is_12_3 :
    hol_iff_is_check 12 3 = true := by native_decide
```
