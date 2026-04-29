---
{
  "projection_kind": "taulib_declaration",
  "title": "trichotomy_15_4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/trichotomy-15-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::trichotomy_15_4",
  "declaration_slug": "trichotomy-15-4",
  "kind": "theorem",
  "name": "trichotomy_15_4",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 271,
  "source_line_end": 272,
  "registry_ids": [
    "III.T14"
  ],
  "related_registry_items": [
    {
      "id": "III.T14",
      "title": "Spectral Trichotomy Lemma",
      "url": "/registry/object/III.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L271-L272",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L271-L272",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L271-L272)
- Source range: L271-L272
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T14` — Spectral Trichotomy Lemma

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Spectral trichotomy [III.T14]
```

## Source Excerpt

```lean
theorem trichotomy_15_4 :
    trichotomy_check 15 4 = true := by native_decide
```
