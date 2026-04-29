---
{
  "projection_kind": "taulib_declaration",
  "title": "limit_unique_10_4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-local-fields/limit-unique-10-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::limit_unique_10_4",
  "declaration_slug": "limit-unique-10-4",
  "kind": "theorem",
  "name": "limit_unique_10_4",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/verify/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 208,
  "source_line_end": 209,
  "registry_ids": [
    "III.P06"
  ],
  "related_registry_items": [
    {
      "id": "III.P06",
      "title": "Completeness Without Topology",
      "url": "/registry/object/III.P06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L208-L209",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.LocalFields",
        "url": "/verify/taulib/docs/book-iii-spectral-local-fields/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L208-L209",
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

- Module: [TauLib.BookIII.Spectral.LocalFields](/verify/taulib/docs/book-iii-spectral-local-fields/)
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L208-L209)
- Source range: L208-L209
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P06` — Completeness Without Topology

## Immediate Comment / Docstring

```lean
-- Limit uniqueness [III.P06]
```

## Source Excerpt

```lean
theorem limit_unique_10_4 :
    limit_uniqueness_check 10 4 = true := by native_decide
```
