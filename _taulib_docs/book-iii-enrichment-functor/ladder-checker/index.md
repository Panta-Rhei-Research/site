---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_checker",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/ladder-checker/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::ladder_checker",
  "declaration_slug": "ladder-checker",
  "kind": "def",
  "name": "ladder_checker",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 197,
  "source_line_end": 210,
  "registry_ids": [
    "III.D10"
  ],
  "related_registry_items": [
    {
      "id": "III.D10",
      "title": "Ladder Checker",
      "url": "/registry/object/III.D10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L197-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L197-L210",
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
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L197-L210)
- Source range: L197-L210
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D10` — Ladder Checker

## Immediate Comment / Docstring

```lean
/-- [III.D10] Full ladder checker: all four properties. -/
```

## Source Excerpt

```lean
def ladder_checker (bound db : TauIdx) : Bool :=
  existence_checker .E0 bound db &&
  existence_checker .E1 bound db &&
  existence_checker .E2 bound db &&
  existence_checker .E3 bound db &&
  stability_checker .E0 bound db &&
  stability_checker .E1 bound db &&
  stability_checker .E2 bound db &&
  stability_checker .E3 bound db &&
  strictness_checker .E0 bound db &&
  strictness_checker .E1 bound db &&
  strictness_checker .E2 bound db &&
  strictness_checker .E3 bound db &&
  saturation_checker bound db
```
