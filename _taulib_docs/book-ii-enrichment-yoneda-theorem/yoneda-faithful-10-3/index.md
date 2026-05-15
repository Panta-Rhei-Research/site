---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_faithful_10_3",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-faithful-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_faithful_10_3",
  "declaration_slug": "yoneda-faithful-10-3",
  "kind": "theorem",
  "name": "yoneda_faithful_10_3",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 285,
  "source_line_end": 286,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L285-L286",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.YonedaTheorem",
        "url": "/corpus/taulib/docs/book-ii-enrichment-yoneda-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L285-L286",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Enrichment.YonedaTheorem](/corpus/taulib/docs/book-ii-enrichment-yoneda-theorem/)
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L285-L286)
- Source range: L285-L286
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
-- Faithfulness [II.T36]
```

## Source Excerpt

```lean
theorem yoneda_faithful_10_3 :
    yoneda_faithful_check 10 3 = true := by native_decide
```
