---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_strictness_8_3",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/e1-strictness-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::e1_strictness_8_3",
  "declaration_slug": "e1-strictness-8-3",
  "kind": "theorem",
  "name": "e1_strictness_8_3",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 227,
  "source_line_end": 228,
  "registry_ids": [
    "III.P01"
  ],
  "related_registry_items": [
    {
      "id": "III.P01",
      "title": "E₁ Strictness Witness",
      "url": "/registry/object/III.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L227-L228",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L227-L228",
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L227-L228)
- Source range: L227-L228
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P01` — E₁ Strictness Witness

## Immediate Comment / Docstring

```lean
-- E₁ strictness witness [III.P01]
```

## Source Excerpt

```lean
theorem e1_strictness_8_3 :
    e1_strictness_witness 8 3 = true := by native_decide
```
