---
{
  "projection_kind": "taulib_declaration",
  "title": "enr_functor_e2_8_3",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/enr-functor-e2-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::enr_functor_e2_8_3",
  "declaration_slug": "enr-functor-e2-8-3",
  "kind": "theorem",
  "name": "enr_functor_e2_8_3",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 266,
  "source_line_end": 267,
  "registry_ids": [
    "III.D04"
  ],
  "related_registry_items": [
    {
      "id": "III.D04",
      "title": "Enrichment Functor",
      "url": "/registry/object/III.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L266-L267",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.Functor",
        "url": "/verify/taulib/docs/book-iii-enrichment-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L266-L267",
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

- Module: [TauLib.BookIII.Enrichment.Functor](/verify/taulib/docs/book-iii-enrichment-functor/)
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L266-L267)
- Source range: L266-L267
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D04` — Enrichment Functor

## Immediate Comment / Docstring

```lean
-- Enrichment functor E₂→E₃ [III.D04]
```

## Source Excerpt

```lean
theorem enr_functor_e2_8_3 :
    enrichment_functor_check .E2 8 3 = true := by native_decide
```
