---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_roundtrip_10_3",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-roundtrip-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_roundtrip_10_3",
  "declaration_slug": "yoneda-roundtrip-10-3",
  "kind": "theorem",
  "name": "yoneda_roundtrip_10_3",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 297,
  "source_line_end": 298,
  "registry_ids": [
    "II.T36"
  ],
  "related_registry_items": [
    {
      "id": "II.T36",
      "title": "Tau-Yoneda Embedding",
      "url": "/registry/object/II.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L297-L298",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.YonedaTheorem",
        "url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L297-L298",
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

- Module: [TauLib.BookII.Enrichment.YonedaTheorem](/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/)
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L297-L298)
- Source range: L297-L298
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
-- Round-trip [II.T36]
```

## Source Excerpt

```lean
theorem yoneda_roundtrip_10_3 :
    yoneda_roundtrip_check 10 3 = true := by native_decide
```
