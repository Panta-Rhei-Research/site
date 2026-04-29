---
{
  "projection_kind": "taulib_declaration",
  "title": "adelic_dense_20_4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-adeles/adelic-dense-20-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::adelic_dense_20_4",
  "declaration_slug": "adelic-dense-20-4",
  "kind": "theorem",
  "name": "adelic_dense_20_4",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/verify/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 233,
  "source_line_end": 234,
  "registry_ids": [
    "III.T12"
  ],
  "related_registry_items": [
    {
      "id": "III.T12",
      "title": "Adelic Embedding Theorem",
      "url": "/registry/object/III.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L233-L234",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Adeles",
        "url": "/verify/taulib/docs/book-iii-spectral-adeles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L233-L234",
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

- Module: [TauLib.BookIII.Spectral.Adeles](/verify/taulib/docs/book-iii-spectral-adeles/)
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L233-L234)
- Source range: L233-L234
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T12` — Adelic Embedding Theorem

## Immediate Comment / Docstring

```lean
-- Adelic dense image [III.T12]
```

## Source Excerpt

```lean
theorem adelic_dense_20_4 :
    adelic_dense_check 20 4 = true := by native_decide
```
