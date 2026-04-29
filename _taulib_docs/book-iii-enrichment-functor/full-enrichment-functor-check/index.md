---
{
  "projection_kind": "taulib_declaration",
  "title": "full_enrichment_functor_check",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/full-enrichment-functor-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::full_enrichment_functor_check",
  "declaration_slug": "full-enrichment-functor-check",
  "kind": "def",
  "name": "full_enrichment_functor_check",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 92,
  "source_line_end": 98,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L92-L98",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L92-L98",
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

- Module: [TauLib.BookIII.Enrichment.Functor](/verify/taulib/docs/book-iii-enrichment-functor/)
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L92-L98)
- Source range: L92-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D04` — Enrichment Functor

## Immediate Comment / Docstring

```lean
/-- [III.D04] Full enrichment functor verification: check at all three
    transition steps E₀→E₁, E₁→E₂, E₂→E₃. -/
```

## Source Excerpt

```lean
def full_enrichment_functor_check (bound db : TauIdx) : Bool :=
  enrichment_functor_check .E0 bound db &&
  enrichment_functor_check .E1 bound db &&
  enrichment_functor_check .E2 bound db &&
  enrichment_functor_faithful .E0 bound db &&
  enrichment_functor_faithful .E1 bound db &&
  enrichment_functor_faithful .E2 bound db
```
