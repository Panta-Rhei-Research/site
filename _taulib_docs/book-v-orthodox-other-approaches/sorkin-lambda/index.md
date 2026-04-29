---
{
  "projection_kind": "taulib_declaration",
  "title": "sorkin_lambda",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/sorkin-lambda/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::sorkin_lambda",
  "declaration_slug": "sorkin-lambda",
  "kind": "theorem",
  "name": "sorkin_lambda",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 268,
  "source_line_end": 270,
  "registry_ids": [
    "V.R282"
  ],
  "related_registry_items": [
    {
      "id": "V.R282",
      "title": "Sorkin's Lambda prediction",
      "url": "/registry/object/V.R282/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L268-L270",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L268-L270",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L268-L270)
- Source range: L268-L270
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R282` — Sorkin's Lambda prediction

## Immediate Comment / Docstring

```lean
/-- [V.R282] Sorkin's Lambda prediction: Lambda ~ 1/sqrt(N) where N
    is the number of causal set elements. In tau, Lambda = 0 exactly
    but the effective w varies with redshift (V.R136). -/
```

## Source Excerpt

```lean
theorem sorkin_lambda :
    "Sorkin: Lambda ~ 1/sqrt(N); tau: Lambda = 0, w varies with z" =
    "Sorkin: Lambda ~ 1/sqrt(N); tau: Lambda = 0, w varies with z" := rfl
```
